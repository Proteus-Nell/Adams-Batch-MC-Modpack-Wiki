# Steel Strength

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Steel Strength](../../../assets/icons/tensura/skill/steel_strength.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:steel_strength` |
| **Cooldowns (s)** | 3, 3 + duration ÷ 20 |
| **Activation** | Toggle, Press |

</div>

> Strengthen your muscles and gain an increase in damage, toggleable when mastered.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 30 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect

## Obtaining

- Intrinsic skill of: [Enlightened Ogre](../../races/enlightened-ogre.md), [Mystic Oni](../../races/mystic-oni.md), [Spirit Oni](../../races/spirit-oni.md), [Divine Oni](../../races/divine-oni.md), [Giant](../../races/giant.md), [Ancient Giant](../../races/ancient-giant.md), [Divine Giant](../../races/divine-giant.md), [Vampire](../../races/vampire.md), [Vampire Overcomer](../../races/vampire-overcomer.md), [Vampire Lord](../../races/vampire-lord.md), [Divine Vampire](../../races/divine-vampire.md)
- Can be learned by: [Cursed Mariner](../../../ascension/races/cursed-mariner.md), [Cursed Dreadnaught](../../../ascension/races/cursed-dreadnaught.md), [Phantom Corsair](../../../ascension/races/phantom-corsair.md), [Davy Jones](../../../ascension/races/davy-jones.md), [Monkey Warrior](../../../ascension/races/monkey-warrior.md), [Monkey Martial Artist](../../../ascension/races/monkey-martial-artist.md), [Monkey King](../../../ascension/races/monkey-king.md), [Divine King](../../../ascension/races/divine-king.md), [Sun Wukong](../../../ascension/races/sun-wukong.md)
- Innate to mobs: [Folgen](../../mobs/folgen.md), [Memoires](../../../tensura-mysticism/mobs/memoires.md)
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/mantis_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Effects:** [Strengthen](../../effects/strengthen.md)
- **Referenced by:** [Mithril Strength](../../../tensura-mysticism/abilities/extra-skills/mithril-strength.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `SteelStrength.epAcquirement` | 20,000 | EP Requirement for Learning. |
| `SteelStrength.magiculeCost` | 30 | Magicule Cost to activate. |
| `SteelStrength.strengthenDuration` | 600 | The duration of the Strengthen effect when activated. |
| `SteelStrength.strengthenDurationMastered` | 1,800 | The duration of the Strengthen effect when activated with mastery. |
| `SteelStrength.strengthenLevel` | 2 | The level of the Strengthen effect when activated (+3 Attack Damage per level). |
| `SteelStrength.strengthenLevelMastered` | 3 | The level of the Strengthen effect when activated when Mastered. |
| `SteelStrength.cooldown` | 3 | The Cooldown in second of the skill. |

## Tags

`tensura:skills/extra_skills`
