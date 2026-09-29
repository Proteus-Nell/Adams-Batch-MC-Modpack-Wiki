# Violent Break

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

![Violent Break](../../../assets/icons/tensura/skill/violent_break.png)

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `tensura:violent_break` |
| **Kind** | Utility |
| **Activation** | Hold |

</div>

> Channel your aura, recklessly enhancing your strength and cleansing you of any negative effects.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 150 |

## How it works

- Charged or channelled by holding the skill key

## Obtaining

- Intrinsic skill of: [Dark Fairy](../../../tr-nightmares/races/dark-fairy.md), [One Eyed God](../../../tr-nightmares/races/one-eyed-god.md)
- Sold by dwarf traders (low manual)
- Listed in the `battlewillManualList` config option (config/tensura/ability/ability_config.toml): List of Battlewills that can be randomly obtained from using the Battlewill Manual.

## Related

- **Effects:** [Strengthen](../../effects/strengthen.md)
- **Referenced by:** [Maximum Will](../../../tr-nightmares/abilities/battlewill/maximum-will.md), [Phainon, The Deliverer](../../../tensura-more-skills/abilities/ultimate-skills/phainon.md)

## Stats (config defaults)

Set in [`config/tensura/ability/battlewill_config.toml`](../../configs/config-tensura-ability-battlewill-config.md).

| Option | Default | Description |
|---|---|---|
| `ViolentBreak.auraCost` | 150 | Aura Cost to activate. |
| `ViolentBreak.holdTime` | 60 | The Hold Time in Tick to activate. |
| `ViolentBreak.strengthenTime` | 1,200 | The Strengthen Time in Tick when activated. |
| `ViolentBreak.strengthenLevel` | 1 | The Strengthen Level when activated (doubled when Mastered). |
| `ViolentBreak.effectToRemove` | "minecraft:bad_omen", "minecraft:nausea", "minecraft:weakness", "minecraft:blindness", "minecraft:hunger", "minecraft:poison", "minecraft:darkness", "minecraft:mining_fatigue", "minecraft:levitation", "minecraft:slowness", "minecraft:unluck", "minecraft:wither", "tensura:burden", "tensura:chill", "tensura:fragility", "tensura:silence", "tensura:corrosion", "tensura:fatal_poison", "tensura:infection", "tensura:paralysis" ... (21 total) | The List of harmful effects that get removed upon activation. |

## Tags

`tensura:skills/battlewill`, `tensura:skills/low_manual_dwarf_trade`
