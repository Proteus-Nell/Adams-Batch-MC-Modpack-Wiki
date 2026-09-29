# Exoskeleton

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Exoskeleton](../../../assets/icons/mysticism/skill/exoskeleton.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `mysticism:exoskeleton` |
| **Cooldowns (s)** | 3 |
| **Activation** | Toggle, Hold |

</div>

> The Insects of the other world all possess this tough Exoskeleton. It grows together with the user, and even allows them to wear armor on top of it.

## How it works

- Can be toggled on and off
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| armor | ulate armor | add |
| toughness | ulate toughness | add |

## Obtaining

- Innate to mobs: [Army Wasp](../../../tensura-reincarnated/mobs/army-wasp.md), [Black Spider](../../../tensura-reincarnated/mobs/black-spider.md), [Knight Spider](../../../tensura-reincarnated/mobs/knight-spider.md)
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/beetle_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/centipede_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/ant_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/scorpion_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/mantis_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/wasp_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Related skills:** [Dragon Skin](../../../tensura-reincarnated/abilities/intrinsic-skills/dragon-skin.md)
- **Items:** [Monster Leather (Special A)](../../../tensura-reincarnated/items/miscellaneous/monster-leather-special-a.md), [Monster Leather (A)](../../../tensura-reincarnated/items/miscellaneous/monster-leather-a.md), [Monster Leather (B)](../../../tensura-reincarnated/items/miscellaneous/monster-leather-b.md), [Monster Leather (C)](../../../tensura-reincarnated/items/miscellaneous/monster-leather-c.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/intrinsic_config.toml`](../../configs/config-mysticism-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `Exoskeleton.hihiirokaneEP` | 4,000,000 | The amount of EP needed for Hihi'irokane Armor's stats. |
| `Exoskeleton.mlSAEP` | 800,000 | The amount of EP needed for Monster Leather Special A Armor's stats. |
| `Exoskeleton.mlAEP` | 80,000 | The amount of EP needed for Monster Leather A Armor's stats. |
| `Exoskeleton.mlBEP` | 50,000 | The amount of EP needed for Monster Leather B Armor's stats. |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/intrinsic_skills`
