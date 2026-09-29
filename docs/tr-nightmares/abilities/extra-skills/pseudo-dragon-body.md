# Pseudo Dragon Body

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `trnightmare:pseudo_dragon_body` |
| **Acquisition cost (MP)** | 50,000 |
| **Activation** | Toggle |

</div>

> Toggle to assume your bonded True Dragon's body (4x EP). Costs 500 magicule per second while active. Requires a True Dragon ultimate. Incompatible with Dragon Mode.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect
- Triggers when you die

## Related

- **Effects:** [True Dragon Body](../../effects/true-dragon-body.md), [Dragon Mode](../../../tensura-reincarnated/effects/dragon-mode.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_extra.toml`](../../configs/config-nightmare-ability-skill-nightmare-extra.md).

| Option | Default | Description |
|---|---|---|
| `PseudoDragonBody.mpAcquirement` | 50,000 | Magicule acquirement cost. |
| `PseudoDragonBody.mpDrainPerTick` | 500 | Magicule drained each skill tick (~1 per second) while toggled on. |
