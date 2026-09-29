# Eternal Steak

<small>[Artifacts](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Food](index.md)</small>

<div class="infobox" markdown>

![Eternal Steak](../../../assets/icons/artifacts/item/eternal_steak.png)

| | |
|---|---|
| **ID** | `artifacts:eternal_steak` |
| **Category** | Food |

</div>

## What it does

Food that is **never used up**: eating it feeds you but keeps the item, then puts it on a short cooldown (15 s for Everlasting Beef, 15 s for Eternal Steak). Everlasting Beef restores 3 hunger and has a chance to drop when a player kills a cow or mooshroom. Cook it into Eternal Steak, which restores 8 hunger.

## Obtaining

### Recipes

**Campfire** &rarr; ![](../../../assets/icons/artifacts/item/eternal_steak.png) [Eternal Steak](eternal-steak.md)

Ingredients: ![](../../../assets/icons/artifacts/item/everlasting_beef.png) [Everlasting Beef](everlasting-beef.md)

**Smelting** &rarr; ![](../../../assets/icons/artifacts/item/eternal_steak.png) [Eternal Steak](eternal-steak.md)

Ingredients: ![](../../../assets/icons/artifacts/item/everlasting_beef.png) [Everlasting Beef](everlasting-beef.md)

**Smoking** &rarr; ![](../../../assets/icons/artifacts/item/eternal_steak.png) [Eternal Steak](eternal-steak.md)

Ingredients: ![](../../../assets/icons/artifacts/item/everlasting_beef.png) [Everlasting Beef](everlasting-beef.md)

## Config

Set in [`config/artifacts/items.toml`](../../configs/config-artifacts-items.md).

| Option | Default | Description |
|---|---|---|
| `eternal_steak.generateAsLoot` | true | Whether this item can be found in structures or drop from entities |
| `eternal_steak.enabled` | true | Whether the Eternal Steak can be eaten |
| `eternal_steak.cooldown` | 15 | The duration in seconds the Eternal Steak goes on cooldown for after being eaten |

## Tags

`artifacts:artifacts`, `origins:meat`
