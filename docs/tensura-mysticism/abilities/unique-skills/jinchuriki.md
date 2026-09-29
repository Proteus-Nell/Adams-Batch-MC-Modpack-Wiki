# Jinchuriki

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Jinchuriki](../../../assets/icons/mysticism/skill/jinchuriki.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:jinchuriki` |
| **Modes** | 2 |
| **Activation** | Toggle, Press, Hold |

</div>

> That voice... It's familiar, yet something so distant. Another side of you, perhaps. But it's something that can be controlled. Provided you have the right tenacity to do it.

## Modes

| # | Mode |
|---|---|
| 1 | Tailed Beast Bomb |
| 2 | Tailed Beast Cloak |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| mpGain | amount | add |
| apGain | amount | add |

## Related

- **Effects:** [Tailed Beast Cloak](../../effects/tailed-beast-cloak.md)
- **Summons / entities:** [Uncontrolled Jinchuriki](../../mobs/uncontrolled-jinchuriki.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Jinchuriki.mpAcquirement` | 95,000 | Magicule Acquirement Cost. |
| `Jinchuriki.epGainIncrease` | 6 | The EP gain increase the user receives while the skill is toggled on. |
| `Jinchuriki.epGainIncreaseMastered` | 11 | The EP gain increase the user receives while the skill is toggled on when the skill is mastered. |
| `Jinchuriki.cloakPreControlLifespan` | 30 | The time that the Tailed Beast Cloak lasts before gaining control over it, in seconds. |
| `Jinchuriki.tailedBeastCloakCooldown` | 60 | The cooldown of the Tailed Beast Cloak mode, in seconds. |
| `Jinchuriki.tailedBeastCloakCooldownMastered` | 30 | The cooldown of the Tailed Beast Cloak mode when the skill is mastered, in seconds. |
| `Jinchuriki.v1Cloak` | 10 | The number of uses to progress to the v1 Cloak. |
| `Jinchuriki.v2Cloak` | 100 | The number of uses to progress to the v2 Cloak. |
| `Jinchuriki.controlledState` | 250 | The number of uses to progress to the Controlled State. |
| `Jinchuriki.perfectControlledState` | 1,000 | The number of uses to achieve Perfect Control State. |
| `Jinchuriki.mpCostPerCharge` | 800 | Magicule cost for each 1.0 of charge for the Tailed Beast Bomb. |
| `Jinchuriki.apCostPerCharge` | 200 | Aura cost for each 1.0 of charge for the Tailed Beast Bomb. |
| `Jinchuriki.maxMultiplier` | 100 | The Max Charge of the Tailed Beast Bomb. |
| `Jinchuriki.maxMultiplierMastered` | 150 | The Max Charge of the Tailed Beast Bomb when Mastered. |
| `Jinchuriki.holdTime` | 20 | Ticks the user must hold to gain 1.0 charge (20 = 1 second). |
| `Jinchuriki.holdTimeMastered` | 10 | Ticks the user must hold to gain 1.0 charge when Mastered (10 = 0.5 second). |
| `Jinchuriki.baseDamage` | 6 | Damage dealt per 1.0 charge (6 per 1.0 = 30 per 5.0). |
| `Jinchuriki.explosionThreshold` | 3 | The bomb explodes on impact only if charged past this amount. |
| `Jinchuriki.explosionDamage` | 150 | Damage of the explosion at the impact zone. |
| `Jinchuriki.explosionBaseRadius` | 3 | Base explosion radius once the explosion threshold is passed. |
| `Jinchuriki.explosionRadiusPer10Charge` | 2 | Explosion radius increase for each 10.0 of charge. |

## Tags

`tensura:skills/unique_skills`
