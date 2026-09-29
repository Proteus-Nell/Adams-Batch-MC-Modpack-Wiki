# Stasis

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Stasis](../../../assets/icons/trnightmare/skill/stasis.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:stasis` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 70,000 |
| **Max mastery** | 1,000 |
| **Activation** | Toggle, Press, Hold |

</div>

> Im boutta stasis rn bro

## Modes

| # | Mode |
|---|---|
| 1 | Fixed State |
| 2 | Air Wall |

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

- Through progression, Stasis has evolved into Cadence
- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.
- Listed in the `virtueDominionSkills` config option (config/nightmare/ability/skill/nightmare_ult.toml): Virtue skills that Ultimate Dominion can copy from targets.
- Listed in the `AngelicSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): List of Angelic skills registry names that can be created via Holy Essence consumption. Format: modid:skill_name
- Listed in the `VirtueSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): Virtue unique skill ids for Michael Ultimate Dominion.

## Related

- **Effects:** [Fixed State](../../effects/stasis-fixed-state.md)
- **Summons / entities:** Stasis Air Wall
- **Referenced by:** [Cadence](cadence.md), [Witch's Greed](witches-greed.md), [｢ Leviathan, Lord of Envy ｣](../ultimate-skills/leviathan.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `stasis.epAcquirement` | 70,000 | EP / magicule obtainment cost to acquire Stasis. |
| `stasis.learningCost` | 1,000 | Learning / mastery point cost. |
| `stasis.maxMastery` | 1,000 | Max mastery. |
| `stasis.fixedStateCooldownSeconds` | 60 | Fixed State: cooldown in seconds |
| `stasis.fixedStateDurationTicks` | 600 | Fixed State: effect duration (ticks) |
| `stasis.airWallMagiculePerSecond` | 1,000 | Air Wall: magicules drained per second while held. |
| `stasis.airWallHalfSize` | 2.5 | Air Wall: horizontal half-size of the wall (blocks) |
| `stasis.airWallCenterDistance` | 2.75 | Air Wall: distance in front of the caster (blocks) |
| `stasis.airWallThickness` | 0.35 | Air Wall: thickness along the facing axis (blocks). |

## Tags

`tensura:skills/patient`
