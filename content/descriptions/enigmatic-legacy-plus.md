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
