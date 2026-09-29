# Brain

<small>[Elite Tensura](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `elitetensura:brain` |
| **Activation** | Hold |

</div>

> A unique skill that cannot be obtained through normal means.

## How it works

- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/UniqueSkillConfig.toml`](../../configs/config-tensura-elitetensura-uniqueskillconfig.md).

| Option | Default | Description |
|---|---|---|
| `Brain.debug` | false | Log Brain's per-evaluation AI decisions to the server console/log (skills toggled, skills pressed, magic buckets, cast attempts and why a cast did/didn't fire). Off by default — turn on to diagnose why a mob isn't using its abilities. |
| `Brain.evalInterval` | 1 | Number of skill-tick passes between Brain evaluations. ManasCore ticks passive skills every 100 game ticks (~5 seconds), so 1 = evaluate every ~5s (default), 2 = ~10s, etc. This is NOT in game ticks — the native passive-tick cadence is the floor. |
| `Brain.lowHealthFraction` | 0.5 | Health fraction (0-1) below which the mob is treated as hurt: prioritises recovery magic and enables pressing active skills defensively. |

## Tags

`tensura:skills/no_plundering`, `tensura:skills/unique_skills`
