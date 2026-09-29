# ｢ Amaterasu, Lord of Shimmering Flames ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![｢ Amaterasu, Lord of Shimmering Flames ｣](../../../assets/icons/trnightmare/skill/amaterasu.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:amaterasu` |
| **Modes** | 5 |
| **Acquisition cost (MP)** | 350,000 |
| **Max mastery** | 5,000 |
| **Activation** | Toggle, Press |

</div>

> Fine mastery over mixing Light, heat, and energy in all forms into every movement, accelerating to light speed.

## Modes

| # | Mode |
|---|---|
| 1 | Thought Communication: Movement |
| 2 | Thought Communication: Targeting |
| 3 | Thought Domination |
| 4 | Hundred Petals Rush |
| 5 | Prominence Acceleration |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Hundred Petals Rush | 150,000 | 150,000 |
| Prominence Acceleration | 100,000 | 50,000 |
| other modes | *set by config (base aura cost)* | *set by config (base aura cost)* |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect

## Obtaining

- Listed in the `astralMasteredCreationUltimates` config option (config/nightmare/ability/skill/nightmare_ult.toml): Ultimate skill IDs only offered from Astral Light Skill Creation when Astral Light is mastered.
- Listed in the `allowedSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can be affected by Raphael-style alteration by default.
- Acquisition checks: [Commander](../../../tensura-reincarnated/abilities/unique-skills/commander.md), [｢ Amaterasu, Lord of Shimmering Flames ｣](amaterasu.md)
- In-game message: *Understood, General, your people need you just as you need them. Fight with the might of the Flame Dragon's Magic, and victory is assured.*

## Related

- **Related skills:** [Commander](../../../tensura-reincarnated/abilities/unique-skills/commander.md), [Haze](../../../tensura-reincarnated/abilities/battlewill/haze.md), [Heat Wave](../../../tensura-reincarnated/abilities/extra-skills/heat-wave.md)
- **Effects:** [Inspiration](../../../tensura-reincarnated/effects/inspiration.md), [Black Burn](../../../tensura-reincarnated/effects/black-burn.md)
- **Referenced by:** [Alteration](../extra-skills/alteration.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Amaterasu.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Amaterasu.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Amaterasu.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Amaterasu.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Amaterasu.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Amaterasu.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Amaterasu.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Amaterasu.mpAcquirement` | 350,000 | Magicule Acquirement Cost. |
| `Amaterasu.degradationExistence` | 800,000 | Existence Point requirement for resistance degradation on Mastery. |
| `Amaterasu.magiculeCostPetals` | 150,000 | Magicule cost of Hundred Petals Rush. |
| `Amaterasu.auraCostPetals` | 150,000 | Aura cost of Hundred Petals Rush. |
| `Amaterasu.magiculeCostProminence` | 100,000 | Magicule cost of Prominence Acceleration. |
| `Amaterasu.auraCostProminence` | 50,000 | Aura cost of Prominence Acceleration. |
| `Amaterasu.damageMultiplier` | 3.5 | Damage Multiplier for Light, Heat, Flame, and Spatial damage. |
| `Amaterasu.inspirationLevel` | 1 | Inspiration level gained by subordinates nearby, +1 on mastery (put 0 to disable). |
| `Amaterasu.petalMultiplier` | 3 | Damage Multiplier for Hundred Petals Rush (Doubled on Mastery). |
| `Amaterasu.prominenceMultiplier` | 10 | Damage Multiplier for Prominence Acceleration. |
| `Amaterasu.amaterasuSubordinates` | 20 | Number of Subordinates required to obtain Amaterasu, Lord of Shimmering Flames. |
| `Amaterasu.amaterasuHealth` | 60 | Percentage of HP required to obtain Amaterasu, Lord of Shimmering Flames. |
| `Amaterasu.enableUltimateEvolution` | true | Whether Amaterasu evolution is allowed. |
| `ultMasteryConfig.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `ultMasteryConfig.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `ultMasteryConfig.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `ultMasteryConfig.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `ultMasteryConfig.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `ultMasteryConfig.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `ultMasteryConfig.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |

## Tags

`tensura:skills/ultimate_skills`
