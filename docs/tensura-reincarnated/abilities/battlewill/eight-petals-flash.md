# Eight Petals Flash

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

![Eight Petals Flash](../../../assets/icons/tensura/skill/eight_petals_flash.png)

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `tensura:eight_petals_flash` |
| **Kind** | Melee |
| **Activation** | Hold |

</div>

> Dash and attack the target's eyes, throat, heart, kidneys, lungs, and groin with eight consecutive and near instant slashes.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 10,000 |

## How it works

- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when you take damage

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Movement Speed | -0.75 | multiply total |

## Obtaining

- Innate to mobs: [Gazel Dwargo](../../mobs/gazel-dwargo.md)

## Related

- **Referenced by:** [Five Petals Thrust](five-petals-thrust.md)

## Stats (config defaults)

Set in [`config/tensura/ability/battlewill_config.toml`](../../configs/config-tensura-ability-battlewill-config.md).

| Option | Default | Description |
|---|---|---|
| `EightPetalsFlash.auraCost` | 10,000 | Aura Cost to activate. |
| `EightPetalsFlash.chargingSpeed` | 0.25 | Speed multiplier when charging the attack. |
| `EightPetalsFlash.chargeTick` | 80 | The charge duration in tick of the attack. |
| `EightPetalsFlash.dashDistance` | 20 | The distance in block of the dash attack. |
| `EightPetalsFlash.dashDamage` | 200 | The damage of the dash attack. |
| `EightPetalsFlash.blossomPetal` | 8 | The number of petals (melee damage negation times) of the blossom. |
| `EightPetalsFlash.blossomDuration` | 1,200 | The duration in tick of the blossom after the dash attack. |
| `EightPetalsFlash.bonusChargeTick` | 160 | The bonus charge duration in tick of the attack when mastered. |
| `EightPetalsFlash.bonusDamage` | 50 | The bonus damage of the attack per each bonus charged second when mastered. |
| `EightPetalsFlash.bonusCost` | 2,500 | The bonus Aura Cost of the attack per each bonus charged second when mastered. |
| `EightPetalsFlash.dashPetal` | 4 | The number of petals to consume to reperform the dash attack when mastered. |

## Tags

`tensura:skills/battlewill`
