# Steel Ki Release

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Steel Ki Release](../../../assets/icons/trnightmare/skill/steel_ki_release.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `trnightmare:steel_ki_release` |
| **Activation** | Toggle |

</div>

> Unleashes concentrated metallic Ki throughout the body, hardening muscles and boosting offensive and defensive power with unbreakable resolve.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect
- Triggers on melee contact
- Triggers when you take damage

## Obtaining

- Listed in the `intrinsicSkills` config option (config/nightmare/race/axolotl/axolotl_config.toml): List of skills obtained by this race.

## Related

- **Effects:** [Aura Sword](../../../tensura-reincarnated/effects/aura-sword.md), [Ogre Guillotine](../../../tensura-reincarnated/effects/ogre-guillotine.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_intrinsic.toml`](../../configs/config-nightmare-ability-skill-nightmare-intrinsic.md).

| Option | Default | Description |
|---|---|---|
| `DarkMagicRelease.elementDamageMultiplier` | 2 | Multiplier on matching elemental damage while released. |
| `DarkMagicRelease.battlewillFlatBonus` | 200 | Flat bonus when battlewill + released (not mastered). |
| `DarkMagicRelease.battlewillFlatBonusMastered` | 400 | Flat bonus when battlewill + released (mastered). |
| `DarkMagicRelease.durabilityFromDamageDivisor` | 6 | Durability break uses max(1, damage / this). |
| `DarkMagicRelease.durabilityBreakBaseMultiplier` | 4 | Multiplier after divisor for durability loss. |
| `DarkMagicRelease.durabilityMasterMultiplier` | 2 | Extra durability multiplier when mastered (multiplicative). |
| `DarkMagicRelease.itemEpBypassThreshold` | 1,000,000 | Skip durability break if stack custom EP is at least this. |
| `HolyMagicRelease.elementDamageMultiplier` | 2 | Multiplier on matching elemental damage while released. |
| `HolyMagicRelease.battlewillFlatBonus` | 200 | Flat bonus when battlewill + released (not mastered). |
| `HolyMagicRelease.battlewillFlatBonusMastered` | 400 | Flat bonus when battlewill + released (mastered). |
| `HolyMagicRelease.durabilityFromDamageDivisor` | 6 | Durability break uses max(1, damage / this). |
| `HolyMagicRelease.durabilityBreakBaseMultiplier` | 4 | Multiplier after divisor for durability loss. |
| `HolyMagicRelease.durabilityMasterMultiplier` | 2 | Extra durability multiplier when mastered (multiplicative). |
| `HolyMagicRelease.itemEpBypassThreshold` | 1,000,000 | Skip durability break if stack custom EP is at least this. |
| `SteelKiRelease.elementDamageMultiplier` | 2 | Multiplier on matching elemental damage while released. |
| `SteelKiRelease.battlewillFlatBonus` | 200 | Flat bonus when battlewill + released (not mastered). |
| `SteelKiRelease.battlewillFlatBonusMastered` | 400 | Flat bonus when battlewill + released (mastered). |
| `SteelKiRelease.durabilityFromDamageDivisor` | 6 | Durability break uses max(1, damage / this). |
| `SteelKiRelease.durabilityBreakBaseMultiplier` | 4 | Multiplier after divisor for durability loss. |
| `SteelKiRelease.durabilityMasterMultiplier` | 2 | Extra durability multiplier when mastered (multiplicative). |
| `SteelKiRelease.itemEpBypassThreshold` | 1,000,000 | Skip durability break if stack custom EP is at least this. |
| `WaterKiRelease.elementDamageMultiplier` | 2 | Multiplier on matching elemental damage while released. |
| `WaterKiRelease.battlewillFlatBonus` | 200 | Flat bonus when battlewill + released (not mastered). |
| `WaterKiRelease.battlewillFlatBonusMastered` | 400 | Flat bonus when battlewill + released (mastered). |
| `WaterKiRelease.durabilityFromDamageDivisor` | 6 | Durability break uses max(1, damage / this). |
| `WaterKiRelease.durabilityBreakBaseMultiplier` | 4 | Multiplier after divisor for durability loss. |
| `WaterKiRelease.durabilityMasterMultiplier` | 2 | Extra durability multiplier when mastered (multiplicative). |
| `WaterKiRelease.itemEpBypassThreshold` | 1,000,000 | Skip durability break if stack custom EP is at least this. |
| `PoisonKiRelease.elementDamageMultiplier` | 2 | Multiplier on matching elemental damage while released. |
| `PoisonKiRelease.battlewillFlatBonus` | 200 | Flat bonus when battlewill + released (not mastered). |
| `PoisonKiRelease.battlewillFlatBonusMastered` | 400 | Flat bonus when battlewill + released (mastered). |
| `PoisonKiRelease.durabilityFromDamageDivisor` | 6 | Durability break uses max(1, damage / this). |
| `PoisonKiRelease.durabilityBreakBaseMultiplier` | 4 | Multiplier after divisor for durability loss. |
| `PoisonKiRelease.durabilityMasterMultiplier` | 2 | Extra durability multiplier when mastered (multiplicative). |
| `PoisonKiRelease.itemEpBypassThreshold` | 1,000,000 | Skip durability break if stack custom EP is at least this. |
| `FireKiRelease.elementDamageMultiplier` | 2 | Multiplier on matching elemental damage while released. |
| `FireKiRelease.battlewillFlatBonus` | 200 | Flat bonus when battlewill + released (not mastered). |
| `FireKiRelease.battlewillFlatBonusMastered` | 400 | Flat bonus when battlewill + released (mastered). |
| `FireKiRelease.durabilityFromDamageDivisor` | 6 | Durability break uses max(1, damage / this). |
| `FireKiRelease.durabilityBreakBaseMultiplier` | 4 | Multiplier after divisor for durability loss. |
| `FireKiRelease.durabilityMasterMultiplier` | 2 | Extra durability multiplier when mastered (multiplicative). |
| `FireKiRelease.itemEpBypassThreshold` | 1,000,000 | Skip durability break if stack custom EP is at least this. |
| `SaintChiRelease.elementDamageMultiplier` | 2 | Multiplier on matching elemental damage while released. |
| `SaintChiRelease.battlewillFlatBonus` | 200 | Flat bonus when battlewill + released (not mastered). |
| `SaintChiRelease.battlewillFlatBonusMastered` | 400 | Flat bonus when battlewill + released (mastered). |
| `SaintChiRelease.durabilityFromDamageDivisor` | 6 | Durability break uses max(1, damage / this). |
| `SaintChiRelease.durabilityBreakBaseMultiplier` | 4 | Multiplier after divisor for durability loss. |
| `SaintChiRelease.durabilityMasterMultiplier` | 2 | Extra durability multiplier when mastered (multiplicative). |
| `SaintChiRelease.itemEpBypassThreshold` | 1,000,000 | Skip durability break if stack custom EP is at least this. |
| `equipmentBreak.elementDamageMultiplier` | 2 | Multiplier on matching elemental damage while released. |
| `equipmentBreak.battlewillFlatBonus` | 200 | Flat bonus when battlewill + released (not mastered). |
| `equipmentBreak.battlewillFlatBonusMastered` | 400 | Flat bonus when battlewill + released (mastered). |
| `equipmentBreak.durabilityFromDamageDivisor` | 6 | Durability break uses max(1, damage / this). |
| `equipmentBreak.durabilityBreakBaseMultiplier` | 4 | Multiplier after divisor for durability loss. |
| `equipmentBreak.durabilityMasterMultiplier` | 2 | Extra durability multiplier when mastered (multiplicative). |
| `equipmentBreak.itemEpBypassThreshold` | 1,000,000 | Skip durability break if stack custom EP is at least this. |
