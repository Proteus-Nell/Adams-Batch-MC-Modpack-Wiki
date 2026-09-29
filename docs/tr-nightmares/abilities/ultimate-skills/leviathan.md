# ｢ Leviathan, Lord of Envy ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![｢ Leviathan, Lord of Envy ｣](../../../assets/icons/trnightmare/skill/leviathan.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:leviathan` |
| **Modes** | 5 |
| **Acquisition cost (MP)** | 1,500,000 |
| **Max mastery** | 15,000 |
| **Cooldowns (s)** | 30 mastered, 60 otherwise, 10, 240 |
| **Activation** | Toggle, Press, Hold |

</div>

> Leviathan, Lord Of Envy is capable of absorbing the strength of all enemies, stealing their power to enhance itself, crippling foes with devastating effects, and improving its user endlessly by stealing the might of others.

## Modes

| # | Mode |
|---|---|
| 1 | Power Siphon |
| 2 | Festival |
| 3 | Dragon Festival |
| 4 | Inferior |
| 5 | Crushing Jealousy |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | *set by config (base cost (ego ultimate cost))* |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers when you take damage
- Triggers when an effect is applied to you

## Obtaining

- Leviathan, Lord Of Envy has evolved from Envy
- Listed in the `skillEngraveBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skills that cannot be engraved through Amatsumara skill engrave.
- Listed in the `AngelicSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): List of Angelic skills registry names that can be created via Holy Essence consumption. Format: modid:skill_name
- Acquisition checks: [Envy](../../../tensura-reincarnated/abilities/unique-skills/envy.md), [｢ Leviathan, Lord of Envy ｣](leviathan.md)
- In-game message: *Your envy has grown... Your Jealousy is running rampant... Your Unique Skill has started to under go evolution... It has awakened into the Ultimate Skill: Leviathan, Lord of Envy*

## Related

