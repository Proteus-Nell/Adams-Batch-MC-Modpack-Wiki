# Sloth

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Sloth](../../../assets/icons/tensura/skill/sloth.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:sloth` |
| **Modes** | 6 |
| **Acquisition cost (MP)** | 100,000 |
| **Max mastery** | 1,500 |
| **Cooldowns (s)** | 10 |
| **Activation** | Press, Hold |

</div>

> Grind the world to a halt. Put your enemies into a deadly sleep, drain their power and rest to regain any lost vitality. May lethargy take over.

## Modes

| # | Mode |
|---|---|
| 1 | Deep Hypno |
| 2 | Fallen Hypno |
| 3 | Deprive |
| 4 | Rest |
| 5 | Phantasmal Style |
| 6 | Fallen Strike |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Deprive | 200 |  |
| Fallen Strike | 5,000 |  |
| other modes | 0 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when you damage a target

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `egoWhitelist` config option (config/nightmare/ability/skill/ego/general_config.toml): Skills allowed to develop ego if in whitelist mode
- Listed in the `DemonicSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): List of Demonic skills registry names that can be created via Demon Essence consumption. Format: modid:skill_name

## Related

- **Related skills:** [Spiritual Attack Nullification](../resistance-skills/spiritual-attack-nullification.md), [Spiritual Attack Resistance](../resistance-skills/spiritual-attack-resistance.md)
- **Effects:** [Shadow Step](../../effects/shadow-step.md), [Rest](../../effects/rest.md), [Drowsiness](../../effects/drowsiness.md)
- **Referenced by:** [｢ Belphegor, Lord of Sloth ｣](../../../tr-nightmares/abilities/ultimate-skills/belphegor.md), [｢ Michael, Lord of Justice ｣](../../../tr-nightmares/abilities/ultimate-skills/michael.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Sloth.mpAcquirement` | 100,000 | Magicule Acquirement Cost. |
| `Sloth.magiculeCostDeprive` | 200 | Magicule Cost to activate Deprive. |
| `Sloth.magiculeCostFallen` | 5,000 | Magicule Cost to activate Fallen Strike. |
| `Sloth.deepRange` | 10 | The range in block of the Deep Hypno mode when used on a living target. |
| `Sloth.deepRangeMagic` | 30 | The range in block of the Deep Hypno mode when used on a magic circle. |
| `Sloth.deepDuration` | 100 | The base duration of the Drowsiness effect when using the Deep Hypno mode. |
| `Sloth.deepDurationMastered` | 200 | The base duration of the Drowsiness effect when using the Deep Hypno mode with mastery. |
| `Sloth.deepIncreaseTick` | 200 | The amount of tick activated needed to increase 1 level of Drowsiness when using the Deep Hypno. |
| `Sloth.deepMagicCooldown` | 3 | The cooldown in second of the magic circle destroyed by Deep Hypno for the targeted caster. |
| `Sloth.deepMagicCooldownMastered` | 5 | The cooldown in second of the magic circle destroyed by Deep Hypno for the targeted caster when mastered. |
| `Sloth.fallenRadius` | 5 | The radius in block of the Fallen Hypno mode. |
| `Sloth.fallenRadiusMastered` | 10 | The radius in block of the Fallen Hypno mode when mastered. |
| `Sloth.fallenDuration` | 100 | The base duration of the Drowsiness effect when using the Fallen Hypno mode. |
| `Sloth.fallenDurationMastered` | 200 | The base duration of the Drowsiness effect when using the Fallen Hypno mode with mastery. |
| `Sloth.fallenIncreaseTick` | 200 | The amount of tick activated needed to increase 1 level of Drowsiness when using the Fallen Hypno. |
| `Sloth.depriveRadius` | 5 | The radius in block of the Deprive mode. |
| `Sloth.depriveRadiusMastered` | 15 | The radius in block of the Deprive mode when mastered. |
| `Sloth.depriveEP` | 1,000 | The amount of EP to drain from targets when using Deprive. |
| `Sloth.depriveEPMastered` | 0.003 | The multiplier of targets' EP to drain from targets when using Deprive with mastery. |
| `Sloth.depriveSHP` | 10 | The amount of Spiritual damage dealt on targets when using Deprive. |
| `Sloth.depriveSHPMastered` | 0.01 | The multiplier of Spiritual damage dealt on targets when using Deprive with mastery. |
| `Sloth.restHP` | 10 | The amount of SHP to heal each second when using Rest. |
| `Sloth.restHPMastered` | 0.01 | The multiplier of SHP to heal each second when using Rest with mastery. |
| `Sloth.restSHP` | 10 | The amount of HP to heal each second when using Rest. |
| `Sloth.restSHPMastered` | 0.01 | The multiplier of HP to heal each second when using Rest with mastery. |
| `Sloth.restAP` | 10 | The multiplier of Aura Regeneration when using Rest. |
| `Sloth.restMP` | 10 | The multiplier of Magicule Regeneration when using Rest. |
| `Sloth.restAllyRadius` | 15 | The radius in block of ally heal area when using Rest. |
| `Sloth.restAllyCost` | 1,000 | The Stored Magicule cost to heal each Ally. |
| `Sloth.restAllyHP` | 50 | The amount of HP to heal Allies each second when using Rest. |
| `Sloth.restAllySHP` | 10 | The amount of SHP to heal Allies each second when using Rest. |
| `Sloth.restAllyEP` | 1,000 | The amount of Aura/Magicule each to heal Allies each second when using Rest. |
| `Sloth.phantasmalSHP` | 10 | The amount of Spiritual damage dealt on targets when using Phantasmal Style. |
| `Sloth.phantasmalSHPMastered` | 0.01 | The multiplier of Spiritual damage dealt on targets when using Phantasmal Style with mastery. |
| `Sloth.fallStrikeRange` | 8 | The max range in block of Fallen Strike. |
| `Sloth.fallStrikeSHP` | 500 | The amount of Spiritual Damage to deal on targets when using Fallen Strike. |
| `Sloth.fallStrikeCooldown` | 10 | The cooldown in second of the Fallen Strike mode. |

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

`tensura:skills/sin_skills`, `tensura:skills/sloth`, `tensura:skills/unique_skills`
