# `config/tensura/EliteTensura/WeaponConfig.toml`

<small>[Elite Tensura](../index.md) &rsaquo; [Configs](index.md)</small>

## `[AetherforgedSpear]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master toggle for the Piercing Vector active. |
| `auraCost` | 300 |  | Aura cost on release. |
| `magiculeCost` | 300 |  | Magicule cost on release. |
| `cooldown` | 160 |  | Cooldown in game ticks (160 = 8s). |
| `fullChargeTicks` | 30 |  | Hold ticks for a full charge (30 = 1.5s). |
| `minChargeTicks` | 10 |  | Minimum hold ticks before release fires at all (10 = 0.5s). |
| `minDamageFactor` | 1.5 |  | Damage = ATTACK_DAMAGE \* factor, scaled min-&gt;max by charge fraction. |
| `maxDamageFactor` | 3 |  |  |
| `lungeStrength` | 1.6 |  | Forward lunge velocity scale at full charge. |
| `strikeRange` | 6 |  | Hit-scan reach of the released thrust, in blocks. |
| `friendlyFire` | false |  | If true, Piercing Vector also hits players in the user's own nation or hunt party. |

## `[AetherforgedKatana]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master toggle for the Phase Cut active. |
| `auraCost` | 250 |  | Aura cost when arming the cut. |
| `magiculeCost` | 250 |  | Magicule cost when arming the cut. |
| `cooldown` | 200 |  | Cooldown in game ticks (200 = 10s), starts when armed. |
| `windowTicks` | 100 |  | Window in game ticks during which the next hit phases (100 = 5s). |
| `bonusFactor` | 0.5 |  | Bonus phase damage = ATTACK_DAMAGE \* this factor, dealt armor-bypassing. |

## `[AetherforgedWarHammer]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master toggle for the Crushing Impact active. |
| `auraCost` | 400 |  | Aura cost per slam. |
| `magiculeCost` | 400 |  | Magicule cost per slam. |
| `cooldown` | 240 |  | Cooldown in game ticks (240 = 12s). |
| `radius` | 4 |  | AoE radius in blocks around the player. |
| `damageFactor` | 1.2 |  | Damage = ATTACK_DAMAGE \* this factor. |
| `knockup` | 0.6 |  | Upward knock velocity applied to victims. |
| `slownessTicks` | 60 |  | Slowness duration in ticks (60 = 3s). |
| `slownessAmplifier` | 1 |  | Slowness amplifier (1 = Slowness II). |
| `friendlyFire` | false |  | If true, Crushing Impact also hits players in the user's own nation or hunt party. |

## `[AetherforgedGauntlets]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master toggle for the Aether Burst active. |
| `auraCost` | 200 |  | Aura cost per burst. |
| `magiculeCost` | 200 |  | Magicule cost per burst. |
| `cooldown` | 160 |  | Cooldown in game ticks (160 = 8s). |
| `radius` | 3.5 |  | Shockwave radius in blocks. |
| `damageFactor` | 0.8 |  | Damage = ATTACK_DAMAGE \* this factor. |
| `knockbackStrength` | 1.5 |  | Outward horizontal knockback strength. |
| `knockbackUp` | 0.4 |  | Upward knockback component. |
| `friendlyFire` | false |  | If true, Aether Burst also hits players in the user's own nation or hunt party. |

## `[VoidEdgeWeapon]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master toggle for all three Void Edge weapon abilities. |
| `useVoiceOfTheWorld` | false |  | Whether Void Edge abilities announce via Voice of the World. |
| `spatialDamageFactor` | 1.5 |  | Spatial Cut: damage = ATTACK_DAMAGE \* this factor + flat. |
| `spatialDamageFlat` | 30 |  |  |
| `spatialRange` | 24 |  | Spatial Cut: line length in blocks (passes through walls). |
| `spatialRadius` | 1.5 |  | Spatial Cut: hit radius around each point of the line. |
| `spatialCooldown` | 40 |  | Spatial Cut: cooldown in ticks. |
| `spatialAuraCost` | 200 |  | Spatial Cut: aura cost. |
| `spatialMagiculeCost` | 200 |  | Spatial Cut: magicule cost. |
| `teleportRange` | 20 |  | Teleport Slash: max target range in blocks. |
| `teleportDamageFactor` | 1.5 |  | Teleport Slash: damage = ATTACK_DAMAGE \* factor + flat. |
| `teleportDamageFlat` | 40 |  |  |
| `teleportMarkBonus` | 1.5 |  | Teleport Slash: damage multiplier when the target carries a Dimensional Mark. |
| `teleportInvulnTicks` | 15 |  | Teleport Slash: invulnerability frames (ticks) granted on arrival. |
| `teleportSlashDelay` | 5 |  | Teleport Slash: delay (ticks) before the follow-up slash lands. |
| `teleportCooldown` | 80 |  | Teleport Slash: cooldown in ticks. |
| `teleportAuraCost` | 300 |  | Teleport Slash: aura cost. |
| `teleportMagiculeCost` | 100 |  | Teleport Slash: magicule cost. |
| `fractureDamageFactor` | 2 |  | Reality Fracture: damage = ATTACK_DAMAGE \* factor + flat. |
| `fractureDamageFlat` | 80 |  |  |
| `fractureRadius` | 6 |  | Reality Fracture: AOE radius in blocks. |
| `fractureCastRange` | 20 |  | Reality Fracture: max cast range when targeting a look point. |
| `fractureCooldown` | 600 |  | Reality Fracture: cooldown in ticks. |
| `fractureMagiculeCost` | 3,000 |  | Reality Fracture: magicule cost. |
| `fractureAuraCost` | 3,000 |  | Reality Fracture: aura cost. |
| `fractureDebuffDuration` | 200 |  | Fractured Reality debuff duration (ticks) applied to caught targets. |
| `fractureDebuffAmplifier` | 1 |  | Fractured Reality debuff amplifier (0 = level I). |
| `fractureTickDamage` | 8 |  | Fractured Reality: Void damage dealt per second, scaled by (amplifier+1). |
| `fractureDamageTakenMultiplier` | 1.25 |  | Fractured Reality: incoming-damage multiplier on afflicted targets. |
| `fractureSlow` | -0.3 |  | Fractured Reality: movement-speed modifier (negative = slow), ADD_MULTIPLIED_TOTAL. |
| `markDuration` | 120 |  | Dimensional Mark duration (ticks) applied by Spatial Cut. |
| `comboWindow` | 100 |  | Combo window (ticks) linking Spatial -&gt; Teleport -&gt; Fracture. |
| `comboRadiusBonus` | 1.5 |  | Reality Fracture radius multiplier when chained from a recent Teleport Slash. |
| `resonanceDamageBonus` | 1.5 |  | Reality Fracture damage multiplier when the full resonance combo lands. |
| `friendlyFire` | false |  | If true, Spatial Cut and Reality Fracture also hit players in the wielder's own nation or hunt party. |

