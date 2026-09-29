# ｢ Susanoo, Lord of Tyranny ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![｢ Susanoo, Lord of Tyranny ｣](../../../assets/icons/trnightmare/skill/susanoo.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:susanoo` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 600,000 |
| **Max mastery** | 5,000 |
| **Cooldowns (s)** | 25 |
| **Activation** | Toggle, Press |

</div>

> The evolved form of Chaotic Fate. Manipulate destiny, distort dimensions, and counter all harm.

## Modes

| # | Mode |
|---|---|
| 1 | True Chaotic Fate |
| 2 | Minus Break |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Triggers when you damage a target
- Triggers when you take damage
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| degrade | 1 | add |
| critical | 100 | add |
| dodgeNegate | 1 | add |
| learning | 8 | add |
| mastery | 8 | add |

## Obtaining

- Listed in the `astralMasteredCreationUltimates` config option (config/nightmare/ability/skill/nightmare_ult.toml): Ultimate skill IDs only offered from Astral Light Skill Creation when Astral Light is mastered.
- Listed in the `allowedSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can be affected by Raphael-style alteration by default.
- Acquisition checks: [Cook](../../../tensura-reincarnated/abilities/unique-skills/cook.md), [｢ Susanoo, Lord of Tyranny ｣](susanoo.md)
- In-game message: *Error- The Unique Skill: "Cook" has attempted evolution. This is considered dangerous, are you sure you wish to continue? Understood. The Unique Skill: "Cook" has begun to undergo evolution into the Ultimate Skill: "Susanoo, Lord of Tyranny".... Er-*

## Related

- **Related skills:** [Cook](../../../tensura-reincarnated/abilities/unique-skills/cook.md)
- **Referenced by:** [Alteration](../extra-skills/alteration.md), [｢ Sariel, Lord of Hope ｣](sariel.md), [Envy Manas](envy-manas.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Susanoo.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Susanoo.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Susanoo.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Susanoo.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Susanoo.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Susanoo.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Susanoo.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Susanoo.mpAcquirement` | 600,000 | Magicule cost required to acquire Susanoo. |
| `Susanoo.enableUltimateEvolution` | true | Enable evolution from Cook to Susanoo. |
| `Susanoo.fateHpReductionMultiplier` | 1 | HP reduction multiplier for True Chaotic Fate. |
| `Susanoo.hpReducedMultiplier` | 1.1 | HP reduction multiplier applied when True Chaotic Fate triggers via onTouchEntity. |
| `Susanoo.trueChaoticFateCooldown` | 3 | Cooldown for activating True Chaotic Fate. |
| `Susanoo.minusBreakCooldown` | 25 | Cooldown for activating Minus Break. |
| `Susanoo.barrierEPThreshold` | 1.5 | EP threshold ratio for barrier shatter immunity. |
| `Susanoo.toggleCritBonus` | 100 | Critical chance bonus while Susanoo is toggled on. |
| `Susanoo.toggleDodgeBonus` | 1 | Dodge negate chance bonus while Susanoo is toggled on. |
| `Susanoo.toggleLearnBonus` | 8 | Ability learning gain bonus while Susanoo is toggled on. |
| `Susanoo.toggleMasteryBonus` | 8 | Ability mastery gain bonus while Susanoo is toggled on. |
| `Susanoo.toggleResistBonus` | 1 | Resistance degradation bonus while Susanoo is toggled on. |
| `Susanoo.barrierNormal` | 4 | Multi-Dimensional Barrier non-mastered |
| `Susanoo.barrierMastered` | 6 | Multi-Dimensional Barrier mastered |
| `Susanoo.SusanooMobKills` | 350 | Mobs Killed to evolve Susanoo. |
| `Susanoo.SusanooSkillsMastered` | 45 | Skills Mastered to evolve Susanoo. |

## In-game messages

<details markdown><summary>Show 3 messages</summary>

- True Chaotic Fate
- Multidimensional Barrier
- Minus Break

</details>

## Tags

`tensura:skills/ultimate_skills`
