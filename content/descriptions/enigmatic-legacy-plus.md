# EnigmaticLegacy+ notes

Hand-written "What it does" notes, read from the mod's code (1.1.1). Placeholders:
{{cfg:file|path.key}} shows the pack's config value, {{link:ns:id}} links an entry.

## enigmaticlegacyplus:etherium_core
A spellstone (it goes in the Spellstone curio slot, and you can only wear one spellstone at a time). It has two states:

| | Etherium Core | Starlight Core |
|---|---|---|
| Armor | **+10**, then **+20%** | **+12**, then **+20%** |
| Armor toughness | **+8**, then **+40%** | **+10**, then **+40%** |
| Knockback resistance | **+50%** | **+80%** |
| Etherium Shield threshold | **+{{cfg:serverconfig/enigmaticlegacyplus-server.toml|spellstone.etheriumCore.etheriumThresholdModifier}}%** | **1.25 ×** the Etherium Core's |
| Damage stored for your next hit | **{{cfg:serverconfig/enigmaticlegacyplus-server.toml|spellstone.etheriumCore.damageConversion}}%** | **{{cfg:serverconfig/enigmaticlegacyplus-server.toml|spellstone.etheriumCore.damageConversion}}% + 10%** |
| Active ability (spellstone key) | none | {{link:enigmaticlegacyplus:starlight_blessing}}, 200 s cooldown |

**Starlight Core** is the upgraded Etherium Core (the item id `etherium_core_active` is only its alternate name, not a separate item). To upgrade it, hold an {{link:enigmaticlegacyplus:starlight_pearl}} on your cursor and **right-click** it onto the Etherium Core in your inventory. One pearl is used up and the core switches to its Starlight state for good.

**Both states:**

- You're immune to explosions, cactus, sweet berry bushes, suffocating in a wall, cramming and falling blocks.
- When you take damage, part of it is stored (up to **{{cfg:serverconfig/enigmaticlegacyplus-server.toml|spellstone.etheriumCore.damageConversionLimit}}**) and added to your next attack, which uses it up.
- **Etherium Shield:** while your health is below *threshold × max health*, the shield is up. Arrows and other projectiles are **deflected** completely, every other hit is reduced (by more the higher your threshold), and melee attackers are knocked back. The core's threshold bonus multiplies the flat threshold you get from other gear (Etherium armor, Etherium tools, the Ethereal Forging Charm, the Cosmic Scroll and Etheric Resonance). So on its own, with no other threshold source, the core adds no shield.

**Starlight Core's active ability** gives you {{link:enigmaticlegacyplus:starlight_blessing}} for **100 s + 100 s × your threshold**. While blessed, your threshold is **10%** higher and your hits deal **+80% × threshold** extra damage. When the blessing runs out on its own you're **healed to full**. If it's removed early (for example by milk), you heal **40%** of your max health instead.

If the Spellstone Tuner has the core tuned in, you get the stored-damage bonus at half rate ({{cfg:serverconfig/enigmaticlegacyplus-server.toml|spellstone.etheriumCore.damageConversion}}% ÷ 2) without wearing it.

<!-- kind: effects -->

## enigmaticlegacyplus:poison
A stronger Poison (it shows up as plain "Poison" in game). It deals **1.5 + 0.125 per level** poison damage, more often at higher levels: every 1.2 s at level I, 0.2 s faster per level, and every tick from level VII. Healing is cut to **50% − 10% per level** of normal, so from level VI you can't heal at all. Like vanilla poison, it stops hurting you once your health is lower than one hit of it.

The Revival Leaf gives it (Poison II for 10 s) to anything that hits its wearer, and its wearer is immune to it. A Spellstone Sword resonating with the Revival Leaf turns a target's vanilla Poison into this one and stacks it up to level V.

This mod also stops **any** poison damage from killing: a creature that would die to poison is left at 1 health instead.

<!-- kind: items -->

## enigmaticlegacyplus:earth_heart_fragment
A shard of the Heart of the Earth, found in chests and sold by wandering traders. Brewing it into an Awkward Potion makes a Potion of Luck, and it's a crafting material.

{{auto}}

## enigmaticlegacyplus:evil_essence
**Nefarious Essence**, a scrap of the Wither's soul that Withers drop. Combine it with a Totem of Malice in an anvil to fully restore the totem. Like other cursed items, only a bearer of the Ring of the Seven Curses can use it.

{{auto}}

## enigmaticlegacyplus:evil_ingot
**Nefarious Ingot**, a cursed metal. It's the centerpiece of the Annihilating (abyssal) recipes.

{{auto}}

## enigmaticlegacyplus:sacred_crystal
The core of a Pure Ichor Spirit, dropped when you kill one in the Nether. A cursed material used for defensive items.

{{auto}}

## enigmaticlegacyplus:twisted_heart
A Heart of the Earth corrupted by the Seven Curses. While a player bearing the Ring of the Seven Curses carries it, it becomes **tainted**, which some recipes (such as the Annihilating recipes) need. It's used in many cursed items.

{{auto}}

## enigmaticlegacyplus:pure_heart
A heart that holds both hidden corruption and faint divinity. While carried by a player bearing either the Ring of the Seven Curses or the Ring of Redemption, it becomes **tainted** for recipes that need it. Brewing it into a Honey Bottle makes a Blessing Potion.

{{auto}}

## enigmaticlegacyplus:exterminato
A snack that gives Blazing Might (a random level from I to III) for 30 seconds when eaten.

{{auto}}

## enigmaticlegacyplus:ichoroot
A root that also removes **one random harmful effect** when you eat it.

{{auto}}

