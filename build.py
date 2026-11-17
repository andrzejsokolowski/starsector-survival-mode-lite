"""Check the data, stage the release folder and zip it folder-at-root for the mod manager.

Run from anywhere: python build.py
No code to compile: the mod is settings only.
Writes the staging folder SurvivalModeLite/ and SurvivalModeLite.zip in the mod root.

Checks:
- no UTF-8 BOM in any JSON, CSV or version file
- every key in data/config/settings.json exists in the base game settings.json
  (a typo would silently do nothing), and every list starts with "core_clearArray"
  (the game appends lists when it merges settings.json)
- version agrees between mod_info.json and the .version file
"""
import json
import os
import re
import shutil
import zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
GAME_SETTINGS = "D:/Games/StarSector0985/starsector-core/data/config/settings.json"
STAGE_NAME = "SurvivalModeLite"
STAGE = os.path.join(ROOT, STAGE_NAME)
ZIP = os.path.join(ROOT, STAGE_NAME + ".zip")
VERSION_FILE = "survival_mode_lite.version"
SHIP = ["mod_info.json", VERSION_FILE, "icon.png", "data"]


def strip_comments(text):
    """Drop # comments outside double quotes, the way the game does."""
    out = []
    for line in text.splitlines():
        quoted = False
        for i, ch in enumerate(line):
            if ch == '"':
                quoted = not quoted
            elif ch == "#" and not quoted:
                line = line[:i]
                break
        out.append(line)
    text = "\n".join(out)
    return re.sub(r",(\s*[}\]])", r"\1", text)  # trailing commas, fine for the game, not for Python


def load_game_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.loads(strip_comments(fh.read()))


def base_settings():
    """key -> list length (or None for a plain value), for the top-level ext_ keys of the base game file.
    The base file uses syntax Python's json refuses, so only these lines are read."""
    with open(GAME_SETTINGS, encoding="utf-8") as fh:
        text = strip_comments(fh.read())
    found = {}
    for m in re.finditer(r'^\s*"(ext_[A-Za-z_]+)"\s*:\s*(\[[^\]]*\]|[^,\n]+)', text, re.M):
        value = m.group(2).strip()
        found[m.group(1)] = len(value[1:-1].split(",")) if value.startswith("[") else None
    return found


def check():
    ours = load_game_json(os.path.join(ROOT, "data", "config", "settings.json"))
    base = base_settings()
    for key, value in ours.items():
        if key not in base:
            raise SystemExit("Not a game setting: " + key)
        if (base[key] is not None) != isinstance(value, list):
            raise SystemExit("List vs value mismatch: " + key)
        if isinstance(value, list):
            if value[0] != "core_clearArray":
                raise SystemExit("List without core_clearArray: " + key)
            if len(value) - 1 != base[key]:
                raise SystemExit("List length differs from the game's: " + key)
    print(len(ours), "settings checked against", GAME_SETTINGS)

    with open(os.path.join(ROOT, "mod_info.json"), encoding="utf-8") as fh:
        info = json.load(fh)
    with open(os.path.join(ROOT, VERSION_FILE), encoding="utf-8") as fh:
        ver = json.load(fh)["modVersion"]
    file_version = "%d.%d.%d" % (ver["major"], ver["minor"], ver["patch"])
    if info["version"] != file_version:
        raise SystemExit("mod_info %s vs version file %s" % (info["version"], file_version))
    return info["version"]


def stage_and_zip(version):
    if os.path.isdir(STAGE):
        shutil.rmtree(STAGE)
    os.makedirs(STAGE)
    for item in SHIP:
        src = os.path.join(ROOT, item)
        dst = os.path.join(STAGE, item)
        if os.path.isdir(src):
            shutil.copytree(src, dst, ignore=shutil.ignore_patterns("*.bak"))
        else:
            shutil.copy2(src, dst)

    # A UTF-8 BOM breaks every Starsector JSON/CSV on 0.98a; refuse to ship one.
    for dp, _, fn in os.walk(STAGE):
        for f in fn:
            if f.endswith((".json", ".csv", ".version")):
                with open(os.path.join(dp, f), "rb") as fh:
                    if fh.read(3) == b"\xef\xbb\xbf":
                        raise SystemExit("BOM in " + f)

    if os.path.exists(ZIP):
        os.remove(ZIP)
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for dp, _, fn in os.walk(STAGE):
            for f in fn:
                p = os.path.join(dp, f)
                z.write(p, os.path.relpath(p, ROOT).replace(os.sep, "/"))
    with zipfile.ZipFile(ZIP) as z:
        names = z.namelist()
        for n in names:
            print("  ", n)
        info = json.loads(z.read(STAGE_NAME + "/mod_info.json"))
        if info["version"] != version:
            raise SystemExit("ZIP has the wrong version")
    print("zip:", ZIP, os.path.getsize(ZIP), "bytes, version", version)


if __name__ == "__main__":
    stage_and_zip(check())
