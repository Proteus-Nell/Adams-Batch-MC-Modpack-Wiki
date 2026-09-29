# Wrath

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Wrath](../../../assets/icons/tensura/skill/wrath.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:wrath` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 100,000 |
| **Max mastery** | 1,500 |
| **Activation** | Hold |

</div>

> Unleash pure rage and use it to get infinitely stronger the longer your anger persists. Beware of the devastating drawback.

## Modes

| # | Mode |
|---|---|
| 1 | Breeder Reactor |
| 2 | Enrage |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 100 or 0 |  |

## How it works

- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect
- Triggers when you respawn

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `egoWhitelist` config option (config/nightmare/ability/skill/ego/general_config.toml): Skills allowed to develop ego if in whitelist mode
- Listed in the `DemonicSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): List of Demonic skills registry names that can be created via Demon Essence consumption. Format: modid:skill_name

## Related

- **Related skills:** [Spiritual Attack Nullification](../resistance-skills/spiritual-attack-nullification.md), [Spiritual Attack Resistance](../resistance-skills/spiritual-attack-resistance.md)
- **Effects:** [Rampage](../../effects/rampage.md)
- **Referenced by:** [｢ Alternative, Proxy Rights ｣](../../../tr-nightmares/abilities/ultimate-skills/alternative.md), [｢ Michael, Lord of Justice ｣](../../../tr-nightmares/abilities/ultimate-skills/michael.md), [｢ Satanael, Lord of Wrath ｣](../../../tr-nightmares/abilities/ultimate-skills/satanael.md), [Pride Manas](../../../tr-nightmares/abilities/ultimate-skills/pride-manas.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Wrath.mpAcquirement` | 100,000 | Magicule Acquirement Cost. |
| `Wrath.magiculeCostEnrage` | 100 | Magicule Cost to activate Enrage. |
| `Wrath.breederMultiplier` | 0.02 | The multiplier of the user's maximum magicule to gain every 100 ticks. |
| `Wrath.breederUnderChance` | 3 | The chance to gain an Rampage level when the user is under maximum Magicule (doubled with mastery). |
| `Wrath.breederAboveChance` | 6 | The chance to gain an Rampage level when the user is above maximum Magicule (doubled with mastery). |
| `Wrath.maxRampage` | 10 | The maximum level of Rampage the user can get from using Magicule Breader. |
| `Wrath.maxRampageMastered` | 20 | The maximum level of Rampage the user can get from using Magicule Breader when mastered. |
| `Wrath.breederDuration` | 600 | The duration in tick of the Rampage effect when using Magicule Breader. |
| `Wrath.rampageArmor` | 5 | The bonus armor points each level of Rampage on the user when using Magicule Breader. |
| `Wrath.rampageAttack` | 30 | The bonus attack points each level of Rampage on the user when using Magicule Breader. |
| `Wrath.rampageAttackSpeed` | 0.02 | The bonus attack speed each level of Rampage on the user when using Magicule Breader. |
| `Wrath.rampageSpeed` | 0.01 | The bonus speed points each level of Rampage on the user when using Magicule Breader. |
| `Wrath.rampageKnockbackResistance` | 0.1 | The bonus knockback resistance each level of Rampage on the user when using Magicule Breader. |
| `Wrath.enrageRadius` | 7 | The radius in block of the Enrage mode. |
| `Wrath.enrageDuration` | 400 | The base duration of the Rampage effect when using the Enrage mode. |
| `Wrath.enrageIncreaseTick` | 200 | The amount of tick activated needed to increase 1 level of Rampage when using the Enrage. |

Set in [`config/tensura/ability/skill_config.toml`](../../configs/config-tensura-ability-skill-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryUniqueSin` | 1,500 | The max amount of mastery point for Unique Skills of Sins. |
| `Mastery.masteryIntrinsic` | 100 | The max amount of mastery point for Intrinsic Skills. |
| `Mastery.masteryExtra` | 500 | The max amount of mastery point for Extra Skills. |
| `Mastery.masteryUnique` | 1,000 | The max amount of mastery point for Unique Skills. |
| `Mastery.masteryUniqueSin` | 1,500 | The max amount of mastery point for Unique Skills of Sins. |
| `Mastery.masteryUltimate` | 10,000 | The max amount of mastery point for Ultimate Skills. |

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

`tensura:skills/sin_skills`, `tensura:skills/unique_skills`, `tensura:skills/wrath`
