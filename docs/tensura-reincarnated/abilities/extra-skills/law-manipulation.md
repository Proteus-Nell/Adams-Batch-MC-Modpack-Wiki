# Law Manipulation

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Law Manipulation](../../../assets/icons/tensura/skill/law_manipulation.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:law_manipulation` |
| **Modes** | 2 |
| **Activation** | Toggle, Press |

</div>

> Bypass many restrictions by manipulating the law of the world.

## Modes

| # | Mode |
|---|---|
| 1 | Abnormality Cleanse |
| 2 | Takeover |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key

## Obtaining

- Can be learned by: [Ascended Djinn](../../../ascension/races/ascended-djinn.md), [Sovereign Djinn](../../../ascension/races/sovereign-djinn.md), [Infinite Djinn](../../../ascension/races/infinite-djinn.md), [Omniversal Djinn](../../../ascension/races/omniversal-djinn.md)
- Acquisition checks: [Mana Manipulation](mana-manipulation.md)

## Related

- **Related skills:** [Mana Manipulation](mana-manipulation.md)
- **Effects:** [Magic Interference](../../effects/magic-interference.md)
- **Referenced by:** [Analyst](../unique-skills/analyst.md), [Seeker](../unique-skills/seeker.md), [Hive King](../../../tr-nightmares/abilities/ultimate-skills/hive-king.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `LawManipulation.epAcquirement` | 800,000 | EP Requirement for Learning. |
| `LawManipulation.magicMastered` | 30 | The number of Magic needed to be mastered to learn. |
| `LawManipulation.resistBypassEP` | 1,000,000 | The amount of EP that the user needs to have minimum to be able to bypass Resist Skills with Magic/Battlewill when toggled. |
| `LawManipulation.cleanseRange` | 20 | The range in block of Abnormality Cleanse. |
| `LawManipulation.takeoverRange` | 30 | The range in block of Takeover. |
| `LawManipulation.brokenMagicCooldown` | 2 | The cooldown in second of the magic circle destroyed by Takeover for the targeted caster. |
| `LawManipulation.brokenMagicCooldownMastered` | 4 | The cooldown in second of the magic circle destroyed by Takeover for the targeted caster when mastered. |
| `LawManipulation.takeoverMultiplier` | 0.75 | The multiplier of the user's EP that a target with Law Manipulation needs to have above to be unaffected by Takeover. |

## Tags

`tensura:skills/extra_skills`, `tensura:skills/no_plundering`
