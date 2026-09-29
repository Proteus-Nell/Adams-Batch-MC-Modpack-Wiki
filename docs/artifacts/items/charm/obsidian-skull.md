# Obsidian Skull

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Charm](index.md)</small>

<div class="infobox" markdown>

![Obsidian Skull](../../../assets/icons/artifacts/item/obsidian_skull.png)

| | |
|---|---|
| **ID** | `artifacts:obsidian_skull` |
| **Category** | Charm |
| **Curio slot** | Charm |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Obsidian Skull into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Redirects heat aimed at harming the relic bearer onto itself.

Found in loot chests of kind: fire/Nether-themed chests (and ruined portals), any Nether chest.

#### Heat Resistance

*Passive. Ability max level 10.*

Completely absorbs damage from fire sources for up to **2-3 (up to 8-12)** seconds. If the player has not taken fire damage for 3 seconds, the absorption time regenerates each second.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Duration | 2-3 | +30% of base per level | 8-12 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/obsidian_skull` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `obsidian_skull.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `obsidian_skull.fireResistanceDuration` | 30 | The duration of the fire resistance effect that is applied when taking fire damage while wearing the Obsidian Skull |
| `obsidian_skull.cooldown` | 60 | The amount of time in seconds the Obsidian Skull goes on cooldown for after taking fire damage |

## Tags

`artifacts:artifacts`, `artifacts:slot/charm`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
