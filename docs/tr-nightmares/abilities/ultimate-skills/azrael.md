# Azrael, Lord of Salvation

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![Azrael, Lord of Salvation](../../../assets/icons/trnightmare/skill/azrael.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:azrael` |
| **Modes** | 4 |
| **Acquisition cost (MP)** | 950,000 |
| **Max mastery** | 5,000 |
| **Cooldowns (s)** | 120 |
| **Activation** | Toggle, Press, Hold |

</div>

> A saving authority that turns mercy into execution, sanctifies the hunted, and shields its bearer behind quiet absolution.

## Modes

| # | Mode |
|---|---|
| 1 | Hostility Erasure |
| 2 | Retribution |
| 3 | Purgatory |
| 4 | Polar Star |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers when you take damage
- Triggers when you die
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| instance | amount | operation |

## Related

- **Effects:** [Salvation](../../effects/salvation.md)
- **Summons / entities:** Tensura

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Azrael.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Azrael.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Azrael.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Azrael.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Azrael.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Azrael.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Azrael.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Azrael.enableUltimateEvolution` | false | Whether Azrael can be obtained via evolution. |
| `Azrael.mpAcquirement` | 950,000 | Magicule acquirement cost. |
| `Azrael.dangerDetectionDodge` | 30 | Danger Detection melee/projectile dodge chance bonus. |
| `Azrael.dangerDetectionCrit` | 50 | Danger Detection critical attack chance bonus. |
| `Azrael.hostilityDamageMultiplier` | 0.01 | Hostility Erasure damage multiplier while peaceful. |
| `Azrael.hostilityPacifyRadius` | 32 | Hostility Erasure pacify radius. |
| `Azrael.retributionChance` | 0.3 | Retribution Salvation proc chance. |
| `Azrael.retributionChanceMastered` | 0.6 | Retribution Salvation proc chance when mastered. |
| `Azrael.salvationDurationTicks` | 600 | Retribution Salvation duration in ticks. |
| `Azrael.salvationCap` | 8 | Retribution Salvation stack cap. |
| `Azrael.salvationCapMastered` | 12 | Retribution Salvation stack cap when mastered. |
| `Azrael.retributionDamagePerLevel` | 250 | Retribution spiritual damage dealt per Salvation level. |
| `Azrael.retributionRadius` | 128 | Retribution burst radius. |
| `Azrael.purgatoryRadius` | 128 | Purgatory target search radius. |
| `Azrael.purgatorySlashRange` | 12 | Purgatory slash range. |
| `Azrael.purgatorySlashIntervalTicks` | 5 | Purgatory slash interval in ticks while channeling. |
| `Azrael.purgatoryAttackMultiplier` | 2 | Purgatory slash attack damage multiplier. |
| `Azrael.purgatoryExecuteEpRatio` | 0.5 | Purgatory execution threshold as a fraction of the user's EP. |
| `Azrael.polarStarCooldownSeconds` | 120 | Polar Star revival cooldown in Tensura seconds. |
| `Azrael.polarStarRestoreCap` | 0.5 | Maximum HP/SHP restoration ratio for Polar Star revival. |
| `ultMasteryConfig.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |

## In-game messages

<details markdown><summary>Show 3 messages</summary>

- Hostility Erasure enabled.
- Hostility Erasure ended.
- %1$s has been marked as Saved. Total Saved: %2$s

</details>

## Tags

`tensura:skills/ultimate_skills`
