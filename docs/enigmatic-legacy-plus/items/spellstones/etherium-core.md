# Etherium Core

<small>[EnigmaticLegacy+](../../index.md) &rsaquo; [Items](../index.md) &rsaquo; [Spellstones](index.md)</small>

<div class="infobox" markdown>

![Etherium Core](../../../assets/icons/enigmaticlegacyplus/item/etherium_core.png)

| | |
|---|---|
| **ID** | `enigmaticlegacyplus:etherium_core` |
| **Category** | Spellstones |
| **Rarity** | Rare |
| **Curio slot** | Spellstone |

</div>

## Description

Active ability:

- Provides Blessing of Starlight effect based on Etherium Threshold.

- Absent.

Сooldown: ? seconds

Passive abilities:

- ? Armor, ? Toughness

- +20% Armor, +40% Toughness

- ? Knockback Resistance

- +? Etherium Shield Threshold

- Convert ? of the damage received into

an increase for the next attack.

- Immunity to pressure, pricking and explosion damage.

Hold Shift to see details.

## What it does

A spellstone (it goes in the Spellstone curio slot, and you can only wear one spellstone at a time). It has two states:

| | Etherium Core | Starlight Core |
|---|---|---|
| Armor | **+10**, then **+20%** | **+12**, then **+20%** |
| Armor toughness | **+8**, then **+40%** | **+10**, then **+40%** |
| Knockback resistance | **+50%** | **+80%** |
| Etherium Shield threshold | **+32%** | **1.25 ×** the Etherium Core's |
| Damage stored for your next hit | **40%** | **40% + 10%** |
| Active ability (spellstone key) | none | [Blessing of Starlight](../../effects/starlight-blessing.md), 200 s cooldown |

**Starlight Core** is the upgraded Etherium Core (the item id `etherium_core_active` is only its alternate name, not a separate item). To upgrade it, hold an [Astral Pearl](../misc/starlight-pearl.md) on your cursor and **right-click** it onto the Etherium Core in your inventory. One pearl is used up and the core switches to its Starlight state for good.

**Both states:**

- You're immune to explosions, cactus, sweet berry bushes, suffocating in a wall, cramming and falling blocks.
- When you take damage, part of it is stored (up to **25**) and added to your next attack, which uses it up.
- **Etherium Shield:** while your health is below *threshold × max health*, the shield is up. Arrows and other projectiles are **deflected** completely, every other hit is reduced (by more the higher your threshold), and melee attackers are knocked back. The core's threshold bonus multiplies the flat threshold you get from other gear (Etherium armor, Etherium tools, the Ethereal Forging Charm, the Cosmic Scroll and Etheric Resonance). So on its own, with no other threshold source, the core adds no shield.

**Starlight Core's active ability** gives you [Blessing of Starlight](../../effects/starlight-blessing.md) for **100 s + 100 s × your threshold**. While blessed, your threshold is **10%** higher and your hits deal **+80% × threshold** extra damage. When the blessing runs out on its own you're **healed to full**. If it's removed early (for example by milk), you heal **40%** of your max health instead.

If the Spellstone Tuner has the core tuned in, you get the stored-damage bonus at half rate (40% ÷ 2) without wearing it.

**Other names:** in some states this item shows a different name: **Starlight Core**.

## Obtaining

### Recipes

**Spellstone Table** &rarr; ![](../../../assets/icons/enigmaticlegacyplus/item/etherium_core.png) [Etherium Core](etherium-core.md)

Ingredients: ![](../../../assets/icons/enigmaticlegacyplus/item/ender_rod.png) [Ender Rod](../generic/ender-rod.md), ![](../../../assets/icons/enigmaticlegacyplus/item/etherium_block.png) [Etherium Block](../../blocks/etherium-block.md), ![](../../../assets/icons/enigmaticlegacyplus/item/ender_rod.png) [Ender Rod](../generic/ender-rod.md), ![](../../../assets/icons/enigmaticlegacyplus/item/earth_heart.png) [Heart of the Earth](../materials/earth-heart.md), ![](../../../assets/icons/enigmaticlegacyplus/item/ender_rod.png) [Ender Rod](../generic/ender-rod.md), ![](../../../assets/icons/enigmaticlegacyplus/item/etherium_block.png) [Etherium Block](../../blocks/etherium-block.md), ![](../../../assets/icons/enigmaticlegacyplus/item/ender_rod.png) [Ender Rod](../generic/ender-rod.md)

Details: debris count 9

## Config

Set in [`serverconfig/enigmaticlegacyplus-server.toml`](../../configs/serverconfig-enigmaticlegacyplus-server.md).

| Option | Default | Description |
|---|---|---|
| `etheriumCore.etheriumThresholdModifier` | 32 (0 to 100) |  |
| `etheriumCore.damageConversion` | 40 (0 to 100) |  |
| `etheriumCore.damageConversionLimit` | 25 (0 to 100) |  |

## Tags

`curios:spellstone`
