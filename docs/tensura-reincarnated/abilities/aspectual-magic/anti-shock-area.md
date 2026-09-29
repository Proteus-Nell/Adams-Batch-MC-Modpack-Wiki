# Anti-Shock Area

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Anti-Shock Area](../../../assets/icons/tensura/skill/anti_shock_area.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:anti_shock_area` |
| **Element** | Barrier |
| **Max mastery** | 700 |
| **Cooldowns (s)** | 3 mastered, 5 otherwise |
| **Activation** | Press, Hold |

</div>

> Creates a zone around the user that limits all physical damage taken.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 15,000 |  |

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
| `AntiShockArea.castTime` | 220 | Cast time in tick. |
| `AntiShockArea.magiculeCost` | 15,000 | Magicule Cost to cast. |
| `AntiShockArea.radius` | 7.5 | The radius in block of the barrier. |
| `AntiShockArea.radiusMastered` | 15 | The radius in block of the barrier when mastered. |
| `AntiShockArea.duration` | 2,400 | The duration in tick of the barrier. |
| `AntiShockArea.durationMastered` | 3,600 | The duration in tick of the barrier when mastered. |
| `AntiShockArea.antiShockDamage` | 1 | The amount of physical damage that attacks reduce to when applied inside the barrier. |
| `AntiShockArea.cooldown` | 5 | The cooldown in second to create a barrier. |
| `AntiShockArea.cooldownMastered` | 3 | The cooldown in second to create a barrier when mastered. |

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
