# Freezing Flame

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Freezing Flame](../../../assets/icons/trnightmare/skill/freezing_flame.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:freezing_flame` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 90,000 |
| **Max mastery** | 1,000 |
| **Cooldowns (s)** | 30 |
| **Activation** | Press |

</div>

> Unique flame skill: pyromaniac aspectuals, paradox white fire, After World, and white-flame coating.

## Modes

| # | Mode |
|---|---|
| 1 | After World |
| 2 | White Flame |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| After World | 5,000 |  |
| White Flame | 0 |  |
| other modes | 0 |  |

## How it works

- Activated by pressing the skill key
- Triggers on melee contact
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| atk | bonus | add |

## Related

- **Related skills:** [Spiritual Attack Nullification](../../../tensura-reincarnated/abilities/resistance-skills/spiritual-attack-nullification.md), [Thermal Fluctuation Nullification](../../../tensura-reincarnated/abilities/resistance-skills/thermal-fluctuation-nullification.md)
- **Effects:** [White Flame](../../effects/white-flame.md), [Freezing Burn](../../effects/freezing-burn.md)
- **Referenced by:** [｢ Belial, Lord of The Dead ｣](../ultimate-skills/belial.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `freezingFlame.mpAcquirement` | 90,000 |  |
| `freezingFlame.maxMastery` | 1,000 |  |
| `freezingFlame.coatingDamage` | 50 |  |
| `freezingFlame.coatingDamageMastered` | 100 |  |
| `freezingFlame.magiculeCostAfterWorld` | 5,000 |  |
| `freezingFlame.magiculeCostWhiteFlame` | 0 |  |
