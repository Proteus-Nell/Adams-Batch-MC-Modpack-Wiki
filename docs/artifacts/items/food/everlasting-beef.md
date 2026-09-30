# Everlasting Beef

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Food](index.md)</small>

<div class="infobox" markdown>

![Everlasting Beef](../../../assets/icons/artifacts/item/everlasting_beef.png)

| | |
|---|---|
| **ID** | `artifacts:everlasting_beef` |
| **Category** | Food |

</div>

## What it does

Food that is **never used up**: eating it feeds you but keeps the item, then puts it on a short cooldown (15 s for Everlasting Beef, 15 s for Eternal Steak). Everlasting Beef restores 3 hunger and has a chance to drop when a player kills a cow or mooshroom. Cook it into Eternal Steak, which restores 8 hunger.

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| `artifacts:items/everlasting_beef` | 1 | 50% | config value |

## Used in

[Eternal Steak](eternal-steak.md)

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `everlasting_beef.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `everlasting_beef.enabled` | true | Whether the Everlasting Beef can be eaten |
| `everlasting_beef.cooldown` | 15 | The duration in seconds the Everlasting Beef goes on cooldown for after being eaten |
| `everlasting_beef.dropRate` | 0.002 | The probability that Everlasting Beef drops when a cow or mooshroom is killed by a player |

## Tags

`artifacts:artifacts`, `origins:meat`
