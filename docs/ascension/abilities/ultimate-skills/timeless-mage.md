# Timeless Mage

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![Timeless Mage](../../../assets/icons/ascension/skill/timeless_mage.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `ascension:timeless_mage` |
| **Modes** | 3 |
| **Max mastery** | 100 |
| **Activation** | Toggle, Press, Hold |

</div>

> Ultimate awakening of Great Mage. Auto-learns and masters every aspectual and spirit magic; passive chant annulment. Toggle: +29 mastery gain, perfect Analytical Appraisal, magic bypasses resistances, and grants creative flight that Magic Jamming cannot interrupt. Modes: Create Tome / Zoltraak / Magic Dominate.

## Modes

| # | Mode |
|---|---|
| 1 | Create Tome |
| 2 | Zoltraak |
| 3 | Magic Dominate |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Does something when first learned

## Related

- **Related skills:** [Infinite Regeneration](../../../tensura-reincarnated/abilities/extra-skills/infinite-regeneration.md), [Ultraspeed Regeneration](../../../tensura-reincarnated/abilities/extra-skills/ultraspeed-regeneration.md), [Healer](../../../tensura-reincarnated/abilities/unique-skills/healer.md)
- **Effects:** [Self-Regeneration](../../../tensura-reincarnated/effects/self-regeneration.md)
- **Summons / entities:** Zoltraak, Tensura

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `timeless_mage.enabled` | true | Enable Timeless Mage. |
| `timeless_mage.passiveBonus` | 29 (0 to 100) | Mastery-gain attribute bonus while toggled (+29 = 30x faster total). |
| `timeless_mage.dominateCooldownSecondsMastered` | 10 (0 to 3,600) | Magic Dominate cooldown (seconds), mastered. |
| `timeless_mage.dominateCooldownSeconds` | 20 (0 to 3,600) | Magic Dominate cooldown (seconds), unmastered. |
| `timeless_mage.zoltraakInstakillRatio` | 1.5 (1 to 100) | Caster Max EP must exceed target Max EP × this ratio to instakill via Zoltraak. |
| `timeless_mage.zoltraakHpFraction` | 0.1 (0 to 1) | Fraction of target's max HP dealt per Zoltraak damage tick (every 0.5s). |
| `timeless_mage.zoltraakCooldownSecondsMastered` | 5 (0 to 3,600) | Zoltraak cooldown (seconds), mastered. |
| `timeless_mage.zoltraakCooldownSeconds` | 20 (0 to 3,600) | Zoltraak cooldown (seconds), unmastered. |
