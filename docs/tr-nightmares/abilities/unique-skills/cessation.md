# Cessation

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Cessation](../../../assets/icons/trnightmare/skill/cadence.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:cessation` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 150,000 |
| **Max mastery** | 1,000 |
| **Activation** | Toggle, Hold |

</div>

> True stillness made manifest. Toggle for Ice Walk (frost-walker freeze); Freeze All halts motion in an area; Ice Wall raises an indestructible barrier — or a Snow Crystal shell with Gabriel or Cthulhu.

## Modes

| # | Mode |
|---|---|
| 1 | Ice Walk |
| 2 | Freeze All |

## How it works

- Can be toggled on and off
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.

## Related

- **Related skills:** [｢ Gabriel, Lord of Patience ｣](../ultimate-skills/gabriel.md), [｢ Cthulhu, King of Divine Ice ｣](../ultimate-skills/cthulhu.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `cessation.mpAcquirement` | 150,000 |  |
| `cessation.maxMastery` | 1,000 |  |
| `cessation.freezeAllHalfWidth` | 4 |  |
| `cessation.freezeAllCooldownSeconds` | 30 |  |
| `cessation.iceWallHeight` | 8 |  |
| `cessation.iceWallThickness` | 3 |  |
| `cessation.snowCrystalHalfSize` | 5 |  |
| `cessation.snowCrystalInteriorHalf` | 3 |  |
