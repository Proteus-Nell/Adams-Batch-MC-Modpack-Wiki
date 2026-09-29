# Schrödinger

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Schrödinger](../../../assets/icons/mysticism/skill/schrodinger.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:schrodinger` |
| **Activation** | Toggle |

</div>

> Is it alive, or is it dead? The only way to find out is to open the box. But since it's a cat, maybe it'll grant you some of its properties.

## How it works

- Can be toggled on and off
- Triggers on melee contact
- Triggers when you die
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| safeFallDistance | 32 | add |

## Related

- **Effects:** [Fatal Poison](../../../tensura-reincarnated/effects/fatal-poison.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Schrodinger.poisonEffectDuration` | 160 | The duration in tick of the poison effect on target when touching them. |

## Tags

`tensura:skills/unique_skills`
