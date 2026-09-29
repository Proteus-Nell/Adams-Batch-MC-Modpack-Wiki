# ｢ Cthulhu, King of Divine Ice ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![｢ Cthulhu, King of Divine Ice ｣](../../../assets/icons/trnightmare/skill/leviathan.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:cthulhu` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 3,000,000 |
| **Max mastery** | 15,000 |
| **Cooldowns (s)** | 240, 120, 90, 200 |
| **Activation** | Toggle, Press, Hold |

</div>

> Fusion of Gabriel and Leviathan. Serpent's Jealousy siphons magicule on hit while in-slot; toggle Envious Fortune for luck and effect purge. Command ice, envy, and absolute temporal fixation.

## Modes

| # | Mode |
|---|---|
| 1 | Cthulhu Absorption |
| 2 | Cthulhu Fixation |
| 3 | Cthulhu Devotion |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | *set by config (base cost (ego ultimate cost))* |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers when you take damage
- Triggers when an effect is applied to you

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| attribute | `-nextAmount` | add |

## Obtaining

- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.
- Listed in the `skillEngraveBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skills that cannot be engraved through Amatsumara skill engrave.
- Acquisition checks: [｢ Gabriel, Lord of Patience ｣](gabriel.md), [｢ Leviathan, Lord of Envy ｣](leviathan.md), [｢ Cthulhu, King of Divine Ice ｣](cthulhu.md)
- In-game message: *You've created a Greater Ultimate Skill! Cthulhu, King of Divine Ice has been formed through the optimization and evolution of Leviathan, Lord of Envy and Gabriel, Lord of Patience.*

## Related

- **Related skills:** [｢ Gabriel, Lord of Patience ｣](gabriel.md), [｢ Leviathan, Lord of Envy ｣](leviathan.md), [Thermal Fluctuation Nullification](../../../tensura-reincarnated/abilities/resistance-skills/thermal-fluctuation-nullification.md)
- **Effects:** [Magicule Poison](../../../tensura-reincarnated/effects/magicule-poison.md), [Inferior](../../effects/cthulhu-inferior.md), [Heat Death](../../effects/gabriel-heat-death.md), [Ending Soul](../../effects/ending-soul.md), [Chill](../../../tensura-reincarnated/effects/chill.md), [White Lock](../../effects/cadence-white-lock.md), [Jealous](../../effects/jealous.md), [Envied](../../effects/envied.md), [Stolen Luck](../../effects/stolen-luck.md)
- **Summons / entities:** Tensura
- **Referenced by:** [Cessation](../unique-skills/cessation.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Cthulhu.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Cthulhu.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Cthulhu.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Cthulhu.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Cthulhu.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Cthulhu.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Cthulhu.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Cthulhu.mpAcquirement` | 3,000,000 | Magicule cost to acquire Cthulhu (paid via skill obtainment, not evolution conditions). |
| `Cthulhu.enableUltimateEvolution` | true | Whether Gabriel and Leviathan may evolve into Cthulhu. |
| `Cthulhu.mobKillsRequired` | 15,000 | Mob kills required to evolve into Cthulhu. |
| `Cthulhu.insanityMinAmplifier` | 3 | Minimum Insanity amplifier required (level IV = amplifier 3). |
| `Cthulhu.fortunePurgeCost` | 1,000 | Magicule cost per purge attempt while Envious Fortune is toggled on. |
| `Cthulhu.fortuneLuckLevel` | 10 | Luck level while Envious Fortune is toggled on. |
| `Cthulhu.CthulhuEffectPurge` | "minecraft:slowness", "minecraft:mining_fatigue", "minecraft:instant_damage", "minecraft:nausea", "minecraft:blindness", "minecraft:hunger", "minecraft:weakness", "minecraft:poison", "minecraft:wither", "minecraft:unluck", "minecraft:bad_omen", "minecraft:darkness" | Effect registry ids purged by Envious Fortune. |
| `Cthulhu.serpentSiphonChance` | 0.15 | Chance for Serpent's Jealousy to siphon magicule on hit while in-slot. |
| `Cthulhu.heatDeathHalfSize` | 15 | Half-size of Heat Death kill cube (30x30x30 = 15). |
| `Cthulhu.heatDeathParticlesPerTick` | 120 | Snowflake particles per tick during Heat Death. |
| `Cthulhu.heatDeathCooldownSeconds` | 30 | Heat Death cooldown in seconds. |
| `Cthulhu.heatDeathEffectDurationTicks` | 600 | Heat Death debuff duration in ticks on survivors. |
| `Cthulhu.counterFreezeWindowTicks` | 60 | Counter Freeze window in ticks. |
| `Cthulhu.counterFreezeCooldownSeconds` | 15 | Cooldown in seconds after activating Counter Freeze. |
| `Cthulhu.counterFreezeLockTicks` | 100 | White Lock duration from Counter Freeze (unmastered). |
| `Cthulhu.counterFreezeLockTicksMastered` | 200 | White Lock duration from Counter Freeze when mastered. |
| `Cthulhu.counterFreezeChillTicks` | 80 | Chill duration from Counter Freeze. |
| `Cthulhu.eternalWorldRadius` | 16 | Eternal World field radius in blocks. |
| `Cthulhu.snowCrystalHalfSize` | 5 | Snow Crystal shell half-size (10x10x10 = 5). |
| `Cthulhu.snowCrystalInteriorHalf` | 2 | Snow Crystal hollow interior half-size (4x4x4 = 2). |
| `Cthulhu.snowCrystalMpDrainPerSecond` | 0.025 | Fraction of current magicule drained per second from targets inside Snow Crystal field. |
| `Cthulhu.inferiorDuration` | 1,200 | Inferior duration in ticks (unmastered). |
| `Cthulhu.inferiorDurationMastered` | 2,000 | Inferior duration in ticks when mastered. |
| `Cthulhu.inferiorDamageCap` | 1,000 | Maximum damage taken per hit while Inferior is active. |
| `Cthulhu.inferiorCooldown` | 240 | Inferior cooldown in seconds (unmastered). |
| `Cthulhu.inferiorCooldownMastered` | 240 | Inferior cooldown in seconds when mastered. |
| `Cthulhu.enviedDuration` | 200 | Envied effect duration from Crushing Jealousy. |
| `Cthulhu.enviedDrainPercent` | 0.02 | MP/AP drain percent when Envied triggers. |
| `Cthulhu.stolenLuckDuration` | 200 | Stolen Luck duration from Crushing Jealousy. |
| `Cthulhu.stolenLuckLevel` | 1 | Stolen Luck amplifier level. |
| `Cthulhu.completeFixationDurationTicks` | 300 | Complete Fixation duration in ticks (15 seconds = 300). |
| `Cthulhu.completeFixationHalfWidth` | 32 | Complete Fixation field half-width (64x64x64 = 32). |
| `Cthulhu.completeFixationCooldownSeconds` | 120 | Complete Fixation cooldown in seconds. |
| `Cthulhu.whiteoutDurationTicks` | 60 | Whiteout Absorb freeze duration in ticks (3 seconds = 60). |
| `Cthulhu.whiteoutHalfWidth` | 16 | Whiteout Absorb field half-width. |
| `Cthulhu.whiteoutMpDrainPerSecond` | 0.15 | Fraction of target max magicule drained per second during Whiteout (bypasses time-stop immunity). |
| `Cthulhu.whiteoutCooldownSeconds` | 90 | Whiteout Absorb cooldown in seconds. |

## Tags

`tensura:skills/patient`, `tensura:skills/ultimate_skills`
