# `config/tensura/ascension-races.toml`

<small>[Ascension](../index.md) &rsaquo; [Configs](index.md)</small>

## `[Races.Angel.angel]`

Angel — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Angel.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 80 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 480 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.2 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 3 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 10,000 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 20,000 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 0 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 0 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Angel.archangel]`

Archangel — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Archangel.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 230 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 1,380 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.3 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 5 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 200,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 100,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Angel.seraphim]`

Seraphim — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Seraphim.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 450 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 2,700 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.4 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 8 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 500,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 250,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Angel.divine_angel]`

Divine Angel — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Divine Angel.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 770 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 4,620 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.5 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 12 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 1,250,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 625,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Angel.fallen_angel]`

Fallen Angel — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Fallen Angel.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 770 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 4,620 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.5 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 12 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 1,250,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 625,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Angel.cosmic_deity]`

Cosmic Deity — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Cosmic Deity.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 1,350 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 8,100 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.7 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 16 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 4,000,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 2,000,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Angel.chaotic_deity]`

Chaotic Deity — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Chaotic Deity.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 1,350 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 8,100 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.7 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 16 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 4,000,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 2,000,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Frog.frog]`

Frog — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Frog.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 80 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 480 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | -0.05 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 4 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 5,000 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 10,000 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 75,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 37,500 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Frog.giant_frog]`

Giant Frog — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Giant Frog.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 195 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 1,170 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | -0.1 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 5 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 75,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 37,500 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Frog.poison_toad]`

Poison Toad — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Poison Toad.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 355 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 2,130 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | -0.05 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 8 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 250,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 125,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Frog.swamp_sovereign]`

Swamp Sovereign — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Swamp Sovereign.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 540 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 3,240 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 11 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 600,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 300,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Frog.bog_ancient]`

Bog Ancient — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Bog Ancient.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 735 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 4,410 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.05 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 13 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 1,500,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 750,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Frog.venom_lord]`

Venom Lord — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Venom Lord.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 735 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 4,410 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.15 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 14 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 1,500,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 750,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Frog.frog_monarch]`

Frog Monarch — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Frog Monarch.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 1,020 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 6,120 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.2 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 17 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 2,000,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 1,000,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Kitsune.kitsune]`

Kitsune — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Kitsune.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 150 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 900 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.15 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 5 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 150,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 75,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Kitsune.three_tail_fox]`

Three-Tail Fox — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Three-Tail Fox.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 380 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 2,280 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.25 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 8 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 300,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 150,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Kitsune.six_tail_fox]`

Six-Tail Fox — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Six-Tail Fox.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 665 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 3,990 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.35 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 12 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 600,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 300,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Kitsune.nine_tail_fox]`

Nine-Tail Fox — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Nine-Tail Fox.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 1,070 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 6,420 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.5 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 16 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 900,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 450,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Kitsune.divine_kitsune]`

Divine Kitsune — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Divine Kitsune.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 1,250 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 7,500 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.6 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 18 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 2,200,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 1,100,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Bloodfiend.fledgling_bloodfiend]`

Fledgling Bloodfiend — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Fledgling Bloodfiend.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 80 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 480 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.1 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 4 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 3,000 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 8,000 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 50,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 25,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Bloodfiend.kindred_bloodfiend]`

Kindred Bloodfiend — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Kindred Bloodfiend.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 215 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 1,290 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.2 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 6 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 50,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 25,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Bloodfiend.blood_noble]`

Blood Noble — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Blood Noble.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 425 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 2,550 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.25 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 9 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 150,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 75,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Bloodfiend.elder_bloodfiend]`

Elder Bloodfiend — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Elder Bloodfiend.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 655 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 3,930 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.35 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 12 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 400,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 200,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Bloodfiend.progenitor_bloodfiend]`

Progenitor Bloodfiend — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Progenitor Bloodfiend.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 1,020 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 6,120 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.5 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 16 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 1,000,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 500,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Djinn.whisper_djinn]`

Whisper Djinn — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Whisper Djinn.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 65 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 390 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.1 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 3 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 5,000 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 12,000 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 30,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 15,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Djinn.trickster_djinn]`

Trickster Djinn — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Trickster Djinn.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 160 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 960 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.15 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 5 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 30,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 15,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Djinn.phantom_djinn]`

