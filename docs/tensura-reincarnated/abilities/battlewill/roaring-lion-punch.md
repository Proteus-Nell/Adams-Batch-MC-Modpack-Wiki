# Roaring Lion Punch

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

![Roaring Lion Punch](../../../assets/icons/tensura/skill/roaring_lion_punch.png)

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `tensura:roaring_lion_punch` |
| **Kind** | Melee |
| **Activation** | Press |

</div>

> Focus your aura into a fearsome blow with the regalness of a lion.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 10 |

## How it works

- Activated by pressing the skill key

## Obtaining

- Listed in the `battlewillManualList` config option (config/tensura/ability/ability_config.toml): List of Battlewills that can be randomly obtained from using the Battlewill Manual.

## Stats (config defaults)

Set in [`config/tensura/ability/battlewill_config.toml`](../../configs/config-tensura-ability-battlewill-config.md).

| Option | Default | Description |
|---|---|---|
| `RoaringLionPunch.auraCost` | 10 | Base Aura Cost to activate. |
| `RoaringLionPunch.maxAuraMultiplier` | 0.1 | The Multiplier compared to user's Max Aura that will be used for the attack. |
| `RoaringLionPunch.maxAuraUsed` | 2,000 | The Maximum amount of Aura can be used for the attack. |
| `RoaringLionPunch.maxAuraUsedMastered` | 4,000 | The Maximum amount of Aura can be used for the attack when mastered. |

## Tags

`tensura:skills/battlewill`
