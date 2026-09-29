# Ending

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Ending](../../../assets/icons/trnightmare/skill/ending.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:ending` |
| **Modes** | 3 |
| **Cooldowns (s)** | 44, 444 |
| **Activation** | Press |

</div>

> All things have an end, and after mastering the power granted to you by your loneliness, you know exactly what those endings look like.

## Modes

| # | Mode |
|---|---|
| 1 | No Escape |
| 2 | Death's Door |
| 3 | Mode 3 |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 0 |  |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you are attacked

## Obtaining

- Listed in the `astralExtraUniqueSkills` config option (config/nightmare/ability/skill/nightmare_ult.toml): Extra unique skill IDs merged into Astral Light Skill Creation (after Tensura Creator).

## Related

- **Items:** [Blade of The End](../../items/weapons/ending-unsealed-sword.md), [Blade of The End](../../items/weapons/ending-sealed-sword.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `Ending.mpAcquirement` | 44,444 | Magicule Acquirement Cost. |
| `Ending.magiculeCostPull` | 4,444 | Magicule Cost to activate No Escape. |
| `Ending.magiculeCostDoor` | 4,444 | Magicule Cost to activate Death's Door. |
| `Ending.pullDamage` | 44 | Damage dealt by no escape. |
| `Ending.pullCooldown` | 44 | Cooldown for activating No Escape. |
| `Ending.doorCooldown` | 444 | Cooldown for activating Death's Door. |
| `Ending.healCooldown` | 1 | Cooldown for removing cook and altered cooked damage automatically. |
