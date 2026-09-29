# Poison Dragon Armor

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `trnightmare:poison_dragon_armor` |
| **Activation** | Toggle |

</div>

> An intrinsic armor skill that coats the user in toxic draconic defenses.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| armor | ulate armor | add |
| toughness | ulate toughness | add |

## Obtaining

- Listed in the `intrinsicSkills` config option (config/nightmare/race/axolotl/salamander_config.toml): List of skills obtained by this race.

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_intrinsic.toml`](../../configs/config-nightmare-ability-skill-nightmare-intrinsic.md).

| Option | Default | Description |
|---|---|---|
| `PoisonDragonArmor.armorNormal` | 50 | Armor bonus when not mastered. |
| `PoisonDragonArmor.armorMastered` | 100 | Armor bonus when mastered. |
| `PoisonDragonArmor.toughnessNormal` | 8 | Toughness when not mastered. |
| `PoisonDragonArmor.toughnessMastered` | 16 | Toughness when mastered. |
| `PoisonDragonArmor.masteryTickInterval` | 10 | Mastery tick interval while toggled. |
