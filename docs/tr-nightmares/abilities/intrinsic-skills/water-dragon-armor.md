# Water Dragon Armor

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `trnightmare:water_dragon_armor` |
| **Activation** | Toggle |

</div>

> An intrinsic armor skill that surrounds the user with fluid draconic protection.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| armor | ulate armor | add |
| toughness | ulate toughness | add |

## Obtaining

- Listed in the `intrinsicSkills` config option (config/nightmare/race/axolotl/axolotl_config.toml): List of skills obtained by this race.

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_intrinsic.toml`](../../configs/config-nightmare-ability-skill-nightmare-intrinsic.md).

| Option | Default | Description |
|---|---|---|
| `WaterDragonArmor.armorNormal` | 50 | Armor bonus when not mastered. |
| `WaterDragonArmor.armorMastered` | 100 | Armor bonus when mastered. |
| `WaterDragonArmor.toughnessNormal` | 8 | Toughness when not mastered. |
| `WaterDragonArmor.toughnessMastered` | 16 | Toughness when mastered. |
| `WaterDragonArmor.masteryTickInterval` | 10 | Mastery tick interval while toggled. |
