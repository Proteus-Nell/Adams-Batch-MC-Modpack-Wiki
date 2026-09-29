# Ancient Soul

<small>[Elite Tensura](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Ancient Soul](../../../assets/icons/elitetensura/skill/ancient_soul.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `elitetensura:ancient_soul` |
| **Modes** | 1 |
| **Acquisition cost (MP)** | 0 |
| **Cooldowns (s)** | 60 |
| **Activation** | Toggle |

</div>

> A primordial soul that resonates with nearby life. While toggled on, grants the holder and nearby allies Strength III, Regeneration III, and Resistance I, while Soul Sight outlines surrounding creatures by alignment — red for enemies, green for allies, cyan for the unaffiliated. Drains a trickle of magicule while active.

## Modes

| # | Mode |
|---|---|
| 1 | Default |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 2 | 0 |

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect

## Related

- **Referenced by:** [Elder Soul](../unique-skills/elder-soul.md)

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/ExtraSkillConfig.toml`](../../configs/config-tensura-elitetensura-extraskillconfig.md).

| Option | Default | Description |
|---|---|---|
| `AncientSoul.enabled` | true | True/False — is the Ancient Soul skill enabled (acquirable)? |
| `AncientSoul.epAcquirement` | 5,000 | EP requirement for learning Ancient Soul. |
| `AncientSoul.mpAcquirement` | 0 | Magicule acquiring cost to learn the skill. |
| `AncientSoul.magiculeDrainPerTick` | 2 | Magicule drained per tick while the skill is held (passive upkeep). |
| `AncientSoul.buffRadius` | 25 | Radius (blocks) of the Aura of the Ancient ally buff. |
| `AncientSoul.soulSightRadius` | 30 | Radius (blocks) within which Soul Sight outlines entities. |
| `AncientSoul.strengthAmplifier` | 2 | Strength effect amplifier (0-indexed; 2 = Strength III). |
| `AncientSoul.regenAmplifier` | 2 | Regeneration effect amplifier (0-indexed; 2 = Regeneration III). |
| `AncientSoul.resistanceAmplifier` | 0 | Resistance effect amplifier (0-indexed; 0 = Resistance I). |
| `AncientSoul.effectDurationTicks` | 120 | Duration (ticks) applied to the aura effects on each refresh. Keep &gt;= 100: ManasCore refreshes toggle skills every 100 game ticks. |
| `AncientSoul.refreshIntervalTicks` | 120 | Legacy — the aura now refreshes on every 100-tick skill tick; this value is no longer read. |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/extra_skills`, `tensura:skills/no_plundering`
