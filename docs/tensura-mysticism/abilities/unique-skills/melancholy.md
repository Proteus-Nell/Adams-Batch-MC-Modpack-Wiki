# Melancholy

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Melancholy](../../../assets/icons/mysticism/skill/melancholy.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:melancholy` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 100,000 |
| **Max mastery** | 1,500 |
| **Cooldowns (s)** | 300, 10 |
| **Activation** | Press, Hold |

</div>

> Summon an aura of sorrow that slows and weakens nearby enemies, filling them with despair. The skill also throws objects or air, amplifying the feeling of hopelessness around you.

> [!NOTE]
> **Pack note:** this pack changes the defaults below.
> - `Melancholy.airThrowDamage` is **4** (mod default: 75)
> - `Melancholy.airThrowDamageMastered` is **6** (mod default: 100)
> - `Melancholy.itemThrowDamage` is **6** (mod default: 125)
> - `Melancholy.itemThrowDamageMastered` is **9** (mod default: 175)

## Modes

| # | Mode |
|---|---|
| 1 | Gust |
| 2 | Turbulent Force |
| 3 | Grief |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 750 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Adjusted by scrolling while active
- Has a continuous (per-tick) effect
- Triggers when you are attacked
- Does something when first learned
- Uses number keys for extra actions

## Obtaining

- Acquisition checks: [Thrower](../../../tensura-reincarnated/abilities/unique-skills/thrower.md), [Molecular Manipulation](../../../tensura-reincarnated/abilities/extra-skills/molecular-manipulation.md)

## Related

- **Related skills:** [Thrower](../../../tensura-reincarnated/abilities/unique-skills/thrower.md), [Molecular Manipulation](../../../tensura-reincarnated/abilities/extra-skills/molecular-manipulation.md), [Burden](../../../tensura-reincarnated/abilities/aspectual-magic/burden.md), [Gravity Domination](../../../tensura-reincarnated/abilities/extra-skills/gravity-domination.md), [Gravity Manipulation](../../../tensura-reincarnated/abilities/extra-skills/gravity-manipulation.md)
- **Effects:** [True Blindness](../../../tensura-reincarnated/effects/true-blindness.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | This pack | Description |
|---|---|---|---|
| `Melancholy.mpAcquirement` | 100,000 | | Magicule Acquirement Cost. |
| `Melancholy.magiculeCost` | 750 | | Flat magicule cost when using Melancholy (per press/activation). |
| `Melancholy.defaultRange` | 15 | | Default targeting range in blocks for Gust. |
| `Melancholy.ishaRange` | 10 | | Range of Ishtar's Tear. |
| `Melancholy.ishaRangeMastered` | 15 | | Range of Ishtar's Tear when the skill is mastered. |
| `Melancholy.ishaLevel` | 4 | | Level of slowness given to entities other than the user. |
| `Melancholy.ishaLevelUser` | 2 | | Level of slowness given to the user. |
| `Melancholy.ishaResistLevel` | 2 | | Level of resistance given to the user. |
| `Melancholy.veilKnockbackRadius` | 12 | | Radius of the Veil mode. |
| `Melancholy.veilSlownessLevel` | 10 | | Level of slowness given to entities when Veil is used. |
| `Melancholy.veilBurdenLevel` | 4 | | Level of slowness given to entities when Veil is used. |
| `Melancholy.griefKnockbackRadius` | 8 | | Radius of the Grief mode. |
| `Melancholy.griefEffectLevel` | 2 | | Level of blindness and weakness given to entities when Grief is used. |
| `Melancholy.maxRange` | 50 | | Maximum adjustable targeting range in blocks. |
| `Melancholy.pushEntity` | 1.4 | | Base push velocity scale applied to entities when using Gust. |
| `Melancholy.pullEntity` | 1.1 | | Base pull velocity scale applied to entities when using Gust while sneaking. |
| `Melancholy.pushEntityManipulation` | 0.25 | | Additional push scale when Gravity Manipulation is toggled. |
| `Melancholy.pushEntityDomination` | 0.45 | | Additional push scale when Gravity Domination is toggled. |
| `Melancholy.pullEntityManipulation` | 0.2 | | Additional pull scale when Gravity Manipulation is toggled. |
| `Melancholy.pullEntityDomination` | 0.4 | | Additional pull scale when Gravity Domination is toggled. |
| `Melancholy.airThrowDamage` | 75 | 4 | The base damage of thrown air. |
| `Melancholy.airThrowDamageMastered` | 100 | 6 | The base damage of thrown air when mastered. |
| `Melancholy.itemThrowDamage` | 125 | 6 | The base damage of thrown items. |
| `Melancholy.itemThrowDamageMastered` | 175 | 9 | The base damage of thrown items when mastered. |
| `Melancholy.itemThrowManipulation` | 1.25 | | Damage multiplier applied to thrown items when Gravity Manipulation is toggled. |
| `Melancholy.itemThrowDomination` | 1.5 | | Damage multiplier applied to thrown items when Gravity Domination is toggled. |

## Tags

`tensura:skills/sin_skills`, `tensura:skills/unique_skills`
