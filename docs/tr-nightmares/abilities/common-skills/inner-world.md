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

## What it does

The template for each player's own Inner World, a flat, dark world where time stands still at noon. Beds and respawn anchors don't work.

**Getting in:**

- The [Inner World](inner-world.md) skill takes you in if you have at least **90%** of your health and magicule. A hollow "echo" of you (your health, no gear, almost no EP) stays behind where you stood and keeps its chunk loaded. Use the skill again to leave and rejoin the echo. If the echo is killed while you're inside, you're thrown back out to where it fell.
- Sleeping in a bed while holding a completed [Ancient History Book](../../items/books-scrolls/ancient-history-book.md) pulls you into your Inner World to meet Veldanava.
- Other skills can visit someone else's Inner World as a guest, such as [Conceptual Existence](../intrinsic-skills/conceptual-existence.md)'s and [｢ Pazuzu, Lord of Mischief ｣](../ultimate-skills/pazuzu.md)'s Enter Mind (Pazuzu only reaches players you have a deal with).
- Several skills use it as a battlefield or prison, such as Abaddon, Samael's Death World and Temptation.

True Dragons you've bonded with (Veldora, Velzard, Velgrynd, Velgaia) live in your Inner World and add extra modes to the skill.

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
