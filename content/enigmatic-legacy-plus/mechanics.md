# Mechanics

EnigmaticLegacy+ comes with an in-game guide, **The Acknowledgment**, reproduced in full in the [guide book](@/enigmatic-legacy-plus/mechanics/the-acknowledgment/index.md) section.

## The Ring of the Seven Curses

The {{link:enigmaticlegacyplus:cursed_ring}} is the heart of the mod. While you wear it, you suffer these curses:

- You take **{{cfg:serverconfig/enigmaticlegacyplus-server.toml|sevenCurses.painMultiplier}}%** damage from every source.
- Neutral creatures within **{{cfg:serverconfig/enigmaticlegacyplus-server.toml|sevenCurses.neutralAngerRange}}** blocks are aggressive toward you.
- Armor is **{{cfg:serverconfig/enigmaticlegacyplus-server.toml|sevenCurses.armorDebuff}}%** less effective.
- Monsters take **{{cfg:serverconfig/enigmaticlegacyplus-server.toml|sevenCurses.monsterDamageDebuff}}%** less damage from you.
- Once on fire, you burn forever.
- You cannot sleep (insomnia).
- Every death tears your soul apart (see Soul Crystals below).

In exchange you get these blessings:

- +**{{cfg:serverconfig/enigmaticlegacyplus-server.toml|sevenCurses.lootingBonus}}** Looting and +**{{cfg:serverconfig/enigmaticlegacyplus-server.toml|sevenCurses.fortuneBonus}}** Fortune
- **{{cfg:serverconfig/enigmaticlegacyplus-server.toml|sevenCurses.experienceBonus}}%** experience from kills
- +**{{cfg:serverconfig/enigmaticlegacyplus-server.toml|sevenCurses.enchantingBonus}}** enchanting power
- unique drops from some creatures
- the Ring of Ender's function
- the ability to use **cursed items**, which only work for a curse bearer

`/cursetime` shows or sets how long a player has borne the curses (see [Commands](@/enigmatic-legacy-plus/commands/index.md)).

## Soul Crystals

When a curse bearer dies, part of their soul becomes a **Soul Crystal** at the place of death. Each lost crystal takes away 10% of your maximum health, up to **{{cfg:serverconfig/enigmaticlegacyplus-server.toml|sevenCurses.maxSoulCrystalLoss}}** crystals (at 10, losing them all means permadeath). Soul Crystals float where you died and can't be destroyed by anyone else, so you can go back and reclaim them.

## Spellstones, rings, amulets and scrolls

- **Spellstones** are powerful curio items with an active ability (press the Spellstone key). They are made at the Spellstone Table.
- **Rings, amulets, charms and scrolls** go into curio slots. Each item page lists its effects and the exact config values.

See [Items](@/enigmatic-legacy-plus/items/index.md) for every item, grouped by type.
