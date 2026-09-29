# Deadly Poison

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:deadly_poison` |
| **Modes** | 4 |
| **Acquisition cost (MP)** | 90,000 |
| **Activation** | Toggle, Press, Hold |

</div>

> A unique poison art: stack Lethal Dose, refine toxins, and unleash domain-wide devastation.

## Modes

| # | Mode |
|---|---|
| 1 | Bloody Bite |
| 2 | Poison Refinement |
| 3 | Deadly Domain |
| 4 | Cursed Poison |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when you damage a target
- Triggers on melee contact

## Obtaining

- Listed in the `astralExtraUniqueSkills` config option (config/nightmare/ability/skill/nightmare_ult.toml): Extra unique skill IDs merged into Astral Light Skill Creation (after Tensura Creator).

## Related

- **Referenced by:** [｢ Samael, Lord of Deadly Poison ｣](../ultimate-skills/samael.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `DeadlyPoison.mpAcquirement` | 90,000 |  |
| `DeadlyPoison.cursedPoisonLearnPoints` | 300 |  |

## In-game messages

<details markdown><summary>Show 2 messages</summary>

- Lethal Dose must reach 100% first.
- Poison Refinement  ▶  Lethal Dose: %1$s%%

</details>
