# `config/tensura/ascension-common.toml`

<small>[Ascension](../index.md) &rsaquo; [Configs](index.md)</small>

## `[Skills]`

Skills added to Tensura's reincarnation pools by this addon.

| Option | Default | Range | Description |
|---|---|---|---|
| `additionalUniqueSkills` | "ascension:eye_of_mind", "ascension:great_mage", "ascension:king_of_curses", "ascension:bubble_majin", "ascension:sealer", "ascension:dragon_slayer", "ascension:imprisoned_jester", "ascension:deus_sanguis", "ascension:trash_gamer" |  | Unique skills added to the reincarnation pool.<br>Remove an entry to exclude that skill from random reincarnation rolls. |

## `[Integrations]`

Integrations with other mods.

| Option | Default | Range | Description |
|---|---|---|---|
| `enableIronsSpellbooksCompat` | true |  | Enable Iron's Spellbooks integration.<br>When on: Tensura race tier/alignment grants IS spell-power and mana bonuses,<br>Tensura's magic cost multiplier scales IS spell mana costs,<br>and Whisper Djinn players are granted the Magic Scribe skill.<br>When off: these behaviors are disabled at runtime (no restart required).<br>Has no effect if Iron's Spellbooks is not installed. |

## `[Races.Djinn]`

Race-specific tweaks applied on top of the base Tensura race system.

| Option | Default | Range | Description |
|---|---|---|---|
| `noHungerAtWishbound` | true |  | When true, players whose race is Wishbound Djinn or any later djinn tier<br>(Primordial / Ascended / Sovereign / Infinite / Omniversal) stop losing hunger<br>and saturation — the food bar is kept topped up each tick, mirroring how<br>slimes don't need to eat. Disable to restore vanilla hunger behaviour. |

## `[Races.Dimensions.HyperbolicChamber]`

Hyperbolic Chamber dimension tunables.

| Option | Default | Range | Description |
|---|---|---|---|
| `epMultiplier` | 3 | 1 to 100 | Multiplier applied to EP gained from kills inside the Hyperbolic Chamber.<br>3.0 = triple the EP. Set to 1.0 to disable the bonus.<br>Stacks multiplicatively with Tensura's own gear/alignment EP-gain modifiers —<br>applied AFTER Tensura's listener computes the base, so 'EP_GAIN' attribute<br>buffs and gamerule caps still apply normally. |

## `[Races.Dimensions.Awakening]`

Ultimate Awakening ritual tunables.

| Option | Default | Range | Description |
|---|---|---|---|
| `cooldownMinutes` | 120 | 0 to 1,440 | Real-time minutes a player must wait between successful awakening<br>rituals. Per-player cooldown — building more altars doesn't bypass it.<br>0 disables the cooldown entirely. |
