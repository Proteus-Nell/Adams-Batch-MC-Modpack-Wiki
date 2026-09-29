# Weather Manipulation

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Weather Manipulation](../../../assets/icons/tensura/skill/weather_manipulation.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:weather_manipulation` |
| **Modes** | 3 |
| **Cooldowns (s)** | 5 mastered, 10 otherwise |
| **Activation** | Press |

</div>

> Use magicule to manipulate the weather.

## Modes

| # | Mode |
|---|---|
| 1 | Clear Weather |
| 2 | Rain |
| 3 | Thunder Storm |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 1,000 |  |

## How it works

- Activated by pressing the skill key
- Does something when mastered

## Obtaining

- Can be learned by: [Davy Jones](../../../ascension/races/davy-jones.md)

## Related

- **Related skills:** [Weather Domination](weather-domination.md), [Water Manipulation](water-manipulation.md), [Wind Manipulation](wind-manipulation.md), [Lightning Manipulation](lightning-manipulation.md)
- **Referenced by:** [Weather Domination](weather-domination.md), [Caedros, God of Conquest](../../../tensura-more-skills/abilities/ultimate-skills/caedros-god-of-conquest.md), [Axiom, Lord of Reflected Judgment](../../../tensura-more-skills/abilities/ultimate-skills/axiom-lord-of-reflected-judgment.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `WeatherManipulation.dominationEpAcquirement` | 400,000 | EP Requirement for to learn Domination. |
| `WeatherManipulation.magiculeCostManipulation` | 1,000 | Magicule Cost to activate Manipulation. |
| `WeatherManipulation.magiculeCostDomination` | 500 | Magicule Cost to activate Domination. |
| `WeatherManipulation.cooldown` | 10 | The cooldown in second when activated Manipulation. |
| `WeatherManipulation.cooldownMastered` | 5 | The cooldown in second when activated Manipulation with mastery. |
| `WeatherManipulation.cooldownDomination` | 5 | The cooldown in second when activated Domination. |
| `WeatherManipulation.cooldownDominationMastered` | 3 | The cooldown in second when activated Domination with mastery. |

## Tags

`tensura:skills/extra_skills`
