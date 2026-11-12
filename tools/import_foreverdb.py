import json
import os
import sys
import time
import argparse
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
API_ROOT = "https://foreverdb.net/api/v1/quests"
OUTPUT = REPO_ROOT / "build" / "ForeverPath" / "ExternalData" / "ForeverDBQuests.lua"
SUPPLEMENTAL_OUTPUT = REPO_ROOT / "build" / "ForeverPath" / "ExternalData" / "ForeverDBSupplemental.lua"
PAGE_SIZE = 100
SUPPLEMENTAL_ENDPOINTS = {
    "dungeons": {"path": "dungeons"},
    "classes": {"path": "classes"},
    "professions": {"path": "professions"},
    "zones": {"path": "zones"},
    # Verified observations include quest XP/rewards and item/NPC changes.
    "changesSeen": {"path": "changes-seen", "params": {"verified": "1"}},
}
EXTENDED_ENDPOINTS = {
    # These endpoints are intentionally opt-in: they can be larger than the
    # core import and should not consume the daily quota on every routine run.
    "itemsets": {"path": "itemsets"},
    "vendors": {"path": "vendors", "params": {"seen": "true"}},
    "poisons": {"path": "poisons"},
    "disenchant": {"path": "disenchant"},
    "battlegrounds": {"path": "battlegrounds"},
    "items": {"path": "items"},
    "spells": {"path": "spells"},
}

# These endpoints are small, optional and useful when the quest snapshot has
# the same build number but the live client received a hotfix.  They are kept
# separate from the large collections so a temporary 502 cannot invalidate a
# complete quest import.
HOTFIX_ENDPOINTS = {
    "builds": "builds",
    "latestBuild": "builds/latest",
    "buffsNerfs": "buffs-nerfs",
    "merchantsFavor": "merchants-favor",
}

# Server-side hotfixes do not change the client build and therefore cannot be
# discovered reliably from the normal build snapshot. Keep these facts in the
# generated data package with a source link so route scoring can use them
# without contacting the API from inside WoW.
KNOWN_SERVER_HOTFIXES = {
    "dungeonKillXP": {
        "multiplier": 1.5,
        "effectiveDate": "2026-11-08",
        "source": "https://foreverdb.net/article/dungeon-kill-xp-increased-november-8",
        "scope": "dungeon enemy kill XP only; dungeon quest XP is unchanged",
    },
}


def request_json(api_key, path, params=None):
    query = urllib.parse.urlencode(params or {})
    url = f"https://foreverdb.net/api/v1/{path}"
    if query:
        url += "?" + query
    request = urllib.request.Request(
        url,
        headers={
            "X-API-Key": api_key,
            "Accept": "application/json",
            "User-Agent": "ForeverPathDataImporter/0.10 (+https://foreverdb.net)",
        },
    )
    attempts = 0
    while True:
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            if error.code == 404:
                return {}
            if error.code == 429:
                time.sleep(max(1, int(error.headers.get("Retry-After", "5"))))
                continue
            if 500 <= error.code < 600:
                attempts += 1
                if attempts >= 5:
                    raise
                time.sleep(min(30, 2 ** attempts))
                continue
            raise


def request_optional_json(api_key, path):
    """Read a small optional endpoint without failing the core snapshot."""
    try:
        return request_json(api_key, path)
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, ValueError) as error:
        print(f"warnung: optionaler Endpoint {path} nicht verfügbar: {error}")
        return {"meta": {"endpoint": path, "warning": str(error)}, "data": []}


def request_page(api_key, offset):
    query = urllib.parse.urlencode({"limit": PAGE_SIZE, "offset": offset})
    request = urllib.request.Request(
        f"{API_ROOT}?{query}",
        headers={
            "X-API-Key": api_key,
            "Accept": "application/json",
            "User-Agent": "ForeverPathDataImporter/0.7 (+https://foreverdb.net)",
        },
    )
    while True:
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            if error.code != 429:
                raise
            retry_after = int(error.headers.get("Retry-After", "5"))
            time.sleep(max(1, retry_after))


