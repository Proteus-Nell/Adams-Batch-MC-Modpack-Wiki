# Cadence

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Cadence](../../../assets/icons/trnightmare/skill/cadence.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:cadence` |
| **Modes** | 6 |
| **Acquisition cost (MP)** | 170,000 |
| **Max mastery** | 1,000 |
| **Cooldowns (s)** | 30, 45, 20 |
| **Activation** | Toggle, Press, Hold |

</div>

> The perfected evolution of Stasis. Anchor magicule and aura with Fixed State, bend localized time through Time Control and Time Freeze, bind a single foe with White Lock, and cross the battlefield on Block Acceleration glass.

## Modes

| # | Mode |
|---|---|
| 1 | Cadence Fixed State |
| 2 | Cadence Air Wall |
| 3 | Cadence Time Control |
| 4 | Cadence Time Freeze |
| 5 | Cadence White Lock |
| 6 | Cadence Block Accel |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect

## Obtaining

- Listed in the `egoWhitelist` config option (config/nightmare/ability/skill/ego/general_config.toml): Skills allowed to develop ego if in whitelist mode
- Listed in the `virtueDominionSkills` config option (config/nightmare/ability/skill/nightmare_ult.toml): Virtue skills that Ultimate Dominion can copy from targets.
- Listed in the `VirtueSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): Virtue unique skill ids for Michael Ultimate Dominion.

## Related

- **Related skills:** [Stasis](stasis.md)
- **Effects:** [Fixed State](../../effects/stasis-fixed-state.md), [White Lock](../../effects/cadence-white-lock.md)
- **Summons / entities:** Tensura, Stasis Air Wall
- **Referenced by:** [Witch's Greed](witches-greed.md), [｢ Gabriel, Lord of Patience ｣](../ultimate-skills/gabriel.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `cadence.epAcquirement` | 170,000 | EP / magicule obtainment cost to acquire Cadence (evolution of Stasis). |
| `cadence.learningCost` | 1,000 | Learning / mastery point cost. |
| `cadence.maxMastery` | 1,000 | Max mastery. |
| `cadence.fixedStateCooldownSeconds` | 60 | Fixed State: cooldown in seconds. |
| `cadence.fixedStateDurationTicks` | 600 | Fixed State: effect duration (ticks). |
| `cadence.airWallMagiculePerSecond` | 1,000 | Air Wall: magicules drained per second while held. |
| `cadence.airWallHalfSize` | 2.5 | Air Wall: horizontal half-size of the wall (blocks). |
| `cadence.airWallCenterDistance` | 2.75 | Air Wall: distance in front of the caster (blocks). |
| `cadence.airWallThickness` | 0.35 | Air Wall: thickness along the facing axis (blocks). |
| `cadence.timeControlMagiculePerSecond` | 2,000 | Time Control (hold): magicules per second. |
| `cadence.timeControlHalfWidth` | 4 | Half-width (blocks) of Time Control / Time Freeze field around the user (4 =&gt; 8 blocks wide). |
| `cadence.learnPointsTimeFreeze` | 100 | Learn points required for Time Freeze mode. |
| `cadence.learnPointsWhiteLock` | 250 | Learn points required for White Lock mode. |
| `cadence.learnPointsBlockAccel` | 2,000 | Learn points required for Block Acceleration mode. |
| `cadence.timeFreezeCooldownSeconds` | 30 | Cooldown in seconds for Time Freeze. |
| `cadence.timeFreezePulseDurationTicks` | 60 | Duration in ticks for one Time Freeze pulse. |
| `cadence.whiteLockCooldownSeconds` | 45 | Cooldown in seconds for White Lock. |
| `cadence.blockAccelCooldownSeconds` | 20 | Cooldown in seconds for placing Block Acceleration. |
| `cadence.blockAccelBonusRandomTicks` | 19 | Block accel bonus random ticks |
| `cadence.timeControlSnowflakesPerTick` | 8 | Time Control snowflake spawn density (0 disables) |
| `cadence.timeFreezeSnowflakesPerTick` | 12 | Time Freeze: snowflake spawn density (0 disables) |

## Tags

`tensura:skills/patient`
