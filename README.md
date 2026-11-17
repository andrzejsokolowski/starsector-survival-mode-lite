# Survival Mode - Lite

Starsector 0.98.5a added Survival mode, picked when you start a new game. This mod keeps everything
Survival mode does and halves every penalty: each number sits halfway between normal and survival.

Only campaigns started in Survival mode change. Normal campaigns are not touched.

## What changes

| What | Normal | Survival | Lite |
| --- | --- | --- | --- |
| Ship prices (frigate to capital) | x1 | x5 to x8 | x3 to x4.5 |
| Weapon prices | x1 | x10 | x5.5 |
| Fighter prices | x1 | x5 | x3 |
| Hull mod prices | x1 | x7 | x4 |
| Crew price | x1 | x10 | x5.5 |
| Marine price | x1 | x4 | x2.5 |
| Fuel price | x1 | x3 | x2 |
| Crew and marine salary | x1 | x3 | x2 |
| Officer pay per battle (frigate to capital) | none | 1 to 16 months | 0.5 to 8 months |
| Ships for sale | 100% | 25% | 63% |
| Weapons and fighters for sale | 100% | 20% | 60% |
| Hull mods for sale | 100% | 35% | 68% |
| Crew and marines for sale | 100% | 20% | 60% |
| Supplies for sale | 100% | 40% | 70% |
| Fuel for sale | 100% | 60% | 80% |
| Enemy ships recoverable | 100% | 20% | 60% |
| Derelicts recoverable | 100% | 10% | 55% |
| Weapons dropped by enemies | 100% | 10% | 55% |
| AI cores dropped | 100% | 10% | 55% |
| Cargo salvaged after battle | 75% | 40% | 58% |
| Fuel tank size | 100% | 50% | 75% |
| Tanker fuel tank size | 100% | 35% | 68% |
| Fuel use, cruisers | x1 | x1.5 | x1.25 |
| Fuel use, capitals | x1 | x2 | x1.5 |
| Open market tariff | 30% | 40% | 35% |
| Black market tariff | 0% | 25% | 13% |
| Colony growth needed | x1 | x2 | x1.5 |
| Building cost and build time | x1 | x2 | x1.5 |
| Colony income taxed above | never | 200k | 400k |
| Officers for hire | 100% | 15% | 58% |
| Administrators for hire | 100% | 10% | 55% |
| Story points per level | 4 | 2 | 3 |
| Retirement | never | 25 to 30 cycles | 40 to 50 cycles |
| Hyperstorm and asteroid damage | x1 | x2 | x1.5 |
| Transverse Jump CR loss | x1 | x10 | x5.5 |

And the same halfway rule for every other survival number: loot of hull mods, fighters, special
items and commodities, cargo scans, survey costs, colony start costs, commission pay, task force
and resupply costs, mission ship prices and more. The full list with both values is in
`data/config/settings.json`.

## What stays as in Survival mode

- The things that help you: threats grow 3 times slower, more Domain-grade parts for sale, bigger
  custom production orders.
- The rules that are not numbers: the Survival start choices, the military market needs a
  commission, abandoned stations in the core worlds cannot be used, custom production ships arrive
  without weapons.

## Compatibility

- Settings only, no code. Safe to add to or remove from a game in progress. Some values (like how
  many derelicts can be recovered) are fixed when the sector is made, so they follow the setting
  the campaign was started with.
- Another mod that changes the same survival settings: the one loaded later wins.