def request_collection(api_key, endpoint, extra_params=None, allow_transient_failure=False):
    records, offset, total, last_meta = [], 0, None, {}
    while total is None or offset < total:
        params = {"limit": PAGE_SIZE, "offset": offset}
        if extra_params:
            params.update(extra_params)
        query = urllib.parse.urlencode(params)
        request = urllib.request.Request(
            f"https://foreverdb.net/api/v1/{endpoint}?{query}",
            headers={"X-API-Key": api_key, "Accept": "application/json", "User-Agent": "ForeverPathDataImporter/0.7 (+https://foreverdb.net)"},
        )
        attempts = 0
        while True:
            try:
                with urllib.request.urlopen(request, timeout=30) as response:
                    page = json.load(response)
                break
            except urllib.error.HTTPError as error:
                if error.code == 429:
                    attempts += 1
                    time.sleep(max(1, int(error.headers.get("Retry-After", "5"))))
                    continue
                if 500 <= error.code < 600:
                    attempts += 1
                    if attempts >= 5 and allow_transient_failure:
                        print(f"warnung: {endpoint} antwortet weiter mit HTTP {error.code}; Endpoint wird für diesen Lauf übersprungen")
                        return {"meta": {"endpoint": endpoint, "warning": f"HTTP {error.code}"}, "data": []}
                    if attempts < 5:
                        time.sleep(min(60, 5 * (2 ** (attempts - 1))))
                        continue
                raise
        last_meta = page.get("meta", {})
        total = int(last_meta.get("total", 0))
        records.extend(page.get("data", []))
        offset += PAGE_SIZE
        if total == 0 or not page.get("data"):
            break
    return {"meta": last_meta, "data": records}


def request_detail(api_key, endpoint, resource_id):
    request = urllib.request.Request(
        f"https://foreverdb.net/api/v1/{endpoint}/{urllib.parse.quote(str(resource_id))}",
        headers={
            "X-API-Key": api_key,
            "Accept": "application/json",
            "User-Agent": "ForeverPathDataImporter/0.9 (+https://foreverdb.net)",
        },
    )
    while True:
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            if error.code != 429:
                raise
            time.sleep(max(1, int(error.headers.get("Retry-After", "5"))))


def endpoint(value):
    if not isinstance(value, dict):
        return None
    location = value.get("location") or {}
    cleaned_location = None
    if isinstance(location, dict) and location.get("uiMapId") and location.get("x") is not None and location.get("y") is not None:
        cleaned_location = {
            "mapID": location.get("uiMapId"),
            "x": location.get("x"),
            "y": location.get("y"),
            "zone": location.get("zone"),
            "source": location.get("source"),
        }
    return {
        "type": value.get("type"),
        "id": value.get("id"),
        "name": value.get("name"),
        "location": cleaned_location,
        "source": value.get("source"),
    }


def chain(value):
    if not isinstance(value, list):
        return []
    return [
        {
            "questID": item.get("questId"),
            "name": item.get("name"),
            "relation": item.get("relation"),
            "source": item.get("source"),
        }
        for item in value
        if isinstance(item, dict) and item.get("questId")
    ]


def normalize(item):
    zone = item.get("zone") or {}
    source = item.get("source")
    chain_data = item.get("chain") or {}
    return {
        "id": item.get("id"),
        "name": item.get("name"),
        "level": item.get("level"),
        "requiredLevel": item.get("requiredLevel"),
        "side": item.get("side"),
        "category": item.get("category"),
        "zone": {"name": zone.get("n"), "mapID": zone.get("m"), "slug": zone.get("slug")},
        "knownInForever": item.get("knownInForever"),
        # Keep reward values when ForeverDB exposes them.  Older snapshots do
        # not provide money for every quest; the addon then falls back to the
        # live quest-log API instead of inventing a value.
        "rewardXP": item.get("rewardXP") or item.get("xpReward") or item.get("experienceReward"),
        "rewardMoney": item.get("rewardMoney") or item.get("moneyReward") or item.get("goldReward"),
        "source": source,
        "start": endpoint(item.get("starts")),
        "turnIn": endpoint(item.get("ends")),
        "previous": chain(chain_data.get("previous")),
        "next": chain(chain_data.get("next")),
        "questLine": chain_data.get("questLine"),
        "url": item.get("url"),
    }


def compact_collection(name, collection):
    """Keep the client-relevant fields while avoiding a second raw API dump."""
    if not isinstance(collection, dict) or not isinstance(collection.get("data"), list):
        return collection
    fields = {
        "items": ("id", "name", "quality", "itemLevel", "requiredLevel", "class", "subclass", "slot", "stats", "damage", "speed", "source", "liveClient", "dataFromBuild", "url"),
        "spells": ("id", "name", "rank", "description", "icon", "requiredLevel", "cooldown", "costs", "school", "source", "liveClient", "dataFromBuild", "url"),
    }.get(name)
    if not fields:
        return collection
    rows = []
    for item in collection["data"]:
        if isinstance(item, dict):
            rows.append({key: item.get(key) for key in fields if item.get(key) is not None})
    result = dict(collection)
    result["data"] = rows
    return result


