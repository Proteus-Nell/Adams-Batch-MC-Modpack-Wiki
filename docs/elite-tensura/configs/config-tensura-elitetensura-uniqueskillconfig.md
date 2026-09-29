# `config/tensura/EliteTensura/UniqueSkillConfig.toml`

<small>[Elite Tensura](../index.md) &rsaquo; [Configs](index.md)</small>

## `[VoidEdge]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mpAcquirement` | 8,000 |  |  |
| `cloakAuraDrainPerTick` | 2 |  |  |
| `cloakConcealmentLevel` | 1 |  |  |
| `cloakConcealmentLevelMastered` | 3 |  |  |
| `cloakDodgeBonus` | 10 |  |  |
| `cloakChantSpeedMultiplier` | 1.4 |  |  |
| `voidEdgeMagiculeCost` | 800 |  |  |
| `voidEdgeDamage` | 25 |  |  |
| `voidEdgeDamageMastered` | 50 |  |  |
| `voidEdgeSize` | 1 |  |  |
| `voidEdgeSizeMastered` | 1.4 |  |  |
| `voidEdgeDuration` | 60 |  |  |
| `voidEdgeDurationMastered` | 90 |  |  |
| `voidEdgeCooldownSeconds` | 4 |  |  |
| `voidEdgeCooldownMasteredSeconds` | 3 |  |  |

## `[Hecate]`

