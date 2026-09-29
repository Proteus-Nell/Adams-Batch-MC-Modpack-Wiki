# Malleable

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Malleable](../../../assets/icons/mysticism/skill/malleable.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:malleable` |
| **Modes** | 3 |
| **Cooldowns (s)** | 10, 30 mastered, 60 otherwise |
| **Activation** | Press, Hold |

</div>

> Malleable like clay, the tides of fate are yours to mold to your desire. Your body seems to work like the metal of a forge, hardening and relaxing under pressure, as you merge yourself with the elements around you.

## Modes

| # | Mode |
|---|---|
| 1 | Alchemy |
| 2 | Harden |
| 3 | Vessel |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Adjusted by scrolling while active
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Attack Damage | -1 | multiply total |
| Movement Speed | -1 | multiply total |
| Armor | 10 | add |

## Related

- **Related skills:** [Flame Attack Resistance](../../../tensura-reincarnated/abilities/resistance-skills/flame-attack-resistance.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Malleable.mpAcquirement` | 50,000 | Magicule Acquirement Cost. |
| `Malleable.learningPoint` | 4 | The bonus learning points gained towards Earth-type abilities AND Resist-type skills when the skill is toggled on. |
| `Malleable.masteryPoint` | 4 | The bonus mastery points gained towards Earth-type abilities AND Resist-type skills when the skill is toggled on. |
| `Malleable.alchemyDuration` | 200 | The duration of the Alchemy mode in ticks when the skill is NOT mastered. |
| `Malleable.alchemyCooldown` | 10 | The cooldown of the Alchemy mode in seconds. |
| `Malleable.alchemyToggleableMastery` | true | If true, Alchemy becomes toggleable on mastery. If false, it follows a cooldown that you can change below. |
| `Malleable.alchemyCooldownMastered` | 10 | The cooldown of the Alchemy mode in seconds when the skill is mastered. |
| `Malleable.hardenCooldown` | 120 | The cooldown of the Harden mode in seconds. |
| `Malleable.hardenCooldownMastered` | 60 | The cooldown of the Harden mode in seconds when the skill is mastered. |
| `Malleable.maximumHardenDuration` | 200 | The maximum duration the Harden mode can be used for in ticks (seconds multiplied by 20.) |
| `Malleable.regenerationLevel` | 5 | The level of the respective effects you gain while Harden is active. |
| `Malleable.resistanceLevel` | 2 |  |
| `Malleable.maximumHardenDurationMastery` | 300 | The maximum duration the Harden mode can be used for in ticks (seconds multiplied by 20.) |
| `Malleable.hardenShouldDisableAttack` | true | Should the Harden mode disable attack/movement speed? False if they should not. |
| `Malleable.hardenShouldDisableMovement` | true |  |
| `Malleable.hardenArmorPoints` | 10 | The amount of armor points that should be granted to the user when the Harden mode is used. |
| `Malleable.vesselCooldown` | 60 | The cooldown of the Vessel mode in seconds. |
| `Malleable.vesselCooldownMastered` | 30 | The cooldown of the Vessel mode in seconds. |
| `Malleable.vesselHP` | 50 | The health points given to the Vessel created. |
| `Malleable.vesselArmor` | 10 | The armor points given to the Vessel created. |
| `Malleable.vesselHPMastered` | 200 | The health points given to the Vessel created when the skill is mastered. |
| `Malleable.vesselArmorMastered` | 30 | The armor points given to the Vessel created when the skill is mastered. |

## Tags

`tensura:skills/unique_skills`
