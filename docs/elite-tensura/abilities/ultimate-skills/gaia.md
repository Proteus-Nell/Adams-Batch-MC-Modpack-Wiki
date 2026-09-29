# Gaia, Lord of Earth

<small>[Elite Tensura](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![Gaia, Lord of Earth](../../../assets/icons/elitetensura/skill/gaia.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `elitetensura:gaia` |
| **Modes** | 5 |
| **Acquisition cost (MP)** | 0 |
| **Max mastery** | 10,000 |
| **Cooldowns (s)** | 8, 35, 2, 60, 10 |
| **Activation** | Toggle, Press |

</div>

> The land itself answers. Raise the earth to impale and to bind, reshape the ground your people hold, coax ore from bare stone, and draw the world's own magicule into yourself. Strongest where your nation's banner flies.

## Modes

| # | Mode |
|---|---|
| 1 | Tectonic Spikes |
| 2 | Stone Grasp |
| 3 | Sculpt |
| 4 | Vein Bloom |
| 5 | Geomancy |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Tectonic Spikes | 3,000 |  |
| Stone Grasp | 12,000 |  |
| Sculpt | 800 |  |
| Vein Bloom | 5,000 |  |
| other modes | 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you are attacked

## Obtaining

- Acquisition checks: [Earth Wall](../../../tensura-reincarnated/abilities/aspectual-magic/earth-wall.md), [Stone Shot](../../../tensura-reincarnated/abilities/aspectual-magic/stone-shot.md)

## Related

- **Related skills:** [Earth Wall](../../../tensura-reincarnated/abilities/aspectual-magic/earth-wall.md), [Stone Shot](../../../tensura-reincarnated/abilities/aspectual-magic/stone-shot.md)
- **Effects:** [Infinite Imprisonment](../../../tensura-reincarnated/effects/infinite-imprisonment.md)

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/UltimateSkillConfig.toml`](../../configs/config-tensura-elitetensura-ultimateskillconfig.md).

| Option | Default | Description |
|---|---|---|
| `GaiaSkill.IsEnabled` | true | Is this Skill Enabled? |
| `GaiaSkill.homeMultiplier` | 1.6 | Power multiplier inside your own nation's claimed chunks. |
| `GaiaSkill.wildMultiplier` | 0.6 | Power multiplier on unclaimed land, or when the nation system is off. |
| `GaiaSkill.hostileMultiplier` | 0.3 | Power multiplier inside another nation's claimed chunks. |
| `GaiaSkill.hostileAtWarMultiplier` | 1 | Power multiplier in an enemy claim while at war with that nation. |
| `GaiaSkill.warLiftsPenalty` | true | If false, a declared war does NOT lift the hostile-claim penalty. |
| `GaiaSkill.friendlyFire` | false | Whether Tectonic Spikes and Stone Grasp can hit members of the caster's own nation.<br>False (default) skips them: Bulwark already shields nation allies, so spiking the<br>same teammate the toggle is protecting reads as a bug. Set true for the older<br>behaviour where the cone hits everything except the caster. |
| `GaiaSkill.spikesCost` | 3,000 | Magicule cost of Tectonic Spikes. |
| `GaiaSkill.spikesCooldown` | 8 | Cooldown of Tectonic Spikes, in SECONDS. |
| `GaiaSkill.spikesDamage` | 45 | Base damage per spike hit, before the zone multiplier. |
| `GaiaSkill.spikesRange` | 12 | Base cone length in blocks, before the zone multiplier. |
| `GaiaSkill.graspCost` | 12,000 | Magicule cost of Stone Grasp. |
| `GaiaSkill.graspCooldown` | 35 | Cooldown of Stone Grasp, in SECONDS. |
| `GaiaSkill.graspRootSeconds` | 5 | Base root duration in SECONDS, before the zone multiplier. |
| `GaiaSkill.graspDamagePerSecond` | 12 | Damage dealt per second while rooted, before the zone multiplier. |
| `GaiaSkill.graspReach` | 32 | Maximum targeting distance in blocks. |
| `GaiaSkill.sculptCost` | 800 | Magicule cost of one Sculpt use. |
| `GaiaSkill.sculptCooldown` | 2 | Cooldown of Sculpt, in SECONDS. |
| `GaiaSkill.veinBloomCost` | 5,000 | Magicule cost paid by the caster for one Vein Bloom. |
| `GaiaSkill.veinBloomCooldown` | 60 | Cooldown of Vein Bloom, in SECONDS. |
| `GaiaSkill.veinBloomSamples` | 24 | Random block positions sampled in the chunk per use. |
| `GaiaSkill.veinBloomChance` | 0.35 | Chance each sampled stone block converts to ore. |
| `GaiaSkill.veinBloomChunkCostPerOre` | 400 | Chunk magicule consumed per converted block. |
| `GaiaSkill.veinBloomDailyCapPerChunk` | 12 | Maximum ore blocks Vein Bloom may create in one chunk per in-game day. |
| `GaiaSkill.veinBloomOreWeights` | "new ArrayList&lt;&gt;(<br>         List.of(<br>            "minecraft:iron_ore\|40",<br>            "minecraft:copper_ore\|30",<br>            "minecraft:coal_ore\|20",<br>            "minecraft:gold_ore\|7",<br>            "minecraft:redstone_ore\|2",<br>            "minecraft:diamond_ore\|1"<br>         )<br>      )" | Ore weight table, one entry per line as 'blockid\|weight'. |
| `GaiaSkill.geomancyCooldown` | 10 | Cooldown of Geomancy, in SECONDS. |
| `GaiaSkill.geomancyTransferAmount` | 2,000 | Magicule moved per Geomancy use, clamped by whichever side has less. |
| `GaiaSkill.geomancyMaxRaisePerUse` | 250 | How much one Geomancy use shifts the chunk's magicule CEILING: seeding raises it,<br>draining (sneak) lowers it by the same figure. Hard-capped by the Magicule World<br>entityMagiculeInfluenceChunkCap, and it decays naturally once the chunk stops being<br>seeded. Moves capacity only — never income. |
| `GaiaSkill.geomancyStripCostPercent` | 0.2 | Fraction of the caster's MAXIMUM magicule burned to strip capacity out of a chunk<br>(sneak-Geomancy). Charged per successful strip, on top of nothing being refunded.<br>Deliberately steep: stripping is not claim-gated, so raiding a rival's cultivated<br>ground should cost far more than seeding your own. 0 = free. |
| `GaiaSkill.bulwarkDrainPerTick` | 1,000 | Magicule drained per skill tick (ManasCore ticks skills every 100 game ticks = 5 s) while Bulwark is lit, even when suppressed. |
| `GaiaSkill.bulwarkRadius` | 12 | Radius in blocks within which nation allies share the Bulwark buff. |
| `GaiaSkill.bulwarkResistanceAmplifier` | 1 | Damage-resistance amplifier granted by Bulwark (0 = Resistance I). |
| `GaiaSkill.reshapeBlockBudget` | 96 | Hard cap on blocks a single skill use may change. Safety valve. |
| `GaiaSkill.reshapeRevertSeconds` | 10 | How long raised combat pillars stand, in SECONDS. |
| `GaiaSkill.requiredNationLevel` | 10 | Nation level required to learn Gaia. Ignored when the nation system is off. |
| `GaiaSkill.requiredClaimedChunks` | 32 | Claimed chunks required to learn Gaia, as an alternative to nation level. |

Set in [`config/tensura/ability/skill_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-skill-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryUltimate` | 10,000 | The max amount of mastery point for Ultimate Skills. |
| `Mastery.masteryIntrinsic` | 100 | The max amount of mastery point for Intrinsic Skills. |
| `Mastery.masteryExtra` | 500 | The max amount of mastery point for Extra Skills. |
| `Mastery.masteryUnique` | 1,000 | The max amount of mastery point for Unique Skills. |
| `Mastery.masteryUniqueSin` | 1,500 | The max amount of mastery point for Unique Skills of Sins. |
| `Mastery.masteryUltimate` | 10,000 | The max amount of mastery point for Ultimate Skills. |

Set in [`config/tensura/EliteTensura/MagiculeWorld.toml`](../../configs/config-tensura-elitetensura-magiculeworld.md).

| Option | Default | Description |
|---|---|---|
| `ENTITY_INFLUENCE.entityMagiculeInfluenceDisableInSpawn` | true | Freeze area magicule inside the LocationManager SpawnProtection region (overworld only): entities there raise no chunk magicule, no bonus diffuses in, and any existing influence bonus is reset to the Tensura base. DEFAULT: true |
| `ENTITY_INFLUENCE.entityMagiculeInfluenceInterval` | 40 | Server ticks between entity-influence cycles. DEFAULT: 40 |
| `ENTITY_INFLUENCE.entityMagiculeInfluenceMinMagicule` | 50,000 | Minimum entity magicule to contribute to its chunk. DEFAULT: 50000 |
| `ENTITY_INFLUENCE.entityMagiculeInfluenceFactor` | 2 | Entity magicule is multiplied by this to get its contribution. DEFAULT: 2.0 |
| `ENTITY_INFLUENCE.entityMagiculeInfluenceEntityCap` | 1,000 | Maximum contribution from a single entity. DEFAULT: 1000 |
| `ENTITY_INFLUENCE.entityMagiculeInfluenceChunkCap` | 5,000 | Maximum target bonus / max-magicule a chunk can reach from influence. DEFAULT: 5000 |
| `ENTITY_INFLUENCE.entityMagiculeInfluenceApproachRate` | 0.2 | Fraction of the gap to the contribution closed each cycle. DEFAULT: 0.2 |
| `ENTITY_INFLUENCE.entityMagiculeInfluenceRegenRatio` | 0.02 | Share of contribution added to the chunk's regen rate. DEFAULT: 0.02 |
| `ENTITY_INFLUENCE.entityMagiculeInfluenceDiffusionRate` | 0.04 | Fraction of a chunk's current bonus diffused to each adjacent loaded chunk per cycle. DEFAULT: 0.04 |
| `ENTITY_INFLUENCE.entityMagiculeInfluenceScanRadiusChunks` | 2 | Chunk radius around each player scanned for contributing entities. DEFAULT: 2 |
| `ENTITY_INFLUENCE.entityMagiculeInfluenceDisableInSpawn` | true | Freeze area magicule inside the LocationManager SpawnProtection region (overworld only): entities there raise no chunk magicule, no bonus diffuses in, and any existing influence bonus is reset to the Tensura base. DEFAULT: true |

## Tags

`tensura:skills/no_plundering`, `tensura:skills/ultimate_skills`