## enigmaticlegacyplus:forbidden_juice
A drink version of the Forbidden Fruit, only enabled when the Thirst mod is installed. You can only drink it once: afterwards you're marked as cursed by it and can't drink another.

{{auto}}

## enigmaticlegacyplus:ichor_curse_bottle
**Bottle of Penance.** Drinking it gives the Ichor Curse for 32 minutes. A blessed player (one bearing the Ring of Redemption) also gets Absorption V for 2 minutes. It's both cursed and blessed.

{{auto}}

## enigmaticlegacyplus:golden_ring
**Exquisite Ring**, a ring (Curios slot) that gives **+1 Luck**, keeps piglins neutral and counts as gold to them. One per player.

{{auto}}

## enigmaticlegacyplus:iron_ring
A plain ring (Curios slot) that gives **+1 armor**. One per player.

{{auto}}

## enigmaticlegacyplus:quartz_ring
**Magic Quartz Ring** (Curios slot): **+2 armor**, **+1.5 Luck** and **{{cfg:serverconfig/enigmaticlegacyplus-server.toml|else.quartzRing.specialDamageResistance}}%** less magic damage. One per player.

{{auto}}

## enigmaticlegacyplus:soul_compass
**Wayfinder of the Damned.** While you carry it, it points to the nearest of your lost Soul Crystals. It spins aimlessly in a Soul Sand Valley or if you can't use it (it's a cursed item).

{{auto}}

## enigmaticlegacyplus:soul_crystal
A piece of your soul. With the Ring of the Seven Curses ("Every death tears your soul apart"), each death takes a crystal from you and each lost crystal lowers your max health by **10%**; up to {{cfg:serverconfig/enigmaticlegacyplus-server.toml|sevenCurses.maxSoulCrystalLoss}} can be lost (the config decides whether you need the ring, {{cfg:serverconfig/enigmaticlegacyplus-server.toml|sevenCurses.soulCrystalsMode}}). Use a Soul Crystal to take it back and restore that health.

{{auto}}

## enigmaticlegacyplus:storage_crystal
**Extradimensional Vessel.** When you die while soul loss applies to you, your items, curios and experience are packed into one of these (with your Soul Crystal) instead of scattering. Picking it up gives everything back, puts items in the slots they came from and returns the soul. It can't be destroyed.

{{auto}}

## enigmaticlegacyplus:spellcore
The core that spellstones are built on. Put it in the {{link:enigmaticlegacyplus:spellstone_table}} to craft spellstones. Holding one in your off hand while using a Spellstone Sword lets you pull out the spell resonance stored in the sword.

{{auto}}

## enigmaticlegacyplus:starlight_particle, enigmaticlegacyplus:starlight_ingot
Stardust from fallen **Starlight Meteors** (and some chests). It's the material for Starlight gear.

{{auto}}

<!-- kind: blocks -->

## enigmaticlegacyplus:spellstone_table
The crafting station for **spellstones**. Put Spellstone Debris in the left slot, a Spellcore in the middle and the recipe's seven ingredients around it, and the spellstone appears in the result slot (see each spellstone's page for its recipe). It also works the other way: put a spellstone alone in the right-hand slot to break it down into **4 Spellstone Debris**. Spellstone Huts have one.

{{auto}}

## enigmaticlegacyplus:dimensional_anchor
A Respawn Anchor that works **in every dimension** and never explodes. Charge it with **Eyes of Ender** (up to 4 charges), then right-click it to set your spawn there. Each respawn uses one charge. It's very tough (like obsidian), the Ender Dragon can't break it, and a comparator reads its charge.

{{auto}}

## enigmaticlegacyplus:ethereal_lantern
A lantern that protects the people around it. Every 5 seconds, players within 8 blocks whose **Ethereal Shield** is down get a new one, worth half of their Etherium shield threshold times their max health. The shield threshold comes from Etherium gear, so players without any get nothing from it. Hang it or stand it like a normal lantern.

{{auto}}

## enigmaticlegacyplus:cosmic_cake
**The Eternal Cake.** Each slice fills you like a Golden Carrot (6 hunger, 14.4 saturation). You can eat up to 6 slices, but the last slice never goes away, and eaten slices **grow back** on their own over time. Sneak and right-click a whole cake with an empty hand to pick it back up; it drops nothing if you break it.

{{auto}}

## enigmaticlegacyplus:astral_glass, enigmaticlegacyplus:astral_glass_pane
Glowing glass (light 10, or 9 for panes). **Hit it or right-click it** (with anything but a block you could place) to cycle through 4 colour styles, or power it with redstone: the signal strength picks the style. Use **Astral Dust** on it to lock it into a shifting, colourful look for good. It tints beacon beams to match its style. Smelting an Astral Dust Sack gives 4 Astral Glass.

{{auto}}

## enigmaticlegacyplus:etherium_ore
The ore of Etherium, found in End Stone on the **outer End islands** (the biomes where End Cities generate), in small veins. It glows faintly, needs a diamond pickaxe, and drops Raw Etherium and some experience.

{{auto}}

## enigmaticlegacyplus:astral_dust_sack
A storage block of 9 Astral Dust. It sparkles, and smelting it makes 4 {{link:enigmaticlegacyplus:astral_glass}}.

{{auto}}

## enigmaticlegacyplus:infernal_cinder_sack
A storage block of 9 Infernal Cinder that gives off smoke and embers.

{{auto}}

<!-- kind: structures -->

## enigmaticlegacyplus:spellstone_hut
A small hut with a {{link:enigmaticlegacyplus:spellstone_table}} (for crafting spellstones) and a treasure chest.

{{auto}}
