# Dragon's Possession

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `trnightmare:dragon_possession` |
| **Activation** | Press |

</div>

> Take control of a target's body while preserving your own physical statistics and core identity.

## How it works

- Activated by pressing the skill key

## Obtaining

- Intrinsic skill of: [Lesser Daemonic Dragon](../../races/lesser-daemonic-dragon.md), [Medium Daemonic Dragon](../../races/medium-daemonic-dragon.md), [Arch Daemonic Dragon](../../races/arch-daemonic-dragon.md), [Daemonic Dragon Lord](../../races/daemonic-dragon-lord.md), [Devil Dragon Lord](../../races/devil-dragon-lord.md), [Lesser Thrall Dragon](../../races/lesser-thrall-dragon.md), [Greater Thrall Dragon](../../races/greater-thrall-dragon.md), [Vampiric Dragon](../../races/vampiric-dragon.md), [Vampiric Dragon Lord](../../races/vampiric-dragon-lord.md), [Divine Vampiric Dragon Lord](../../races/divine-vampiric-dragon-lord.md)

## Related

- **Effects:** [Energy Blockade](../../../tensura-reincarnated/effects/energy-blockade.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_intrinsic.toml`](../../configs/config-nightmare-ability-skill-nightmare-intrinsic.md).

| Option | Default | Description |
|---|---|---|
| `DragonPossession.epAcquirement` | 1,000 | EP cost to acquire Dragon Possession. |

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `Possession.bodyDespawnTick` | 300 | The number of seconds that Possession Bodies will despawn. (0 = instant despawn, -1 = doesn't despawn) |
| `Possession.range` | 5 | The possession range in block. |
| `Possession.hpMultiplier` | 0.1 | The multiplier of the maximum Health that a target needs to be under to be possessed. |
| `Possession.shpMultiplier` | 0.1 | The multiplier of the maximum Spiritual Health that a target needs to be under to be possessed. |
| `Possession.epMultiplier` | 0.25 | The multiplier of the user's maximum EP that a target needs to be under to be possessed. |
| `Possession.resistanceMultiplier` | 0.5 | The multiplier of the possession requirement multipliers when the target has Spiritual Attack Resistance. |
| `Possession.maxHealth` | 1,000 | The maximum amount of HP the user can get from possessing an entity. |
| `Possession.maxAttack` | 100 | The maximum amount of Attack Damage the user can get from possessing an entity. |
| `Possession.bodyDespawnTick` | 300 | The number of seconds that Possession Bodies will despawn. (0 = instant despawn, -1 = doesn't despawn) |
