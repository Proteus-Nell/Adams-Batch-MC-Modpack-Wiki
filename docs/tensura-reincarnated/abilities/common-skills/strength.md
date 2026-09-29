# Strength

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Common Skills](index.md)</small>

<div class="infobox" markdown>

![Strength](../../../assets/icons/tensura/skill/strength.png)

| | |
|---|---|
| **Type** | Common Skill |
| **ID** | `tensura:strength` |
| **Cooldowns (s)** | 3, 3 + duration ÷ 20 |
| **Activation** | Toggle, Press |

</div>

> Use magicule to strengthen your muscles.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 30 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect

## Obtaining

- Intrinsic skill of: [Ogre](../../races/ogre.md), [Kijin](../../races/kijin.md), [Enlightened Ogre](../../races/enlightened-ogre.md), [Mystic Oni](../../races/mystic-oni.md), [Wicked Oni](../../races/wicked-oni.md), [Spirit Oni](../../races/spirit-oni.md), [Death Oni](../../races/death-oni.md), [Divine Oni](../../races/divine-oni.md), [Divine Fighter](../../races/divine-fighter.md), [Ghoul](../../races/ghoul.md), [Vampire](../../races/vampire.md), [Vampire Overcomer](../../races/vampire-overcomer.md), [Vampire Lord](../../races/vampire-lord.md), [Divine Vampire](../../races/divine-vampire.md), [Monkey Warrior](../../../ascension/races/monkey-warrior.md), [Monkey Martial Artist](../../../ascension/races/monkey-martial-artist.md), [Monkey King](../../../ascension/races/monkey-king.md), [Divine King](../../../ascension/races/divine-king.md), [Sun Wukong](../../../ascension/races/sun-wukong.md)
- Innate to mobs: [Mark Lauren](../../mobs/mark-lauren.md), [Orc Disaster](../../mobs/orc-disaster.md), [Orc Lord](../../mobs/orc-lord.md)
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/beetle_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Effects:** [Strengthen](../../effects/strengthen.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/common_config.toml`](../../configs/config-tensura-ability-skill-common-config.md).

| Option | Default | Description |
|---|---|---|
| `Strength.epAcquirement` | 3,000 | EP Requirement for Learning. |
| `Strength.magiculeCost` | 30 | Base Magicule Cost to activate. |
| `Strength.strengthenDuration` | 1,200 | The duration of the Strengthen effect when activated. |
| `Strength.strengthenDurationMastered` | 2,400 | The duration of the Strengthen effect when activated with mastery. |
| `Strength.strengthenLevel` | 1 | The level of the Strengthen effect when activated (+3 Attack Damage per level). |
| `Strength.strengthenLevelMastered` | 2 | The level of the Strengthen effect when activated with Mastered. |
| `Strength.cooldown` | 3 | The Cooldown in second of the skill. |

## Tags

`tensura:skills/common_skills`
