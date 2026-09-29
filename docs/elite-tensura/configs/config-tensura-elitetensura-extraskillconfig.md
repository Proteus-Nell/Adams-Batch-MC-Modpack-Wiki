# `config/tensura/EliteTensura/ExtraSkillConfig.toml`

<small>[Elite Tensura](../index.md) &rsaquo; [Configs](index.md)</small>

## `[MeditationSkill]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | True/False Disable this skill? |
| `epAcquirement` | 500 |  | EP Requirement for Learning Meditation. |
| `magiculeCost` | 20 |  | Magicule Cost to activate . |
| `auraRegenRate` | 0.5 |  | Aura Regen rate. |
| `manaRegenRate` | 0.5 |  | Mana Regen rate |
| `shpRegenRate` | 0.5 |  | SHP Regen rate |

## `[Iron_Resolve]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 10,000 |  |  |
| `hasteAmplifier` | 9 |  |  |
| `aegisMaxReduction` | 40 |  |  |
| `surgeMagiculeCost` | 2,000 |  |  |
| `surgeStrengthAmplifier` | 2 |  |  |
| `surgeDurationTicks` | 6,000 |  |  |
| `surgeDurationMasteredTicks` | 12,000 |  |  |
| `surgeCooldownSeconds` | 360 |  | Cooldown after using Resolute Surge, in SECONDS. Default 360 = 6 minutes. |
| `surgeCooldownMasteredSeconds` | 720 |  | Cooldown after using Resolute Surge when mastered, in SECONDS. Default 720 = 12 minutes. |
| `lastStandThresholdPct` | 40 |  |  |
| `lastStandImmunityTicks` | 60 |  | Duration of the Last Stand immunity window, in TICKS. Default 60 = 3 seconds. |
| `lastStandResistanceAmplifier` | 4 |  |  |
| `lastStandInternalCooldownTicks` | 300 |  | Internal cooldown before Last Stand can re-fire, in TICKS. Default 300 = 15 seconds. |
| `enabled` | true |  |  |
| `epAcquirement` | 20,000 |  |  |

## `[Scavenger]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 500 |  | Magicule cost to learn Scavenger. |
| `baseLuckAmplifier` | 1 |  | Luck amplifier for unmastered holders (0=Luck I, 1=Luck II, 2=Luck III). Default: 1 = Luck II. |
| `masteredLuckAmplifier` | 2 |  | Luck amplifier for mastered holders with toggle active (0=Luck I, 1=Luck II, 2=Luck III). Default: 2 = Luck III. |
| `enabled` | true |  |  |
| `epAcquirement` | 15,000 |  |  |

## `[AncientSoul]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | True/False — is the Ancient Soul skill enabled (acquirable)? |
| `epAcquirement` | 5,000 |  | EP requirement for learning Ancient Soul. |
| `mpAcquirement` | 0 |  | Magicule acquiring cost to learn the skill. |
| `magiculeDrainPerTick` | 2 |  | Magicule drained per tick while the skill is held (passive upkeep). |
| `buffRadius` | 25 |  | Radius (blocks) of the Aura of the Ancient ally buff. |
| `soulSightRadius` | 30 |  | Radius (blocks) within which Soul Sight outlines entities. |
| `strengthAmplifier` | 2 |  | Strength effect amplifier (0-indexed; 2 = Strength III). |
| `regenAmplifier` | 2 |  | Regeneration effect amplifier (0-indexed; 2 = Regeneration III). |
| `resistanceAmplifier` | 0 |  | Resistance effect amplifier (0-indexed; 0 = Resistance I). |
| `effectDurationTicks` | 120 |  | Duration (ticks) applied to the aura effects on each refresh. Keep &gt;= 100: ManasCore refreshes toggle skills every 100 game ticks. |
| `refreshIntervalTicks` | 120 |  | Legacy — the aura now refreshes on every 100-tick skill tick; this value is no longer read. |
