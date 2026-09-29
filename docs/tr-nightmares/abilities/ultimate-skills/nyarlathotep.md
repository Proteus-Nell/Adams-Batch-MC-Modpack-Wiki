# ｢ Nyarlathotep, King of Chaos ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:nyarlathotep` |
| **Modes** | 6 |
| **Acquisition cost (MP)** | 1,550,000 |
| **Max mastery** | 35,000 |
| **Cooldowns (s)** | 30 |
| **Activation** | Toggle, Press, Hold |

</div>

> When you control the chances of anything happening, nothing goes without your say, but no one can predict what that say is.

## Modes

| # | Mode |
|---|---|
| 1 | Analytical Appraisal |
| 2 | Pursuit of Truth |
| 3 | Probability Manipulation |
| 4 | Parallel Existence |
| 5 | Book of Truth |
| 6 | Pursuit of Tutelage |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect
- Triggers when you take damage
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| melee | 80 | add |
| projectile | 50 | add |
| ignore | 70 | add |
| crit | 50 | add |
| melee | 4 | multiply total |
| crit | 100 | add |

## Obtaining

- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.
- Acquisition checks: [｢ Faust, Lord of Investigation ｣](faust.md), [｢ Nyarlathotep, King of Chaos ｣](nyarlathotep.md)
- In-game message: *Evolution complete: Nyarla has awakened.*

## Related

- **Related skills:** [Investigator](../unique-skills/investigator.md), [｢ Faust, Lord of Investigation ｣](faust.md), [Spacetime Manipulation](../extra-skills/spacetime-manipulation.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Nyarlathotep.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Nyarlathotep.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Nyarlathotep.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Nyarlathotep.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Nyarlathotep.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Nyarlathotep.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Nyarlathotep.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Nyarlathotep.mpAcquirement` | 1,550,000 | Magicule Acquirement Cost. |
| `Nyarlathotep.appraisalLevel` | 30 | Level of Analytical Appraisal. |
| `Nyarlathotep.appraisalLevelMastered` | 60 | Level of Analytical Appraisal when Mastered. |
| `Nyarlathotep.critChance` | 50 | Critical Attack chance. |
| `Nyarlathotep.dodgeChanceIgnore` | 70 | Dodge ignoring chance. |
| `Nyarlathotep.dodgeChance` | 80 | Dodge chance. |
| `Nyarlathotep.dodgeChanceProjectile` | 50 | Projectile dodge chance. |
| `Nyarlathotep.surpriseBlocks` | "minecraft:tnt", "minecraft:tnt_minecart", "minecraft:end_crystal", "minecraft:trapped_chest", "minecraft:powdered_snow", "minecraft:sculk_sensor" | List of blocks highlighted by Pursuit of Surprise. |
| `Nyarlathotep.treasureBlocks` | "tensura:charybdis_core", "minecraft:chest", "minecraft:barrel", "minecraft:dragon_egg", "minecraft:ancient_debris", "tensura:magic_ore" | List of blocks highlighted by Pursuit of Treasure. |
| `Nyarlathotep.luckLevel` | 10 | Level of Luck from Probability Manipulation. |
| `Nyarlathotep.critMultiplier` | 5 | Damage Multiplier for critical hits. |
| `Nyarlathotep.presenceSense` | 5 | The level of Presence Sense when activated. |
| `Nyarlathotep.presenceRadius` | 50 | The bonus Presence Sense Radius when activated. |
| `Nyarlathotep.learningPoint` | 30 | Learning point boost |
| `Nyarlathotep.masteryPoint` | 30 | Mastery point gain |
| `Nyarlathotep.damageMultiplier` | 4 | damage buff for elements from Nyarlathotep. |
| `Nyarlathotep.barrierEPThreshold` | 1.5 | EP threshold ratio for barrier shatter immunity. |
| `Nyarlathotep.barrierNormal` | 4 | Multi-Dimensional Barrier non-mastered |
| `Nyarlathotep.barrierMastered` | 6 | Multi-Dimensional Barrier mastered |
| `Nyarlathotep.cloneCooldown` | 30 | Cooldown for summoning a parallel Existence. |
| `Nyarlathotep.counterChance` | 0.3 | Chance to counter attack (Default: 30%) |
| `Nyarlathotep.enableUltimateEvolution` | true | Whether Nyarlathotep evolution is allowed. |
| `Nyarlathotep.nyarlaFulls` | 30 | Full investigations required for Nyarlathotep |
| `Nyarlathotep.nyarlaExistence` | 30,000,000 | The Existence value required for Nyarlathotep. |
| `ultMasteryConfig.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
