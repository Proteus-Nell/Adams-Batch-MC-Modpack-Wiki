# Relapse

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Relapse](../../../assets/icons/mysticism/skill/relapse.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `mysticism:relapse` |
| **Modes** | 5 |
| **Cooldowns (s)** | 0 (mode cooldown), 1 (mode cooldown), 3 (mode cooldown), 2 (mode cooldown), 4 (mode cooldown) |
| **Activation** | Press |

</div>

> Collapse back into whence you came. Your memory is fleeting and the people you once knew start to forget you as well. Relapse and claim what belongs to you.

## Modes

| # | Mode |
|---|---|
| 1 | Aleph |
| 2 | Bet |
| 3 | Gimel |
| 4 | Daleth |
| 5 | Aleph: Null |

## How it works

- Activated by pressing the skill key

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| attackDamage | multiplier - 1 | multiply total |

## Obtaining

- Innate to mobs: [Memoires](../../mobs/memoires.md)
- Listed in the `intrinsicSkills` config option (config/mysticism/race/forgotten_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Related skills:** [Possession](../../../tensura-reincarnated/abilities/intrinsic-skills/possession.md)
- **Effects:** [Revenant's Horror](../../effects/revenants-horror.md), [Collective](../../effects/collective.md), [Sanctifying Light](../../effects/sanctifying-light.md), [Awakened Foresight](../../effects/awakened-foresight.md), [Unstable Requiem](../../effects/unstable-requiem.md), [Fragility](../../../tensura-reincarnated/effects/fragility.md)
- **Summons / entities:** [Relapse Clone](../../mobs/relapse-clone.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/intrinsic_config.toml`](../../configs/config-mysticism-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `Relapse.alephCloneFragilityForgotten` | 2 | The level of Fragility given to a clone created by the Aleph mode, when the user is a Forgotten. |
| `Relapse.alephCloneSlownessForgotten` | 5 | The level of Slowness given to a clone created by the Aleph mode, when the user is a Forgotten. |
| `Relapse.alephCloneFragilityRemnant` | 2 | The level of Fragility given to a clone created by the Aleph mode, when the user is a Remnant. |
| `Relapse.alephCloneSlownessRemnant` | 4 | The level of Slowness given to a clone created by the Aleph mode, when the user is a Remnant. |
| `Relapse.alephCloneFragilityEmptyWhole` | 1 | The level of Fragility given to a clone created by the Aleph mode, when the user is an Empty or Whole. |
| `Relapse.alephCloneSlownessEmptyWhole` | 3 | The level of Slowness given to a clone created by the Aleph mode, when the user is an Empty or Whole. |
| `Relapse.alephCloneFragilityRevenantAscended` | 1 | The level of Fragility given to a clone created by the Aleph mode, when the user is a Revenant or Ascended. |
| `Relapse.alephCloneSlownessRevenantAscended` | 1 | The level of Slowness given to a clone created by the Aleph mode, when the user is a Revenant or Ascended. |
| `Relapse.alephCloneFragilityInferiusExcelsius` | 0 | The level of Fragility given to a clone created by the Aleph mode, when the user is a Divine Inferius or Divine Excelsius. |
| `Relapse.alephCloneSlownessInferiusExcelsius` | 0 | The level of Slowness given to a clone created by the Aleph mode, when the user is a Divine Inferius or Divine Excelsius. |
| `Relapse.alephCooldownForgotten` | 300 | The cooldown of the Aleph mode, when the user is a Forgotten in seconds. |
| `Relapse.alephCooldownRemnant` | 240 | The cooldown of the Aleph mode, when the user is a Remnant in seconds. |
| `Relapse.alephCooldownEmptyWhole` | 180 | The cooldown of the Aleph mode, when the user is an Empty or Whole in seconds. |
| `Relapse.alephCooldownRevenantAscended` | 120 | The cooldown of the Aleph mode, when the user is a Revenant or Ascended in seconds. |
| `Relapse.alephCooldownInferiusExcelsius` | 60 | The cooldown of the Aleph mode, when the user is a Divine Inferius or Divine Excelsius in seconds. |
| `Relapse.betClonesSummonedRemnant` | 5 | The amount of clones summoned with the Bet mode, when the user is a Remnant. |
| `Relapse.betClonesSummonedEmptyWhole` | 7 | The amount of clones summoned with the Bet mode, when the user is an Empty or Whole. |
| `Relapse.betClonesSummonedRevenantAscended` | 10 | The amount of clones summoned with the Bet mode, when the user is a Revenant or Ascended. |
| `Relapse.betClonesSummonedInferiusExcelsius` | 10 | The amount of clones summoned with the Bet mode, when the user is a Divine Inferius or Divine Excelsius. |
| `Relapse.betCooldownRemnant` | 300 | The cooldown of the Bet mode, when the user is a Remnant in seconds. |
| `Relapse.betCooldownEmptyWhole` | 180 | The cooldown of the Bet mode, when the user is an Empty or Whole in seconds. |
| `Relapse.betCooldownRevenantAscended` | 120 | The cooldown of the Bet mode, when the user is a Revenant or Ascended in seconds. |
| `Relapse.betCooldownInferiusExcelsius` | 60 | The cooldown of the Bet mode, when the user is a Divine Inferius or Divine Excelsius in seconds. |
| `Relapse.gimelEmptyKills` | 10 | The number of kills required for the user to use Gimel if the user is an Empty. |
| `Relapse.gimelRevenantKills` | 50 | The number of kills required for the user to use Gimel if the user is a Revenant. |
| `Relapse.gimelInferiusKills` | 100 | The number of kills required for the user to use Gimel if the user has achieved Divinity. |
| `Relapse.gimelCooldownEmpty` | 180 | The cooldown of the Gimel mode if the user is an Empty. |
| `Relapse.gimelCooldownRevenant` | 120 | The cooldown of the Gimel mode if the user is a Revenant. |
| `Relapse.gimelCooldownInferius` | 60 | The cooldown of the Gimel mode if the user is a Divine Inferius. |
| `Relapse.gimelBeamsWhole` | 3 | The number of beams that descend onto a target if the user is a Whole. |
| `Relapse.gimelDamageWhole` | 30 | The damage of the beams that descend onto a target if the user is a Whole. |
| `Relapse.gimelBeamsAscended` | 5 | The number of beams that descend onto a target if the user is an Ascended. |
| `Relapse.gimelDamageAscended` | 40 | The damage of the beams that descend onto a target if the user is an Ascended. |
| `Relapse.gimelBeamsExcelsius` | 10 | The number of beams that descend onto a target if the user is a Divine Excelsius. |
| `Relapse.gimelDamageExcelsius` | 50 | The damage of the beams that descend onto a target if the user is a Divine Excelsius. |
| `Relapse.gimelDurationHoly` | 30 | The duration in seconds that target marking will last while Gimel is activated on the Excelsius path. |
| `Relapse.gimelCooldownWhole` | 180 | The cooldown of the Gimel mode if the user is a Whole. |
| `Relapse.gimelCooldownAscended` | 120 | The cooldown of the Gimel mode if the user is an Ascended. |
| `Relapse.gimelCooldownExcelsius` | 60 | The cooldown of the Gimel mode if the user is a Divine Excelsius. |
| `Relapse.dalethDurationRevenant` | 30 | The duration of the Daleth mode if the user is a Revenant, in seconds. |
| `Relapse.dalethDurationInferius` | 60 | The cooldown of the Daleth mode if the user is a Divine Inferius, in seconds. |
| `Relapse.dalethDurationAscended` | 30 | The duration of the Daleth mode if the user is an Ascended, in seconds. |
| `Relapse.dalethDurationExcelsius` | 60 | The cooldown of the Daleth mode if the user is a Divine Excelsius, in seconds. |
| `Relapse.dalethCooldownRevenant` | 600 | The cooldown of the Daleth mode if the user is a Revenant, in seconds. |
| `Relapse.dalethCooldownInferius` | 300 | The cooldown of the Daleth mode if the user is a Divine Inferius, in seconds. |
| `Relapse.dalethCooldownAscended` | 600 | The cooldown of the Daleth mode if the user is an Ascended, in seconds. |
| `Relapse.dalethCooldownExcelsius` | 300 | The cooldown of the Daleth mode if the user is a Divine Excelsius, in seconds. |
| `Relapse.alephNullCooldownInferius` | 600 | The cooldown placed on both Aleph and Aleph: Null when Aleph: Null is used as a Divine Inferius. |
| `Relapse.alephNullInferiusCollective` | 120 | The seconds of Collective given to the user if the user uses Aleph: Null as a Divine Inferius. |
| `Relapse.alephNullCooldownExcelsius` | 300 | The cooldown placed on both Aleph and Aleph: Null when Aleph: Null is used as a Divine Excelsius. |
| `Relapse.alephNullExcelsiusRange` | 20 | The range of the Aleph: Null mode, when the user is a Divine Excelsius. |
| `Relapse.alephNullExcelsiusInvincibility` | 60 | The seconds of invincibility given to an Aleph clone if the user uses Aleph: Null as a Divine Excelsius. |

## Tags

`tensura:skills/intrinsic_skills`
