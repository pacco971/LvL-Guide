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
}


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


def request_collection(api_key, endpoint, extra_params=None):
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
        while True:
            try:
                with urllib.request.urlopen(request, timeout=30) as response:
                    page = json.load(response)
                break
            except urllib.error.HTTPError as error:
                if error.code != 429:
                    raise
                time.sleep(max(1, int(error.headers.get("Retry-After", "5"))))
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
        "source": source,
        "start": endpoint(item.get("starts")),
        "turnIn": endpoint(item.get("ends")),
        "previous": chain(chain_data.get("previous")),
        "next": chain(chain_data.get("next")),
        "questLine": chain_data.get("questLine"),
        "url": item.get("url"),
    }


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
    metadata = {"build": build, "client": client, "total": total, "attribution": attribution, "endpoint": API_ROOT, "imported": len(records)}
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
        supplemental[key] = request_collection(api_key, spec["path"], spec.get("params"))

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
    with SUPPLEMENTAL_OUTPUT.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write("-- GENERATED from the ForeverDB API.\n")
        handle.write("-- Source: https://foreverdb.net/developers\n")
        handle.write("-- Do not put an API key in this file.\n")
        handle.write("local ADDON, ns = ...\n")
        handle.write("ns.ForeverDBSupplemental = " + lua(supplemental) + "\n")
    print(f"geschrieben: {SUPPLEMENTAL_OUTPUT}")


if __name__ == "__main__":
    main()
