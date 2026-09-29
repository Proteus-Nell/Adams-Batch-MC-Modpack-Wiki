# Nihilistic Banish

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Other Magic](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Other Magic |
| **ID** | `trnightmare:nihilistic_banish` |
| **Activation** | Hold |

</div>

> A dark magic that expels targets with nihil-aligned banishment force.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 575,000 mastered, 850,000 otherwise |  |

## How it works

- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Can be found in skill tomes

## Related

- **Effects:** [Movement Interference](../../../tensura-reincarnated/effects/movement-interference.md)
- **Summons / entities:** Nihilistic Banish Entity

## Stats (config defaults)

Set in [`config/nightmare/ability/magic/nuclear.toml`](../../configs/config-nightmare-ability-magic-nuclear.md).

| Option | Default | Description |
|---|---|---|
| `NihilisticBanish.castTime` | 10 | Cast time in seconds. |
| `NihilisticBanish.castTimeMastered` | 5 | Cast time in seconds (Mastered). |
| `NihilisticBanish.magiculeCost` | 850,000 | Magicule Cost to cast. |
| `NihilisticBanish.magiculeCostMastered` | 575,000 | Magicule Cost to cast (Mastered). |
| `NihilisticBanish.magicDamage` | 2,800 | Burst magic damage dealt at the end of banishment. |
| `NihilisticBanish.shpDamage` | 800 | Spiritual damage dealt every second during banishment. |

## Tags

`tensura:skills/found_in_tome`, `tensura:skills/magic`