Phantom Djinn — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Phantom Djinn.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 285 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 1,710 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.2 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 6 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 80,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 40,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Djinn.royal_djinn]`

Royal Djinn — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Royal Djinn.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 430 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 2,580 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.25 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 8 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 200,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 100,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Djinn.wishbound_djinn]`

Wishbound Djinn — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Wishbound Djinn.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 605 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 3,630 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.3 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 10 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 400,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 200,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Djinn.primordial_djinn]`

Primordial Djinn — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Primordial Djinn.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 795 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 4,770 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.4 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 12 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 700,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 350,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Djinn.ascended_djinn]`

Ascended Djinn — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Ascended Djinn.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 970 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 5,820 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.5 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 13 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 1,200,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 600,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Djinn.sovereign_djinn]`

Sovereign Djinn — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Sovereign Djinn.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 1,135 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 6,810 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.6 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 14 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 2,000,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 1,000,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Djinn.infinite_djinn]`

Infinite Djinn — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Infinite Djinn.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 1,280 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 7,680 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.8 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 15 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 3,000,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 1,500,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Djinn.omniversal_djinn]`

Omniversal Djinn — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Omniversal Djinn.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 1,470 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 8,820 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 1 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 16 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 10,000,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 5,000,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Wight.cursed_mariner]`

Cursed Mariner — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Cursed Mariner.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 320 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 1,920 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.1 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 8 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 250,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 125,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Wight.cursed_dreadnaught]`

Cursed Dreadnaught — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Cursed Dreadnaught.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 610 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 3,660 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.2 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 12 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 600,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 300,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Wight.phantom_corsair]`

Phantom Corsair — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Phantom Corsair.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 875 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 5,250 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.3 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 15 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 1,000,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 500,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Wight.davy_jones]`

Davy Jones — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Davy Jones.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 1,130 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 6,780 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.4 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 18 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 1,500,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 750,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Dragonewt.ender_dragonewt]`

Ender Dragonewt — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Ender Dragonewt.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 0 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 0 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 0 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 200,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 100,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Dragonewt.void_dragonewt]`

Void Dragonewt — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Void Dragonewt.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 270 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 1,620 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.1 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 5 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 500,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 250,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Dragonewt.abyssal_dragonewt]`

Abyssal Dragonewt — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Abyssal Dragonewt.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 640 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 3,840 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.2 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 10 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 1,000,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 500,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Dragonewt.chaos_dragon]`

Chaos Dragon — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Chaos Dragon.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 1,150 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 6,900 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.35 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 16 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 2,500,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 1,250,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.CorruptedDragon.corrupted_dragonkin]`

Corrupted Dragonkin — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Corrupted Dragonkin.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 0 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 0 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 0 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 50,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 25,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.CorruptedDragon.corrupted_dragon]`

Corrupted Dragon — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Corrupted Dragon.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 230 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 1,380 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.1 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 5 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 125,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 62,500 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.CorruptedDragon.cursed_dragon]`

Cursed Dragon — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Cursed Dragon.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 555 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 3,330 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.2 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 10 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 500,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 250,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.CorruptedDragon.demonic_dragon]`

Demonic Dragon — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Demonic Dragon.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 1,015 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 6,090 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.35 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 16 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 1,000,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 500,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.CorruptedDragon.demon_dragon_god]`

Demon Dragon God — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Demon Dragon God.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 1,250 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 7,500 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.55 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 22 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 5,000,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 2,500,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Gazer.gazer]`

Gazer — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Gazer.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 65 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 390 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | -0.05 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 3 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 5,000 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 10,000 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 30,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 15,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Gazer.spectator_gazer]`

Spectator Gazer — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Spectator Gazer.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 160 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 960 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 5 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 100,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 50,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Gazer.mindwitness]`

Mindwitness — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Mindwitness.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 330 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 1,980 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.05 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 7 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 300,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 150,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Gazer.gauth]`

Gauth — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Gauth.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 560 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 3,360 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.1 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 10 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 800,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 400,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Gazer.beholder]`

Beholder — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Beholder.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 850 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 5,100 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.2 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 13 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 2,000,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 1,000,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Gazer.death_tyrant]`