def lua(value):
    if value is None:
        return "nil"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return repr(value)
    if isinstance(value, str):
        return '"' + value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n") + '"'
    if isinstance(value, list):
        return "{" + ",".join(lua(item) for item in value) + "}"
    if isinstance(value, dict):
        fields = []
        for key, item in value.items():
            if item is None:
                continue
            key_lua = f"[{key}]" if isinstance(key, int) else f"[{lua(str(key))}]"
            fields.append(f"{key_lua}={lua(item)}")
        return "{" + ",".join(fields) + "}"
    raise TypeError(type(value))


def main():
    parser = argparse.ArgumentParser(description="Importiert öffentliche ForeverDB-Daten ohne den API-Key zu speichern.")
    parser.add_argument(
        "--extended",
        action="store_true",
        help="importiert zusätzlich Itemsets, Händler, Gifte, Disenchant, Battlegrounds und Dungeon-Details",
    )
    args = parser.parse_args()
    api_key = os.environ.get("FOREVERDB_API_KEY")
    if not api_key:
        raise SystemExit("FOREVERDB_API_KEY fehlt. Der Schlüssel wird nicht in eine Datei geschrieben.")

    records = {}
    offset = 0
    total = None
    build = None
    client = None
    attribution = "Data from ForeverDB.net (https://foreverdb.net)"
    while total is None or offset < total:
        page = request_page(api_key, offset)
        page_meta = page.get("meta", {})
        total = int(page_meta.get("total", 0))
        build = page_meta.get("build") or build
        client = page_meta.get("client") or client
        attribution = page_meta.get("attribution") or attribution
        for item in page.get("data", []):
            normalized = normalize(item)
            if normalized.get("id"):
                records[int(normalized["id"])] = normalized
        offset += PAGE_SIZE
        print(f"geladen: {min(offset, total)}/{total}")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    api_meta = request_json(api_key, "meta")
    metadata = {"build": build, "client": client, "total": total, "attribution": attribution, "endpoint": API_ROOT, "imported": len(records), "apiMeta": api_meta.get("data") or api_meta.get("meta") or api_meta}
    with OUTPUT.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write("-- GENERATED from the ForeverDB API.\n")
        handle.write("-- Source: https://foreverdb.net/developers\n")
        handle.write("-- Do not put an API key in this file.\n")
        handle.write("local ADDON, ns = ...\n")
        handle.write("ns.ForeverDBMetadata = " + lua(metadata) + "\n")
        handle.write("ns.ForeverDBQuests = " + lua(records) + "\n")
    print(f"geschrieben: {OUTPUT} ({len(records)} Quests)")

    endpoint_specs = dict(SUPPLEMENTAL_ENDPOINTS)
    if args.extended:
        endpoint_specs.update(EXTENDED_ENDPOINTS)

    supplemental = {"meta": {"profile": "extended" if args.extended else "core"}}
    for key, spec in endpoint_specs.items():
        print(f"lade: {spec['path']}")
        supplemental[key] = compact_collection(
            key,
            request_collection(
                api_key,
                spec["path"],
                spec.get("params"),
                allow_transient_failure=key in {"items", "spells"},
            ),
        )

    if args.extended:
        dungeon_rows = supplemental.get("dungeons", {}).get("data", [])
        details = {}
        for dungeon in dungeon_rows:
            dungeon_id = dungeon.get("id") if isinstance(dungeon, dict) else None
            is_forever_dungeon = isinstance(dungeon, dict) and (
                dungeon.get("status") == "forever" or dungeon.get("newInForever") is True
            )
            if not dungeon_id or not is_forever_dungeon:
                continue
            print(f"lade: dungeons/{dungeon_id}")
            details[str(dungeon_id)] = request_detail(api_key, "dungeons", dungeon_id)
        supplemental["dungeonDetails"] = details

        hotfixes = {"meta": {"profile": "optional-hotfix", "source": "ForeverDB.net"}}
        for key, path in HOTFIX_ENDPOINTS.items():
            print(f"prüfe optional: {path}")
            hotfixes[key] = request_optional_json(api_key, path)
        supplemental["hotfixes"] = hotfixes
        supplemental["serverHotfixes"] = KNOWN_SERVER_HOTFIXES
        supplemental["meta"]["hotfixEndpoints"] = list(HOTFIX_ENDPOINTS.values())
        supplemental["meta"]["refreshedAtUtc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    with SUPPLEMENTAL_OUTPUT.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write("-- GENERATED from the ForeverDB API.\n")
        handle.write("-- Source: https://foreverdb.net/developers\n")
        handle.write("-- Do not put an API key in this file.\n")
        handle.write("local ADDON, ns = ...\n")
        handle.write("ns.ForeverDBSupplemental = " + lua(supplemental) + "\n")
    print(f"geschrieben: {SUPPLEMENTAL_OUTPUT}")


if __name__ == "__main__":
    main()
