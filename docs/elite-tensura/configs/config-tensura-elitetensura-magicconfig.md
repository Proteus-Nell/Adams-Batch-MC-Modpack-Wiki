# `config/tensura/EliteTensura/MagicConfig.toml`

<small>[Elite Tensura](../index.md) &rsaquo; [Configs](index.md)</small>

## `[StaticChain]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 30 |  | Cast time in ticks (20 = 1s). |
| `castTimeMastered` | 20 |  | Cast time in ticks when mastered. |
| `magiculeCost` | 120 |  | Magicule cost per normal cast. |
| `magiculeCostCharged` | 200 |  | Magicule cost for the charged (mastered, held-longer) cast. |
| `cooldown` | 0 |  | Cooldown in seconds. |
| `cooldownMastered` | 0 |  | Cooldown in seconds when mastered. |
| `baseDamage` | 20 |  | Magic damage dealt to the first target (decays each hop). |
| `baseDamageCharged` | 35 |  | Base damage for the charged cast. |
| `damageDecay` | 0.65 |  | Damage multiplier applied per chain hop (0.65 = each hop deals 65% of the previous). |
| `chargedDamageDecay` | 0.8 |  | Damage decay per hop for the charged cast (higher = holds damage longer). |
| `maxHops` | 4 |  | Maximum number of targets the arc chains through. |
| `chargedBonusHops` | 4 |  | Extra hops added by the charged cast. |
| `initialRange` | 14 |  | Range (blocks) to acquire the first target in the look direction. |
| `chainRange` | 6 |  | Max distance (blocks) the arc can jump between chain links. |
| `strikeRadius` | 1.5 |  | Radius (blocks) of each lightning strike's area damage at a link. |
| `glowingDuration` | 60 |  | Glowing effect duration (ticks) applied to each hit target. |
| `slowDuration` | 30 |  | Slowness effect duration (ticks) applied to each hit target. |
| `slowAmplifier` | 2 |  | Slowness amplifier (0-indexed; 2 = Slowness III). |
| `friendlyFire` | false |  | If true the arc also chains onto players in the caster's own nation or hunt party. The deliberately-aimed first target is never filtered. |

## `[Kamehameha]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 60 |  | Cast (charge) time in ticks (20 = 1s). |
| `castTimeMastered` | 40 |  | Cast (charge) time in ticks when mastered. |
| `magiculeCost` | 2,500 |  | Magicule cost per normal cast. |
| `magiculeCostCharged` | 5,000 |  | Magicule cost for the charged (mastered, held-longer) cast. |
| `cooldown` | 10 |  | Cooldown in seconds. |
| `cooldownMastered` | 3 |  | Cooldown in seconds when mastered. |
| `damage` | 20 |  | Damage per beam hit. The beam hits targets repeatedly while they stay inside it, so total damage over the full beam duration is several times this value. |
| `damageCharged` | 35 |  | Damage per beam hit for the charged cast. |
| `beamSize` | 1.5 |  | Beam thickness (blocks). |
| `beamSizeCharged` | 2.5 |  | Beam thickness for the charged cast. |
| `range` | 40 |  | Beam reach (blocks). |
| `beamDuration` | 60 |  | How long the beam lasts, in ticks (the final 20 ticks fade out). |
| `beamDurationCharged` | 100 |  | Beam duration in ticks for the charged cast. |
| `explosionRadius` | 1.5 |  | Explosion radius where the beam meets terrain or targets (0 = no explosion). |
| `explosionRadiusCharged` | 3 |  | Explosion radius for the charged cast. |

## `[GravityWell]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 60 |  | Cast (charge) time in ticks (20 = 1s). |
| `castTimeMastered` | 40 |  | Cast (charge) time in ticks when mastered. |
| `magiculeCost` | 500 |  | Magicule cost per normal cast. |
| `magiculeCostCharged` | 900 |  | Magicule cost for the charged (mastered, held-longer) cast. |
| `cooldown` | 25 |  | Cooldown in seconds. |
| `cooldownMastered` | 18 |  | Cooldown in seconds when mastered. |
| `radius` | 6 |  | Sphere radius in blocks. |
| `radiusCharged` | 9 |  | Sphere radius for the charged cast. |
| `durationTicks` | 160 |  | How long the well lasts, in ticks (20 = 1s). |
| `durationTicksCharged` | 200 |  | Well duration in ticks for the charged cast. |
| `crushPercent` | 0.03 |  | Crush damage per second as a fraction of the victim's max health (0.03 = 3%). |
| `crushPercentCharged` | 0.05 |  | Crush fraction per second for the charged cast. |
| `crushDamageCap` | 100 |  | Hard cap on a single crush hit, in half-hearts of damage. Keeps percent-max-HP crush from melting huge-HP bosses. 0 = uncapped. |
| `pullStrength` | 0.15 |  | Inward pull strength per tick at the sphere's rim (pull weakens toward the centre). |
| `castRange` | 24 |  | Max distance (blocks) at which the well can be anchored along the caster's aim. |
| `friendlyFire` | false |  | If true the well also pulls and crushes players in the caster's own nation or hunt party. |
