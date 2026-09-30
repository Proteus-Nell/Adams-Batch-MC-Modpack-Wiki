# Scholar

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Scholar](../../../assets/icons/mysticism/skill/scholar.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:scholar` |
| **Activation** | Toggle, Press |

</div>

> Learn and master skills quicker. Study your targets when they attack. Learn enchantments and apply them to weaponry.

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Triggers when you are attacked
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| learning | 6 | add |
| mastery | 6 | add |

## Related

- **Summons / entities:** Tensura

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Scholar.mpAcquirement` | 35,000 | Magicule Acquirement Cost. |
| `Scholar.learningPoint` | 6 | The bonus number of learning point to gain when toggled. |
| `Scholar.masteryPoint` | 6 | The bonus number of mastery point to gain when toggled. |
| `Scholar.studyChance` | 20 | The chance to study the opponent when they attack you. |
| `Scholar.studyDodgeBase` | 0 | The base dodge chance without studying the opponent. |
| `Scholar.studyDodgePerPoint` | 1 | The study points that translate into dodge chance you gain towards that entity type whenever you successfully study them. |
| `Scholar.studyDodgePlayerMax` | 50 | The maximum amount of dodge chance you can gain against players. |
| `Scholar.studyDodgePlayerMaxMastered` | 70 | The maximum amount of dodge chance you can gain against players when the skill is mastered. |
| `Scholar.studyDodgeEntityMax` | 75 | The maximum amount of dodge chance you can gain against a specific entity type. |
| `Scholar.studyDodgeEntityMaxMastered` | 100 | The maximum amount of dodge chance you can gain against a specific entity type when the skill is mastered. |
| `Scholar.enchantmentBlacklist` | - | Lists of enchantments that Scholar cannot learn or enchant. |
| `Scholar.maxBonusBlacklist` | - | Lists of enchantments that Scholar cannot learn or enchant above the enchantment's maximum level. |
| `Scholar.maxBonusLevel` | 5 | The maximum bonus of level that the player can increase. |

## In-game messages

<details markdown><summary>Show 4 messages</summary>

- You could not raise the book's level! Needs %s experience levels.
- By lowering the level of [%s] you have received %s experience levels.
- Enchantment [%s]'s level was raised! Consumed %s experience levels.
- Gained a study point for %s!

</details>

## Tags

`tensura:skills/unique_skills`
