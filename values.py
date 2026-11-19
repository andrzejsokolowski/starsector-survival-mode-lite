"""Every survival value the mod sets, in one place.

build.py turns this table into:
- data/config/settings.json (the Lite defaults, used with or without LunaLib)
- data/config/LunaSettings.csv (one LunaLib field per value, one tab per group)
- the value tables in README.md

Row: (tab, label, setting key, list index or None, unit, survival, lite, vanilla, note)
Units:
- "x":   multiplier, shown as x2
- "pct": fraction, shown and edited in LunaLib as a percent (0.25 -> 25)
- "num": plain decimal number
- "int": whole number
- "bool": on or off
vanilla can be a number or a short text for things the base game does not have.
note is added to the LunaLib field description.
"""

NEW_GAME = "Only takes effect when a new sector is made."

ROWS = [
    # Prices
    ("Prices", "Frigate prices", "ext_shipBuyPriceMult", 0, "x", 5, 3, 1, ""),
    ("Prices", "Destroyer prices", "ext_shipBuyPriceMult", 1, "x", 5, 3, 1, ""),
    ("Prices", "Cruiser prices", "ext_shipBuyPriceMult", 2, "x", 6, 3.5, 1, ""),
    ("Prices", "Capital ship prices", "ext_shipBuyPriceMult", 3, "x", 8, 4.5, 1, ""),
    ("Prices", "Weapon prices", "ext_weaponPriceMult", None, "x", 10, 5.5, 1, ""),
    ("Prices", "Fighter LPC prices", "ext_fighterPriceMult", None, "x", 5, 3, 1, ""),
    ("Prices", "Hull mod spec prices", "ext_hullmodPriceMult", None, "x", 7, 4, 1, ""),
    ("Prices", "Blueprint sell price", "ext_blueprintSellPriceMult", None, "pct", 0.3, 0.65, 1, ""),
    ("Prices", "Domain-grade parts price", "ext_partsPriceMult", None, "x", 2, 1.5, 1, ""),
    ("Prices", "Crew price", "ext_crewPriceMult", None, "x", 10, 5.5, 1, ""),
    ("Prices", "Marine price", "ext_marinesPriceMult", None, "x", 4, 2.5, 1, ""),
    ("Prices", "Fuel price", "ext_fuelPriceMult", None, "x", 3, 2, 1, ""),
    ("Prices", "Crew and marines sold back", "ext_personnelSellPriceMult", None, "pct", 0.1, 0.18, 1,
     "Share of the raised price you get back. 100% divided by the crew price keeps buying and selling even."),
    ("Prices", "Open market tariff", "ext_normalTariff", None, "pct", 0.4, 0.35, 0.3, ""),
    ("Prices", "Black market tariff", "ext_blackMarketTariff", None, "pct", 0.25, 0.125, 0, ""),
    ("Prices", "Hand-me-down freighter mission: extra price", "ext_worseHandMeDownFreighterPriceMult", None, "x", 1.25, 1.125, 1, ""),
    ("Prices", "Hijacked ship mission: extra price", "ext_hijackedShipCostMult", None, "x", 2, 1.5, 1, ""),
    ("Prices", "Surplus hull mission: extra price", "ext_surplusHullPriceMult", None, "x", 2, 1.5, 1, ""),
    ("Prices", "Task force cost", "ext_taskForceCostMult", None, "x", 2, 1.5, 1, ""),
    ("Prices", "Resupply fleet cost", "ext_resupplyFleetCostMult", None, "x", 1.5, 1.25, 1, ""),
    ("Prices", "Crew a resupply fleet brings", "ext_resupplyCrewBroughtMult", None, "pct", 0.25, 0.625, 1, ""),

    # Pay
    ("Pay", "Crew salary", "ext_crewSalaryMult", None, "x", 3, 2, 1, ""),
    ("Pay", "Marine salary", "ext_marineSalaryMult", None, "x", 3, 2, 1, ""),
    ("Pay", "Officer pay per battle, frigate (months of salary)", "ext_officerCombatPay", 0, "num", 0.5, 0.25, "none", ""),
    ("Pay", "Officer pay per battle, destroyer (months of salary)", "ext_officerCombatPay", 1, "num", 1, 0.5, "none", ""),
    ("Pay", "Officer pay per battle, cruiser (months of salary)", "ext_officerCombatPay", 2, "num", 2, 1, "none", ""),
    ("Pay", "Officer pay per battle, capital (months of salary)", "ext_officerCombatPay", 3, "num", 8, 4, "none", ""),
    ("Pay", "Commission monthly pay", "ext_commissionMonthlyIncomeMult", None, "pct", 0.1, 0.55, 1, ""),

    # Markets
    ("Markets", "Ships for sale", "ext_shipForSaleFraction", None, "pct", 0.25, 0.625, 1, ""),
    ("Markets", "Quality of ships for sale", "ext_shipForSaleQualityMod", None, "pct", -0.35, -0.175, 0,
     "Lower means more d-mods."),
    ("Markets", "Weapons for sale", "ext_weaponForSaleFraction", None, "pct", 0.2, 0.6, 1, ""),
    ("Markets", "Fighter LPCs for sale", "ext_fighterForSaleFraction", None, "pct", 0.2, 0.6, 1, ""),
    ("Markets", "Hull mod specs for sale", "ext_hullmodForSaleFraction", None, "pct", 0.35, 0.675, 1, ""),
    ("Markets", "Crew for sale", "ext_crewForSaleFraction", None, "pct", 0.2, 0.6, 1, ""),
    ("Markets", "Marines for sale", "ext_marinesForSaleFraction", None, "pct", 0.2, 0.6, 1, ""),
    ("Markets", "Supplies for sale", "ext_suppliesForSaleFraction", None, "pct", 0.4, 0.7, 1, ""),
    ("Markets", "Fuel for sale", "ext_fuelForSaleFraction", None, "pct", 0.6, 0.8, 1, ""),
    ("Markets", "Drugs for sale", "ext_drugsForSaleFraction", None, "pct", 0.3, 0.65, 1, ""),
    ("Markets", "Organs for sale", "ext_organsForSaleFraction", None, "pct", 0.3, 0.65, 1, ""),
    ("Markets", "Heavy armaments for sale", "ext_hand_weaponsForSaleFraction", None, "pct", 0.2, 0.6, 1, ""),
    ("Markets", "Drugs at free ports", "ext_drugsForSaleFractionFreePort", None, "pct", 0.15, 0.575, 1, ""),
    ("Markets", "Organs at free ports", "ext_organsForSaleFractionFreePort", None, "pct", 0.15, 0.575, 1, ""),
    ("Markets", "Heavy armaments at free ports", "ext_hand_weaponsForSaleFractionFreePort", None, "pct", 0.1, 0.55, 1, ""),
    ("Markets", "Crew at your colonies", "ext_crewForSaleFractionPlayerColony", None, "pct", 0.5, 0.75, 1, ""),
    ("Markets", "Marines at your colonies", "ext_marinesForSaleFractionPlayerColony", None, "pct", 0.5, 0.75, 1, ""),
    ("Markets", "Supplies at your colonies", "ext_suppliesForSaleFractionPlayerColony", None, "pct", 0.65, 0.825, 1, ""),
    ("Markets", "Fuel at your colonies", "ext_fuelForSaleFractionPlayerColony", None, "pct", 0.75, 0.875, 1, ""),
    ("Markets", "Your colonies' local resources stockpile", "ext_localResourcesStockpileAndRateMult", None, "pct", 0.3, 0.65, 1, ""),

    # Loot
    ("Loot", "Enemy ships recoverable after battle", "ext_shipRecoverableFraction", None, "pct", 0.2, 0.6, 1, ""),
    ("Loot", "Derelict ships recoverable", "ext_derelictShipRecoverableFraction", None, "pct", 0.1, 0.55, 1, NEW_GAME),
    ("Loot", "Derelicts that offer the story point recovery", "ext_shipRecoveryWithStoryPointsFraction", None, "pct", 0.2, 0.6, 1, ""),
    ("Loot", "Story points to recover a frigate", "ext_recoveryNonOwnSPCost", 0, "int", 1, 1, 1, ""),
    ("Loot", "Story points to recover a destroyer", "ext_recoveryNonOwnSPCost", 1, "int", 1, 1, 1, ""),
    ("Loot", "Story points to recover a cruiser", "ext_recoveryNonOwnSPCost", 2, "int", 2, 1, 1, ""),
    ("Loot", "Story points to recover a capital", "ext_recoveryNonOwnSPCost", 3, "int", 4, 2, 1, ""),
    ("Loot", "Story points to recover a civilian frigate", "ext_recoveryNonOwnSPCostCiv", 0, "int", 1, 1, 1, ""),
    ("Loot", "Story points to recover a civilian destroyer", "ext_recoveryNonOwnSPCostCiv", 1, "int", 1, 1, 1, ""),
    ("Loot", "Story points to recover a civilian cruiser", "ext_recoveryNonOwnSPCostCiv", 2, "int", 1, 1, 1, ""),
    ("Loot", "Story points to recover a civilian capital", "ext_recoveryNonOwnSPCostCiv", 3, "int", 2, 1, 1, ""),
    ("Loot", "Weapons dropped by enemies", "ext_weaponDropFraction", None, "pct", 0.1, 0.55, 1, ""),
    ("Loot", "Weapons from salvage", "ext_weaponSalvageDropFraction", None, "pct", 0.2, 0.6, 1, ""),
    ("Loot", "Fighter LPCs dropped by enemies", "ext_fighterDropFraction", None, "pct", 0.2, 0.6, 1, ""),
    ("Loot", "Fighter LPCs from salvage", "ext_fighterSalvageDropFraction", None, "pct", 0.3, 0.65, 1, ""),
    ("Loot", "Hull mod specs dropped by enemies", "ext_hullmodDropFraction", None, "pct", 0.25, 0.625, 1, ""),
    ("Loot", "Hull mod specs from salvage", "ext_hullmodSalvageDropFraction", None, "pct", 0.5, 0.75, 1, ""),
    ("Loot", "Special items from salvage", "ext_specialItemSalvageDropFraction", None, "pct", 0.5, 0.75, 1, ""),
    ("Loot", "Commodities from salvage", "ext_commoditySalvageDropFraction", None, "pct", 0.3, 0.65, 1, ""),
    ("Loot", "Crew from sleeper pods", "ext_sleeperPodsSpecialCrewFraction", None, "pct", 0.3, 0.65, 1, ""),
    ("Loot", "Cargo salvaged after battle", "ext_salvageCargoFractionPostCombat", None, "pct", 0.4, 0.575, 0.75, ""),
    ("Loot", "Resources from Threat fleets", "ext_threatResourceSalvageMult", None, "pct", 0.25, 0.625, 1, ""),
    ("Loot", "AI cores dropped", "ext_aiCoreDropFraction", None, "pct", 0.1, 0.55, 1, ""),
    ("Loot", "Dweller substrate dropped", "ext_substrateDropFraction", None, "pct", 0.4, 0.7, 1, ""),
    ("Loot", "Domain-grade parts from special salvage", "ext_partsSpecialSalvageDropFraction", None, "pct", 0.5, 0.75, 1, ""),
    ("Loot", "Domain-grade parts per 100 supplies salvaged", "ext_partsPerUnitOfSupplies", None, "per100", 0.025, 0.0375, 0.05, ""),
    ("Loot", "Domain-grade parts back when you scuttle a ship", "ext_partsFractionReturnedFromScuttling", None, "pct", 0.5, 0.625, 0.75,
     "Share of the parts used on the ship."),

    # Fuel
    ("Fuel", "Fuel tank size", "ext_fuelCapacityMult", None, "pct", 0.5, 0.75, 1, ""),
    ("Fuel", "Tanker fuel tank size", "ext_fuelCapacityMultTanker", None, "pct", 0.35, 0.675, 1, ""),
    ("Fuel", "Fuel use, frigates", "ext_fuelUseMult", 0, "x", 1, 1, 1, ""),
    ("Fuel", "Fuel use, destroyers", "ext_fuelUseMult", 1, "x", 1, 1, 1, ""),
    ("Fuel", "Fuel use, cruisers", "ext_fuelUseMult", 2, "x", 1.5, 1.25, 1, ""),
    ("Fuel", "Fuel use, capitals", "ext_fuelUseMult", 3, "x", 2, 1.5, 1, ""),

    # Colonies
    ("Colonies", "Colony growth needed", "ext_colonyGrowthRequiredMult", None, "x", 2, 1.5, 1, ""),
    ("Colonies", "Building cost", "ext_industryCostMult", None, "x", 2, 1.5, 1, ""),
    ("Colonies", "Building build time", "ext_industryBuiltTimeMult", None, "x", 2, 1.5, 1, ""),
    ("Colonies", "Corruption starts at monthly income", "ext_corruptionThreshold", None, "int", 200000, 400000, "never", ""),
    ("Colonies", "Corruption power", "ext_corruptionExponent", None, "num", 2, 1.5, "none",
     "2 means 4 times the income doubles the tax. Higher is harsher."),
    ("Colonies", "Heavy machinery to found a colony", "ext_establishColonyMachinery", None, "int", 200, 150, 100, ""),
    ("Colonies", "Supplies to found a colony", "ext_establishColonySupplies", None, "int", 500, 350, 200, ""),
    ("Colonies", "Survey crew cost", "ext_surveyCrewMult", None, "x", 1.5, 1.25, 1, ""),
    ("Colonies", "Survey heavy machinery cost", "ext_surveyMachineryMult", None, "x", 1.5, 1.25, 1, ""),

    # Officers
    ("Officers", "Officers for hire (also crew promotion offers)", "ext_officersAvailableFraction", None, "pct", 0.15, 0.575, 1, ""),
    ("Officers", "Administrators for hire", "ext_adminAvailableFraction", None, "pct", 0.1, 0.55, 1, ""),
    ("Officers", "Officers in cryopods", "ext_cryopodOfficersFraction", None, "pct", 0.5, 0.75, 1, ""),
    ("Officers", "Administrators in cryopods", "ext_cryopodAdminsFraction", None, "pct", 0.1, 0.55, 1, ""),

    # Experience
    ("Experience", "Story points per level", "ext_storyPointsPerLevel", None, "int", 2, 3, 4, ""),
    ("Experience", "Bonus XP for a clean disengage", "ext_bonusXP_cleanDisengage", None, "pct", 0, 0.5, 1, ""),
    ("Experience", "Bonus XP for avoiding a cargo scan", "ext_bonusXP_avoidCargoScan", None, "pct", 0.5, 0.75, 1, ""),
    ("Experience", "Recovering a ship gives no bonus XP from (DP)", "ext_bonusXP_recoverNoBonusXPDeploymentPoints", None, "int", 5, 17, 30, ""),

    # Hazards and missions
    ("Hazards", "Hyperstorm and asteroid damage", "ext_environmentalDamageMult", None, "x", 2, 1.5, 1, ""),
    ("Hazards", "Transverse Jump CR loss", "ext_transverseJumpDamageMult", None, "x", 5, 3, 1, ""),
    ("Hazards", "Cargo scan: chance to find contraband", "ext_cargoScanFindContrabandMult", None, "x", 2, 1.5, 1, ""),
    ("Hazards", "Cargo scan: penalty spread over ships", "ext_cargoScanNumShipsMult", None, "x", 4, 2.5, 1, ""),
    ("Hazards", "Cargo scan: CR lost", "ext_cargoScanShipDamageMult", None, "x", 2, 1.5, 1, ""),
    ("Hazards", "Sensor strength above base needed for Analyze missions", "ext_analyzeMissionSensorStrengthAboveBaseRequired", None, "int", 200, 100, "none", ""),
    ("Hazards", "Value of specimens turned in to Inesis", "ext_ZGRTurnInValueMult", None, "pct", 0.3, 0.65, 1, ""),
    ("Hazards", "Delivery missions with large amounts", "ext_deliveryMissionHighQuantityChanceMult", None, "pct", 0.1, 0.55, 1, ""),

    # Retirement and the spacer start
    ("Retirement", "Retirement, earliest cycle", "ext_retirementMinCycles", None, "int", 25, 40, "never",
     "0 turns retirement off. Keep it at or below the latest cycle."),
    ("Retirement", "Retirement, latest cycle", "ext_retirementMaxCycles", None, "int", 30, 50, "never", ""),
    ("Retirement", "Cost to delay retirement, base", "ext_retirementDelayCostBase", None, "int", 20000, 10000, "none", ""),
    ("Retirement", "Cost to delay retirement, per month", "ext_retirementDelayCostPerMonth", None, "int", 1000, 500, "none", ""),
    ("Retirement", "Cost to delay retirement, at most", "ext_retirementDelayCostMax", None, "int", 50000, 25000, "none", ""),
    ("Retirement", "Spacer start: monthly share of credits above 12 months of pay", "ext_spacerSharePerMonth", None, "pct", 0.1, 0.05, "none", ""),
    ("Retirement", "Spacer start: extra debt per level", "ext_extraSpacerDebtPerLevel", None, "int", 2000, 1000, 0, ""),

    # Kept as in survival mode by default
    ("Survival help", "Threats that grow with time: slowdown", "ext_timeBasedThingsDelayFactor", None, "x", 3, 3, 1,
     "Pirate raids, pirate base strength and the like grow this many times slower."),
    ("Survival help", "Domain-grade parts for sale", "ext_partsForSaleFraction", None, "x", 2, 2, 1, ""),
    ("Survival help", "Custom production order size (bar contacts)", "ext_barCustomProductionMaxValueMult", None, "x", 3, 3, 1, ""),
    ("Survival help", "Custom production order size (your industry)", "ext_playerIndustryCustomProductionMaxValueMult", None, "x", 3, 3, 1, ""),
    ("Survival help", "Ship storage fee", "ext_shipStoragePriceMult", None, "pct", 0.5, 0.5, 1, ""),
    ("Survival help", "Ship sell value per Domain-grade part used on d-mods", "ext_shipSellValueIncreasePerPartUsed", None, "int", 5000, 5000, 0, ""),
    ("Survival help", "Ship sell value per S-mod", "ext_shipSellValueMultPerSMod", None, "pct", 1, 1, 0,
     "Keep it the same as the buy price per S-mod, or buying and selling S-modded ships makes credits."),
    ("Survival help", "Ship buy price per S-mod", "ext_shipBuyValueMultPerSMod", None, "pct", 1, 1, 0,
     "Keep it the same as the sell value per S-mod, or buying and selling S-modded ships makes credits."),
    ("Survival help", "Weapons and fighter LPCs dropped by Threat fleets", "ext_threatNonResourceDropMult", None, "x", 2, 2, 1,
     "Applied on top of the weapon and fighter LPC drop settings."),
    ("Survival help", "Crew at military markets", "ext_crewForSaleMilitaryMult", None, "x", 1.5, 1.5, 1, ""),
    ("Survival help", "Marines at military markets", "ext_marinesForSaleMilitaryMult", None, "x", 1.5, 1.5, 1, ""),
    ("Survival help", "Supplies at military markets", "ext_suppliesForSaleMilitaryMult", None, "x", 1.2, 1.2, 1, ""),
    ("Survival help", "Fuel at military markets", "ext_fuelForSaleMilitaryMult", None, "x", 1.2, 1.2, 1, ""),
    ("Survival help", "Personnel for sale at bad reputation", "ext_personnelForSaleMinMultBadRep", None, "pct", 0.25, 0.25, "no effect", ""),
    ("Survival help", "Personnel for sale at good reputation", "ext_personnelForSaleMaxMultGoodRep", None, "pct", 2, 2, "no effect", ""),
    ("Survival help", "Weapons and fighters sold back", "ext_weaponAndFighterSellPriceMult", None, "x", 1.5, 1.5, "vanilla ratio",
     "Applied after the raised price."),
    ("Survival help", "Hull mod specs sold back", "ext_hullmodSellPriceMult", None, "pct", 0.25, 0.25, "vanilla ratio",
     "Applied after the raised price."),
    ("Survival help", "Ship price kept per d-mod", "ext_shipBuyPriceMultPerDMod", None, "pct", 0.85, 0.85, "none", ""),

    # Rules
    ("Rules", "Military market needs a commission", "ext_militaryMarketRequiresCommission", None, "bool", True, True, False, ""),
    ("Rules", "Galatia Academy stipend removed", "ext_removeGalatiaStipend", None, "bool", True, True, False, "Only takes effect in a new game."),
    ("Rules", "Fewer Legion XIV wrecks", "ext_reduceLegionXIVSpawns", None, "bool", True, True, False, NEW_GAME),
    ("Rules", "Derelicts in worse condition", "ext_reduceDerelictQuality", None, "bool", True, True, False, NEW_GAME),
    ("Rules", "Stronger Alpha Site defenders", "ext_strongerAlphaSiteDefenders", None, "bool", True, True, False, NEW_GAME),
    ("Rules", "More dangerous Mk I Threat", "ext_moreDangerousMkIThreat", None, "bool", True, True, False, ""),
    ("Rules", "Worse hand-me-down freighter (5 d-mods)", "ext_worseHandMeDownFreighter", None, "bool", True, True, False, ""),
    ("Rules", "Analyze missions need sensor strength", "ext_analyzeMissionRequiresSensorStrength", None, "bool", True, True, False, ""),
]

