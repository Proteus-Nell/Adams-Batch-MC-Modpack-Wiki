# Greed

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Greed](../../../assets/icons/tensura/skill/greed.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:greed` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 100,000 |
| **Max mastery** | 1,500 |
| **Cooldowns (s)** | 10 mastered, 20 otherwise |
| **Activation** | Press, Hold |

</div>

> Take everything. Conquer the world and your enemies with it. Kill anyone who stands in your path while strengthening yourself or your allies.

## Modes

| # | Mode |
|---|---|
| 1 | Spiritual Domination |
| 2 | Greed Flare |
| 3 | Death Wish |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 1,000 |  |
| Always | 10 or 0 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Triggers when you damage a target

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `egoWhitelist` config option (config/nightmare/ability/skill/ego/general_config.toml): Skills allowed to develop ego if in whitelist mode
- Listed in the `DemonicSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): List of Demonic skills registry names that can be created via Demon Essence consumption. Format: modid:skill_name

## Related

- **Effects:** [Movement Interference](../../effects/movement-interference.md), [Mind Control](../../effects/mind-control.md)
- **Referenced by:** [｢ Mammon, Lord of Greed ｣](../../../tr-nightmares/abilities/ultimate-skills/mammon.md), [｢ Michael, Lord of Justice ｣](../../../tr-nightmares/abilities/ultimate-skills/michael.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Greed.mpAcquirement` | 100,000 | Magicule Acquirement Cost. |
| `Greed.magiculeCostFlare` | 10 | Base Magicule Cost to activate Greed Flare's buff. |
| `Greed.magiculeCostFlareAlly` | 50 | Base Magicule Cost to activate Greed Flare's ally buff. |
| `Greed.magiculeCostFlareAttack` | 20 | Base Magicule Cost to activate Greed Flare's attack. |
| `Greed.magiculeCostWish` | 1,000 | Base Magicule Cost to activate Death Wish. |
| `Greed.maxDistance` | 30 | The max distance in block for Spiritual Domination. |
| `Greed.playerControl` | 60 | The base time in second to control a player with Spiritual Domination. |
| `Greed.entityControl` | 90 | The base time in second to control a non-player entity with Spiritual Domination. |
| `Greed.closeDistance` | 5 | The distance in block to be considered close-range for Spiritual Domination. |
| `Greed.closeControl` | 30 | The reduced time in second to control a player with Spiritual Domination when in close range. |
| `Greed.farDistance` | 20 | The distance in block to be considered far-range for Spiritual Domination. |
| `Greed.farControl` | 30 | The increased time in second to control a player with Spiritual Domination when in far range. |
| `Greed.playerTradeControl` | 10 | The number of Villager Trade that the targeted player needed to do to reduce 1 second in control time for Spiritual Domination. |
| `Greed.mobTradeControl` | 2 | The amount of second to reduce from control time of Spiritual Domination for each merchant trade of a trader mob. |
| `Greed.deathTime` | 10 | The activation time in second needed to activate Death Wish. |
| `Greed.deathInterference` | 6 | The level of movement interference when the target is being casted with Death Wish (-10% speed each level). |
| `Greed.flareRange` | 20 | The range in block of Greed Flare. |
| `Greed.flareBuff` | 0.05 | The multiplier of the user's current SHP when using Greed Flare's Buff. |
| `Greed.flareBuffMastery` | 0.1 | The multiplier of the user's current SHP when using Greed Flare's Buff with Mastery. |
| `Greed.flareAllyBuff` | 0.025 | The multiplier of the ally's current SHP when using Greed Flare's Buff on allies. |
| `Greed.flareAllyBuffMastery` | 0.05 | The multiplier of the ally's current SHP when using Greed Flare's Buff on allies with Mastery. |
| `Greed.flareAttack` | 0.025 | The multiplier of the user's current SHP when using Greed Flare's Attack. |
| `Greed.flareAttackMastery` | 0.05 | The multiplier of the user's current SHP when using Greed Flare's Attack with Mastery. |
| `Greed.flareCooldown` | 20 | The cooldown in second of Greed Flare's Buff activate. |
| `Greed.flareCooldownMastered` | 10 | The cooldown in second of Greed Flare's Buff activate when mastered. |
| `Greed.flareAttackCooldown` | 20 | The cooldown in second of Greed Flare's Attack. |
| `Greed.flareAttackCooldownMastered` | 10 | The cooldown in second of Greed Flare's Attack when mastered. |

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

`tensura:skills/greed`, `tensura:skills/sin_skills`, `tensura:skills/unique_skills`
