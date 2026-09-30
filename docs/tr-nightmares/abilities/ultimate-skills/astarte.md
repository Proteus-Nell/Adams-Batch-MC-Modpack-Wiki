# ｢ Astarte, Lord of Heaven ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:astarte` |
| **Modes** | 5 |
| **Acquisition cost (MP)** | 1,900,000 |
| **Max mastery** | 1,000 |
| **Activation** | Press, Hold |

</div>

> An ultimate skill that governs heavenly authority and divine administration.

## Modes

| # | Mode |
|---|---|
| 1 | Skill Evolution |
| 2 | Recycle |
| 3 | Magicule Furnace |
| 4 | True Apocrypha |
| 5 | Divine Darkness |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| atk | atk bonus | add |
| armor | armor bonus | add |
| inst | amount | add |

## Obtaining

- Listed in the `virtueDominionSkills` config option (config/nightmare/ability/skill/nightmare_ult.toml): Virtue skills that Ultimate Dominion can copy from targets.
- Listed in the `skillEngraveBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skills that cannot be engraved through Amatsumara skill engrave.
- Acquisition checks: [｢ Astarte, Lord of Heaven ｣](astarte.md), [Designer](../unique-skills/designer.md)
- In-game message: *Designer ascends. Astarte, Lord of Heaven, awakens.*

## Related

- **Related skills:** [Designer](../unique-skills/designer.md), [Darkness Cannon](../../../tensura-reincarnated/abilities/spiritual-magic/darkness-cannon.md)
- **Summons / entities:** Tensura, Holy Cannon Projectile
- **Referenced by:** [｢ Astaroth, King of Fallen ｣](astaroth.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Astarte.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Astarte.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Astarte.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Astarte.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Astarte.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Astarte.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Astarte.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Astarte.enableUltimateEvolution` | true |  |
| `Astarte.mpAcquirement` | 1,900,000 |  |
| `Astarte.masteredSkillsRequired` | 100 | Mastered skills required for Astarte evolution. |
| `Astarte.mobKillsRequired` | 500 | Mob kills required for Astarte evolution. |
| `Astarte.designersPlanLearningBonus` | 12 |  |
| `Astarte.designersPlanMasteryBonus` | 12 |  |
| `Astarte.maxMasteryForUniqueCreate` | 1,000 |  |
| `Astarte.uniqueCreateMpMultiplier` | 6 |  |
| `Astarte.uniqueTempMasteryCost` | 10,000 |  |
| `Astarte.uniquePermMasteryCost` | 5,000 |  |
| `Astarte.ultimateTempMasteryCost` | 8,000 |  |
| `Astarte.recycleBonusChance` | 0.15 |  |
| `Astarte.recycleBonusChanceMastered` | 0.2 |  |
| `Astarte.recycleBonusMpFraction` | 0.1 |  |
| `Astarte.recycleBonusMpFractionMastered` | 0.2 |  |
| `Astarte.furnaceRestorePercent` | 0.05 |  |
| `Astarte.furnaceRestorePercentMastered` | 0.07 |  |
| `Astarte.furnaceMaxMpPercent` | 2.5 |  |
| `Astarte.apocryphaDrainPercent` | 0.08 |  |
| `Astarte.apocryphaDrainPercentMastered` | 0.06 |  |
| `Astarte.apocryphaAtkBonus` | 30 |  |
| `Astarte.apocryphaAtkBonusMastered` | 60 |  |
| `Astarte.apocryphaArmorBonus` | 35 |  |
| `Astarte.apocryphaArmorBonusMastered` | 70 |  |
| `Astarte.divineDarknessDamage` | 100 |  |
| `Astarte.divineDarknessDamageMastered` | 250 |  |
| `Astarte.divineDarknessMpCostPercent` | 0.035 |  |

## In-game messages

<details markdown><summary>Show 7 messages</summary>

- True Apocrypha activated.
- True Apocrypha deactivated.
- True Apocrypha ended - out of Magicules!
- Magicule Furnace is full!
- Not enough Magicules for Divine Darkness Barrage!
- Use Deep Analysis to store skills first.
- Heavenly Design requires Astarte mastery to forge unique skills.

</details>

## Tags

`tensura:skills/ultimate_skills`
