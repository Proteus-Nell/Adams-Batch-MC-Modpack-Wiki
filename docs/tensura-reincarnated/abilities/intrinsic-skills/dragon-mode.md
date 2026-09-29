# Dragon Mode

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Dragon Mode](../../../assets/icons/tensura/skill/dragon_mode.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `tensura:dragon_mode` |
| **Cooldowns (s)** | 1,200 |
| **Activation** | Press |

</div>

> Once a day, draw out your monstrous potential to double your EP and to boost your physical prowess. Doing this will leave a temporary toll on your body.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 0 |  |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect

## Obtaining

- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Lesser Chimera can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Greater Chimera can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Golden Chimera can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Chimera Lord can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Divine Chimera can randomly receive.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/wyrm_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Effects:** [Dragon Mode](../../effects/dragon-mode.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `DragonMode.magiculeCost` | 0 | Magicule Cost to activate. |
| `DragonMode.transformationDuration` | 3,600 | The duration in tick of the Transformation. |
| `DragonMode.transformationDurationMastered` | 7,200 | The duration in tick of the Transformation. |
| `DragonMode.cooldown` | 1,200 | The Cooldown in second after activation. |

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

`tensura:skills/intrinsic_skills`
