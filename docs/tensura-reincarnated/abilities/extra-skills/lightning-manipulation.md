# Lightning Manipulation

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Lightning Manipulation](../../../assets/icons/tensura/skill/lightning_manipulation.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:lightning_manipulation` |
| **Activation** | Toggle, Press |

</div>

> Boosts Lightning abilities by a decent amount.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 100 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Does something when mastered

## Obtaining

- Listed in the `intrinsicSkills` config option (config/mysticism/race/sculk_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/direwolf/special_direwolf_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/beetle_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Related skills:** [Lightning Domination](lightning-domination.md)
- **Referenced by:** [Lightning Domination](lightning-domination.md), [Weather Manipulation](weather-manipulation.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `LightningManipulation.lightningSkillAcquirement` | 3 | The number of mastered lightning skills needed to learn Lightning Manipulation. |
| `LightningManipulation.magiculeCost` | 100 | Magicule Cost to activate. |
| `LightningManipulation.dominationEpAcquirement` | 400,000 | EP Requirement for to learn Domination. |
| `LightningManipulation.resistDegradationAcquirement` | 800,000 | EP Requirement for to use Resist Degradation when mastered. |
| `LightningManipulation.manipulationBoost` | 1.5 | The Lightning Damage Boost when activated Manipulation. |
| `LightningManipulation.dominationBoost` | 3 | The Lightning Damage Boost when activated Domination. |
| `LightningManipulation.boltDamage` | 15 | How much damage that the Lightning Bolt does when activated. |
| `LightningManipulation.boltRange` | 3 | The range for damage that the Lightning Bolt does when activated. |
| `LightningManipulation.boltDamageDomination` | 30 | How much damage that the Domination Lightning Bolt does when activated. |
| `LightningManipulation.boltRangeDomination` | 5 | The range for damage that the Domination Lightning Bolt does when activated. |

## Tags

`tensura:skills/extra_skills`, `tensura:skills/lightning_skills`
