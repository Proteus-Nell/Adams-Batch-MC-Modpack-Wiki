# Lust

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Lust](../../../assets/icons/tensura/skill/lust.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:lust` |
| **Modes** | 5 |
| **Acquisition cost (MP)** | 100,000 |
| **Max mastery** | 1,500 |
| **Cooldowns (s)** | 5, 1, 3 mastered, 5 otherwise |
| **Activation** | Press, Hold |

</div>

> Assert your control over life and death. Drain your enemies of their strength or invigorate those under your wing.

## Modes

| # | Mode |
|---|---|
| 1 | Drain |
| 2 | Invigorate |
| 3 | Rebirth |
| 4 | Embracing Drain |
| 5 | Death Blessing |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Drain | 100 |  |
| other modes | 0 |  |
| Rebirth | 3,000 |  |
| Embracing Drain | 500 |  |
| Death Blessing | 7,500 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `egoWhitelist` config option (config/nightmare/ability/skill/ego/general_config.toml): Skills allowed to develop ego if in whitelist mode
- Listed in the `DemonicSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): List of Demonic skills registry names that can be created via Demon Essence consumption. Format: modid:skill_name

## Related

- **Effects:** [Lust Drain](../../effects/lust-drain.md), [Lust Embracement](../../effects/lust-embracement.md)
- **Referenced by:** [｢ Asmodeus, Lord of Lust ｣](../../../tr-nightmares/abilities/ultimate-skills/asmodeus.md), [｢ Michael, Lord of Justice ｣](../../../tr-nightmares/abilities/ultimate-skills/michael.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Lust.mpAcquirement` | 100,000 | Magicule Acquirement Cost. |
| `Lust.magiculeCostDrain` | 100 | Magicule Cost to activate Drain. |
| `Lust.magiculeCostRebirth` | 3,000 | Magicule Cost to activate Rebirth. |
| `Lust.magiculeCostEmbrace` | 500 | Magicule Cost to activate Embracing Drain. |
| `Lust.magiculeCostBless` | 7,500 | Magicule Cost to activate Death Blessing. |
| `Lust.magiculeCostHP` | 80 | Magicule Cost to heal each HP with Invigorate. |
| `Lust.magiculeCostHPMastered` | 40 | Magicule Cost to heal each HP with Invigorate with Mastery. |
| `Lust.drainEP` | 200 | The amount of EP drained from targets when using Drain. |
| `Lust.drainEPMastered` | 0.005 | The multiplier of EP drained from targets when using Drain with mastery. |
| `Lust.drainDuration` | 200 | The duration in tick of the Lust Drain effect applied on the user's attack when activated Drain. |
| `Lust.cooldownDrain` | 1 | The cooldown in second of the Drain Mode. |
| `Lust.cooldownInvigorate` | 5 | The cooldown in second when activated Invigorate. |
| `Lust.cooldownInvigorateMastered` | 3 | The cooldown in second when activated Invigorate with mastery. |
| `Lust.embraceDuration` | 100 | The duration in tick of the Embracing Drain effect. |
| `Lust.embraceEP` | 200 | The amount of EP drained from targets when using Embracing Drain. |
| `Lust.embraceEPMastered` | 0.005 | The multiplier of EP drained from targets when using Embracing Drain with mastery. |
| `Lust.blessRange` | 10 | The max range in block of the Death Blessing attack. |
| `Lust.blessRadius` | 3 | The radius in block of the Death Blessing attack. |
| `Lust.blessTime` | 100 | The amount of time in tick needed to activate the Death Blessing attack. |
| `Lust.blessInterference` | 6 | The level of movement interference when the target is being casted with Death Wish (-10% speed each level). |
| `Lust.blessEP` | 0.5 | The multiplier of the user's EP that the target needs to have below to take full effect of Death Blessing. |
| `Lust.blessHalfEP` | 0.75 | The multiplier of the user's EP that the target needs to have below to take half effect of Death Blessing. |
| `Lust.blessFullRestore` | 1 | The multiplier of the target's EP that the user will use for energy restoring when killed with full-effect Death Blessing. |
| `Lust.blessHalfDamage` | 0.5 | The multiplier of the target's HP that it takes when applied with half-effect Death Blessing. |
| `Lust.blessHalfRestore` | 0.25 | The multiplier of the target's EP that the user will use for energy restoring when killed with half-effect Death Blessing. |
| `Lust.blessMinimalEP` | 1 | The multiplier of the user's EP that the target needs to have below to take minimal effect of Death Blessing. |
| `Lust.blessMinimalDamage` | 0.25 | The multiplier of the target's HP that it takes when applied with minimal-effect Death Blessing. |
| `Lust.blessMinimalRestore` | 0.05 | The multiplier of the target's EP that the user will use for energy restoring when killed with minimal-effect Death Blessing. |
| `Lust.blessMPHeal` | 0.75 | The multiplier of the target's EP that the player will use to restore Magicule when killed with Death Blessing (the other half used for restoring Aura). |
| `Lust.cooldownBless` | 5 | The cooldown in second of the Death Bless mode. |

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
| `Learning.learningPointRequirement` | 100 | The number of learning points a new ability need to get to become fully learnt. |
| `Learning.learningPoint` | 1 | The base value of how many learning points the player gains when learning an ability. |
| `Learning.minBonus` | 0 | The min bonus learning points the player can gain when learning an ability. |
| `Learning.maxBonus` | 4 | The max bonus learning points the player can gain when learning an ability. |
| `Learning.learningCostMultiplier` | 5 | The multiplier of energy cost compared to normal cost when learning a new ability. |
| `Learning.learningPointRequirement` | 100 | The number of learning points a new ability need to get to become fully learnt. |
| `Learning.learningCooldown` | 10 | The number of seconds of cooldown when a new ability gains a learning point. |
| `Learning.learningFailCooldown` | 3 | The number of seconds of cooldown when a new ability fails to gain a learning point. |
| `Learning.failingPenaltyChance` | 0.1 | The chance to the failing penalty to apply. |
| `Learning.failingPenaltyLevel` | 1 | The level of the misfire status effect when failing penalty applies. |
| `Learning.failingPenaltyDuration` | 200 | The duration in ticks of the misfire status effect when failing penalty applies. |
| `Learning.failingPenaltyMin` | 1 | The min learning points the player can lose when failing to learn an ability. |
| `Learning.failingPenaltyMax` | 3 | The max learning points the player can lose when failing to learn an ability. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/lust`, `tensura:skills/sin_skills`, `tensura:skills/unique_skills`
