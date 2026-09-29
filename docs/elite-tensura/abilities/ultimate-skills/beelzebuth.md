# Beelzebuth, Lord of Gluttony

<small>[Elite Tensura](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![Beelzebuth, Lord of Gluttony](../../../assets/icons/elitetensura/skill/beelzebuth.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `elitetensura:beelzebuth` |
| **Modes** | 6 |
| **Acquisition cost (MP)** | 0 |
| **Max mastery** | 10,000 |
| **Cooldowns (s)** | 2 mastered, 8 otherwise |
| **Activation** | Press, Hold |

</div>

> The insatiable Ultimate evolved from Gluttony at the cost of Merciless. Devour, store, convert, and redistribute power through the Food Chain.

## Modes

| # | Mode |
|---|---|
| 1 | Predation |
| 2 | Stomach |
| 3 | Isolate |
| 4 | Food Chain: Provide |
| 5 | Food Chain: Receive |
| 6 | Soul Consume |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Food Chain: Provide | var1 (a) × 0.9 |  |
| Food Chain: Receive | var1 (a) × 0.9 |  |
| Soul Consume | 60,000 |  |
| other modes | 0 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Adjusted by scrolling while active
- Triggers when you damage a target
- Triggers when a projectile hits you
- Does something when first learned

## Obtaining

- Acquisition checks: [Gluttony](../../../tensura-reincarnated/abilities/unique-skills/gluttony.md), [Merciless](../../../tensura-reincarnated/abilities/unique-skills/merciless.md)

## Related

- **Related skills:** [Gluttony](../../../tensura-reincarnated/abilities/unique-skills/gluttony.md), [Merciless](../../../tensura-reincarnated/abilities/unique-skills/merciless.md)
- **Effects:** [Fear](../../../tensura-reincarnated/effects/fear.md), [Soul Drain](../../../tensura-reincarnated/effects/soul-drain.md)

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/UltimateSkillConfig.toml`](../../configs/config-tensura-elitetensura-ultimateskillconfig.md).

| Option | Default | Description |
|---|---|---|
| `BeelzebuthSkill.IsEnabled` | true | Is this Skill Enabled? |
| `BeelzebuthSkill.predationRange` | 12 | The max range in blocks of the Predation mist. |
| `BeelzebuthSkill.predationRangeMastered` | 18 | The max range in blocks of the Predation mist when mastered. |
| `BeelzebuthSkill.predationDamage` | 300 | The attack damage of the Predation mist. |
| `BeelzebuthSkill.predationEPSteal` | 0.8 | The multiplier of the target's EP turned into the user's EP when killed by the Predation mist. |
| `BeelzebuthSkill.predationEPDrain` | 5,000 | The amount of magicule the mist drains from targets per hit. |
| `BeelzebuthSkill.predationSkillChance` | 80 | The chance (percent) to steal skills from targets without killing them. |
| `BeelzebuthSkill.predationSkillNumber` | 3 | The number of skills stolen from a target at a time without killing it. |
| `BeelzebuthSkill.predationUniqueDevourLimit` | 4 | The max number of Unique skills the kill-devour (devour all skills) can steal from a single target. Non-unique skills are not capped. |
| `BeelzebuthSkill.predationMagicCopyChance` | 1 | The chance (0.0-1.0) for the kill-devour (devour all skills) to copy a target's Magic. 0 disables Magic copying. |
| `BeelzebuthSkill.predationCorrosionDuration` | 200 | The duration in ticks of the Corrosion effect applied by the Predation mist. |
| `BeelzebuthSkill.predationCorrosionLevel` | 4 | The level of the Corrosion effect applied by the Predation mist. |
| `BeelzebuthSkill.stomachSlots` | 108 | Number of slots in the Stomach spatial storage. |
| `BeelzebuthSkill.stomachStackSize` | 999 | Max stack size per slot in the Stomach spatial storage. |
| `BeelzebuthSkill.isolateCleanseCostPerEffect` | 2,000 | Magicule Cost to absorb each of your own harmful status effects into the Isolate pool. |
| `BeelzebuthSkill.isolateEffectCredit` | 250 | Magicule credited to the Isolate pool per absorbed harmful effect. |
| `BeelzebuthSkill.isolateConversionMultiplier` | 3 | Multiplier applied to an item's dissolving registry value when converting quarantined items. |
| `BeelzebuthSkill.isolateFallbackMagicule` | 50 | Flat magicule value per quarantined item with no dissolving registry entry. |
| `BeelzebuthSkill.isolateMaxStacks` | 54 | Max number of quarantined item stacks the Isolate can hold. |
| `BeelzebuthSkill.isolateConvertCooldownSeconds` | 8 | Cooldown in seconds of the Isolate batch conversion. |
| `BeelzebuthSkill.isolateConvertCooldownMasteredSeconds` | 2 | Cooldown in seconds of the Isolate batch conversion when mastered. |
| `BeelzebuthSkill.absorbProjectileCost` | 500 | Magicule Cost per hostile projectile swallowed while toggled. |
| `BeelzebuthSkill.isolateProjectileCredit` | 500 | Magicule credited to the Isolate pool per swallowed projectile. |
| `BeelzebuthSkill.isolateProjectileCooldown` | 60 | Internal cooldown in ticks between projectile absorbs. |
| `BeelzebuthSkill.provideRange` | 5 | The range in blocks for targeting a subordinate in Provide/Receive Mode. |
| `BeelzebuthSkill.provideCostPercentage` | 0.9 | Cost of Provide % 0.9 = 90% magicules. |
| `BeelzebuthSkill.provideCooldownSeconds` | 120 | Cooldown in seconds of Provide Mode (applied when the copy succeeds). |
| `BeelzebuthSkill.provideCooldownMasteredSeconds` | 60 | Cooldown in seconds of Provide Mode when mastered. |
| `BeelzebuthSkill.receiveCostPercentage` | 0.9 | Cost of Receive % 0.9 = 90% magicules. |
| `BeelzebuthSkill.receiveCooldownSeconds` | 120 | Cooldown in seconds of Receive Mode (applied when the copy succeeds). |
| `BeelzebuthSkill.receiveCooldownMasteredSeconds` | 60 | Cooldown in seconds of Receive Mode when mastered. |
| `BeelzebuthSkill.soulConsumeMagiculeCost` | 60,000 | Magicule Cost of Soul Consume, charged once per second while the aura is held. |
| `BeelzebuthSkill.drainDuration` | 200 | The duration in tick of the Soul Drain effect applied on targets hit while Soul Consume is slotted. |
| `BeelzebuthSkill.drainLevel` | 3 | The level of the Soul Drain effect applied on targets hit while Soul Consume is slotted. |
| `BeelzebuthSkill.stealRadius` | 32 | The radius in blocks of the held Soul Steal aura. |
| `BeelzebuthSkill.stealMaxTargets` | 10 | Max targets the Soul Steal aura reaps per second. |
| `BeelzebuthSkill.stealHP` | 0.4 | HP fraction a target must be below to be instakilled by the Soul Steal aura. |
| `BeelzebuthSkill.stealEP` | 0.6 | Fraction of the user's max EP a target must be below to be instakilled by the Soul Steal aura. |
| `BeelzebuthSkill.stealFear` | 2 | Fear level a target must have to be instakilled by the Soul Steal aura. |
| `BeelzebuthSkill.stealDamageMultiplier` | 10 | Multiplier of the target's max health dealt as Soul Steal instakill damage. |
| `BeelzebuthSkill.friendlyFire` | false | If true, the Predation mist and Soul Steal aura also affect players in the user's own nation or hunt party. |

Set in [`config/tensura/ability/skill_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-skill-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryUltimate` | 10,000 | The max amount of mastery point for Ultimate Skills. |
| `Mastery.masteryIntrinsic` | 100 | The max amount of mastery point for Intrinsic Skills. |
| `Mastery.masteryExtra` | 500 | The max amount of mastery point for Extra Skills. |
| `Mastery.masteryUnique` | 1,000 | The max amount of mastery point for Unique Skills. |
| `Mastery.masteryUniqueSin` | 1,500 | The max amount of mastery point for Unique Skills of Sins. |
| `Mastery.masteryUltimate` | 10,000 | The max amount of mastery point for Ultimate Skills. |

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

`tensura:skills/no_plundering`, `tensura:skills/ultimate_skills`
