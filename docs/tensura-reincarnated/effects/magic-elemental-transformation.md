# Magic Elemental Transformation

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Effects](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensura:magic_elemental_transformation` |
| **Type** | Beneficial |

</div>

## What it does

Magic Elemental Transformation: you become a being of one element. Your damage of that element is multiplied by **1.2**, and your hits add an element effect:

| Element | On hit |
|---|---|
| Darkness | Darkness |
| Earth | [Burden](burden.md) |
| Flame | sets the target on fire |
| Light | Nausea |
| Water | [Fatal Poison](fatal-poison.md) |
| Wind | [Paralysis](paralysis.md) |
| Space | your physical hits count as severance damage |

Plain physical attacks barely touch you: in the current code a physical hit is reduced to just **0.01** damage, or **0.5** if the attacker has Haki Coat I, Magic Aura or Cook. Attackers with Haki Coat II or higher, Divine Ki or Anti-Skill hit you normally.

It lasts 180 s (360 s mastered). When it ends you get the transformation hangover: [Weakness](https://minecraft.wiki/w/Weakness) II, [Fragility](fragility.md) II and [Paralysis](paralysis.md) I for 10 minutes.
