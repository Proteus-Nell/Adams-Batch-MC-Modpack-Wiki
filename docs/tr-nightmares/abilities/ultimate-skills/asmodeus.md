# ｢ Asmodeus, Lord of Lust ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![｢ Asmodeus, Lord of Lust ｣](../../../assets/icons/trnightmare/skill/asmodeus.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:asmodeus` |
| **Modes** | 6 |
| **Max mastery** | 15,000 |
| **Activation** | Toggle, Press, Hold |

</div>

> Asmodeus, Lord Of Lust is a powerful Ultimate Skill capable of bending the rules of Life and Death

## Modes

| # | Mode |
|---|---|
| 1 | Rebirth |
| 2 | Seduction |
| 3 | Embracing Drain |
| 4 | Arousal |
| 5 | Death Blessing |
| 6 | Memory End Requiem |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | *set by config (base cost (ego ultimate cost))* |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when you damage a target

## Obtaining

- Asmodeus, Lord Of Lust has evolved from Lust
- Listed in the `AngelicSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): List of Angelic skills registry names that can be created via Holy Essence consumption. Format: modid:skill_name
- Acquisition checks: [Lust](../../../tensura-reincarnated/abilities/unique-skills/lust.md)
- In-game message: *The Unique Skill Lust has evolved into Asmodeus*

## Related

- **Related skills:** [Lust](../../../tensura-reincarnated/abilities/unique-skills/lust.md)
- **Effects:** [Asmodeus](../../effects/asmodeus.md), [Lust Embracement](../../../tensura-reincarnated/effects/lust-embracement.md), [Mind Control](../../../tensura-reincarnated/effects/mind-control.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Asmodeus.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Asmodeus.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Asmodeus.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Asmodeus.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Asmodeus.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Asmodeus.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Asmodeus.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Asmodeus.mpAcquirement` | 1,200,000 | The Cost for the Ultimate Skill: Asmodeus. |
| `Asmodeus.magiculeCostRebirth` | 0 | The Cost of Re-Birth. |
| `Asmodeus.magiculeCostSeduction` | 750 | The Cost of Seduction. |
| `Asmodeus.magiculeCostEmbracingDrain` | 500 | The Cost of Embracing Drain. |
| `Asmodeus.magiculeCostArousal` | 2,500 | The Cost of Arousal. |
| `Asmodeus.magiculeCostDeathBlessing` | 25,000 | The Cost of Death Blessing. |
| `Asmodeus.magiculeCostMemoryEndRequiem` | 125,000 | The Cost of Memory End Requiem. |
| `Asmodeus.cooldownRebirth` | 0 | The Cooldown of Re-Birth. |
| `Asmodeus.cooldownSeduction` | 40 | The Cooldown of Seduction. |
| `Asmodeus.cooldownEmbracingDrain` | 60 | The Cooldown of Embracing Drain. |
| `Asmodeus.cooldownArousal` | 10 | The Cooldown of Arousal. |
| `Asmodeus.cooldownDeathBlessing` | 60 | The Cooldown for Death Blessing. |
| `Asmodeus.cooldownMemoryEndRequiem` | 3 | The Cooldown for Memory End Requiem. |
| `Asmodeus.consumptionHealPercent` | 10 | The Lifesteal Percentage of Asmodeus' Consumption. |
| `Asmodeus.slfImmunityThreshold` | 0.75 | The EP Threshold to that Asmodeus is immune to Draining. |
| `Asmodeus.slfReductionFactor` | 0.5 | The amount of Drain Reduction that Asmodeus has.. |
| `Asmodeus.slfCancelBelowThreshold` | true | The option to turn off Asmodeus' Drain Immunity. |
| `Asmodeus.seductionPercentDamage` | 0.01 | The Percent SHP Damage per second of Asmodeus. |
| `Asmodeus.seductionCharmThreshold` | 0.3 | The SHP Threshold in which the target is charmed. |
| `Asmodeus.seductionMaxHoldTime` | 200 | The max duration to hold Asmodeus. |
| `Asmodeus.seductionCharmDuration` | 60 | The duration of Seduction's Charm. |
| `Asmodeus.embraceRange` | 3 | The range of Embrace. |
| `Asmodeus.embraceDuration` | 100 | The duration of Embrace. |
| `Asmodeus.magiculeCostArousalMastered` | 20 | Magicule cost per HP healed when Arousal is mastered. |
| `Asmodeus.cooldownArousalMastered` | 100 | Cooldown of Arousal when mastered (in ticks). |
| `Asmodeus.deathBlessTime` | 200 | Maximum duration Death Blessing can be held (in ticks). |
| `Asmodeus.deathBlessRadius` | 6 | Radius of Death Blessing's effect. |
| `Asmodeus.deathBlessRange` | 10 | Range used to detect targets for Death Blessing. |
| `Asmodeus.requiemThreshold1` | 0.3 | EP threshold #1 for Memory End Requiem (targetEP &lt; ownerEP \* threshold). |
| `Asmodeus.requiemDrain1` | 0.8 | Drain percent applied when threshold #1 is met. |
| `Asmodeus.requiemThreshold2` | 0.5 | EP threshold #2 for Memory End Requiem. |
| `Asmodeus.requiemDrain2` | 0.6 | Drain percent applied when threshold #2 is met. |
| `Asmodeus.requiemThreshold3` | 0.7 | EP threshold #3 for Memory End Requiem. |
| `Asmodeus.requiemDrain3` | 0.4 | Drain percent applied when threshold #3 is met. |
| `Asmodeus.requiemNoUltimateDrain` | 0.99 | Drain percent applied when target has no Ultimate Skill and is below threshold #2. |
| `Asmodeus.requiemCooldown` | 400 | Cooldown of Memory End Requiem (in ticks). |
| `Asmodeus.AsmodeusSubordinates` | 25 | Number of subordinates required to evolve Lust into Asmodeus. |
| `Asmodeus.AsmodeusAnimalsBreed` | 100 | Number of animals the player must breed to evolve Lust into Asmodeus. |
| `Asmodeus.enableUltimateEvolution` | true | Whether Asmodeus evolution is allowed. If false, Lust cannot evolve into Asmodeus. |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/ultimate_skills`
