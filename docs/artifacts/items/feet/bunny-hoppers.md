# Bunny Hoppers

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Feet](index.md)</small>

<div class="infobox" markdown>

![Bunny Hoppers](../../../assets/icons/artifacts/item/bunny_hoppers.png)

| | |
|---|---|
| **ID** | `artifacts:bunny_hoppers` |
| **Category** | Feet |
| **Curio slot** | Feet |

</div>

## In this pack: relic version (RAR-Compat)

> [!NOTE]
> **Pack note:** this pack includes RAR-Compat, which turns Bunny Hoppers into a Relics-style relic. It levels up as you use it and unlocks the abilities below instead of the stock behaviour.

Relic levelling: up to level **10**, first level costs **100** XP, +100 XP per level.

> Strengthens the relic bearer's legs, allowing them to push off the ground more powerfully.

Found in loot chests of kind: chests in plains biomes, chests in forest biomes.

#### Jumper

*Passive. Ability max level 10.*

Allows high jumps by continuously holding the jump key for up to **0.15-0.25 (up to 0.45-0.75)** seconds.

| Stat | Starting value | Per level | At max level |
|---|---|---|---|
| Duration | 0.15-0.25 | +20% of base per level | 0.45-0.75 |

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/bunny_hoppers` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `bunny_hoppers.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `bunny_hoppers.modifyHurtSounds` | true | Whether the Bunny Hoppers change the player's hurt sounds |
| `bunny_hoppers.fallDamageMultiplier` | 0 | How much the Bunny Hoppers reduce or increase fall damage<br>Values between -1 and 0 reduce fall damage<br>Values above 0 increase fall damage |
| `bunny_hoppers.jumpStrengthBonus` | 0.4 | The amount of extra jump strength the Bunny Hoppers apply to players |
| `bunny_hoppers.safeFallDistanceBonus` | 10 | The amount of extra safe fall distance in blocks that is granted by the Bunny Hoppers |

## Tags

`artifacts:artifacts`, `artifacts:slot/feet`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