- **Related skills:** [Stasis](../unique-skills/stasis.md), [Envy](../../../tensura-reincarnated/abilities/unique-skills/envy.md)
- **Effects:** [Envious Mirror](../../effects/envious-mirror.md), [Jealous](../../effects/jealous.md), [Magic Interference](../../../tensura-reincarnated/effects/magic-interference.md), [Fragility](../../../tensura-reincarnated/effects/fragility.md), [Paralysis](../../../tensura-reincarnated/effects/paralysis.md), [Chill](../../../tensura-reincarnated/effects/chill.md), [Slowheal](../../effects/slowheal.md), [Fear](../../../tensura-reincarnated/effects/fear.md), [Envied](../../effects/envied.md), [Stolen Luck](../../effects/stolen-luck.md)
- **Referenced by:** [｢ Cthulhu, King of Divine Ice ｣](cthulhu.md), [Envy Manas](envy-manas.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Leviathan.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Leviathan.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Leviathan.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Leviathan.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Leviathan.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Leviathan.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Leviathan.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Leviathan.mpAcquirement` | 1,500,000 | The Cost for the Ultimate Skill: Leviathan. |
| `Leviathan.fortunePurgeCost` | 1,000 | Magicule cost per purge attempt while Envious Fortune is active. |
| `Leviathan.fortuneLuckLevel` | 5 | Luck level granted while Envious Fortune is toggled on. |
| `Leviathan.LeviathanEffectPurge` | "minecraft:slowness", "minecraft:mining_fatigue", "minecraft:instant_damage", "minecraft:nausea", "minecraft:blindness", "minecraft:hunger", "minecraft:weakness", "minecraft:poison", "minecraft:wither", "minecraft:unluck", "minecraft:bad_omen", "minecraft:darkness" | List of effect IDs that Envious Fortune will purge or block. |
| `Leviathan.costPowerSiphon` | 25,000 | Magicule cost of Power Siphon. |
| `Leviathan.powerSiphonCooldown` | 60 | Cooldown of Power Siphon (unmastered). |
| `Leviathan.powerSiphonCooldownMastered` | 30 | Cooldown of Power Siphon (mastered). |
| `Leviathan.powerSiphonFactor` | 0.25 | Power Siphon drain factor relative to Absorption. |
| `Leviathan.powerSiphonAuraRatio` | 0.5 | Ratio of Aura drained by Power Siphon. |
| `Leviathan.powerSiphonMagiculeRatio` | 0.5 | Ratio of Magicules drained by Power Siphon. |
| `Leviathan.powerSiphonReturnRatio` | 0.25 | Ratio of drained energy returned to the user. |
| `Leviathan.powerSiphonSlowHealDuration` | 200 | Duration of Slow Heal applied by Power Siphon. |
| `Leviathan.powerSiphonSlowHealLevel` | 1 | Level of Slow Heal applied by Power Siphon. |
| `Leviathan.costFestival` | 150,000 | Magicule cost of Festival. |
| `Leviathan.festivalRadius` | 60 | Radius of Festival's AoE. |
| `Leviathan.festivalResistNormal` | 0.6 | MP % required to resist Festival (unmastered). |
| `Leviathan.festivalResistMastered` | 0.8 | MP % required to resist Festival (mastered). |
| `Leviathan.festivalDuration` | 200 | Duration of Festival's applied effects. |
| `Leviathan.festivalFragilityLevel` | 1 | Fragility level applied by Festival. |
| `Leviathan.festivalParalysisLevel` | 1 | Paralysis level applied by Festival. |
| `Leviathan.festivalChillLevel` | 1 | Chill level applied by Festival. |
| `Leviathan.festivalSlowHealLevel` | 1 | Slow Heal level applied by Festival. |
| `Leviathan.costDragonFestival` | 0 | Magicule cost of Dragon Festival. |
| `Leviathan.dragonFestivalRadius` | 20 | Radius of Dragon Festival's AoE. |
| `Leviathan.dragonFestivalMaxResistance` | 5 | Maximum Resistance level the user can gain. |
| `Leviathan.dragonFestivalUnluckNormal` | 1 | Unluck level applied (unmastered). |
| `Leviathan.dragonFestivalUnluckMastered` | 2 | Unluck level applied (mastered). |
| `Leviathan.dragonFestivalDuration` | 200 | Duration of Dragon Festival effects. |
| `Leviathan.dragonFestivalCooldown` | 10 | Cooldown of Dragon Festival (unmastered). |
| `Leviathan.dragonFestivalCooldownMastered` | 10 | Cooldown of Dragon Festival (mastered). |
| `Leviathan.costInferior` | 15,000 | Magicule cost of Inferior. |
| `Leviathan.inferiorDuration` | 1,200 | Duration of Inferior (unmastered). |
| `Leviathan.inferiorDurationMastered` | 2,000 | Duration of Inferior (mastered). |
| `Leviathan.inferiorDamageCap` | 1,000 | Damage cap while Inferior is active (unmastered). |
| `Leviathan.inferiorDamageCapMastered` | 1,000 | Damage cap while Inferior is active (mastered). |
| `Leviathan.inferiorAttackBonus` | 8 | Flat Attack Damage bonus while Inferior is active (unmastered). |
| `Leviathan.inferiorAttackBonusMastered` | 12 | Flat Attack Damage bonus while Inferior is active (mastered). |
| `Leviathan.inferiorArmorBonus` | 8 | Flat Armor bonus while Inferior is active (unmastered). |
| `Leviathan.inferiorArmorBonusMastered` | 12 | Flat Armor bonus while Inferior is active (mastered). |
| `Leviathan.inferiorCooldown` | 240 | Cooldown of Inferior (unmastered). |
| `Leviathan.inferiorCooldownMastered` | 240 | Cooldown of Inferior (mastered). |
| `Leviathan.costCrushingJealousy` | 150 | Magicule cost of Crushing Jealousy. |
| `Leviathan.enviedDuration` | 200 | Duration of Envied effect applied by Crushing Jealousy. |
| `Leviathan.enviedDrainMax` | 500 | Maximum Magicule drained when Envied triggers. |
| `Leviathan.stolenLuckDuration` | 200 | Duration of Stolen Luck effect. |
| `Leviathan.stolenLuckLevel` | 1 | Level of Stolen Luck effect. |
| `Leviathan.serpentSiphonChance` | 0.15 | Chance for Serpent's Jealousy to trigger on hit. |
| `Leviathan.serpentSiphonMin` | 50 | Minimum Magicule drained by Serpent's Jealousy. |
| `Leviathan.serpentSiphonMax` | 150 | Maximum Magicule drained by Serpent's Jealousy. |
| `Leviathan.leviathanMP` | 1,500,000 | Magicules required to evolve Envy into Leviathan. |
| `Leviathan.enableUltimateEvolution` | true | Whether Leviathan evolution is allowed. |
| `Leviathan.leviathanHeroCount` | 5 | Leviathan evolution: required Raid Wins |

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
