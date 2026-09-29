# Mortal Fear

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Mortal Fear](../../../assets/icons/tensura/skill/mortal_fear.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:mortal_fear` |
| **Cooldowns (s)** | 3 mastered, 5 otherwise |
| **Activation** | Press, Hold |

</div>

> Inspire a gripping fear of death in weaker enemies while empowering your allies.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 25 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Adjusted by scrolling while active

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Movement Speed | -0.95 | multiply total |

## Obtaining

- Can be learned by: [Frog Monarch](../../../ascension/races/frog-monarch.md), [Kindred Bloodfiend](../../../ascension/races/kindred-bloodfiend.md), [Blood Noble](../../../ascension/races/blood-noble.md), [Elder Bloodfiend](../../../ascension/races/elder-bloodfiend.md), [Progenitor Bloodfiend](../../../ascension/races/progenitor-bloodfiend.md), [Primordial Djinn](../../../ascension/races/primordial-djinn.md), [Ascended Djinn](../../../ascension/races/ascended-djinn.md), [Sovereign Djinn](../../../ascension/races/sovereign-djinn.md), [Infinite Djinn](../../../ascension/races/infinite-djinn.md), [Omniversal Djinn](../../../ascension/races/omniversal-djinn.md), [Cursed Mariner](../../../ascension/races/cursed-mariner.md), [Cursed Dreadnaught](../../../ascension/races/cursed-dreadnaught.md), [Phantom Corsair](../../../ascension/races/phantom-corsair.md), [Davy Jones](../../../ascension/races/davy-jones.md), [Mindwitness](../../../ascension/races/mindwitness.md), [Gauth](../../../ascension/races/gauth.md), [Beholder](../../../ascension/races/beholder.md), [Death Tyrant](../../../ascension/races/death-tyrant.md), [Dark Lord Dullahan](../../../ascension/races/dark-lord-dullahan.md), [Lich King](../../../ascension/races/lich-king.md)

## Related

- **Referenced by:** [Haki](haki.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `MortalFear.epAcquirement` | 200,000 | EP Requirement for Learning. |
| `MortalFear.epDifferenceMultiplier` | 0.25 | The EP difference multiplier for each Fear Level. |
| `MortalFear.hakiRadius` | 7 | The base radius of the haki in blocks before multiplying with entities' size. |
| `MortalFear.strengthDuration` | 1,200 | The duration in tick of the Strength effect applied on subordinates. |
| `MortalFear.strengthLevel` | 3 | The level of the Strength effect applied on subordinates (+3 Attack Damage per level). |
| `MortalFear.strengthLevelMastered` | 7 | The level of the Strength effect applied on subordinates when mastered. |
| `Haki.speedMultiplier` | 0.05 | Activation Speed Multiplier when activated. |
| `Haki.epAcquirement` | 100,000 | EP Requirement for Learning. |
| `Haki.magiculeCost` | 25 | Magicule Cost to activate. |
| `Haki.speedMultiplier` | 0.05 | Activation Speed Multiplier when activated. |
| `Haki.speedMultiplierMastered` | 0.1 | Activation Speed Multiplier when activated with mastery. |
| `Haki.hakiRadius` | 15 | The attack radius of the haki in blocks. |
| `Haki.epDifferenceMultiplier` | 0.25 | The EP difference multiplier for each Fear Level. |
| `Haki.fearDuration` | 200 | The duration in tick of the Fear effect when applied. |
| `Haki.cooldown` | 5 | The cooldown in second of the haki. |
| `Haki.cooldownMastered` | 3 | The cooldown in second of the haki when mastered. |

Set in [`config/tensura/ability/ability_config.toml`](../../configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/extra_skills`
