# Healer

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Healer](../../../assets/icons/tensura/skill/healer.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:healer` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 50,000 |
| **Cooldowns (s)** | 3 mastered, 5 otherwise, 1 mastered, 3 otherwise |
| **Activation** | Press, Hold |

</div>

> Mend wounds with a touch or unleash devastating afflictions, capable of both salvation and suffering.

## Modes

| # | Mode |
|---|---|
| 1 | Heal |
| 2 | Infection |
| 3 | Plague |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Infection | 200 |  |
| Plague | 300 |  |
| other modes | 0 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key

## Obtaining

- Innate to mobs: [Shinji Tanimura](../../mobs/shinji-tanimura.md)
- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Related

- **Effects:** [Infection](../../effects/infection.md)
- **Summons / entities:** Tensura
- **Referenced by:** [Pride Manas](../../../tr-nightmares/abilities/ultimate-skills/pride-manas.md), [Timeless Mage](../../../ascension/abilities/ultimate-skills/timeless-mage.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Healer.mpAcquirement` | 50,000 | Magicule Acquirement Cost. |
| `Healer.magiculeCostInfection` | 200 | Magicule Cost to apply/remove Infection for other entities. |
| `Healer.magiculeCostHP` | 80 | Magicule Cost to heal each HP. |
| `Healer.magiculeCostHPMastered` | 40 | Magicule Cost to heal each HP when mastered. |
| `Healer.magiculeCostSHP` | 60 | Magicule Cost to heal each SHP when mastered. |
| `Healer.cooldown` | 5 | The cooldown in second when activated Heal. |
| `Healer.cooldownMastered` | 3 | The cooldown in second when activated Heal with mastery. |
| `Healer.infectionDuration` | 900 | The duration in tick of the Infection effect when applied on targets. |
| `Healer.plagueRadius` | 7 | The radius in block of the Plague Mode. |
| `Healer.cooldownInfection` | 3 | The cooldown in second when activated Infection. |
| `Healer.cooldownInfectionMastered` | 1 | The cooldown in second when activated Infection with mastery. |

Set in [`config/tensura/ability/ability_config.toml`](../../configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/unique_skills`
