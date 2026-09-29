# Lock

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Lock](../../../assets/icons/trnightmare/skill/lock.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `trnightmare:lock` |
| **Activation** | Toggle |

</div>

> This skill prevents your skills from being taken via Skill Plundering.

## How it works

- Can be toggled on and off

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_intrinsic.toml`](../../configs/config-nightmare-ability-skill-nightmare-intrinsic.md).

| Option | Default | Description |
|---|---|---|
| `LockSkill.epAcquirement` | 30 | Learning cost. |
| `LockSkill.meetEpThreshold` | 10,000 | Minimum EP with plunder gamerule. |
| `LockSkill.magiculeCost` | 30 | Magicule cost. |
