# Mirage

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Mirage](../../../assets/icons/tensura/skill/mirage.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:mirage` |
| **Element** | Illusion |
| **Max mastery** | 300 |
| **Cooldowns (s)** | 3 mastered, 5 otherwise |
| **Activation** | Hold |

</div>

> Create illusionary clones around the caster.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 2,000 |  |

## How it works

- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Can appear in uncommon tomes in rotted wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Related

- **Effects:** [Energy Blockade](../../effects/energy-blockade.md)
- **Summons / entities:** Tensura

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Mirage.castTime` | 60 | Cast time in tick. |
| `Mirage.castTimeMastered` | 120 | Cast time in tick to create more clones when mastered while sneaking. |
| `Mirage.magiculeCost` | 2,000 | Magicule Cost to cast. |
| `Mirage.cloneEP` | 500 | The amount of EP that each illusionary clone has. |
| `Mirage.cloneNumber` | 4 | The number of clones can the magic create each cast. |
| `Mirage.cloneNumberMastered` | 8 | The number of clones can the magic create each cast when mastered while sneaking. |
| `Mirage.cloneDuration` | 300 | The duration in ticks of each Clone before disappearing. |
| `Mirage.cloneDurationMastered` | 600 | The duration in ticks of each Clone before disappearing when mastered. |
| `Mirage.cooldown` | 5 | The cooldown in second to spawn a clone. |
| `Mirage.cooldownMastered` | 3 | The cooldown in second to spawn a clone when mastered. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/uncommon_tome_rotted_wizard_tower`
