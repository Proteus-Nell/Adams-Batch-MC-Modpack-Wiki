# Magic Aura

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Magic Aura](../../../assets/icons/tensura/skill/magic_aura.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:magic_aura` |
| **Modes** | 7 |
| **Activation** | Press |

</div>

> Empower your attacks with many elemental aura.

## Modes

| # | Mode |
|---|---|
| 1 | Default |
| 2 | Holy |
| 3 | Earth |
| 4 | Fire |
| 5 | Space |
| 6 | Water |
| 7 | Wind |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 500 or 1,000 |  |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect

## Obtaining

- Listed in the `intrinsicSkills` config option (config/nightmare/race/scholar_config.toml): List of skills obtained by this race.

## Related

- **Effects:** [Magic Aura](../../effects/magic-aura.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `MagicAura.magicMastered` | 7 | The number of Magic needed to be mastered to learn Magic Aura. |
| `MagicAura.magiculeCost` | 500 | Magicule Cost to activate the Default Mode. |
| `MagicAura.magiculeCostElemental` | 1,000 | Magicule Cost to activate other Elemental Modes. |
| `MagicAura.auraDuration` | 6,000 | The duration in tick of the Magic Aura effect when activated. |
| `MagicAura.auraMultiplier` | 0.5 | The damage multiplier for the bonus Aura Damage compared to the user's normal attack damage. |

## Tags

`tensura:skills/extra_skills`
