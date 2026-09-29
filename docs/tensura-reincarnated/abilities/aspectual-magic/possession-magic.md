# Possession

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Possession](../../../assets/icons/tensura/skill/possession_magic.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:possession_magic` |
| **Element** | Illusion |
| **Max mastery** | 1,500 |
| **Activation** | Press, Hold |

</div>

> Possess a weakened material body to gain a new powers from that body.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 100,000 |  |

## How it works

- Activated by pressing the skill key
- Triggers when the held key is released

## Obtaining

- Can appear in epic tomes from wizard towers

## Related

- **Effects:** [Energy Blockade](../../effects/energy-blockade.md)
- **Referenced by:** [Possession](../intrinsic-skills/possession.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Possession.castTime` | 200 | Cast time in tick. |
| `Possession.magiculeCost` | 100,000 | Magicule Cost to cast. |
| `Possession.range` | 6 | The range in block of the magic. |
| `Possession.hpMultiplier` | 0.1 | The multiplier of the maximum Health that a target needs to be under to be possessed. |
| `Possession.shpMultiplier` | 0.1 | The multiplier of the maximum Spiritual Health that a target needs to be under to be possessed. |
| `Possession.epMultiplier` | 0.25 | The multiplier of the user's maximum EP that a target needs to be under to be possessed. |
| `Possession.resistanceMultiplier` | 0.5 | The multiplier of the possession requirement multipliers when the target has Spiritual Attack Resistance. |
| `Possession.maxHealth` | 1,000 | The maximum amount of HP the user can get from possessing an entity. |
| `Possession.maxAttack` | 100 | The maximum amount of Attack Damage the user can get from possessing an entity. |
| `Possession.bodyDespawnTick` | 300 | The number of seconds that Possession Bodies will despawn. (0 = instant despawn, -1 = doesn't despawn) |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

## Tags

`tensura:skills/aspectual_magic`, `tensura:skills/epic_tome_wizard_tower`, `tensura:skills/unlearnt_cast_excluded`
