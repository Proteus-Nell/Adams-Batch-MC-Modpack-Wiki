# Dominate

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Dominate](../../../assets/icons/tensura/skill/dominate.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:dominate` |
| **Element** | Mental |
| **Max mastery** | 300 |
| **Activation** | Press, Hold |

</div>

> Dominate over any low-leveled targets.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 10,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Can appear in rare tomes in buried wizard towers
- Can appear in rare tomes in burnt wizard towers
- Can appear in rare tomes in frozen wizard towers
- Can appear in rare tomes in ruined wizard towers
- Can appear in uncommon tomes in rotted wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Related

- **Related skills:** [Spiritual Attack Resistance](../resistance-skills/spiritual-attack-resistance.md)
- **Effects:** [Mind Control](../../effects/mind-control.md)
- **Referenced by:** [Demon Dominate](demon-dominate.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Dominate.castTime` | 100 | Cast time in tick. |
| `Dominate.magiculeCost` | 10,000 | Magicule Cost to cast. |
| `Dominate.range` | 6 | The range in block of the magic. |
| `Dominate.epRequirement` | 10,000 | The amount of EP that the target needs to have below to be controlled. |
| `Dominate.resistedRequirement` | 5,000 | The amount of EP that the target needs to have below to be controlled when having Spiritual Attack Resistance toggled. |
| `Dominate.controlDuration` | 12,000 | The duration in tick of the Mind Control effect (-1 = permanent). |
| `Dominate.controlDurationMastered` | -1 | The duration in tick of the Mind Control effect when mastered (-1 = permanent). |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

## Tags

`tensura:skills/aspectual_magic`, `tensura:skills/rare_tome_buried_wizard_tower`, `tensura:skills/rare_tome_burnt_wizard_tower`, `tensura:skills/rare_tome_frozen_wizard_tower`, `tensura:skills/rare_tome_ruined_wizard_tower`, `tensura:skills/uncommon_tome_rotted_wizard_tower`
