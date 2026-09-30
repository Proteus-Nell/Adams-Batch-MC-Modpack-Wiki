# Divine Saiyan

<small>[Elite Tensura](../index.md) &rsaquo; [Races](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `elitetensura:divine_saiyan` |
| **Stage** | <span class="stage stage-final">Final</span> |
| **Difficulty** | Extreme |
| **Alignment** | Default |
| **Aura** | 1,000,000 - 1,000,000 |
| **Magicule** | 1,000,000 - 1,000,000 |
| **Health bonus** | 980 |
| **Spiritual health bonus** | 6,000 |
| **Attack damage bonus** | 10 |
| **Movement speed bonus** | 0.05 |
| **EP to evolve into** | 1,000,000 |

</div>

## Evolution

- **Evolves from:** [High Class Saiyan](high-saiyan.md)

### Requirements to evolve into Divine Saiyan

Each requirement adds its weight to the evolution progress bar; you can evolve at 100%.

| Requirement | Weight |
|---|---|
| Reach Existence Points of 1,000,000 | 100% |

### Evolution tree

```mermaid
flowchart LR
  r0["Divine Saiyan"]
  r1["High Class Saiyan"]
  r2["Lesser Saiyan"]
  r3["Medium Class Saiyan"]
  r1 --> r0
  r2 --> r1
  r2 --> r3
  r3 --> r1
```

## Intrinsic skills

Granted automatically when you become this race.

- ![](../../assets/icons/tensura/skill/haki.png) [Haki](../../tensura-reincarnated/abilities/extra-skills/haki.md)
- ![](../../assets/icons/tensura/skill/divine_ki_release.png) [Divine Ki Release](../../tensura-reincarnated/abilities/intrinsic-skills/divine-ki-release.md)
- ![](../../assets/icons/tensura/skill/dragon_eye.png) [Dragon Eye](../../tensura-reincarnated/abilities/intrinsic-skills/dragon-eye.md)
- ![](../../assets/icons/tensura/skill/dragon_skin.png) [Dragon Skin](../../tensura-reincarnated/abilities/intrinsic-skills/dragon-skin.md)
- ![](../../assets/icons/tensura/skill/dragon_ear.png) [Dragon Ear](../../tensura-reincarnated/abilities/intrinsic-skills/dragon-ear.md)
- ![](../../assets/icons/tensura/skill/body_armor.png) [Body Armor](../../tensura-reincarnated/abilities/intrinsic-skills/body-armor.md)
- ![](../../assets/icons/tensura/skill/charm.png) [Charm](../../tensura-reincarnated/abilities/intrinsic-skills/charm.md)
- ![](../../assets/icons/tensura/skill/sage.png) [Sage](../../tensura-reincarnated/abilities/extra-skills/sage.md)
- ![](../../assets/icons/tensura/skill/absorb_and_dissolve.png) [Absorb &amp; Dissolve](../../tensura-reincarnated/abilities/intrinsic-skills/absorb-and-dissolve.md)

## Attribute modifiers

| Attribute | Amount | Operation |
|---|---|---|
| Scale | 0 | add |
| Max Health | 980 | add |
| Max Spiritual Health | 6,000 | add |
| Attack Damage | 10 | add |
| Attack Speed | 3 | add |
| Knockback Resistance | 1 | add |
| Movement Speed | 0.05 | add |
| Swim Speed Multiplier | 1 | add |

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/Races.toml`](../configs/config-tensura-elitetensura-races.md).

| Option | Default | Description |
|---|---|---|
| `divineSaiyan.minAura` | 1,000,000 | Minimal aura. |
| `divineSaiyan.maxAura` | 1,000,000 | Maximum aura. |
| `divineSaiyan.minMagicule` | 1,000,000 | Minimal magicule. |
| `divineSaiyan.maxMagicule` | 1,000,000 | Maximum magicule. |
| `divineSaiyan.size` | 0 | Bonus Size. |
| `divineSaiyan.maxHealth` | 980 | Bonus Max Health. |
| `divineSaiyan.maxSpiritualHealth` | 6,000 | Bonus Max Spiritual Health. |
| `divineSaiyan.attack` | 10 | Bonus Attack Damage. |
| `divineSaiyan.attackSpeed` | 3 | Bonus Attack Speed. |
| `divineSaiyan.knockbackResistance` | 1 | Bonus Knockback Resistance. |
| `divineSaiyan.movementSpeed` | 0.05 | Bonus Movement Speed. |
| `divineSaiyan.swimSpeed` | 1 | Bonus Swimming Speed Multiplier. |
| `divineSaiyan.epRequirement` | 1,000,000 |  |
| `highSaiyan.minAura` | 40,000 | Minimal aura. |
| `highSaiyan.maxAura` | 40,000 | Maximum aura. |
| `highSaiyan.minMagicule` | 100,000 | Minimal magicule. |
| `highSaiyan.maxMagicule` | 100,000 | Maximum magicule. |
| `highSaiyan.size` | 0 | Bonus Size. |
| `highSaiyan.maxHealth` | 25 | Bonus Max Health. |
| `highSaiyan.maxSpiritualHealth` | 10 | Bonus Max Spiritual Health. |
| `highSaiyan.attack` | 3.75 | Bonus Attack Damage. |
| `highSaiyan.attackSpeed` | 1 | Bonus Attack Speed. |
| `highSaiyan.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `highSaiyan.movementSpeed` | 0.02 | Bonus Movement Speed. |
| `highSaiyan.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `highSaiyan.epRequirement` | 500,000 |  |
| `mediumSaiyan.minAura` | 6,000 | Minimal aura. |
| `mediumSaiyan.maxAura` | 10,000 | Maximum aura. |
| `mediumSaiyan.minMagicule` | 12,000 | Minimal magicule. |
| `mediumSaiyan.maxMagicule` | 20,000 | Maximum magicule. |
| `mediumSaiyan.size` | 0 | Bonus Size. |
| `mediumSaiyan.maxHealth` | 12 | Bonus Max Health. |
| `mediumSaiyan.maxSpiritualHealth` | 5 | Bonus Max Spiritual Health. |
| `mediumSaiyan.attack` | 2 | Bonus Attack Damage. |
| `mediumSaiyan.attackSpeed` | 0.5 | Bonus Attack Speed. |
| `mediumSaiyan.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `mediumSaiyan.movementSpeed` | 0.01 | Bonus Movement Speed. |
| `mediumSaiyan.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `mediumSaiyan.epRequirement` | 100,000 |  |
| `lesserSaiyan.epRequirement` | 0 | EP required to enter this race (starter tier — 0 = no gate). |
| `lesserSaiyan.minAura` | 2,000 | Minimal aura. |
| `lesserSaiyan.maxAura` | 3,000 | Maximum aura. |
| `lesserSaiyan.minMagicule` | 5,000 | Minimal magicule. |
| `lesserSaiyan.maxMagicule` | 6,000 | Maximum magicule. |
| `lesserSaiyan.size` | 0 | Bonus Size. |
| `lesserSaiyan.maxHealth` | 5 | Bonus Max Health. |
| `lesserSaiyan.maxSpiritualHealth` | 10 | Bonus Max Spiritual Health. |
| `lesserSaiyan.attack` | 0.5 | Bonus Attack Damage. |
| `lesserSaiyan.attackSpeed` | 0 | Bonus Attack Speed. |
| `lesserSaiyan.knockbackResistance` | 0 | Bonus Knockback Resistance. |
| `lesserSaiyan.movementSpeed` | 0 | Bonus Movement Speed. |
| `lesserSaiyan.swimSpeed` | 0 | Bonus Swimming Speed Multiplier. |
| `lesserSaiyan.learnableMagics` | "tensura:earth_lock", "tensura:liquidize", "tensura:fire_aspectual", "tensura:water_aspectual", "tensura:drainage", "tensura:wind_gust", "tensura:escape", "tensura:freeze" |  |
