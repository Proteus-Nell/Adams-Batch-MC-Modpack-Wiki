# Body Double

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Body Double](../../../assets/icons/tensura/skill/body_double.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:body_double` |
| **Modes** | 2 |
| **Cooldowns (s)** | 1 mastered, 3 otherwise |
| **Activation** | Press |

</div>

> Use a tenth of your magical power to summon an identical clone which takes increased damage but will fight for you until the end. The user can exchange places with the clone but risk taking increased damage.

## Modes

| # | Mode |
|---|---|
| 1 | Clone Creation |
| 2 | Clone Control |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | base max MP × 0.1 ÷ 5 |  |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you die
- Triggers when you respawn
- Triggers when one of your subordinates dies

## Obtaining

- Can be learned by: [Cursed Dreadnaught](../../../ascension/races/cursed-dreadnaught.md), [Phantom Corsair](../../../ascension/races/phantom-corsair.md), [Davy Jones](../../../ascension/races/davy-jones.md)
- Innate to mobs: [Ifrit](../../mobs/ifrit.md)
- Acquisition checks: [Doppelganger](../aspectual-magic/doppelganger.md)

## Related

- **Related skills:** [Doppelganger](../aspectual-magic/doppelganger.md)
- **Effects:** [Fragility](../../effects/fragility.md), [Energy Blockade](../../effects/energy-blockade.md)
- **Referenced by:** [Hive King](../../../tr-nightmares/abilities/ultimate-skills/hive-king.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `BodyDouble.epAcquirement` | 100,000 | EP Requirement for Learning. |
| `BodyDouble.cloneEP` | 0.1 | The EP multiplier of the user's maximum Magicule that a body double will have. |
| `BodyDouble.originalBodyRadius` | 50 | The radius in block that the user needs to stay near the Original Body when controlling a clone. |
| `BodyDouble.originalBodyDamage` | 0.1 | The multiplier of max health and spiritual health that the use loses every 5 second when controlling a clone too far away from the Original Body. |
| `BodyDouble.cloneHeal` | 2 | The amount of HP that a clone heals each second. |
| `BodyDouble.cloneHealEnergy` | 20 | The amount of Energy that a clone uses each second when healing. |
| `BodyDouble.cloneFragility` | 2 | The level of Fragility to given to a clone or the user has when controlling a clone. |
| `BodyDouble.cooldown` | 3 | The cooldown in second to spawn a clone. |
| `BodyDouble.cooldownMastered` | 1 | The cooldown in second to spawn a clone when mastered. |

## Tags

`tensura:skills/extra_skills`
