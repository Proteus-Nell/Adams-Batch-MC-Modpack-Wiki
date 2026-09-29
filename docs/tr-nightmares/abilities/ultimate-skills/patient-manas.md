# Patient Manas

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![Patient Manas](../../../assets/icons/trnightmare/skill/cadence.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:patient_manas` |
| **Modes** | 9 |
| **Acquisition cost (MP)** | 1,500,000 |
| **Activation** | Toggle, Press, Hold |

</div>

## Modes

| # | Mode |
|---|---|
| 1 | Gabriel Air Wall |
| 2 | Gabriel Time Control |
| 3 | Gabriel Time Freeze |
| 4 | Gabriel White Lock |
| 5 | Gabriel Eternal World |
| 6 | Gabriel Block Accel |
| 7 | Gabriel Heat Death |
| 8 | Gabriel Counter Freeze |
| 9 | Gabriel Snow Crystal |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 0 (ego ultimate cost) |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Triggers when you take damage
- Does something when first learned

## Obtaining

- Acquisition checks: [Cadence](../unique-skills/cadence.md), [｢ Gabriel, Lord of Patience ｣](gabriel.md)
- In-game message: *Cadence has stilled itself completely. Your Unique Skill has evolved into the Ultimate Skill: Gabriel, Lord of Patience.*

## Related

- **Related skills:** [｢ Gabriel, Lord of Patience ｣](gabriel.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Gabriel.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Gabriel.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Gabriel.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Gabriel.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Gabriel.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Gabriel.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Gabriel.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Gabriel.mpAcquirement` | 1,500,000 | Magicule cost to acquire Gabriel (paid via skill obtainment, not evolution conditions). |
| `Gabriel.enableUltimateEvolution` | true | Whether Cadence may evolve into Gabriel. |
| `Gabriel.gabrielHeroCount` | 10 | Hero raid wins required to evolve Cadence into Gabriel. |
| `Gabriel.timeFreezeUses` | 50 | Time Freeze uses on Cadence required to evolve into Gabriel. |
| `Gabriel.learnPointsTimeFreeze` | 500 | Learning points required to unlock Time Freeze mode. |
| `Gabriel.learnPointsWhiteLock` | 1,000 | Learning points required to unlock White Lock mode. |
| `Gabriel.learnPointsBlockAccel` | 750 | Learning points required to unlock Block Accel mode. |
| `Gabriel.timeFreezePulseDurationTicks` | 100 | Duration (ticks) of each Time Freeze pulse. |
| `Gabriel.timeFreezeCooldownSeconds` | 20 | Cooldown (seconds) for Time Freeze mode. |
| `Gabriel.whiteLockCooldownSeconds` | 60 | Cooldown (seconds) for White Lock mode. |
| `Gabriel.whiteLockDurationTicks` | 600 | White Lock duration in ticks. |
| `Gabriel.blockAccelCooldownSeconds` | 15 | Cooldown (seconds) for Block Accel mode. |
| `Gabriel.airWallMagiculePerSecond` | 50 | Magicules drained per second while holding Air Wall. |
| `Gabriel.timeControlMagiculePerSecond` | 40 | Magicules drained per second while holding Time Control. |
| `Gabriel.timeControlSlowFactor` | 0.5 | Time slow factor while holding Time Control (unmastered). 0.5 = 50% slower. |
| `Gabriel.timeControlSlowFactorMastered` | 0.2 | Time slow factor while holding Time Control when mastered. 0.2 = 80% slower. |
| `Gabriel.eternalWorldRadius` | 16 | Radius of Eternal World field (blocks). |
| `Gabriel.timeFreezeHalfWidth` | 16 | Half-width of Gabriel Time Freeze field (32x32 field = 16). |
| `Gabriel.timeControlHalfWidth` | 4 | Half-width of Gabriel Time Control field (8x8 field = 4). |
| `Gabriel.heatDeathHalfSize` | 15 | Half-size of Heat Death kill cube (30x30x30 = 15). |
| `Gabriel.heatDeathParticlesPerTick` | 120 | Snowflake particles spawned per tick during Heat Death. |
| `Gabriel.heatDeathCooldownSeconds` | 30 | Cooldown in seconds for Heat Death. |
| `Gabriel.heatDeathEffectDurationTicks` | 600 | Heat Death debuff duration in ticks on survivors. |
| `Gabriel.counterFreezeWindowTicks` | 60 | Counter Freeze active window in ticks. |
| `Gabriel.counterFreezeCooldownSeconds` | 15 | Cooldown in seconds after activating Counter Freeze. |
| `Gabriel.counterFreezeLockTicks` | 100 | White Lock duration in ticks applied by Counter Freeze (unmastered). |
| `Gabriel.counterFreezeLockTicksMastered` | 200 | White Lock duration in ticks applied by Counter Freeze when mastered. |
| `Gabriel.counterFreezeChillTicks` | 80 | Chill duration in ticks applied by Counter Freeze. |
| `Gabriel.snowCrystalHalfSize` | 5 | Half-size of Snow Crystal shell (10x10x10 = 5). |
| `Gabriel.snowCrystalInteriorHalf` | 2 | Half-size of hollow interior (4x4x4 = 2). |
| `Gabriel.snowCrystalHolderCheckPadding` | 6 | Extra block distance used when checking if a crystal block should persist. |
