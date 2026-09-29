# Black Flame

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Black Flame](../../../assets/icons/tensura/skill/black_flame.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:black_flame` |
| **Modes** | 4 |
| **Cooldowns (s)** | 1, 2 |
| **Activation** | Press, Hold |

</div>

> Command the tempest infused flames to spew out black flames at your enemies or even shoot deadly fireballs and hell flares.

## Modes

| # | Mode |
|---|---|
| 1 | Flame Breath |
| 2 | Fireball |
| 3 | Hell Flare |
| 4 | Limited Hell Flare |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Flame Breath | 50 |  |
| Fireball | 100 |  |
| other modes | 2,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers on melee contact

## Obtaining

- Intrinsic skill of: [High-Class Demon](../../../tr-nightmares/races/high-class-demon.md), [Cursed Dragon](../../../ascension/races/cursed-dragon.md), [Demonic Dragon](../../../ascension/races/demonic-dragon.md), [Demon Dragon God](../../../ascension/races/demon-dragon-god.md)
- Can be learned by: [Corrupted Dragonkin](../../../ascension/races/corrupted-dragonkin.md), [Corrupted Dragon](../../../ascension/races/corrupted-dragon.md)
- Listed in the `intrinsicPool` config option (config/nightmare/race/demon_clan_config.toml): Intrinsic pool (if used).
- Acquisition checks: [Black Lightning](black-lightning.md), [Molecular Manipulation](molecular-manipulation.md), [Flame Transform](../intrinsic-skills/flame-transform.md)

## Related

- **Related skills:** [Black Lightning](black-lightning.md), [Molecular Manipulation](molecular-manipulation.md), [Flame Transform](../intrinsic-skills/flame-transform.md), [Ogre Flame](../battlewill/ogre-flame.md), [Flame Manipulation](flame-manipulation.md), [Flame Domination](flame-domination.md)
- **Effects:** [Black Burn](../../effects/black-burn.md)
- **Summons / entities:** [Ranged Barrier](../common-skills/ranged-barrier.md), Black Flame Breath, Black Flame Ball, Hell Flare
- **Referenced by:** [Coffin of Darkness](../../../tr-nightmares/abilities/unique-skills/coffin-of-darkness.md), [Black Flame Thunder](../../../tr-nightmares/abilities/intrinsic-skills/black-flame-thunder.md), [｢ Hastur, Lord of Starwind ｣](../../../tr-nightmares/abilities/ultimate-skills/hastur.md), [Godly Scientist](../../../tensura-more-skills/abilities/unique-skills/godly-scientist.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `BlackFlame.magiculeCostBreath` | 50 | Magicule Cost to activate Flame Breath. |
| `BlackFlame.magiculeCostBall` | 100 | Magicule Cost to activate Fire Ball. |
| `BlackFlame.magiculeCostCoating` | 5 | Magicule Cost to activate Coating. |
| `BlackFlame.magiculeCostFlare` | 2,000 | Magicule Cost to activate Hell Flare. |
| `BlackFlame.blackBurnDuration` | 200 | The Duration in tick of Black Burn when applied on target. |
| `BlackFlame.blackBurnDamage` | 2 | How much damage that the effect Black Burn does each second per level. |
| `BlackFlame.breathFlameDamage` | 9 | How much Flame damage that Black Flame Breath does each second. |
| `BlackFlame.breathFlameDamageMastered` | 18 | How much Flame damage that Black Flame Breath does each second when mastered. |
| `BlackFlame.breathMagicDamage` | 1 | How much Magic damage that Black Flame Breath does each second. |
| `BlackFlame.breathMagicDamageMastered` | 2 | How much Magic damage that Black Flame Breath does each second when mastered. |
| `BlackFlame.ballFlameDamage` | 45 | How much Flame damage that Black Fire Ball does on impact. |
| `BlackFlame.ballMagicDamage` | 5 | How much Magic damage that Black Fire Ball does on impact. |
| `BlackFlame.ballCooldown` | 1 | The cooldown to activate Black Fire Ball. |
| `BlackFlame.flareFlameDamage` | 270 | How much Flame damage that Hell Flare does on activation. |
| `BlackFlame.flareMagicDamage` | 30 | How much Magic damage that Hell Flare does on activation. |
| `BlackFlame.flareRadius` | 15 | The radius of Hell Flare. |
| `BlackFlame.flareCooldown` | 1 | The cooldown to activate Hell Flare. |
| `BlackFlame.flareFlameDamageLimited` | 720 | How much Flame damage that Hell Flare Limited does on activation. |
| `BlackFlame.flareMagicDamageLimited` | 80 | How much Magic damage that Hell Flare Limited does on activation. |
| `BlackFlame.flareRadiusLimited` | 2.5 | The radius of Hell Flare Limited. |
| `BlackFlame.flareCooldownLimited` | 2 | The cooldown to activate Hell Flare Limited. |

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

`tensura:skills/extra_skills`, `tensura:skills/flame_skills`
