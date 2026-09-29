# Imaginator

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Imaginator](../../../assets/icons/trnightmare/skill/imaginator.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:imaginator` |
| **Modes** | 5 |
| **Acquisition cost (MP)** | 99,000 |
| **Cooldowns (s)** | 5, 1, 20, 15 |
| **Activation** | Toggle, Press, Hold |

</div>

> Curiosity turns every advancement and every newly analyzed kind of creature into Knowledge Points, and Vast Imagination makes every ability stronger the more you know. Steel Body, Clone Creation, Skill Control, and Environmental Control all grow with your knowledge.

## Modes

| # | Mode |
|---|---|
| 1 | Clone Creation |
| 2 | Clone Control |
| 3 | Skill Control: Analyze |
| 4 | Skill Control: Ability Copy |
| 5 | Environmental Control |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Clone Creation | max MP × 0.1 |  |
| other modes | 0 |  |
| Skill Control: Analyze | 1,000 |  |
| Skill Control: Ability Copy | 2,500 |  |
| Environmental Control | 500 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Triggers when you take damage

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| attribute | armor | add |

## Related

- **Related skills:** [Infinite Regeneration](../../../tensura-reincarnated/abilities/extra-skills/infinite-regeneration.md), [Ultraspeed Regeneration](../../../tensura-reincarnated/abilities/extra-skills/ultraspeed-regeneration.md), [Burden](../../../tensura-reincarnated/abilities/aspectual-magic/burden.md)
- **Effects:** [Spatial Blockade](../../../tensura-reincarnated/effects/spatial-blockade.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `Imaginator.mpAcquirement` | 99,000 | Magicule cost to acquire Imaginator. |
| `Imaginator.mpAcquirement` | 99,000 | Magicule cost to acquire Imaginator. |
| `Imaginator.kpPerAdvancement` | 1 | Curiosity: knowledge points per completed advancement (unmastered / mastered). |
| `Imaginator.kpPerAdvancementMastered` | 2 |  |
| `Imaginator.analyzeGrantsKp` | true | Analyze: whether analyzing a new entity type grants knowledge points. |
| `Imaginator.analyzeKpDipInterval` | 5 | Analyze: the Nth new entity type grants N knowledge points; every Nth-interval type is a dip instead. |
| `Imaginator.analyzeKpDipMultiplier` | 0.5 | Analyze: multiplier applied on dip types (0.5 = the 5th, 10th, 15th... type gives half). |
| `Imaginator.potencyPerKp` | 0.01 | Vast Imagination: potency gained per knowledge point (0.01 = +1%). |
| `Imaginator.maxPotency` | 3 | Vast Imagination: maximum potency multiplier. |
| `Imaginator.steelArmorPerKp` | 0.5 | Steel Body: armor per knowledge point, and the cap. |
| `Imaginator.steelMaxArmor` | 40 |  |
| `Imaginator.steelReductionPerKp` | 0.5 | Steel Body: physical damage reduction percent per knowledge point, and the cap. |
| `Imaginator.steelMaxReduction` | 60 |  |
| `Imaginator.steelBreakHealthFraction` | 0.3 | Steel Body (mastered): health fraction at which hardening breaks into regeneration. |
| `Imaginator.steelBreakMpFraction` | 0.2 | Steel Body (mastered): fraction of max MP consumed when hardening breaks. |
| `Imaginator.steelUltraspeedKp` | 25 | Steel Body (mastered): knowledge points for Ultraspeed / Infinite Regeneration. |
| `Imaginator.steelInfiniteKp` | 50 |  |
| `Imaginator.steelRegenSeconds` | 60 | Steel Body (mastered): seconds the regeneration skill lasts. |
| `Imaginator.steelBreakCooldown` | 300 | Steel Body (mastered): cooldown in seconds before hardening can break into regeneration again. |
| `Imaginator.cloneBase` | 5 | Clone Creation: base clone cap, +1 per this many knowledge points, and caps (unmastered / mastered). |
| `Imaginator.cloneKpPerExtra` | 10 |  |
| `Imaginator.cloneCap` | 10 |  |
| `Imaginator.cloneCapMastered` | 15 |  |
| `Imaginator.cloneMpFraction` | 0.1 | Clone Creation: fraction of max MP consumed per clone (Body Double uses a tenth). |
| `Imaginator.cloneDeathHealFraction` | 0.1 | Clone Creation: fraction of a clone's max health healed to the user when it dies. |
| `Imaginator.cloneCooldown` | 5 | Clone Creation / Control cooldowns (seconds). |
| `Imaginator.cloneControlCooldown` | 1 |  |
| `Imaginator.analyzeIntrinsicKp` | 5 | Analyze: knowledge points required per skill category. |
| `Imaginator.analyzeCommonKp` | 10 |  |
| `Imaginator.analyzeExtraKp` | 20 |  |
| `Imaginator.analyzeUniqueKp` | 50 |  |
| `Imaginator.analyzeMpCost` | 1,000 | Analyze: magicule cost, cooldown (seconds) and range. |
| `Imaginator.analyzeCooldown` | 20 |  |
| `Imaginator.analyzeRange` | 20 |  |
| `Imaginator.analyzeMinChance` | 0.1 | Analyze: minimum success chance against much stronger targets. |
| `Imaginator.copyMpCost` | 2,500 | Ability Copy: magicule cost per copy, seconds a temporary copy lasts, and cooldown (seconds). |
| `Imaginator.copyDurationSeconds` | 600 |  |
| `Imaginator.copyCooldown` | 3 |  |
| `Imaginator.envWaterSmallKp` | 5 | Environmental Control: knowledge points for each stage (water 3x3, water 5x5, airless, spatial lock). |
| `Imaginator.envWaterLargeKp` | 10 |  |
| `Imaginator.envAirlessKp` | 15 |  |
| `Imaginator.envSpatialLockKp` | 20 |  |
| `Imaginator.envMpPerSecond` | 500 | Environmental Control: magicule cost per second held, range, and cooldown (seconds) after release. |
| `Imaginator.envRange` | 20 |  |
| `Imaginator.envCooldown` | 15 |  |
| `Imaginator.envAirlessDamage` | 6 | Environmental Control: suffocation damage per second in the airless stage (scaled by potency). |
| `Imaginator.envWaterLifetimeTicks` | 100 | Environmental Control: ticks conjured water lingers after it is placed. |

## In-game messages

<details markdown><summary>Show 14 messages</summary>

- Imaginator
- +%s Knowledge Points (%s total)
- You need %s Knowledge Points to imagine that.
- Imagined a temporary copy of %s.
- The copy could not take shape.
- Your hardened body gives way to %s!
- You cannot imagine more than %s clones.
- Clones: %s / %s
- Clones hold their position.
- Clones follow you again.
- Look at one of your clones to swap places.
- No target in sight.
- %s resisted your analysis.
- Analyzed %s: %s skills readable (%s new), %s beyond your knowledge.

</details>
