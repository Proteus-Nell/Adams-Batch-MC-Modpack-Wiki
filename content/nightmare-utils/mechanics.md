# Mechanics

Nightmare Utils (Nightmare's Tensura Utils) is a library that [TR: Nightmares](@/tr-nightmares/index.md) and other Tensura addons build on. Most of what it adds is used through other mods, but it also brings a few systems of its own.

## Mimicry

Mimicry lets a skill copy the appearance, and some of the skills, of a creature or player it has analysed:

1. **Mimicry Analysis** stores a target's data (players, entities and races can each be stored).
2. The Mimicry menu lists what you have stored. For each entry it shows the intrinsic, extra, common and resistance skills it would grant, or notes that a player entry applies only their skin.
3. Applying an entry turns you into that creature or player. Some targets can't be analysed.

## Awakenings and weapon presets

The library tracks progress-based **awakenings** that other mods define (see `/nightmareutils awakening ...` on the [Commands](@/nightmare-utils/commands/index.md) page). It also stores **weapon presets** for weapons with abilities.

The skills listed under [Abilities](@/nightmare-utils/abilities/index.md) are mostly test and helper skills used by other mods.