## `[AstralEdgeWeapon]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master toggle for all three Astral Edge weapon abilities. |
| `useVoiceOfTheWorld` | false |  | Whether Astral Edge abilities announce via Voice of the World. |
| `lanceDamageFactor` | 1.5 |  | Starlight Lance: damage = ATTACK_DAMAGE \* this factor + flat. |
| `lanceDamageFlat` | 30 |  |  |
| `lanceRange` | 24 |  | Starlight Lance: line length in blocks (passes through walls). |
| `lanceRadius` | 1.5 |  | Starlight Lance: hit radius around each point of the line. |
| `lanceCooldown` | 40 |  | Starlight Lance: cooldown in ticks. |
| `lanceAuraCost` | 200 |  | Starlight Lance: aura cost. |
| `lanceMagiculeCost` | 200 |  | Starlight Lance: magicule cost. |
| `purgeBonus` | 1.5 |  | Starlight Lance: damage multiplier when purging void effects (Dimensional Mark / Fractured Reality) off a target. |
| `stepRange` | 20 |  | Astral Step: max target range in blocks. |
| `stepDamageFactor` | 1.5 |  | Astral Step: damage = ATTACK_DAMAGE \* factor + flat. |
| `stepDamageFlat` | 40 |  |  |
| `stepMarkBonus` | 1.5 |  | Astral Step: damage multiplier when the target carries a Celestial Mark. |
| `stepInvulnTicks` | 15 |  | Astral Step: invulnerability frames (ticks) granted on arrival. |
| `stepSlashDelay` | 5 |  | Astral Step: delay (ticks) before the follow-up slash lands. |
| `stepAbsorptionDuration` | 100 |  | Astral Step: Absorption duration (ticks) granted to the wielder on arrival. |
| `stepAbsorptionAmplifier` | 1 |  | Astral Step: Absorption amplifier (0 = level I). |
| `stepCooldown` | 80 |  | Astral Step: cooldown in ticks. |
| `stepAuraCost` | 300 |  | Astral Step: aura cost. |
| `stepMagiculeCost` | 100 |  | Astral Step: magicule cost. |
| `dawnDamageFactor` | 2 |  | Creation's Dawn: damage = ATTACK_DAMAGE \* factor + flat. |
| `dawnDamageFlat` | 80 |  |  |
| `dawnRadius` | 6 |  | Creation's Dawn: AOE radius in blocks. |
| `dawnCastRange` | 20 |  | Creation's Dawn: max cast range when targeting a look point. |
| `dawnHealAmount` | 40 |  | Creation's Dawn: flat healing granted to the wielder and allies in the radius. |
| `dawnRegenDuration` | 200 |  | Creation's Dawn: Regeneration duration (ticks) granted to the wielder and allies. |
| `dawnRegenAmplifier` | 1 |  | Creation's Dawn: Regeneration amplifier (0 = level I). |
| `dawnCooldown` | 600 |  | Creation's Dawn: cooldown in ticks. |
| `dawnMagiculeCost` | 3,000 |  | Creation's Dawn: magicule cost. |
| `dawnAuraCost` | 3,000 |  | Creation's Dawn: aura cost. |
| `dawnDebuffDuration` | 200 |  | Starlight Judgment debuff duration (ticks) applied to caught targets. |
| `dawnDebuffAmplifier` | 1 |  | Starlight Judgment debuff amplifier (0 = level I). |
| `judgmentTickDamage` | 8 |  | Starlight Judgment: Celestial damage dealt per second, scaled by (amplifier+1). |
| `judgmentDamageTakenMultiplier` | 1.25 |  | Starlight Judgment: incoming-damage multiplier on afflicted targets. |
| `judgmentAttackDown` | -0.3 |  | Starlight Judgment: attack-damage modifier (negative = weaker), ADD_MULTIPLIED_TOTAL. |
| `markDuration` | 120 |  | Celestial Mark duration (ticks) applied by Starlight Lance. |
| `comboWindow` | 100 |  | Combo window (ticks) linking Lance -&gt; Step -&gt; Dawn. |
| `comboRadiusBonus` | 1.5 |  | Creation's Dawn radius multiplier when chained from a recent Astral Step. |
| `resonanceDamageBonus` | 1.5 |  | Creation's Dawn damage multiplier when the full resonance combo lands. |
| `friendlyFire` | false |  | If true, Starlight Lance hits nation/hunt-party members, and Creation's Dawn damages them instead of healing them. |
