# Goddess hIncarnation

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `trnightmare:goddess_incarnation` |
| **Activation** | Press |

</div>

> An intrinsic skill that manifests divine traits and sacred power within the user.

## How it works

- Activated by pressing the skill key

## Obtaining

- Intrinsic skill of: [Lesser hGoddess](../../races/lesser-goddess.md)

## Related

- **Effects:** [Energy Blockade](../../../tensura-reincarnated/effects/energy-blockade.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `Possession.range` | 5 | The possession range in block. |
| `Possession.hpMultiplier` | 0.1 | The multiplier of the maximum Health that a target needs to be under to be possessed. |
| `Possession.shpMultiplier` | 0.1 | The multiplier of the maximum Spiritual Health that a target needs to be under to be possessed. |
| `Possession.epMultiplier` | 0.25 | The multiplier of the user's maximum EP that a target needs to be under to be possessed. |
| `Possession.resistanceMultiplier` | 0.5 | The multiplier of the possession requirement multipliers when the target has Spiritual Attack Resistance. |
| `Possession.maxHealth` | 1,000 | The maximum amount of HP the user can get from possessing an entity. |
| `Possession.maxAttack` | 100 | The maximum amount of Attack Damage the user can get from possessing an entity. |
| `Possession.bodyDespawnTick` | 300 | The number of seconds that Possession Bodies will despawn. (0 = instant despawn, -1 = doesn't despawn) |
