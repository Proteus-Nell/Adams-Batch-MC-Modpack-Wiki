# Acid Shell

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Acid Shell](../../../assets/icons/tensura/skill/acid_shell.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:acid_shell` |
| **Element** | Water |
| **Max mastery** | 700 |
| **Activation** | Press, Hold |

</div>

> Shoots a ball of corrosive acid toward targets.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 38,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Innate to mobs: [Arch Daemon](../../mobs/arch-daemon.md), [Greater Daemon](../../mobs/greater-daemon.md)
- Sold by dwarf traders (high basic tome)
- Can appear in rare tomes in frozen wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.
- Listed in the `grantedSkillIds` config option (config/tensuramoreskills-grand.toml): Skill registry IDs automatically granted with Albis Vina.

## Related

- **Effects:** [Corrosion](../../effects/corrosion.md)
- **Summons / entities:** Acid Ball

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `AcidShell.castTime` | 80 | Cast time in tick. |
| `AcidShell.magiculeCost` | 38,000 | Magicule Cost to cast. |
| `AcidShell.magicDamage` | 175 | The magic damage of the projectile. |
| `AcidShell.armorHurt` | 300 | The durability that the target's armors get reduced when hit by the projectile. |
| `AcidShell.corrosionLevel` | 2 | The level of the Corrosion effect of the projectile when mastered. |
| `AcidShell.corrosionDuration` | 400 | The duration in tick of the Corrosion effect of the projectile when mastered. |
| `AcidShell.cooldown` | 3 | The cooldown in second of the magic. |
| `AcidShell.cooldownMastered` | 1 | The cooldown in second of the magic when mastered. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/high_basic_tome_dwarf_trade`, `tensura:skills/rare_tome_frozen_wizard_tower`
