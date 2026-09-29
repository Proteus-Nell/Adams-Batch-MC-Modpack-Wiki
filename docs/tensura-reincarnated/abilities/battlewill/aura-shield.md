# Aura Shield

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

![Aura Shield](../../../assets/icons/tensura/skill/aura_shield.png)

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `tensura:aura_shield` |
| **Kind** | Utility |
| **Cooldowns (s)** | 3 mastered, 5 otherwise |
| **Activation** | Hold |

</div>

> Create a shield of condensed aura to block attacks.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 1,000 |

## How it works

- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Sold by dwarf traders (high manual)
- Listed in the `battlewillManualList` config option (config/tensura/ability/ability_config.toml): List of Battlewills that can be randomly obtained from using the Battlewill Manual.

## Related

- **Summons / entities:** [Aura Shield](aura-shield.md)

## Stats (config defaults)

Set in [`config/tensura/ability/battlewill_config.toml`](../../configs/config-tensura-ability-battlewill-config.md).

| Option | Default | Description |
|---|---|---|
| `AuraShield.auraCost` | 1,000 | Aura Cost to activate. |
| `AuraShield.size` | 3 | The size in blocks of the created shield gets. |
| `AuraShield.health` | 100 | How much Health that the created shield gets. |
| `AuraShield.cooldown` | 5 | The cooldown in second of the battlewill. |
| `AuraShield.cooldownMastered` | 3 | The cooldown in second of the battlewill when mastered. |

## Tags

`tensura:skills/battlewill`, `tensura:skills/high_manual_dwarf_trade`
