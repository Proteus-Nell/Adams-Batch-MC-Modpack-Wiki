# Instant-move

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

![Instant-move](../../../assets/icons/tensura/skill/instant_move.png)

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `tensura:instant_move` |
| **Kind** | Utility |
| **Activation** | Toggle, Press |

</div>

> Gather your aura at your feet to travel faster than the eye can see.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 50 |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| dodge | 0.1 | add |
| invulnerability | 1 | add |

## Obtaining

- Sold by dwarf traders (low manual)
- Listed in the `battlewillManualList` config option (config/tensura/ability/ability_config.toml): List of Battlewills that can be randomly obtained from using the Battlewill Manual.

## Related

- **Summons / entities:** Tensura

## Stats (config defaults)

Set in [`config/tensura/ability/battlewill_config.toml`](../../configs/config-tensura-ability-battlewill-config.md).

| Option | Default | Description |
|---|---|---|
| `InstantMove.auraCost` | 50 | Aura Cost to activate. |
| `InstantMove.distance` | 6 | How far ahead the user will instant move toward (doubled when Mastered). |
| `InstantMove.dodgeStrength` | 0.1 | The bonus dodge strength when toggled. |
| `InstantMove.dodgeInvulnerability` | 1 | The bonus dodge invulnerability when toggled. |

## Tags

`tensura:skills/battlewill`, `tensura:skills/low_manual_dwarf_trade`
