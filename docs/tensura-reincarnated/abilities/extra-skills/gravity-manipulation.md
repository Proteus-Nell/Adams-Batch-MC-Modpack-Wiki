# Gravity Manipulation

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Gravity Manipulation](../../../assets/icons/tensura/skill/gravity_manipulation.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:gravity_manipulation` |
| **Activation** | Toggle, Press |

</div>

> Boosts Gravity abilities by a decent amount and allows you to fly without hindrance.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 1,000 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Triggers when you damage a target
- Does something when mastered

## Obtaining

- Intrinsic skill of: [qFairy pPrince](../../../tr-nightmares/races/fairy-prince.md)
- Can be learned by: [Void Dragonewt](../../../ascension/races/void-dragonewt.md), [Abyssal Dragonewt](../../../ascension/races/abyssal-dragonewt.md), [Chaos Dragon](../../../ascension/races/chaos-dragon.md)
- Innate to mobs: [Charybdis](../../mobs/charybdis.md)
- Listed in the `charybdisCoreSkills` config option (config/tensura/block_config.toml): List of Skills that can be obtained from right-clicking Inert Charybdis Core.
- Listed in the `charybdisCoreFusingSkills` config option (config/tensura/block_config.toml): List of Skills that can be obtained from fusing with Inert Charybdis Core using Degenerate and similar abilities.
- Listed in the `charybdisCoreFusingSkillsActive` config option (config/tensura/block_config.toml): List of Skills that can be obtained from fusing with Active Charybdis Core using Degenerate and similar abilities.
- Listed in the `charybdisCoreFusingSkillsInactive` config option (config/tensura/block_config.toml): List of Skills that can be obtained from fusing with Inactive Charybdis Core using Degenerate and similar abilities.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/scorpion_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Related skills:** [Gravity Domination](gravity-domination.md)
- **Effects:** [Magic Interference](../../effects/magic-interference.md)
- **Referenced by:** [Oppressor](../unique-skills/oppressor.md), [Thrower](../unique-skills/thrower.md), [Gravity Domination](gravity-domination.md), [Molecular Manipulation](molecular-manipulation.md), [Gravity Hammer](../../../tr-nightmares/abilities/battlewill/gravity-hammer.md), [Pain, Lord of Six Paths](../../../tensura-more-skills/abilities/ultimate-skills/pain-lord-of-six-paths.md), [Melancholy](../../../tensura-mysticism/abilities/unique-skills/melancholy.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `GravityManipulation.gravitySkillMasteredAcquirement` | 3 | The number of mastered gravity skills needed to learn Gravity Manipulation. |
| `GravityManipulation.magiculeCost` | 1,000 | Magicule Cost to activate. |
| `GravityManipulation.dominationEpAcquirement` | 400,000 | EP Requirement for to learn Domination. |
| `GravityManipulation.resistDegradationAcquirement` | 800,000 | EP Requirement for to use Resist Degradation when mastered. |
| `GravityManipulation.manipulationBoost` | 1.5 | The Gravity Damage Boost when activated Manipulation. |
| `GravityManipulation.dominationBoost` | 3 | The Gravity Damage Boost when activated Domination. |

## Tags

`tensura:skills/extra_skills`, `tensura:skills/gravity_skills`
