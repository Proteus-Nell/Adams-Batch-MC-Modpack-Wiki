# Michael, Angel of Locks

<small>[TensuraMoreSkills](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![Michael, Angel of Locks](../../../assets/icons/tensuramoreskills/skill/michael_angel_of_locks.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `tensuramoreskills:michael_angel_of_locks` |
| **Modes** | 8 |
| **Acquisition cost (MP)** | 8,000,000 |
| **Max mastery** | 1,000 |
| **Activation** | Toggle, Press, Hold |

</div>

> An ultimate angelic key that devours prisons and suppressors, crowning space itself with divine locks.

## Modes

| # | Mode |
|---|---|
| 1 | Summon: Key Form |
| 2 | Segva: The Key of Sealing |
| 3 | Lataib: The Key of Unleashing |
| 4 | Lataib: Spatial Storage |
| 5 | Lataib: Severing Space |
| 6 | Shifuru: Key of Release |
| 7 | Jerez: Key of Solution |
| 8 | Keter: Key of Crown |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | *set by config (base cost)* |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Triggers when you damage a target

## Stats (config defaults)

Set in [`config/tensuramoreskills-grand.toml`](../../configs/config-tensuramoreskills-grand.md).

| Option | Default | Description |
|---|---|---|
| `obtainment.acquirementMagiculeCost` | 8,000,000 (0 to no limit) |  |
| `obtainment.acquirementMastery` | 0 (-1 to no limit) |  |
| `obtainment.maxMastery` | 1,000 (1 to no limit) |  |
| `obtainment.requiredSkillId` | "tensura:oppressor" |  |
| `obtainment.requiredSkillMustBeMastered` | false |  |
| `lataib.spatialStorageSlots` | 108 (1 to 216) |  |
| `lataib.spatialStorageStack` | 999 (1 to 999) |  |
