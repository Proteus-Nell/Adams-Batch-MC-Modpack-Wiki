# Diamond Path

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

![Diamond Path](../../../assets/icons/tensura/skill/diamond_path.png)

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `tensura:diamond_path` |
| **Kind** | Utility |
| **Activation** | Toggle, Press |

</div>

> Harden your aura around you to block incoming attacks.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 150 |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect

## Obtaining

- Listed in the `battlewillManualList` config option (config/tensura/ability/ability_config.toml): List of Battlewills that can be randomly obtained from using the Battlewill Manual.

## Related

- **Effects:** [Diamond Path](../../effects/diamond-path.md)

## Stats (config defaults)

Set in [`config/tensura/ability/battlewill_config.toml`](../../configs/config-tensura-ability-battlewill-config.md).

| Option | Default | Description |
|---|---|---|
| `DiamondPath.auraCost` | 150 | Aura Cost to activate. |
| `DiamondPath.effectTime` | 1,200 | How long in tick that Diamond Path will stay on user after activated. |
| `DiamondPath.effectTimeMastered` | 3,600 | How long in tick that Diamond Path will stay on user after activated while mastered. |
| `DiamondPath.damageBoost` | 10 | How much attack damage that the user gains after activated (doubled when Mastered). |
| `DiamondPath.knockBackResistanceBoost` | 0.4 | How much knockback resistance that the user gains after activated (doubled when Mastered). |

## Tags

`tensura:skills/battlewill`, `tensura:skills/rare_manual_dwarf_trade`
