# Reshiram

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Reshiram](../../../assets/icons/mysticism/skill/reshiram.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:reshiram` |
| **Modes** | 4 |
| **Acquisition cost (MP)** | 64,300 |
| **Cooldowns (s)** | 5 mastered, 10 otherwise, 20, 10 |
| **Activation** | Toggle, Press, Hold |

</div>

> You seek to build a world of truths. Are you prepared to scorch and burn everything in your path to make the truthful world you seek so badly?

## Modes

| # | Mode |
|---|---|
| 1 | Blue Flare |
| 2 | Fusion Flare |
| 3 | Draconic Meteor |
| 4 | Flamethrower |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Blue Flare | 800 |  |
| Fusion Flare | 700 |  |
| Draconic Meteor | 1,000 |  |
| Flamethrower | 400 |  |
| other modes | 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Acquisition checks: [Zekrom](zekrom.md), [Kyurem](kyurem.md), [Reshiram](reshiram.md), [Flame Essence](../../items/materials/flame-essence.md), [Dragon Essence](../../../tensura-reincarnated/items/materials/dragon-essence.md)

## Related

- **Related skills:** [Zekrom](zekrom.md), [Kyurem](kyurem.md)
- **Items:** [Flame Essence](../../items/materials/flame-essence.md), [Dragon Essence](../../../tensura-reincarnated/items/materials/dragon-essence.md)
- **Summons / entities:** Tensura, Blue Flare Projectile, Draconic Meteor, [Flame Breath](../../../tensura-reincarnated/abilities/intrinsic-skills/flame-breath.md)
- **Referenced by:** [Kyurem](kyurem.md), [Zekrom](zekrom.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Reshiram.epRequirement` | 100,000 | EP Needed to Obtain. |
| `Reshiram.canAcquireWithOtherSkills` | true | Should this skill be acquirable if you have [Zekrom] or [Kyurem]? |
| `Reshiram.blazeEssenceAmount` | 10 | Amount of Blaze Essence needed to be consumed for acquisition. |
| `Reshiram.dragonEssenceAmount` | 10 | Amount of Dragon Essence needed to be consumed for acquisition. |
| `Reshiram.mpAcquirement` | 64,300 | Magicule Acquirement Cost. |
| `Reshiram.flameBoostAmount` | 1.5 | The amount to boost Flame Damage by. |
| `Reshiram.blueFlareMPCost` | 800 | MP Cost of Blue Flare. |
| `Reshiram.blueFlareDamage` | 60 | Damage of Blue Flare. |
| `Reshiram.blueFlareRadius` | 20 | Radius of Blue Flare. |
| `Reshiram.blueFlareCooldown` | 10 | Cooldown of Blue Flare. |
| `Reshiram.blueFlareCooldownMastered` | 5 | Cooldown of Blue Flare when Mastered. |
| `Reshiram.fusionFlareMPCost` | 700 | MP Cost of Fusion Flare. |
| `Reshiram.fusionFlareZekromMPCostBoost` | 2 | MP Cost of Fusion Flare with Zekrom boosted from Original Cost. |
| `Reshiram.fusionFlareDamage` | 200 | Damage of Fusion Flare. |
| `Reshiram.fusionFlareRadius` | 5 | Radius of Fusion Flare. |
| `Reshiram.fusionFlareZekromBonus` | 40 | Damage of Fusion Flare Zekrom Bonus |
| `Reshiram.fusionFlareCooldown` | 20 | Cooldown of Fusion Flare. |
| `Reshiram.draconicMeteorMPCost` | 1,000 | MP Cost of Draconic Meteor. |
| `Reshiram.draconicMeteorDamage` | 70 | Damage of Draconic Meteor. |
| `Reshiram.draconicMeteorExplosionRadius` | 10 | Explosion Radius of Draconic Meteor. |
| `Reshiram.draconicMeteorKnockbackForce` | 5 | Knockback Force of Draconic Meteor. |
| `Reshiram.draconicMeteorCooldown` | 20 | Cooldown of Draconic Meteor. |
| `Reshiram.flamethrowerMPCost` | 400 | MP Cost of Flamethrower. |
| `Reshiram.flamethrowerDamage` | 30 | Damage of Flamethrower. |
| `Reshiram.flamethrowerCooldown` | 10 | Cooldown of Flamethrower. |

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
