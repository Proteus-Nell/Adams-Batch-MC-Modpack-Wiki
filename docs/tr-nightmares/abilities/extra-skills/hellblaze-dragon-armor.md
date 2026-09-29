# Hellblaze Dragon Armor

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Hellblaze Dragon Armor](../../../assets/icons/trnightmare/skill/hellblaze_dragon_armor.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `trnightmare:hellblaze_dragon_armor` |
| **Activation** | Toggle |

</div>

> Ignites the body in cursed hellfire and draconic fury, granting immunity to fire and unleashing burning retaliation against attackers.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| armor | armor amount | add |
| toughness | toughness amount | add |
| attack | attack amount | add |

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_intrinsic.toml`](../../configs/config-nightmare-ability-skill-nightmare-intrinsic.md).

| Option | Default | Description |
|---|---|---|
| `HellblazeDragonArmor.epAcquirement` | 25,000 | Learning cost. |
| `HellblazeDragonArmor.armorNormal` | 40 | Armor when not mastered. |
| `HellblazeDragonArmor.armorMastered` | 80 | Armor when mastered. |
| `HellblazeDragonArmor.toughnessNormal` | 50 | Toughness when not mastered. |
| `HellblazeDragonArmor.toughnessMastered` | 500 | Toughness when mastered. |
| `HellblazeDragonArmor.attackBonusNormal` | 30 | Attack damage bonus when not mastered. |
| `HellblazeDragonArmor.attackBonusMastered` | 300 | Attack damage bonus when mastered. |
| `HellblazeDragonArmor.masteryTickInterval` | 10 | Mastery tick interval while toggled. |
