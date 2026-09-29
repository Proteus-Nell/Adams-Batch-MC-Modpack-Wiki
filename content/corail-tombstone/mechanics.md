# Mechanics

## Graves

When you die, your items go into a **grave** at the spot where you died instead of spilling on the ground. You keep a **Grave's Key**, which lets you:

- see your grave from a distance
- teleport to it
- recover your items by right-clicking the grave or sneaking over it

If a decay time is set (it is off by default), graves unlock for everyone once it runs out. You lose **{{cfg:serverconfig/tombstone-server.toml|player_death.xp_loss_on_death}}%** of your experience on death, and you get the **Ghostly Shape** effect for **{{cfg:serverconfig/tombstone-server.toml|player_death.ghostly_shape_duration}}** seconds after respawning.

## Knowledge of Death and perks

You earn **Knowledge of Death** as you go, for example by praying with the Ankh of Prayer near a decorative grave. Its levels are spent on [Perks](@/corail-tombstone/perks/index.md). Operators can adjust it with `/tbknowledge`.

## Alignment

Your alignment goes up or down with what you do:

- **Raises it:** freeing souls from graves with a Receptacle of Soul, defending villages during a siege, exorcising zombie villagers, and similar good deeds.
- **Lowers it:** killing villagers, plundering graves without the key, killing your own pets, and similar bad deeds.

Alignment unlocks some perks and magic items, and it reduces damage from undead or living creatures depending on which side you are on.

## Compendium

The mod's in-game compendium explains every magic item, enchantment and system:

{{langtable:tombstone\.compendium\.(.+)\.desc|Topic}}
