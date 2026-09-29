# Mithril Strength

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Mithril Strength](../../../assets/icons/mysticism/skill/mithril_strength.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `mysticism:mithril_strength` |
| **Activation** | Toggle, Press |

</div>

> Turn your muscles as hard as Mithril and gain an increase in damage, toggleable when mastered.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 10,000 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect

## Obtaining

- Acquisition checks: [Steel Strength](../../../tensura-reincarnated/abilities/extra-skills/steel-strength.md)

## Related

- **Related skills:** [Steel Strength](../../../tensura-reincarnated/abilities/extra-skills/steel-strength.md)
- **Effects:** [Strengthen](../../../tensura-reincarnated/effects/strengthen.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/extra_config.toml`](../../configs/config-mysticism-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `MithrilStrength.magiculeCost` | 10,000 | Magicule Cost to activate. |
| `MithrilStrength.strengthenDuration` | 1,200 | The duration of the Strengthen effect when activated (doubled when mastered). |
| `MithrilStrength.strengthenLevel` | 3 | The level of the Strengthen effect when activated (+3 Attack Damage per level). |
| `MithrilStrength.strengthenLevelMastered` | 4 | The level of the Strengthen effect when activated when Mastered. |

## Tags

`tensura:skills/extra_skills`
