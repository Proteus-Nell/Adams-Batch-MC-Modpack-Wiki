# Acceleration

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:acceleration` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 150,000 |
| **Max mastery** | 3,000 |
| **Activation** | Toggle, Hold |

</div>

> Compress and amplify flame into devastating heat. Toggle Scorching Flames (+4 flame boost); grants heat and flame nullification. Hold Burning Breath, Bloody Lava, or Superheating.

## Modes

| # | Mode |
|---|---|
| 1 | Scorching Flames |
| 2 | Burning Breath |
| 3 | Bloody Lava |

## How it works

- Can be toggled on and off
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when you damage a target
- Triggers when an effect is applied to you
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| flameBoost | 4 | add |
| attr | mult - 1 | multiply total |

## Related

- **Related skills:** [Heat Nullification](../../../tensura-reincarnated/abilities/resistance-skills/heat-nullification.md), [Flame Attack Nullification](../../../tensura-reincarnated/abilities/resistance-skills/flame-attack-nullification.md)
- **Effects:** [Magicule Poison](../../../tensura-reincarnated/effects/magicule-poison.md)
- **Summons / entities:** Melting Heated Beam

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `acceleration.mpAcquirement` | 150,000 |  |
| `acceleration.maxMastery` | 3,000 |  |
| `acceleration.scorchingFlameDamage` | 25 |  |
| `acceleration.scorchingFlameDamageMastered` | 50 |  |
| `acceleration.burningBreathFlameDamage` | 25 |  |
| `acceleration.burningBreathFlameDamageMastered` | 50 |  |
| `acceleration.burningBreathSpiritDamage` | 50 |  |
| `acceleration.burningBreathSpiritDamageMastered` | 100 |  |
| `acceleration.burningBreathRange` | 105 |  |
| `acceleration.bloodyLavaFlameDamage` | 50 |  |
| `acceleration.bloodyLavaRadius` | 12 |  |
| `acceleration.superheatMpRegenMultiplier` | 4 |  |
| `acceleration.superheatMpRegenMultiplierMastered` | 8 |  |