Death Tyrant — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Death Tyrant.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 1,135 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 6,810 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.35 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 16 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 4,000,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 2,000,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Wukong.monkey]`

Monkey — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Monkey.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 80 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 480 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.1 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 4 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 1,000 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 2,000 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 25,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 12,500 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Wukong.monkey_warrior]`

Monkey Warrior — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Monkey Warrior.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 195 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 1,170 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.15 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 6 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 25,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 12,500 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Wukong.monkey_martial_artist]`

Monkey Martial Artist — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Monkey Martial Artist.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 355 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 2,130 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.25 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 9 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 100,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 50,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Wukong.monkey_king]`

Monkey King — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Monkey King.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 540 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 3,240 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.35 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 12 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 400,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 200,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Wukong.divine_king]`

Divine King — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Divine King.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 770 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 4,620 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.45 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 15 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 750,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 375,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Wukong.sun_wukong]`

Sun Wukong — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Sun Wukong.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 1,135 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 6,810 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.6 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 18 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 1,500,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 750,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Undead.zombie]`

Zombie — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Zombie.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 20 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 120 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 3 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 500 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 1,000 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 100,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 50,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Undead.undead_skeleton]`

Skeleton — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Skeleton.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 30 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 180 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.25 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 4 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 200,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 100,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Undead.skeleton_warrior]`

Skeleton Warrior — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Skeleton Warrior.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 75 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 450 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.3 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 7 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 350,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 175,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Undead.death_knight]`

Death Knight — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Death Knight.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 250 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 1,500 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.35 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 11 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 700,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 350,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Undead.dullahan]`

Dullahan — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Dullahan.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 600 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 3,600 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.45 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 15 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 1,500,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 750,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Undead.dark_lord_dullahan]`

Dark Lord Dullahan — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Dark Lord Dullahan.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 1,200 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 7,200 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.55 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 18 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 4,000,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 2,000,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Undead.mage_skeleton]`

Mage Skeleton — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Mage Skeleton.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 50 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 300 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.3 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 5 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 500,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 250,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Undead.elder_lich]`

Elder Lich — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Elder Lich.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 200 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 1,200 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.3 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 7 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 1,000,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 500,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Undead.lich]`

Lich — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Lich.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 450 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 2,700 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.35 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 9 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 2,000,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 1,000,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |

## `[Races.Undead.lich_king]`

Lich King — attribute bonuses and EP thresholds.

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Lich King.<br>Base races: when false, removed from the reincarnation pool.<br>Evolved races: reserved for future use, currently cosmetic. |
| `maxHealthBonus` | 1,100 | 0 to 1,000,000 | Flat bonus to max HP applied while this race is active. 0 = no modifier. |
| `spiritualHealthBonus` | 6,600 | 0 to 1,000,000 | Flat bonus to max spiritual HP applied while this race is active. 0 = no modifier. |
| `movementSpeedBonus` | 0.45 | -1 to 100 | Multiplier bonus to movement speed (0.20 = +20%). Negative = slower. 0 = no modifier. |
| `attackDamageBonus` | 12 | 0 to 1,000 | Flat bonus to melee attack damage. 0 = no modifier. |
| `startingEpMin` | 0 | 0 to 1,000,000,000,000 | Minimum starting EP rolled when this race is assigned. Used only for base races.<br>Set both min and max to 0 to skip the roll (correct default for evolved races). |
| `startingEpMax` | 0 | 0 to 1,000,000,000,000 | Maximum starting EP rolled when this race is assigned. Used only for base races. |
| `evolutionEpRequirement` | 4,000,000 | 0 to 1,000,000,000,000 | EP required to evolve INTO this race. 0 = no EP gate from config (base races,<br>or evolved races whose evolution uses only non-EP requirements). |
| `bonusEpOnEvolve` | 2,000,000 | 0 to 1,000,000,000,000 | Bonus EP granted automatically when a player evolves INTO this race.<br>Defaults to 50% of evolutionEpRequirement — a player who just paid<br>the entry cost gets half of it back as a head start. Set to 0 to<br>disable the bonus for this race. |