# On/off switches (LunaLib only). Every key that is not a yes/no rule gets one switch, placed above its rows.
# Off writes the vanilla value instead of the slider value. Keys listed here share one switch; any other key
# gets its own, named after its row label.
GROUPS = {
    "ext_shipBuyPriceMult": ("shipBuyPriceMult", "Ship prices"),
    "ext_officerCombatPay": ("officerCombatPay", "Officer pay per battle"),
    "ext_recoveryNonOwnSPCost": ("recoveryNonOwnSPCost", "Story points to recover a ship"),
    "ext_recoveryNonOwnSPCostCiv": ("recoveryNonOwnSPCostCiv", "Story points to recover a civilian ship"),
    "ext_fuelUseMult": ("fuelUseMult", "Fuel use"),
    "ext_corruptionThreshold": ("corruption", "Corruption"),
    "ext_corruptionExponent": ("corruption", "Corruption"),
    "ext_retirementMinCycles": ("retirement", "Retirement"),
    "ext_retirementMaxCycles": ("retirement", "Retirement"),
    "ext_retirementDelayCostBase": ("retirement", "Retirement"),
    "ext_retirementDelayCostPerMonth": ("retirement", "Retirement"),
    "ext_retirementDelayCostMax": ("retirement", "Retirement"),
}