| Option | Default | Range | Description |
|---|---|---|---|
| `inSlotCostMultiplier` | 0.1 |  | In-slot passive: multiplier applied to every spell's magicule cost (0.0 = floored to free/minimum). Blacklisted spells (see costFloorBlacklist) keep their normal cost. |
| `costFloorBlacklist` | "tensura:reincarnation" |  | Spell registry IDs excluded from the in-slot cost floor (kept at full cost). |
| `magiculeCostPerTick` | 50 |  | Magicule drained per tick while the toggle is active. |
| `learningPoint` | 1 |  | Bonus learning gain (ADD_VALUE) while toggled. |
| `masteryPoint` | 1 |  | Bonus mastery gain (ADD_VALUE) while toggled. |
| `passiveLearningBonus` | 1 |  | In-slot passive: flat bonus to learning-point gain for Magic (spells) only, always active while Hecate is slotted (stacks with the toggle's learningPoint bonus). |
| `passiveMasteryBonus` | 1 |  | In-slot passive: flat bonus to mastery-point gain for Magic (spells) only, always active while Hecate is slotted (stacks with the toggle's masteryPoint bonus). |
| `spellDamageBonus` | 30 |  | Flat bonus damage added to all spell (magic) damage while toggled. |
| `spellDamageBonusMastered` | 75 |  | Flat bonus spell damage while toggled, when Hecate is mastered. |

## `[Brain]`

| Option | Default | Range | Description |
|---|---|---|---|
| `debug` | false |  | Log Brain's per-evaluation AI decisions to the server console/log (skills toggled, skills pressed, magic buckets, cast attempts and why a cast did/didn't fire). Off by default — turn on to diagnose why a mob isn't using its abilities. |
| `evalInterval` | 1 |  | Number of skill-tick passes between Brain evaluations. ManasCore ticks passive skills every 100 game ticks (~5 seconds), so 1 = evaluate every ~5s (default), 2 = ~10s, etc. This is NOT in game ticks — the native passive-tick cadence is the floor. |
| `lowHealthFraction` | 0.5 |  | Health fraction (0-1) below which the mob is treated as hurt: prioritises recovery magic and enables pressing active skills defensively. |

## `[Stillness]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master enable. When false the skill can never be acquired. |
| `epAcquirement` | 50,000 |  | Max EP required to evolve Meditation into Stillness. |
| `bossKillsRequired` | 3 |  | Total boss kills required (Tensura bossesCounter bosses + world calamities). |
| `magiculeCost` | 30 |  | Magicule drained per tick while Serenity is toggled on. |
| `regenRate` | 1 |  | Aura/magicule/SHP regeneration added while Serenity is active (Meditation is 0.5). |
| `regenRateMastered` | 1.5 |  | Serenity regeneration when mastered. |
| `restorePercent` | 25 |  | Inner Calm: percent of MAX magicule and aura restored instantly (0-100). |
| `restorePercentMastered` | 40 |  | Inner Calm restore percent when mastered. |
| `calmCooldownSeconds` | 300 |  | Inner Calm cooldown in SECONDS. |
| `calmCooldownMasteredSeconds` | 180 |  | Inner Calm cooldown in SECONDS when mastered. |

## `[FortunesEye]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master enable. When false the skill can never be acquired. |
| `epAcquirement` | 100,000 |  | Max EP required to evolve Scavenger into Fortune's Eye. |
| `bossKillsRequired` | 5 |  | Total boss kills required (Tensura bossesCounter bosses + world calamities). |
| `baseLuckAmplifier` | 2 |  | Passive Luck amplifier (2 = Luck III, 0-indexed). Scavenger's passive is Luck II. |
| `masteredLuckAmplifier` | 3 |  | Passive Luck amplifier when mastered (3 = Luck IV). |
| `senseRadius` | 24 |  | Loot Sense: radius in blocks that dropped items are revealed in. |
| `senseRadiusMastered` | 40 |  | Loot Sense radius when mastered. |
| `senseDurationTicks` | 200 |  | Loot Sense: how long revealed items glow, in ticks. |
| `senseCooldownSeconds` | 60 |  | Loot Sense cooldown in SECONDS. |
| `senseCooldownMasteredSeconds` | 30 |  | Loot Sense cooldown in SECONDS when mastered. |
| `senseMagiculeCost` | 100 |  | Loot Sense magicule cost per press. |

## `[Unbreakable]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master enable. When false the skill can never be acquired. |
| `epAcquirement` | 150,000 |  | Max EP required to evolve Iron Resolve into Unbreakable. |
| `bossKillsRequired` | 8 |  | Total boss kills required (Tensura bossesCounter bosses + world calamities). |
| `hasteAmplifier` | 9 |  | Vein Sense Haste amplifier (9 = Haste 10, 0-indexed). |
| `aegisMaxReduction` | 50 |  | Iron Aegis: maximum incoming-damage reduction percent at full magicule (Iron Resolve caps at 40). |
| `surgeMagiculeCost` | 2,000 |  | Resolute Surge magicule cost per activation. |
| `surgeStrengthAmplifier` | 3 |  | Resolute Surge Strength amplifier (3 = Strength IV, 0-indexed). |
| `surgeDurationTicks` | 6,000 |  | Resolute Surge duration in ticks. |
| `surgeDurationMasteredTicks` | 12,000 |  | Resolute Surge duration in ticks when mastered. |
| `surgeCooldownSeconds` | 360 |  | Resolute Surge cooldown in SECONDS. |
| `surgeCooldownMasteredSeconds` | 720 |  | Resolute Surge cooldown in SECONDS when mastered. Deliberately longer: duration doubles too (6000→12000t), holding uptime at ~83% — mastery buys fewer activations, not more uptime. |
| `undyingSurviveHealthPct` | 10 |  | Undying Will: percent of max health restored when a fatal hit is cheated (0-100). |
| `undyingImmunityTicks` | 60 |  | Undying Will: full-immunity duration in ticks after triggering (Resistance V). |
| `undyingCooldownSeconds` | 600 |  | Undying Will internal cooldown in SECONDS. |
| `undyingCooldownMasteredSeconds` | 360 |  | Undying Will internal cooldown in SECONDS when mastered. |

## `[ElderSoul]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master enable. When false the skill can never be acquired. |
| `epAcquirement` | 100,000 |  | Max EP required to evolve Ancient Soul into Elder Soul. |
| `bossKillsRequired` | 5 |  | Total boss kills required (Tensura bossesCounter bosses + world calamities). |
| `magiculeDrainPerTick` | 4 |  | Magicule drained per tick while the aura is toggled on (Ancient Soul is 2). |
| `buffRadius` | 40 |  | Ally-buff aura radius in blocks (Ancient Soul is 25). |
| `buffRadiusMastered` | 50 |  | Ally-buff aura radius when mastered. |
| `soulSightRadius` | 50 |  | Soul Sight ESP radius in blocks for the holder (covers the mastered aura). |
| `strengthAmplifier` | 2 |  | Aura Strength amplifier (2 = Strength III). |
| `regenAmplifier` | 2 |  | Aura Regeneration amplifier (2 = Regeneration III). |
| `resistanceAmplifier` | 1 |  | Aura Resistance amplifier (1 = Resistance II; Ancient Soul gives I). |
| `effectDurationTicks` | 120 |  | Duration in ticks of each aura effect application. Keep &gt;= 100: ManasCore refreshes toggle skills every 100 game ticks. |
| `refreshIntervalTicks` | 120 |  | Revealing Presence: glow lease per sweep = this + revealLingerTicks (sweeps run every 100-tick skill tick). |
| `revealLingerTicks` | 40 |  | Revealing Presence: ticks an enemy keeps glowing after leaving the aura. |

## `[CrocodileSkin]`

| Option | Default | Range | Description |
|---|---|---|---|
| `IsEnabled` | true |  | Is this Skill Enabled? When false it can never be acquired. |
| `epTierPureMagisteel` | 100,000 |  | Max EP at which the armour becomes Pure Magisteel (below: High Magisteel). |
| `epTierAdamantite` | 500,000 |  | Max EP at which the armour becomes Adamantite. |
| `epTierHihiirokane` | 900,000 |  | Max EP at which the armour becomes Hihiirokane. |
