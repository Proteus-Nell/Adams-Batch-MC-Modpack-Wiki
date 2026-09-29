# Inner World

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Common Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Common Skill |
| **ID** | `trnightmare:inner_world` |
| **Modes** | 5 |
| **Acquisition cost (MP)** | 1,000 |
| **Activation** | Toggle, Press |

</div>

> Manifest a private inner dimension. A skin-only echo of you remains outside; if it dies, you return to where it fell. Activate again to leave and rejoin your echo.

## Modes

| # | Mode |
|---|---|
| 1 | Inner World |
| 2 | Veldora |
| 3 | Velzard |
| 4 | Velgrynd |
| 5 | Velgaia |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_common.toml`](../../configs/config-nightmare-ability-skill-nightmare-common.md).

| Option | Default | Description |
|---|---|---|
| `InnerWorld.epAcquirement` | 100,000 | EP requirement for natural learning. |
| `InnerWorld.mpAcquirement` | 1,000 | Minimum base max magicule required to learn. |
| `InnerWorld.magiculeCost` | 0 | Magicule cost to activate. |
| `InnerWorld.cooldown` | 10 | Cooldown in seconds after activation. |

## In-game messages

<details markdown><summary>Show 3 messages</summary>

- Inner World requires at least 90% of your maximum health.
- Inner World requires at least 90% of your maximum magicule.
- Could not return from Inner World — return anchor was lost.

</details>

## Tags

`tensura:skills/common_skills`
