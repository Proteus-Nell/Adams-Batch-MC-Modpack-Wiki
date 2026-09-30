# Zekrom

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Zekrom](../../../assets/icons/mysticism/skill/zekrom.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:zekrom` |
| **Modes** | 4 |
| **Acquisition cost (MP)** | 64,400 |
| **Cooldowns (s)** | 10 mastered, 20 otherwise, 20, 10 |
| **Activation** | Toggle, Press, Hold |

</div>

> You seek to build a world of ideals. Be warned as not everyone shares the same ideals. Raze anything in your path with a clap of lightning.

## Modes

| # | Mode |
|---|---|
| 1 | Bolt Strike |
| 2 | Fusion Bolt |
| 3 | Draconic Breath |
| 4 | Thunderbolt |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Bolt Strike | 800 |  |
| Fusion Bolt | 800 |  |
| Draconic Breath | 800 |  |
| Thunderbolt | 1,000 |  |
| other modes | 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Acquisition checks: [Zekrom](zekrom.md), [Kyurem](kyurem.md), [Reshiram](reshiram.md), [Dragon Essence](../../../tensura-reincarnated/items/materials/dragon-essence.md), [Lightning Essence](../../items/food/lightning-essence.md)

## Related

- **Related skills:** [Kyurem](kyurem.md), [Reshiram](reshiram.md)
- **Items:** [Dragon Essence](../../../tensura-reincarnated/items/materials/dragon-essence.md), [Lightning Essence](../../items/food/lightning-essence.md)
- **Summons / entities:** Tensura, Lightning Bolt, Draconic Breath
- **Referenced by:** [Kyurem](kyurem.md), [Reshiram](reshiram.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Zekrom.epRequirement` | 100,000 | EP Needed to Obtain. |
| `Zekrom.canAcquireWithOtherSkills` | true | Should this skill be acquirable if you have [Reshiram] or [Kyurem]? |
| `Zekrom.dragonEssenceAmount` | 10 | Amount of Dragon Essence needed to be consumed for acquisition. |
| `Zekrom.lightningEssenceAmount` | 10 | Amount of Lightning Strikes needed to be consumed for acquisition. |
| `Zekrom.mpAcquirement` | 64,400 | Magicule Acquirement Cost. |
| `Zekrom.lightningBoostAmount` | 1.5 | Amount to boost Lightning Damage by. |
| `Zekrom.boltStrikeMPCost` | 800 | MP Cost of Bolt Strike Mode. |
| `Zekrom.boltStrikeDamage` | 150 | Damage of Bolt Strike Mode. |
| `Zekrom.boltStrikeRadius` | 7.5 | Radius of Bolt Strike Mode.. |
| `Zekrom.boltStrikeAdditionalVisual` | 8 | Additional Visual of Bolt Strike. |
| `Zekrom.boltStrikeCooldown` | 20 | Cooldown of Bolt Strike Mode. |
| `Zekrom.boltStrikeCooldownMastered` | 10 | Cooldown of Bolt Strike Mode when Mastered. |
| `Zekrom.fusionBoltMPCost` | 800 | MP Cost of Fusion Bolt Mode. |
| `Zekrom.fusionBoltDamage` | 60 | Damage of Fusion Bolt Mode. |
| `Zekrom.fusionBoltReshiramBonus` | 40 | Bonus Damage if Reshiram in slot. |
| `Zekrom.fusionboltReshiramMPCost` | 2 | MP Cost of Fusion Bolt Mode with Reshiram boosted from Original Cost. |
| `Zekrom.fusionBoltRange` | 15 | Range of Fusion Bolt. |
| `Zekrom.fusionBoltFireDuration` | 5 | Duration of Fire on Target in seconds. |
| `Zekrom.fusionBoltCooldown` | 20 | Fusion Bolt Cooldown. |
| `Zekrom.draconicBreathMPCost` | 800 | MP Cost of Draconic Breath Mode. |
| `Zekrom.draconicBreathDamage` | 60 | Damage of Draconic Breath. |
| `Zekrom.draconicBreathCooldown` | 10 | Cooldown of Draconic Breath Mode. |
| `Zekrom.thunderboltMPCost` | 1,000 | MP Cost of Thunderbolt Mode. |
| `Zekrom.thunderboltDamage` | 100 | Damage of Thunderbolt Mode. |
| `Zekrom.thunderboltRange` | 30 | Range of Thunderbolt in blocks. |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/unique_skills`
