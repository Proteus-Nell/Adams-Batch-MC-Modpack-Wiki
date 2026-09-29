# Aura Sword

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

![Aura Sword](../../../assets/icons/tensura/skill/aura_sword.png)

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `tensura:aura_sword` |
| **Kind** | Melee |
| **Activation** | Toggle, Press |

</div>

> Coat your weapon in aura enhancing its blows.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 200 |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect

## Obtaining

- Sold by dwarf traders (low manual)
- Listed in the `battlewillManualList` config option (config/tensura/ability/ability_config.toml): List of Battlewills that can be randomly obtained from using the Battlewill Manual.

## Related

- **Effects:** [Aura Sword](../../effects/aura-sword.md)

## Stats (config defaults)

Set in [`config/tensura/ability/battlewill_config.toml`](../../configs/config-tensura-ability-battlewill-config.md).

| Option | Default | Description |
|---|---|---|
| `AuraSword.auraCost` | 200 | Aura Cost to activate. |
| `AuraSword.effectTime` | 1,200 | How long in tick that Aura Sword will stay on user after activated. |
| `AuraSword.attackMultiplier` | 1 | The bonus multiplier of the user's weapon base attack damage when activated. |

## Tags

`tensura:skills/battlewill`, `tensura:skills/low_manual_dwarf_trade`
