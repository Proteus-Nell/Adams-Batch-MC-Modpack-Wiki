# ｢ Uriel, Lord of Oaths ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![｢ Uriel, Lord of Oaths ｣](../../../assets/icons/trnightmare/skill/uriel_lord_of_oath.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:uriel_lord_of_oath` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 1,500,000 |
| **Max mastery** | 5,000 |
| **Cooldowns (s)** | 10, 700 |
| **Activation** | Toggle, Press |

</div>

> Altered covenant authority over prison, barrier, cleansing and law degradation.

## Modes

| # | Mode |
|---|---|
| 1 | Imprison |
| 2 | Universal Barrier |
| 3 | Insulated Prison |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | *set by config (base cost (ego ultimate cost))* |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you take damage
- Triggers when an effect is applied to you

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| barrier | left | add |
| barrier | points | add |

## Obtaining

- Listed in the `virtueDominionSkills` config option (config/nightmare/ability/skill/nightmare_ult.toml): Virtue skills that Ultimate Dominion can copy from targets.
- Listed in the `allowedSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can be affected by Raphael-style alteration by default.

## Related

- **Related skills:** [Spatial Domination](../../../tensura-reincarnated/abilities/extra-skills/spatial-domination.md), [Spatial Manipulation](../../../tensura-reincarnated/abilities/extra-skills/spatial-manipulation.md), [｢ Uriel, Lord of Vows ｣](uriel-lord-of-vow.md)
- **Effects:** [Infinite Imprisonment](../../../tensura-reincarnated/effects/infinite-imprisonment.md), [Magic Interference](../../../tensura-reincarnated/effects/magic-interference.md)
- **Referenced by:** [Alteration](../extra-skills/alteration.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `UrielOath.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `UrielOath.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `UrielOath.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `UrielOath.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `UrielOath.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `UrielOath.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `UrielOath.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `UrielOath.mpAcquirement` | 1,500,000 | Magicule cost to acquire Uriel Lord of Oath. |
| `UrielOath.lawPower` | 1 | Law degradation bonus while toggled. |
| `UrielOath.lawPowerHighEp` | 2 | Law degradation bonus while toggled at high EP. |
| `UrielOath.lawPowerHighEpThreshold` | 1,000,000 | EP required for high law power. |
| `UrielOath.spaceBoost` | 4 | Space boost while toggled (if no native spatial domination/manipulation). |
| `UrielOath.masteredLawPower` | 1 | Extra law degradation from spatial package when mastered. |
| `UrielOath.masteredLawPowerThreshold` | 800,000 | EP required for mastered law bonus. |
| `UrielOath.imprisonCost` | 45,000 | Imprison MP cost. |
| `UrielOath.imprisonDuration` | 300 | Imprison duration in seconds. |
| `UrielOath.imprisonDurationMastered` | 600 | Imprison duration in seconds when mastered. |
| `UrielOath.imprisonCooldown` | 10 | Imprison cooldown in seconds. |
| `UrielOath.imprisonMissCooldown` | 10 | Imprison miss cooldown in seconds. |
| `UrielOath.imprisonMissCooldownMastered` | 5 | Imprison miss cooldown in seconds when mastered. |
| `UrielOath.imprisonDrainPerPulse` | 500 | Magicules drained from imprisoned targets every 10 ticks. |
| `UrielOath.barrierSelfMultiplier` | 2.5 | Universal Barrier self points multiplier by max HP. |
| `UrielOath.barrierAllyMultiplier` | 1.75 | Universal Barrier ally points multiplier by max HP. |
| `UrielOath.barrierCooldown` | 10 | Universal Barrier cooldown in seconds. |
| `UrielOath.insulatedPrisonCost` | 50,000 | Insulated Prison base MP cost before per-target EP costs. |
| `UrielOath.insulatedPrisonDuration` | 100 | Insulated Prison duration in seconds. |
| `UrielOath.insulatedPrisonDurationMastered` | 200 | Insulated Prison duration in seconds when mastered. |
| `UrielOath.insulatedPrisonCooldown` | 700 | Insulated Prison cooldown in seconds. |
| `UrielOath.insulatedPrisonFailCooldown` | 10 | Insulated Prison fallback cooldown in seconds when no targets are hit. |
| `UrielOath.barrierMpPerDamage` | 3 | Magicule cost per 1 blocked damage for Universal Barrier. |
| `UrielOath.enableUltimateEvolution` | true | Whether uriel of Oath can be obtained naturally |

## Tags

`tensura:skills/paladin`, `tensura:skills/ultimate_skills`
