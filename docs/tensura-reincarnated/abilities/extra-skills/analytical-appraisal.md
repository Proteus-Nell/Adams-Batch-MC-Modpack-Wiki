# Analytical Appraisal

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Analytical Appraisal](../../../assets/icons/tensura/skill/analytical_appraisal.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:analytical_appraisal` |
| **Activation** | Press |

</div>

> Assess the strength of your opponents to gain insight into their overall strength.

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you die
- Triggers when you respawn

## Obtaining

- Can be learned by: [Spectator](../../../ascension/races/spectator-gazer.md), [Mindwitness](../../../ascension/races/mindwitness.md), [Gauth](../../../ascension/races/gauth.md), [Beholder](../../../ascension/races/beholder.md), [Death Tyrant](../../../ascension/races/death-tyrant.md)
- Listed in the `grantedSkillIds` config option (config/tensuramoreskills-grand.toml): Skill IDs granted by Elfaria. Includes Albis so old Ars Weiss clones stay compatible, magic basics, transforms, senses, chant annulment,...
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/beetle_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/centipede_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/ant_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/scorpion_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/mantis_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/wasp_config.toml): The list of intrinsic skills that the race gets.
- Acquisition checks: [Analyze](../aspectual-magic/analyze.md)

## Related

- **Related skills:** [Analyze](../aspectual-magic/analyze.md)
- **Summons / entities:** Tensura
- **Referenced by:** [Divine Protection of Judgement](../../../tr-nightmares/abilities/extra-skills/judgement-blessing.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `AnalyticalAppraisal.epAcquirement` | 20,000 | EP Requirement for Learning. |
| `AnalyticalAppraisal.level` | 1 | The Bonus Analysis Level when activated. |
| `AnalyticalAppraisal.levelMastered` | 2 | The Bonus Analysis Level when activated with Mastery. |
| `AnalyticalAppraisal.radius` | 0 | The Bonus Analysis Radius when activated. |
| `AnalyticalAppraisal.radiusMastered` | 5 | The Bonus Analysis Radius when activated with Mastery. |

Set in [`config/tensura/ability/ability_config.toml`](../../configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/extra_skills`
