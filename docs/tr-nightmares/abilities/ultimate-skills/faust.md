# ｢ Faust, Lord of Investigation ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:faust` |
| **Modes** | 5 |
| **Acquisition cost (MP)** | 750,000 |
| **Max mastery** | 5,000 |
| **Activation** | Toggle, Press, Hold |

</div>

> Curiosity has always been your strong suit, learning came easy, and teaching just as much. You find yourself able to see and touch the information of the world itself.

## Modes

| # | Mode |
|---|---|
| 1 | Analytical Appraisal |
| 2 | Pursuit of Truth |
| 3 | Probability Manipulation |
| 4 | Book of Truth |
| 5 | Pursuit of Tutelage |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| melee | 50 | add |
| projectile | 25 | add |
| ignore | 40 | add |
| crit | 30 | add |
| melee | 1 | multiply total |
| crit | 100 | add |

## Obtaining

- Listed in the `astralMasteredCreationUltimates` config option (config/nightmare/ability/skill/nightmare_ult.toml): Ultimate skill IDs only offered from Astral Light Skill Creation when Astral Light is mastered.
- Acquisition checks: [Investigator](../unique-skills/investigator.md), [｢ Faust, Lord of Investigation ｣](faust.md)
- In-game message: *Your pursuit of truth deepens until knowledge itself bends to your will. [ Ultimate Skill: Faust, Lord of Investigation ] has been obtained.*

## Related

- **Related skills:** [Investigator](../unique-skills/investigator.md)
- **Referenced by:** [Investigator](../unique-skills/investigator.md), [｢ Nyarlathotep, King of Chaos ｣](nyarlathotep.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Faust.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Faust.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Faust.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Faust.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Faust.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Faust.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Faust.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Faust.mpAcquirement` | 750,000 | Magicule Acquirement Cost. |
| `Faust.appraisalLevel` | 15 | Level of Analytical Appraisal. |
| `Faust.appraisalLevelMastered` | 30 | Level of Analytical Appraisal when Mastered. |
| `Faust.critChance` | 30 | Critical Attack chance. |
| `Faust.dodgeChanceIgnore` | 40 | Dodge ignoring chance. |
| `Faust.dodgeChance` | 50 | Dodge chance. |
| `Faust.dodgeChanceProjectile` | 25 | Projectile dodge chance. |
| `Faust.surpriseBlocks` | "minecraft:tnt", "minecraft:tnt_minecart", "minecraft:end_crystal", "minecraft:trapped_chest", "minecraft:powdered_snow", "minecraft:sculk_sensor" | List of blocks highlighted by Pursuit of Surprise. |
| `Faust.treasureBlocks` | "tensura:charybdis_core", "minecraft:chest", "minecraft:barrel", "minecraft:dragon_egg", "minecraft:ancient_debris", "tensura:magic_ore" | List of blocks highlighted by Pursuit of Treasure. |
| `Faust.luckLevel` | 10 | Level of Luck from Probability Manipulation. |
| `Faust.critMultiplier` | 2 | Damage Multiplier for critical hits. |
| `Faust.presenceSense` | 4 | The level of Presence Sense when activated. |
| `Faust.presenceRadius` | 30 | The bonus Presence Sense Radius when activated. |
| `Faust.learningPoint` | 10 | Learning point boost |
| `Faust.masteryPoint` | 10 | Mastery point gain |
| `Faust.enableUltimateEvolution` | true | Whether Faust evolution is allowed. |
| `Faust.faustFulls` | 10 | Full investigations required for Faust |
| `ultMasteryConfig.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |

## Tags

`tensura:skills/ultimate_skills`