# The game value a switched-off key gets, where the vanilla column is not that number already.
# A string is the name of the base game setting to copy, so a mod that changes it is respected.
OFF = {
    "ext_officerCombatPay": 0,                       # pay = salary x 0, so none
    "ext_corruptionThreshold": 1e30,                 # income never gets there
    "ext_corruptionExponent": 1,                     # unused once the threshold is never reached
    "ext_retirementMinCycles": 0,                    # the game turns retirement off at 0
    "ext_retirementMaxCycles": 0,
    "ext_retirementDelayCostBase": 0,
    "ext_retirementDelayCostPerMonth": 0,
    "ext_retirementDelayCostMax": 0,
    "ext_spacerSharePerMonth": 0,                    # the game turns the share off at 0
    "ext_analyzeMissionSensorStrengthAboveBaseRequired": 0,
    "ext_personnelForSaleMinMultBadRep": 1,          # 1 = reputation does not change the amount
    "ext_personnelForSaleMaxMultGoodRep": 1,
    "ext_weaponAndFighterSellPriceMult": 1,          # the game uses 1 outside survival
    "ext_hullmodSellPriceMult": 1,
    "ext_shipBuyPriceMultPerDMod": 1,
    "ext_storyPointsPerLevel": "storyPointsPerLevel",
    "ext_salvageCargoFractionPostCombat": "salvageCargoFraction",
    "ext_partsPerUnitOfSupplies": "partsPerUnitOfSupplies",
    "ext_partsFractionReturnedFromScuttling": "partsFractionReturnedFromScuttling",
}

# LunaLib tab order and a short header for each.
TABS = [
    ("Prices", "Prices"),
    ("Pay", "Pay"),
    ("Markets", "What markets sell"),
    ("Loot", "Loot and recovery"),
    ("Fuel", "Fuel"),
    ("Colonies", "Colonies"),
    ("Officers", "Officers and administrators"),
    ("Experience", "Story points and experience"),
    ("Hazards", "Hazards and missions"),
    ("Retirement", "Retirement and the spacer start"),
    ("Survival help", "Things survival mode makes easier"),
    ("Rules", "Survival rules"),
]

# Survival rules that are not settings, shown in the README only.
FIXED_RULES = [
    ("Start choices", "Survival starts only, no tutorial or difficulty choice", "vanilla starts, tutorial, Easy or Normal"),
    ("Abandoned stations in the core worlds", "cannot be used", "can be used"),
    ("Custom production ships", "arrive without weapons", "arrive armed"),
    ("Some special ships", "no random d-mods, one fixed flaw", "random d-mods"),
]
