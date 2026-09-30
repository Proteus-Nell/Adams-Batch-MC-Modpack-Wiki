# ｢ Tantalous, King of Evil ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![｢ Tantalous, King of Evil ｣](../../../assets/icons/trnightmare/skill/tantalus.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:tantalus` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 600,000 |
| **Max mastery** | 35,000 |
| **Activation** | Press, Hold |

</div>

## Modes

| # | Mode |
|---|---|
| 1 | Evil Charisma |
| 2 | Soul Crushing Haki |
| 3 | Soul Destruction |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Adjusted by scrolling while active
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Does something when first learned

## Obtaining

- Acquisition checks: [Villain](../../../tensura-reincarnated/abilities/unique-skills/villain.md), [｢ Tantalous, King of Evil ｣](tantalus.md)
- In-game message: *%s has evolved into %s.*

## Related

- **Related skills:** [Villain](../../../tensura-reincarnated/abilities/unique-skills/villain.md), [Spiritual Attack Nullification](../../../tensura-reincarnated/abilities/resistance-skills/spiritual-attack-nullification.md), [Spiritual Attack Resistance](../../../tensura-reincarnated/abilities/resistance-skills/spiritual-attack-resistance.md)
- **Effects:** [Fear](../../../tensura-reincarnated/effects/fear.md)
- **Summons / entities:** Tensura

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Tantalus.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Tantalus.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Tantalus.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Tantalus.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Tantalus.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Tantalus.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Tantalus.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Tantalus.mpAcquirement` | 600,000 | The Cost for the Ultimate Skill: Tantalus. |
| `Tantalus.epAcquirement` | 2,000,000 | The EP requirement to qualify for Evil King Tantalus. |
| `Tantalus.evilCharismaRadius` | 20 | Evil Charisma radius. |
| `Tantalus.soulCrushingRadius` | 30 | Soul Crushing Haki radius. |
| `Tantalus.soulCrushingMagiculeCost` | 50 | Soul Crushing Haki magicule cost per second. |
| `Tantalus.soulCrushingResistedDuration` | 120 | Soul Crushing Haki duration when the target has resistance. |
| `Tantalus.soulCrushingDuration` | 2,400 | Soul Crushing Haki base duration in ticks. |
| `Tantalus.soulCrushingImmunityRatio` | 0.75 | Soul Crushing Haki EP immunity ratio. |
| `Tantalus.soulCrushingDamagePerStep` | 100 | Soul Crushing Haki damage per 20% EP difference. |
| `Tantalus.soulDestructionRadius` | 32 | Soul Destruction radius. |
| `Tantalus.soulDestructionSoulDivisor` | 1,000 | Soul Destruction soul gain divisor. |
| `Tantalus.soulCopyThreshold` | 25,000 | Soul Destruction soul threshold for skill absorption. |
| `Tantalus.taintedGrowthGainMastered` | 9 | Tainted Growth EP gain bonus when mastered. |
| `Tantalus.taintedGrowthGain` | 5 | Tainted Growth EP gain bonus while unmastered. |
| `Tantalus.villainCritChance` | 100 | Villain's Intimidation critical chance bonus. |
| `Tantalus.villainCritDamageBonus` | 1 | Villain's Intimidation critical damage bonus. |
| `Tantalus.villainDodgeNegateChance` | 10 | Villain's Intimidation dodge negate bonus. |
| `Tantalus.physicalSoulDamagePerSoul` | 0.01 | Physical attacks deal spiritual damage per soul point. |
| `Tantalus.physicalSoulDamageCap` | 250 | Physical soul damage cap. |
| `Tantalus.enableUltimateEvolution` | true | Whether Tantalus evolution is allowed. |
| `ultMasteryConfig.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `ultMasteryConfig.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `ultMasteryConfig.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `ultMasteryConfig.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `ultMasteryConfig.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `ultMasteryConfig.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `ultMasteryConfig.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `ultMasteryConfig.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |

## In-game messages

<details markdown><summary>Show 1 messages</summary>

- %s has evolved into %s.

</details>
