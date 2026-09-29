# Demon Lord Haki

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Demon Lord Haki](../../../assets/icons/tensura/skill/demon_lord_haki.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:demon_lord_haki` |
| **Modes** | 2 |
| **Cooldowns (s)** | 3 mastered, 5 otherwise |
| **Activation** | Press, Hold |

</div>

> Unleash your Demonic aura causing those around you to quake in fear.

## Modes

| # | Mode |
|---|---|
| 1 | Magicule Release |
| 2 | Magicule Coat |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 100 or 50 |  |

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

- Can be learned by: [Chaotic Deity](../../../ascension/races/chaotic-deity.md), [Abyssal Dragonewt](../../../ascension/races/abyssal-dragonewt.md), [Chaos Dragon](../../../ascension/races/chaos-dragon.md), [Death Tyrant](../../../ascension/races/death-tyrant.md)
- Acquisition checks: [Haki](haki.md)

## Related

- **Related skills:** [Haki](haki.md)
- **Effects:** [Haki Coat](../../effects/haki-coat.md)
- **Referenced by:** [｢ Hastur, Lord of Starwind ｣](../../../tr-nightmares/abilities/ultimate-skills/hastur.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `DemonLordHaki.epAcquirement` | 200,000 | EP Requirement for Learning. |
| `DemonLordHaki.magiculeCost` | 50 | Magicule Cost to activate Magicule Release. |
| `DemonLordHaki.magiculeCostCoat` | 100 | Magicule Cost to activate Haki Coat. |
| `DemonLordHaki.coatDuration` | 2,400 | The duration in tick of the Haki Coat when activated. |
| `DemonLordHaki.epDifferenceMultiplier` | 0.5 | The EP difference multiplier for each Fear Level. |
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

`tensura:skills/extra_skills`, `tensura:skills/has_magicule_rich_haki`
