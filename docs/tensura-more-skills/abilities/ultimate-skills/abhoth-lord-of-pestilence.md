# Abhoth, Lord of Pestilence

<small>[TensuraMoreSkills](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![Abhoth, Lord of Pestilence](../../../assets/icons/tensuramoreskills/skill/abhoth_lord_of_pestilence.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `tensuramoreskills:abhoth_lord_of_pestilence` |
| **Modes** | 4 |
| **Acquisition cost (MP)** | 500,000 |
| **Cooldowns (s)** | 5, 2, 50 or 20, 40 |
| **Activation** | Press |

</div>

> The evolved lord of fungal plague.

## Modes

| # | Mode |
|---|---|
| 1 | Epidemic Sequencing Sweep |
| 2 | Mutation Vault |
| 3 | Fungal Catalyst |
| 4 | Fleshy Miscreations |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Epidemic Sequencing Sweep | 12,000 |  |
| Mutation Vault | 0 |  |
| Fungal Catalyst | 140,000 or 35,000 |  |
| Fleshy Miscreations | 25,000 |  |
| other modes | 0 |  |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect

## Related

- **Effects:** [Self-Regeneration](../../../tensura-reincarnated/effects/self-regeneration.md), [Magicule Regeneration](../../../tensura-reincarnated/effects/magicule-regeneration.md)
- **Referenced by:** [Fungus Infection](../unique-skills/fungus-infection.md)

## Stats (config defaults)

Set in [`config/tensuramoreskills-grand.toml`](../../configs/config-tensuramoreskills-grand.md).

| Option | Default | Description |
|---|---|---|
| `obtainment.acquirementMagiculeCost` | 500,000 (0 to no limit) | Magicule cost required to naturally acquire Abhoth. |
| `obtainment.acquirementMastery` | 0 (-1 to no limit) | Starting mastery value when acquired. |
| `obtainment.requiredSkillId` | "tensuramoreskills:fungus_infection" | Required skill registry ID for obtainment. Empty string disables the required skill check. |
| `obtainment.requiredSkillMustBeMastered` | true | If true, Fungus Infection must be mastered before Abhoth can be acquired. |
| `costs.epidemicSequencingSweepCost` | 12,000 (0 to no limit) |  |
| `costs.mutationVaultCost` | 0 (0 to no limit) |  |
| `costs.fungalCatalystAscendedCost` | 140,000 (0 to no limit) |  |
| `costs.fungalCatalystCost` | 35,000 (0 to no limit) |  |
| `costs.fleshyMiscreationsCost` | 25,000 (0 to no limit) |  |
| `passive_visuals.passiveVisualIntervalTicks` | 10 (1 to no limit) |  |
| `passive_visuals.passiveAshParticles` | 12 (0 to 10,000) |  |
| `passive_visuals.passiveParticleXZ` | 0.45 (0 to 128) |  |
| `passive_visuals.passiveParticleY` | 0.55 (0 to 128) |  |
| `passive_visuals.passiveParticleSpeed` | 0.01 (0 to 128) |  |
| `passive_visuals.passiveMyceliumParticles` | 8 (0 to 10,000) |  |
| `passive_visuals.passiveMyceliumXZ` | 0.55 (0 to 128) |  |
| `passive_visuals.passiveMyceliumY` | 0.15 (0 to 128) |  |
| `ooze_films.oozeFilmIntervalTicks` | 160 (1 to no limit) |  |
| `ooze_films.oozeFilmDurationTicks` | 260 (1 to no limit) |  |
| `ooze_films.oozeFilmAshParticles` | 42 (0 to 10,000) |  |
| `ooze_films.oozeFilmParticleXZ` | 1.8 (0 to 128) |  |
| `ooze_films.oozeFilmParticleY` | 0.06 (0 to 128) |  |
| `ooze_films.oozeFilmParticleSpeed` | 0.02 (0 to 128) |  |
| `ooze_films.oozeFilmSoundVolume` | 0.65 (0 to 100) |  |
| `ooze_films.oozeFilmSoundPitch` | 0.55 (0 to 4) |  |
| `cooldowns.epidemicSequencingSweepCooldownTicks` | 5 (0 to no limit) |  |
| `cooldowns.mutationVaultCooldownTicks` | 2 (0 to no limit) |  |
| `cooldowns.fungalCatalystAscendedCooldownTicks` | 50 (0 to no limit) |  |
| `cooldowns.fungalCatalystCooldownTicks` | 20 (0 to no limit) |  |
| `cooldowns.fleshyMiscreationsCooldownTicks` | 40 (0 to no limit) |  |
| `epidemic_sequencing_sweep.epidemicSequencingSweepRadius` | 15 (0 to 512) |  |
| `epidemic_sequencing_sweep.epidemicSequencingPoisonParticles` | 64 (0 to 10,000) |  |
| `epidemic_sequencing_sweep.epidemicSequencingParticleRadius` | 1.6 (0 to 128) |  |
| `epidemic_sequencing_sweep.epidemicSequencingAshParticles` | 80 (0 to 10,000) |  |
| `epidemic_sequencing_sweep.epidemicSequencingAshRadius` | 7.5 (0 to 512) |  |
| `epidemic_sequencing_sweep.epidemicSequencingAshY` | 1 (0 to 128) |  |
| `epidemic_sequencing_sweep.epidemicSequencingAshSpeed` | 0.04 (0 to 128) |  |
| `epidemic_sequencing_sweep.epidemicSequencingPointsPerEffect` | 5 (0 to no limit) |  |
| `fungal_catalyst.fungalCatalystAscendedRadius` | 30 (0 to 512) |  |
| `fungal_catalyst.fungalCatalystRadius` | 15 (0 to 512) |  |
| `fungal_catalyst.fungalCatalystAscendedEffectDurationTicks` | 260 (1 to no limit) |  |
| `fungal_catalyst.fungalCatalystAscendedBonusAmplifier` | 1 (0 to 255) |  |
| `fungal_catalyst.fungalCatalystEffectDurationTicks` | 160 (1 to no limit) |  |
| `fungal_catalyst.fungalCatalystBonusAmplifier` | 0 (0 to 255) |  |
| `fungal_catalyst.fungalCatalystAscendedInfectionDurationTicks` | 700 (1 to no limit) |  |
| `fungal_catalyst.fungalCatalystInfectionDurationTicks` | 420 (1 to no limit) |  |
| `fungal_catalyst.fungalCatalystAscendedAshParticles` | 170 (0 to 10,000) |  |
| `fungal_catalyst.fungalCatalystAshParticles` | 90 (0 to 10,000) |  |
| `fungal_catalyst.fungalCatalystAshRadiusMultiplier` | 0.45 (0 to 16) |  |
| `fungal_catalyst.fungalCatalystAshY` | 1.2 (0 to 128) |  |
| `fungal_catalyst.fungalCatalystAshSpeed` | 0.08 (0 to 128) |  |
| `fungal_catalyst.fungalCatalystAscendedMyceliumParticles` | 120 (0 to 10,000) |  |
| `fungal_catalyst.fungalCatalystMyceliumParticles` | 70 (0 to 10,000) |  |
| `fungal_catalyst.fungalCatalystMyceliumRadiusMultiplier` | 0.38 (0 to 16) |  |
| `fungal_catalyst.fungalCatalystMyceliumY` | 0.35 (0 to 128) |  |
| `fungal_catalyst.fungalCatalystMyceliumSpeed` | 0.04 (0 to 128) |  |
| `fungal_catalyst.fungalCatalystAscendedSoundVolume` | 1.4 (0 to 100) |  |
| `fungal_catalyst.fungalCatalystSoundVolume` | 0.9 (0 to 100) |  |
| `fungal_catalyst.fungalCatalystSoundPitch` | 0.45 (0 to 4) |  |
| `fleshy_miscreations.fleshyMiscreationsMinimumHealth` | 2 (0 to 340282349999999991754788743781432688640) |  |
| `fleshy_miscreations.fleshyMiscreationsMinimumSacrifice` | 1 (0 to 340282349999999991754788743781432688640) |  |
| `fleshy_miscreations.fleshyMiscreationsHealthSacrificeRatio` | 0.1 (0 to 1) |  |
| `fleshy_miscreations.fleshyMiscreationsSpawnCount` | 2 (0 to 64) |  |
| `fleshy_miscreations.fleshyMiscreationsSpawnSpread` | 0.7 (0 to 16) |  |
| `fleshy_miscreations.fleshyMiscreationsSlimeSize` | 2 (1 to 16) |  |
| `fleshy_miscreations.fleshyMiscreationsLifetimeTicks` | 300 (1 to no limit) |  |
| `fleshy_miscreations.fleshyMiscreationsParticles` | 60 (0 to 10,000) |  |
| `fleshy_miscreations.fleshyMiscreationsParticleXZ` | 0.8 (0 to 128) |  |
| `fleshy_miscreations.fleshyMiscreationsParticleY` | 0.6 (0 to 128) |  |
| `fleshy_miscreations.fleshyMiscreationsParticleSpeed` | 0.08 (0 to 128) |  |
| `fleshy_miscreations.fleshyMiscreationsSoundVolume` | 1 (0 to 100) |  |
| `fleshy_miscreations.fleshyMiscreationsSoundPitch` | 0.55 (0 to 4) |  |
| `stored_effects_and_combat.storedEffectMinimumDurationTicks` | 60 (1 to no limit) |  |
| `stored_effects_and_combat.storedEffectDurationMultiplierPerUpgrade` | 0.25 (0 to 100) |  |
| `ascended_self_buffs.ascendedSelfEffectExtensionTicks` | 200 (0 to no limit) |  |
| `ascended_self_buffs.ascendedSelfEffectMinimumDurationTicks` | 400 (1 to no limit) |  |
| `ascended_self_buffs.ascendedSelfEffectAmplifierBonus` | 1 (0 to 255) |  |
| `ascended_self_buffs.ascendedSelfRegenerationDurationTicks` | 400 (1 to no limit) |  |
| `ascended_self_buffs.ascendedSelfRegenerationAmplifier` | 1 (0 to 255) |  |
| `ascended_self_buffs.ascendedMagiculeRegenerationDurationTicks` | 400 (1 to no limit) |  |
| `ascended_self_buffs.ascendedMagiculeRegenerationAmplifier` | 1 (0 to 255) |  |
| `ascended_self_buffs.ascendedMagiculeGain` | 5,000 (0 to no limit) |  |
| `stored_effects_and_combat.combatRecentTargetMaxDistanceSqr` | 1,024 (0 to no limit) |  |
| `stored_effects_and_combat.combatNearbyRadius` | 12 (0 to 512) |  |

## In-game messages

<details markdown><summary>Show 6 messages</summary>

- Abhoth is still fermenting.
- No living hosts were found for sequencing.
- No active effects were found to mutate.
- Epidemic sequencing gained %s mutation points.
- Fungal catalyst applied %s stored mutations.
- You do not have enough biomass to rip away.

</details>
