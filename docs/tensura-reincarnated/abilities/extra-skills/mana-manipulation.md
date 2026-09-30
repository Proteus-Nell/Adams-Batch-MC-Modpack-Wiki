# Mana Manipulation

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Mana Manipulation](../../../assets/icons/tensura/skill/mana_manipulation.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:mana_manipulation` |
| **Activation** | Toggle |

</div>

> Grant better control on Mana with less magicule cost on casted Magics and less damage taken from magicule-based attacks.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect
- Triggers when you take damage

## Obtaining

- Can be learned by: [3 Tailed Fox](../../../ascension/races/three-tail-fox.md), [6 Tailed Fox](../../../ascension/races/six-tail-fox.md), [9 Tailed Fox](../../../ascension/races/nine-tail-fox.md), [Divine Kitsune](../../../ascension/races/divine-kitsune.md), [Kindred Bloodfiend](../../../ascension/races/kindred-bloodfiend.md), [Blood Noble](../../../ascension/races/blood-noble.md), [Elder Bloodfiend](../../../ascension/races/elder-bloodfiend.md), [Progenitor Bloodfiend](../../../ascension/races/progenitor-bloodfiend.md), [Trickster Djinn](../../../ascension/races/trickster-djinn.md), [Phantom Djinn](../../../ascension/races/phantom-djinn.md), [Royal Djinn](../../../ascension/races/royal-djinn.md), [Wishbound Djinn](../../../ascension/races/wishbound-djinn.md), [Primordial Djinn](../../../ascension/races/primordial-djinn.md), [Ascended Djinn](../../../ascension/races/ascended-djinn.md), [Sovereign Djinn](../../../ascension/races/sovereign-djinn.md), [Infinite Djinn](../../../ascension/races/infinite-djinn.md), [Omniversal Djinn](../../../ascension/races/omniversal-djinn.md)
- Listed in the `grantedSkillIds` config option (config/tensuramoreskills-grand.toml): Skill IDs granted by Elfaria. Includes Albis so old Ars Weiss clones stay compatible, magic basics, transforms, senses, chant annulment,...
- Acquisition checks: [Molecular Manipulation](molecular-manipulation.md), [Magic Jamming](magic-jamming.md)

## Related

- **Related skills:** [Molecular Manipulation](molecular-manipulation.md), [Magic Jamming](magic-jamming.md)
- **Summons / entities:** Tensura
- **Referenced by:** [Law Manipulation](law-manipulation.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `ManaManipulation.epAcquirement` | 200,000 | EP Requirement for Learning. |
| `ManaManipulation.magiculeDamageMultiplier` | 0.9 | The input magicule-based damage multiplier that user takes when toggled. |
| `ManaManipulation.magicCostReduction` | 0.1 | The magicule cost reduction multiplier on the user's magics when toggled. |
| `ManaManipulation.magicCostReductionMastered` | 0.2 | The magicule cost reduction multiplier on the user's magics when toggled with mastery. |

Set in [`config/tensura/ability/ability_config.toml`](../../configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/extra_skills`
