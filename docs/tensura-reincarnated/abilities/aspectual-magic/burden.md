# Burden

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Burden](../../../assets/icons/tensura/skill/burden.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:burden` |
| **Element** | Gravity |
| **Max mastery** | 100 |
| **Activation** | Hold |

</div>

> Shoot energy projectiles that increase the target's gravity.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 50 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Sold by dwarf traders (low upgraded tome)
- Can appear in uncommon tomes in buried wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.
- Listed in the `effectToRemove` config option (config/tensura/ability/battlewill_config.toml): The List of harmful effects that get removed upon activation.
- Listed in the `effectImmunities` config option (config/nightmare/ability/skill/nightmare_unique.toml): List of effects stopped by Force.

## Related

- **Referenced by:** [Magma Surge](../spiritual-magic/magma-surge.md), [Earth Jail](../spiritual-magic/earth-jail.md), [Oppressor](../unique-skills/oppressor.md), [Reverser](../unique-skills/reverser.md), [Survivor](../unique-skills/survivor.md), [Earth Transform](../intrinsic-skills/earth-transform.md), [Abnormal Condition Resistance](../resistance-skills/abnormal-condition-resistance.md), [Abnormal Condition Nullification](../resistance-skills/abnormal-condition-nullification.md), [Gravity Attack Nullification](../resistance-skills/gravity-attack-nullification.md), [Imaginator](../../../tr-nightmares/abilities/unique-skills/imaginator.md), [｢ Mammon, Lord of Greed ｣](../../../tr-nightmares/abilities/ultimate-skills/mammon.md), [Gravity Well](../../../elite-tensura/abilities/aspectual-magic/gravity-well.md), [Naberius](../../../tensura-more-skills/abilities/ultimate-skills/naberius.md), [Caedros, God of Conquest](../../../tensura-more-skills/abilities/ultimate-skills/caedros-god-of-conquest.md), [Pain, Lord of Six Paths](../../../tensura-more-skills/abilities/ultimate-skills/pain-lord-of-six-paths.md), [Gravity Flux](../../../tensura-mysticism/abilities/extra-skills/gravity-flux.md), [Coalescence](../../../tensura-mysticism/abilities/unique-skills/coalescence.md), [Melancholy](../../../tensura-mysticism/abilities/unique-skills/melancholy.md), [Restricted](../../../tensura-mysticism/abilities/unique-skills/restricted.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Burden.castTime` | 80 | Cast time in tick. |
| `Burden.magiculeCost` | 50 | Magicule Cost to cast. |
| `Burden.burdenLevel` | 3 | The level of the Burden effect of the projectile. |
| `Burden.burdenDuration` | 600 | The duration in tick of the Burden effect of the projectile. |
| `Burden.slownessLevel` | 2 | The level of the Slowness effect of the projectile when mastered. |
| `Burden.slownessDuration` | 600 | The duration in tick of the Slowness effect of the projectile when mastered. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

## Tags

`tensura:skills/aspectual_magic`, `tensura:skills/low_upgraded_tome_dwarf_trade`, `tensura:skills/uncommon_tome_buried_wizard_tower`
