# Forbidden Magic

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Other Magic](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Other Magic |
| **ID** | `trnightmare:forbidden` |
| **Activation** | Hold |

</div>

> A dark magic art that invokes dangerous, forbidden power at great risk.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 5,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Can appear in epic tomes from wizard towers
- Can be found in skill tomes

## Related

- **Summons / entities:** Forbidden Blast Projectile

## Stats (config defaults)

Set in [`config/nightmare/ability/magic/nuclear.toml`](../../configs/config-nightmare-ability-magic-nuclear.md).

| Option | Default | Description |
|---|---|---|
| `Forbidden.castTime` | 4 | Cast time in seconds. |
| `Forbidden.magiculeCost` | 5,000 | Magicule Cost to cast. |
| `Forbidden.magicDamage` | 50 | The magic damage of the blast. |
| `Forbidden.magicDamageMastered` | 100 | The magic damage of the blast (Mastered). |
| `Forbidden.shpDamage` | 150 | The soul damage of the blast. |
| `Forbidden.shpDamageMastered` | 250 | The soul damage of the blast (Mastered). |
| `Forbidden.coreDuration` | 4 | The duraction of Core Damage Effect in seconds. |

## Tags

`tensura:skills/epic_tome_wizard_tower`, `tensura:skills/found_in_tome`, `tensura:skills/magic`
