# Five Petals Thrust

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

![Five Petals Thrust](../../../assets/icons/tensura/skill/five_petals_thrust.png)

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `tensura:five_petals_thrust` |
| **Kind** | Melee |
| **Activation** | Hold |

</div>

> Dash and pierce the opponent in five of ten vital points and uses the other five as feints.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 8,000 |

## How it works

- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when you take damage
- Does something when mastered

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Movement Speed | -0.75 | multiply total |

## Obtaining

- Innate to mobs: [Gazel Dwargo](../../mobs/gazel-dwargo.md)

## Related

- **Related skills:** [Eight Petals Flash](eight-petals-flash.md)
- **Summons / entities:** Hazy Blossom

## Stats (config defaults)

Set in [`config/tensura/ability/battlewill_config.toml`](../../configs/config-tensura-ability-battlewill-config.md).

| Option | Default | Description |
|---|---|---|
| `FivePetalsThrust.auraCost` | 8,000 | Aura Cost to activate. |
| `FivePetalsThrust.chargingSpeed` | 0.25 | Speed multiplier when charging the attack. |
| `FivePetalsThrust.chargeTick` | 80 | The charge duration in tick of the attack. |
| `FivePetalsThrust.dashDistance` | 15 | The distance in block of the dash attack. |
| `FivePetalsThrust.dashDamage` | 100 | The damage of the dash attack. |
| `FivePetalsThrust.blossomPetal` | 5 | The number of petals (melee damage negation times) of the blossom. |
| `FivePetalsThrust.blossomDuration` | 1,200 | The duration in tick of the blossom after the dash attack. |
| `FivePetalsThrust.bonusChargeTick` | 160 | The bonus charge duration in tick of the attack when mastered. |
| `FivePetalsThrust.bonusDamage` | 25 | The bonus damage of the attack per each bonus charged second when mastered. |
| `FivePetalsThrust.bonusCost` | 1,500 | The bonus Aura Cost of the attack per each bonus charged second when mastered. |

## Tags

`tensura:skills/battlewill`
