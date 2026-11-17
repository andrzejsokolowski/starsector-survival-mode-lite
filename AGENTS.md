# Survival Mode - Lite

These instructions apply to this repository, including when it is opened without the parent mod workspace.
The workspace `AGENTS.md` one folder up still governs releases, packaging, Git identity and communication.

## Notion

Tasks, history and test lists: the **Survival Mode - Lite board** in Andrzej's Notion, under
**Starsector mods** (`collection://41b20ca7-5d20-81a5-a3bf-000b03c48e3e`). Ticket ids start with SML.
Read the board with `notion-query-data-sources` mode `view` on `view://41b20ca7-5d20-81b5-9b17-000c82200ee7`.
SML-1 holds Andrzej's original request word for word and the full list of what survival mode does.

## Build

`python build.py` checks the settings against the game's settings.json and writes `SurvivalModeLite.zip`
here (staging folder `SurvivalModeLite`). No code, no jar.

## How it works

- Survival mode is the 0.98.5a "extended mode" (`SectorAPI.isExtMode()`, `Misc.isExtended()`), chosen at
  new game. Nearly all of it reads `ext_` keys from `starsector-core/data/config/settings.json`.
- The mod ships `data/config/settings.json` with lighter `ext_` values. The game merges it over the base
  file at startup, before anything reads it (some values are cached in statics, for example
  `Tuning.EXT_DELAY_FACTOR`, so changing them at runtime would not work).
- The game appends lists when merging, so every list starts with `"core_clearArray"` (0.98.5a drops the
  marker from the merged list). Merged plain values become strings; `getFloat` and `getInt` still read them.
- Rule: every penalty halfway between normal and survival. Things that help the player and yes/no rules stay.
