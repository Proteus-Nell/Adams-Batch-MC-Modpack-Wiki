# Berserker

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Berserker](../../../assets/icons/tensura/skill/berserker.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:berserker` |
| **Acquisition cost (MP)** | 40,000 |
| **Cooldowns (s)** | 10 |
| **Activation** | Toggle, Hold |

</div>

> Feed on your enemies' defeat. Gain EP from kills, destroy equipment faster, and boost your physical stats based on your power level.

## How it works

- Can be toggled on and off
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect
- Triggers on melee contact
- Triggers when you take damage

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| aura | 2 | add |
| magicule | 2 | add |
| damage | e p (attack) × 2 mastered, e p (attack) otherwise | add |
| speed | e p (speed) ÷ 100 | add |

## Obtaining

- Innate to mobs: [Shogo Taguchi](../../mobs/shogo-taguchi.md)
- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Related

- **Referenced by:** [Pride Manas](../../../tr-nightmares/abilities/ultimate-skills/pride-manas.md), [Phainon, The Deliverer](../../../tensura-more-skills/abilities/ultimate-skills/phainon.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Berserker.mpAcquirement` | 40,000 | Magicule Acquirement Cost. |
| `Berserker.auraPercentage` | 2 | The bonus Aura percentage the user gains when toggled on. |
| `Berserker.magiculePercentage` | 2 | The bonus Magicule percentage the user gains when toggled on. |
| `Berserker.armorDurability` | 0.25 | How much of the attack damage that Berserker will inflict on targets' armor durability. |
| `Berserker.weaponDurability` | 5 | How much durability that Berserker will take from attackers' weapon when attacking the user. |
| `Berserker.holdTime` | 40 | The Hold Time in Tick to activate Berserker. |
| `Berserker.armorEP` | 20,000 | How much EP the user needs to have for each armor point. |
| `Berserker.armorMax` | 100 | The maximum amount of armor point that the user can gain. |
| `Berserker.attackBase` | 5 | The base attack point the user gain when activated. |
| `Berserker.attackEP` | 40,000 | How much EP the user needs to have for each additional attack point. |
| `Berserker.attackMax` | 55 | The maximum amount of armor point that the user can gain (every bonus attack point is doubled with mastery). |
| `Berserker.speedEP` | 25,000 | How much EP the user needs to have for each additional speed point. |
| `Berserker.speedMax` | 40 | The maximum amount of armor point that the user can gain. |

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

`tensura:skills/sadistic`, `tensura:skills/unique_skills`
