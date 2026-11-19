# Survival Mode - Lite

These instructions apply to this repository, including when it is opened without the parent mod workspace.
The workspace `AGENTS.md` one folder up still governs releases, packaging, Git identity and communication.

## Notion

Tasks, history and test lists: the **Survival Mode - Lite board** in Andrzej's Notion, under
**Starsector mods** (`collection://41b20ca7-5d20-81a5-a3bf-000b03c48e3e`). Ticket ids start with SML.
Read the board with `notion-query-data-sources` mode `view` on `view://41b20ca7-5d20-81b5-9b17-000c82200ee7`.
SML-1 holds Andrzej's original request word for word and the full list of what survival mode does.
Forum topic 36456.

## Build

`python build.py` does everything: it generates the data files and docs from `values.py`, compiles
`jars/SurvivalModeLite.jar` (javac, Java 17, against the game and LunaLib), and writes `SurvivalModeLite.zip`
here (staging folder `SurvivalModeLite`).

## values.py is the source

One row per survival value: tab, label, setting key, list index, unit, survival, lite, vanilla, note.
build.py turns it into `data/config/settings.json` (Lite defaults), `data/config/LunaSettings.csv` (one
LunaLib field per row, one tab per group), `data/config/survival_mode_lite_fields.json` (field id to key,
read by the plugin), the tables in README.md and `forum-post.txt` (from `forum-post.template.txt`).
Never edit the generated files by hand. Field ids are `sml_` + key without `ext_` (+ `_<index>`): keep them
stable, LunaLib stores the player's values under them.

## How it works

- Survival mode is the 0.98.5a "extended mode" (`SectorAPI.isExtMode()`, `Misc.isExtended()`), chosen at
  new game. Nearly all of it reads `ext_` keys from `starsector-core/data/config/settings.json`.
- settings.json is merged over the base file at startup. The merge appends lists, so lists start with
  `"core_clearArray"`. Merged plain values become strings; `getFloat`/`getInt` still read them.
- With LunaLib, `SurvivalModeLitePlugin` copies the LunaLib values into the game's settings at application
  load, on every game load and when the player changes them (`SettingsAPI.setFloat`/`setBoolean`, lists
  changed in place in `getSettingsJSON()`). The game reads these keys live through StarfarerSettings' float
  cache, which setFloat updates. The only copy taken at startup is `Tuning.EXT_DELAY_FACTOR`, set directly.
- Units: pct and per100 are edited in LunaLib times 100, because LunaLib's slider rounds to 2 decimals.
  Other Double defaults may have at most 2 decimals (build.py rejects more).
- No `%` anywhere in `LunaSettings.csv`: LunaLib 2.1.0 draws names and descriptions with
  `addPara(text, pad, color, highlight, new String[0])`, which runs `String.format` in 0.98.5a, so a bare `%`
  crashes the game when the tab opens. build.py writes "percent" and rejects `%`.
- On/off switches (LunaLib only): every key that is not a yes/no rule has a Boolean field `sml_on_<key without ext_>`
  above its rows; `GROUPS` in `values.py` makes keys share one (ship sizes, corruption, retirement). Off writes the
  vanilla value: the vanilla column, or `OFF` in `values.py` where that column is text ("none", "never") or where a
  base game setting should be copied (`offKey`). The field map carries `switch` and `off`/`offKey` per value.
- The game also copies the Analyze mission sensor requirement once (`AnalyzeEntityMissionIntel.MIN_SENSOR_STRENGTH`);
  the plugin sets that field directly too.
- `LunaBridge` is the only class naming LunaLib, loaded only when LunaLib is enabled.
