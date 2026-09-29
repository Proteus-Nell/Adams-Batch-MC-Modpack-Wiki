# Self-Regeneration

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Common Skills](index.md)</small>

<div class="infobox" markdown>

![Self-Regeneration](../../../assets/icons/tensura/skill/self_regeneration.png)

| | |
|---|---|
| **Type** | Common Skill |
| **ID** | `tensura:self_regeneration` |
| **Activation** | Toggle |

</div>

> Speed up your body’s natural regeneration to increase your survivability.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 100 |  |

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect

## Obtaining

- Innate to mobs: [Metal Slime](../../mobs/metal-slime.md), [Orc Disaster](../../mobs/orc-disaster.md), [Orc Lord](../../mobs/orc-lord.md), [Slime](../../mobs/slime.md), [Okami](../../../tensura-mysticism/mobs/okami.md)
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Greater Chimera can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Golden Chimera can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Chimera Lord can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Divine Chimera can randomly receive.
- Listed in the `intrinsicSkills` config option (config/nightmare/race/axolotl/salamander_config.toml): List of skills obtained by this race.
- Listed in the `intrinsicSkills` config option (config/nightmare/race/axolotl/axolotl_config.toml): List of skills obtained by this race.
- Listed in the `intrinsicPool` config option (config/nightmare/race/demon_clan_config.toml): List of intrinsic skills Lower Class Demon can randomly receive.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/angel_config.toml): The list of intrinsic skills that the race gets.
- Acquisition checks: [Slime](../../races/slime.md), [Metal Slime](../../races/metal-slime.md)

## Related

- **Effects:** [Self-Regeneration](../../effects/self-regeneration.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/common_config.toml`](../../configs/config-tensura-ability-skill-common-config.md).

| Option | Default | Description |
|---|---|---|
| `SelfRegeneration.slimeAcquirement` | 500 | Slime beaten Requirement for Learning. |
| `SelfRegeneration.magiculeCost` | 100 | Base Magicule Cost to activate. |
| `SelfRegeneration.regenLevel` | 1 | The level of the self-regeneration effect. |
| `SelfRegeneration.regenLevelMastered` | 2 | The level of the self-regeneration effect when mastered. |
| `SelfRegeneration.regenHP` | 2 | How much HP to regenerate each second per level. |
| `SelfRegeneration.regenSHP` | 4 | How much SHP to regenerate each second per level when mastered. |

Set in [`config/tensura/ability/ability_config.toml`](../../configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/common_skills`
