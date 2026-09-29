# Cloud in a Bottle

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Charm](index.md)</small>

<div class="infobox" markdown>

![Cloud in a Bottle](../../../assets/icons/artifacts/item/cloud_in_a_bottle.png)

| | |
|---|---|
| **ID** | `artifacts:cloud_in_a_bottle` |
| **Category** | Charm |
| **Curio slot** | Charm |

</div>

## What it does

Belt artifact. Lets you **double jump**: press jump again in mid-air to jump a second time. Sprinting while you double jump gives extra forward and upward speed. It also raises your safe fall distance by 3 blocks, and fall damage after a double jump is multiplied by 0.

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/cloud_in_a_bottle` | 1 | 50% | config value |

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `cloud_in_a_bottle.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `cloud_in_a_bottle.enabled` | true | Whether the Cloud in a Bottle allows the wearer to double jump |
| `cloud_in_a_bottle.sprintJumpVerticalVelocity` | 0.25 | The amount of extra vertical velocity that is applied to players that double jump while sprinting using the Cloud in a Bottle |
| `cloud_in_a_bottle.sprintJumpHorizontalVelocity` | 0.25 | The amount of extra horizontal velocity that is applied to players that double jump while sprinting using the Cloud in a Bottle |
| `cloud_in_a_bottle.safeFallDistanceBonus` | 3 | The amount of extra safe fall distance in blocks that is granted by the Cloud in a Bottle |
| `cloud_in_a_bottle.fallDamageMultiplier` | 0 | How much fall damage is dealt when double jumping with the Cloud in a Bottle |

## Tags

`artifacts:artifacts`, `artifacts:slot/charm`, `rarcompat:mimic_loot`, `rarcompat:mimificable`
