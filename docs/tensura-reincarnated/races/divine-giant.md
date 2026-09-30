# Divine Giant

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensura:divine_giant` |
| **Stage** | <span class="stage stage-final">Final</span> |
| **Difficulty** | Easy |
| **Alignment** | Majin |
| **Aura** | 1,000,000 - 1,000,000 |
| **Magicule** | 1,000,000 - 1,000,000 |
| **Health bonus** | 1,080 |
| **Spiritual health bonus** | 6,940 |
| **Attack damage bonus** | 14 |
| **Movement speed bonus** | 0.05 |
| **EP to evolve into** | 2,000,000 |

</div>

> A godly race born from the earth itself, possessing an immortal physical body that will never age.

## Evolution

- **Evolves from:** [Ancient Giant](ancient-giant.md)

### Requirements to evolve into Divine Giant

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 2,000,000 | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Ancient Giant"]
  r1["Divine Giant"]
  r2["Giant"]
  r0 --> r1
  r2 --> r0
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/divine_ki_release.png) [Divine Ki Release](../abilities/intrinsic-skills/divine-ki-release.md)
- ![](../../assets/icons/tensura/skill/titanification.png) [Titanification](../abilities/intrinsic-skills/titanification.md)
- ![](../../assets/icons/tensura/skill/ultraspeed_regeneration.png) [Ultraspeed Regeneration](../abilities/extra-skills/ultraspeed-regeneration.md)
- ![](../../assets/icons/tensura/skill/giantification.png) [Giantification](../abilities/intrinsic-skills/giantification.md)
- ![](../../assets/icons/tensura/skill/steel_strength.png) [Steel Strength](../abilities/extra-skills/steel-strength.md)
- ![](../../assets/icons/tensura/skill/strengthen_body.png) [Strengthen Body](../abilities/extra-skills/strengthen-body.md)
- ![](../../assets/icons/tensura/skill/magic_resistance.png) [Magic Resistance](../abilities/resistance-skills/magic-resistance.md)

## Traits

- Divine

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0.5 | add |
| Max Health | 1,080 | add |
| Max Spiritual Health | 6,940 | add |
| Attack Damage | 14 | add |
| Attack Speed | 0 | add |
| Knockback Resistance | 1 | add |
| Movement Speed | 0.05 | add |
| Swim Speed Multiplier | 0.5 | add |

## Stats (config defaults)

Set in [`config/tensura/race/giant_config.toml`](../configs/config-tensura-race-giant-config.md).

| Option | Default | Description |
|---|---|---|
| `DivineGiant.epRequirement` | 2,000,000 | EP requirement to evolve into Divine Giant. |
| `DivineGiant.minAura` | 1,000,000 | Minimal aura. |
| `DivineGiant.maxAura` | 1,000,000 | Maximum aura. |
| `DivineGiant.minMagicule` | 1,000,000 | Minimal magicule. |
| `DivineGiant.maxMagicule` | 1,000,000 | Maximum magicule. |
| `DivineGiant.size` | 0.5 | Bonus Size. |
| `DivineGiant.maxHealth` | 1,080 | Bonus Max Health. |
| `DivineGiant.maxSpiritualHealth` | 6,940 | Bonus Max Spiritual Health. |
| `DivineGiant.attack` | 14 | Bonus Attack Damage. |
| `DivineGiant.attackSpeed` | 0 | Bonus Attack Speed. |
| `DivineGiant.knockbackResistance` | 1 | Bonus Knockback Resistance. |
| `DivineGiant.movementSpeed` | 0.05 | Bonus Movement Speed. |
| `DivineGiant.swimSpeed` | 0.5 | Bonus Swimming Speed Multiplier. |
| `DivineGiant.armorDurability` | 0.5 | How much of the attack damage that Giant will inflict on targets' armor durability. |
| `AncientGiant.epRequirement` | 300,000 | EP requirement to evolve into Ancient Giant. |
| `AncientGiant.debrisRequirement` | 20 | The number of Ancient Debris needed to evolve into Ancient Giant. |
| `AncientGiant.minAura` | 150,000 | Minimal aura. |
| `AncientGiant.maxAura` | 150,000 | Maximum aura. |
| `AncientGiant.minMagicule` | 150,000 | Minimal magicule. |
| `AncientGiant.maxMagicule` | 150,000 | Maximum magicule. |
| `AncientGiant.size` | 0.5 | Bonus Size. |
| `AncientGiant.maxHealth` | 480 | Bonus Max Health. |
| `AncientGiant.maxSpiritualHealth` | 640 | Bonus Max Spiritual Health. |
| `AncientGiant.attack` | 7 | Bonus Attack Damage. |
| `AncientGiant.attackSpeed` | -0.25 | Bonus Attack Speed. |
| `AncientGiant.knockbackResistance` | 0.8 | Bonus Knockback Resistance. |
| `AncientGiant.movementSpeed` | 0.03 | Bonus Movement Speed. |
| `AncientGiant.swimSpeed` | 0.3 | Bonus Swimming Speed Multiplier. |
| `AncientGiant.armorDurability` | 0.25 | How much of the attack damage that Giant will inflict on targets' armor durability. |
| `Giant.minAura` | 4,000 | Minimal aura. |
| `Giant.maxAura` | 6,000 | Maximum aura. |
| `Giant.minMagicule` | 6,000 | Minimal magicule. |
| `Giant.maxMagicule` | 8,000 | Maximum magicule. |
| `Giant.size` | 0.5 | Bonus Size. |
| `Giant.maxHealth` | 30 | Bonus Max Health. |
| `Giant.maxSpiritualHealth` | 140 | Bonus Max Spiritual Health. |
| `Giant.attack` | 5 | Bonus Attack Damage. |
| `Giant.attackSpeed` | -0.5 | Bonus Attack Speed. |
| `Giant.knockbackResistance` | 0.4 | Bonus Knockback Resistance. |
| `Giant.movementSpeed` | 0 | Bonus Movement Speed. |
| `Giant.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |

## Tags

`tensura:races/divine`
