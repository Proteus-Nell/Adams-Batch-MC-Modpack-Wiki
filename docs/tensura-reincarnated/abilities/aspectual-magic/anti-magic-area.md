# Anti-Magic Area

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Anti-Magic Area](../../../assets/icons/tensura/skill/anti_magic_area.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:anti_magic_area` |
| **Element** | Barrier |
| **Max mastery** | 700 |
| **Cooldowns (s)** | 3 mastered, 5 otherwise |
| **Activation** | Press, Hold |

</div>

> Creates a zone around the user that limits all Aspectual and Summoning Magics.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 20,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Can appear in rare tomes in buried wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `AntiMagicArea.castTime` | 220 | Cast time in tick. |
| `AntiMagicArea.magiculeCost` | 20,000 | Magicule Cost to cast. |
| `AntiMagicArea.radius` | 10 | The radius in block of the barrier. |
| `AntiMagicArea.radiusMastered` | 25 | The radius in block of the barrier when mastered. |
| `AntiMagicArea.duration` | 1,200 | The duration in tick of the barrier. |
| `AntiMagicArea.cooldown` | 5 | The cooldown in second to create a barrier. |
| `AntiMagicArea.cooldownMastered` | 3 | The cooldown in second to create a barrier when mastered. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

## Tags

`tensura:skills/aspectual_magic`, `tensura:skills/rare_tome_buried_wizard_tower`
