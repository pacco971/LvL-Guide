#!/usr/bin/env python3
"""Refresh the static ForeverDB snapshot inside ForeverPath.zip.

The API key is consumed by tools/import_foreverdb.py and is never written to
the addon archive or to the repository.
"""

from __future__ import annotations

import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ARCHIVE = REPO_ROOT / "ForeverPath.zip"
BUILD_ROOT = REPO_ROOT / "build"
STAGED_ADDON = BUILD_ROOT / "ForeverPath"
DATA_ROOT = "ExternalData"


def extract_archive(archive: Path, destination: Path) -> Path:
    destination.mkdir(parents=True, exist_ok=True)
    destination_resolved = destination.resolve()

    with zipfile.ZipFile(archive) as source:
        for member in source.infolist():
            target = (destination / member.filename).resolve()
            if target != destination_resolved and destination_resolved not in target.parents:
                raise RuntimeError(f"Unsafe archive path: {member.filename}")
        source.extractall(destination)

    toc_files = list(destination.rglob("ForeverPath.toc"))
    if len(toc_files) != 1:
        raise RuntimeError(
            f"Expected exactly one ForeverPath.toc, found {len(toc_files)}"
        )
    return toc_files[0].parent


def dataset_digest(addon_root: Path) -> str:
    data_root = addon_root / DATA_ROOT
    digest = hashlib.sha256()

    if not data_root.exists():
        return "missing"

    for path in sorted(p for p in data_root.rglob("*") if p.is_file()):
        digest.update(path.relative_to(data_root).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")

    return digest.hexdigest()


def read_build(addon_root: Path) -> str:
    metadata_file = addon_root / DATA_ROOT / "ForeverDBQuests.lua"
    match = re.search(
        r'\["build"\]\s*=\s*"([^"]+)"',
        metadata_file.read_text(encoding="utf-8"),
    )
    if not match:
        raise RuntimeError(f"Could not read ForeverDB build from {metadata_file}")
    return match.group(1)


def write_archive(addon_root: Path, archive: Path) -> None:
    if archive.exists():
        archive.unlink()

    with zipfile.ZipFile(
        archive,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as target:
        for path in sorted(p for p in addon_root.rglob("*") if p.is_file()):
            relative = path.relative_to(BUILD_ROOT).as_posix()
            info = zipfile.ZipInfo(relative, date_time=(2020, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            target.writestr(info, path.read_bytes())


def set_output(name: str, value: str) -> None:
    output_path = os.environ.get("GITHUB_OUTPUT")
    if not output_path:
        return
    with open(output_path, "a", encoding="utf-8", newline="\n") as output:
        output.write(f"{name}={value}\n")


def main() -> int:
    if not SOURCE_ARCHIVE.is_file() or SOURCE_ARCHIVE.stat().st_size == 0:
        raise RuntimeError(f"Missing release archive: {SOURCE_ARCHIVE}")

    if BUILD_ROOT.exists():
        shutil.rmtree(BUILD_ROOT)
    BUILD_ROOT.mkdir(parents=True)

    with tempfile.TemporaryDirectory(prefix="foreverpath-old-") as old_dir:
        old_addon = extract_archive(SOURCE_ARCHIVE, Path(old_dir))
        old_digest = dataset_digest(old_addon)

    extracted_root = BUILD_ROOT / "source"
    extracted_addon = extract_archive(SOURCE_ARCHIVE, extracted_root)
    shutil.copytree(extracted_addon, STAGED_ADDON)

    env = os.environ.copy()
    if not env.get("FOREVERDB_API_KEY"):
        raise RuntimeError(
            "FOREVERDB_API_KEY is missing. Add it as a GitHub Actions secret."
        )

    subprocess.run(
        [sys.executable, str(REPO_ROOT / "tools" / "import_foreverdb.py")],
        cwd=REPO_ROOT,
        env=env,
        check=True,
    )

    new_digest = dataset_digest(STAGED_ADDON)
    data_build = read_build(STAGED_ADDON)

    if old_digest == new_digest:
        set_output("data_changed", "false")
        set_output("data_build", data_build)
        print(f"No ForeverDB data changes detected ({data_build}).")
        return 0

    safe_build = re.sub(r"[^A-Za-z0-9._-]+", "-", data_build)
    archive_name = f"ForeverPath-{safe_build}.zip"
    upload_archive = REPO_ROOT / archive_name
    write_archive(STAGED_ADDON, upload_archive)
    shutil.copyfile(upload_archive, SOURCE_ARCHIVE)

    set_output("data_changed", "true")
    set_output("data_build", data_build)
    set_output("archive_name", archive_name)
    print(f"Prepared {archive_name} from ForeverDB build {data_build}.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"::error::{error}")
        raise
