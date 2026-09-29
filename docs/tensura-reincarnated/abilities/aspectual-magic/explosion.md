# Explosion

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Explosion](../../../assets/icons/tensura/skill/explosion.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:explosion` |
| **Element** | Explosion |
| **Modes** | 2 |
| **Max mastery** | 1,500 |
| **Activation** | Press, Hold |

</div>

> Summon a single beam of light, that detonates at the target, creating a devastating blast of pure magical power.

## Modes

| # | Mode |
|---|---|
| 1 | Explosion Strike |
| 2 | Explosion Trap |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 10,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Can appear in epic tomes from wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Related

- **Referenced by:** [Chain Explosion](chain-explosion.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Explosion.castTimeLevel` | 50 | Cast time in tick per level. |
| `Explosion.magiculeCost` | 10,000 | Magicule Cost multiplier to add up each level (level 1 = 10,000 and level 2 equals 20,000 for a total cost of 30,000. Level 3 total cost would be 60,000, etc.) |
| `Explosion.range` | 64 | The range in block of the explosion mode. |
| `Explosion.rangeTrap` | 20 | The range in block of the Trap mode. |
| `Explosion.blastRadius` | 5 | The radius in block of the explosion each level. |
| `Explosion.magicDamage` | 100 | The magic damage of the explosion each level. |
| `Explosion.minLevel` | 3 | The min level the explosion mode has to reach to be casted. |
| `Explosion.maxLevel` | 5 | The max level the explosion mode can reach. |
| `Explosion.maxLevelMastered` | 10 | The max level the explosion mode can reach when mastered. |
| `Explosion.maxLevelTrap` | 3 | The max level the Trap mode can reach. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |
| `unlearntCastMultiplier` | 2 | The multiplier of cast time compared to normal cast when casting a unlearnt magic from a magic-holder item. |

## Tags

`tensura:skills/aspectual_magic`, `tensura:skills/epic_tome_wizard_tower`
