# Investigator

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Investigator](../../../assets/icons/trnightmare/skill/investigator.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:investigator` |
| **Modes** | 4 |
| **Activation** | Toggle, Press, Hold |

</div>

> In pursuit of all that interests you, there are many things to find, be it danger, treasure, students, or more.

## Modes

| # | Mode |
|---|---|
| 1 | Analytical Appraisal |
| 2 | Pursuit of Truth |
| 3 | Book of Truth |
| 4 | Pursuit of Tutelage |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| melee | 50 | add |
| projectile | 25 | add |
| ignore | 40 | add |
| crit | 30 | add |

## Obtaining

- Listed in the `astralExtraUniqueSkills` config option (config/nightmare/ability/skill/nightmare_ult.toml): Extra unique skill IDs merged into Astral Light Skill Creation (after Tensura Creator).

## Related

- **Related skills:** [｢ Faust, Lord of Investigation ｣](../ultimate-skills/faust.md)
- **Summons / entities:** Tensura
- **Referenced by:** [｢ Faust, Lord of Investigation ｣](../ultimate-skills/faust.md), [｢ Nyarlathotep, King of Chaos ｣](../ultimate-skills/nyarlathotep.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `Investigator.mpAcquirement` | 75,000 | Magicule Acquirement Cost. |
| `Investigator.appraisalLevel` | 5 | Level of Analytical Appraisal. |
| `Investigator.appraisalLevelMastered` | 15 | Level of Analytical Appraisal when Mastered. |
| `Investigator.critChance` | 30 | Critical Attack chance. |
| `Investigator.dodgeChanceIgnore` | 40 | Dodge ignoring chance. |
| `Investigator.dodgeChance` | 50 | Dodge chance. |
| `Investigator.dodgeChanceProjectile` | 25 | Projectile dodge chance. |
| `Investigator.surpriseBlocks` | "minecraft:tnt", "minecraft:tnt_minecart", "minecraft:end_crystal", "minecraft:trapped_chest", "minecraft:powdered_snow", "minecraft:sculk_sensor" | List of blocks highlighted by Pursuit of Surprise. |
| `Investigator.treasureBlocks` | "tensura:charybdis_core", "minecraft:chest", "minecraft:barrel", "minecraft:dragon_egg", "minecraft:ancient_debris", "tensura:magic_ore" | List of blocks highlighted by Pursuit of Treasure. |
| `Investigator.tutelageCooldown` | 60 | Cooldown for Pursuit of Tutelage. |
| `Investigator.presenceSense` | 3 | The level of Presence Sense when activated. |
| `Investigator.presenceRadius` | 20 | The bonus Presence Sense Radius when activated. |
| `Investigator.learningPoint` | 10 | Learning point boost for skills |
| `Investigator.masteryPoint` | 10 | Mastery point gain for Skills |
