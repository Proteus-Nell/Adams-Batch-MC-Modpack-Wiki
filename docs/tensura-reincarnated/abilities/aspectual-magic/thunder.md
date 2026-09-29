# Thunder

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Thunder](../../../assets/icons/tensura/skill/thunder.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:thunder` |
| **Element** | Lightning |
| **Max mastery** | 700 |
| **Cooldowns (s)** | 1 mastered, 3 otherwise |
| **Activation** | Press, Hold |

</div>

> Strike powerful thunder where the caster looks.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 30,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Sold by dwarf traders (high upgraded tome)
- Can appear in rare tomes in ruined wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Related

- **Referenced by:** [Thunder Orb](thunder-orb.md), [Thunder Rain](thunder-rain.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `Thunder.castTime` | 20 | Cast time in tick. |
| `Thunder.magiculeCost` | 30,000 | Magicule Cost to cast. |
| `Thunder.range` | 30 | The range in block of the magic. |
| `Thunder.blastRadius` | 3 | The radius in block of the thunder strike's blast. |
| `Thunder.blastRadiusMastered` | 5 | The radius in block of the thunder strike's blast when mastered. |
| `Thunder.magicDamage` | 100 | The magic damage of the thunder strike. |
| `Thunder.magicDamageMastered` | 200 | The magic damage of the thunder strike when mastered. |
| `Thunder.cooldown` | 3 | The cooldown in second of the magic. |
| `Thunder.cooldownMastered` | 1 | The cooldown in second of the magic when mastered. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/high_upgraded_tome_dwarf_trade`, `tensura:skills/rare_tome_ruined_wizard_tower`
