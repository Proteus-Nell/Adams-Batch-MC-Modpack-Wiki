# Heart of the Guardian

<small>[EnigmaticLegacy+](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Misc](index.md)</small>

<div class="infobox" markdown>

![Heart of the Guardian](../../../assets/icons/enigmaticlegacyplus/item/guardian_heart.png)

| | |
|---|---|
| **ID** | `enigmaticlegacyplus:guardian_heart` |
| **Category** | Misc |
| **Rarity** | Uncommon |
| **Fire resistant** | Yes |

</div>

## Description

While in inventory, Guardians within ? blocks

from you are rendered neutral towards you

and will target nearby monsters.

While on hotbar, casting your sight upon the

monster within ? blocks from you causes it to

become temporarily enraged, gaining greater

strength and switching target to other closest

monster within ? blocks from it.

Other monsters within this radius will instantly

prioritize attacking enraged monster.

Some monsters are immune to being enraged.

This ability has 10 seconds cooldown.

## Obtaining

### Loot

| Source | Count | Chance | Notes |
|---|---|---|---|
| Dropped by Elder Guardian Addon | 1 | 25% | Looting increases the chance |

## Config

Set in [`serverconfig/enigmaticlegacyplus-server.toml`](../../configs/serverconfig-enigmaticlegacyplus-server.md).

| Option | Default | Description |
|---|---|---|
| `guardianHeart.effectiveRange` | 24 (4 to 64) |  |
| `guardianHeart.cooldown` | 200 (100 to 600) |  |
