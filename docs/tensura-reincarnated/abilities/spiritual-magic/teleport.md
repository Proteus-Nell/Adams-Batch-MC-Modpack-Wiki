# Teleport

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Teleport](../../../assets/icons/tensura/skill/teleport.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:teleport` |
| **Element** | Space |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Cooldowns (s)** | 10 mastered, 20 otherwise |
| **Activation** | Hold |

</div>

> Quickly blink forward in space to a location within view.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 150 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Innate to mobs: [Akash](../../mobs/akash.md)
- Removed and re-rolled when you change race
- Listed in the `formulaSuccessionBlacklist` config option (config/tensuramoreskills-grand.toml): Spell registry IDs that Formula Succession is not allowed to mirror.

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `Teleport.castTime` | 5 | Cast time in tick. |
| `Teleport.castTimeMastered` | 5 | Cast time in tick when mastered. |
| `Teleport.magiculeCost` | 150 | Magicule Cost to cast. |
| `Teleport.magiculeCostBlock` | 10 | Additional Magicule Cost per block to teleport. |
| `Teleport.range` | 30 | The range in block of the magic. |
| `Teleport.rangeMastered` | 50 | The range in block of the magic when mastered. |
| `Teleport.cooldown` | 20 | The cooldown in second of the magic. |
| `Teleport.cooldownMastered` | 10 | The cooldown in second of the magic when mastered. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `SpiritualMagic.masteryLesser` | 100 | The max amount of mastery point for Lesser Spiritual Magic. |
| `SpiritualMagic.masteryLesser` | 100 | The max amount of mastery point for Lesser Spiritual Magic. |
| `SpiritualMagic.masteryMedium` | 500 | The max amount of mastery point for Medium Spiritual Magic. |
| `SpiritualMagic.masteryGreater` | 1,000 | The max amount of mastery point for Greater Spiritual Magic. |
| `SpiritualMagic.masteryLord` | 10,000 | The max amount of mastery point for Lord Spiritual Magic. |

## In-game messages

<details markdown><summary>Show 3 messages</summary>

- You cannot go outside the world border.
- Successfully warped to %s.
- This dimension doesn't match this Warp Point's settings.

</details>

## Tags

`tensura:skills/reset_with_race`, `tensura:skills/spiritual_magic`
