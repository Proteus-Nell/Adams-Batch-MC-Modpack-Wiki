# Spiritualist

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Spiritualist](../../../assets/icons/mysticism/skill/spiritualist.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:spiritualist` |
| **Modes** | 3 |
| **Cooldowns (s)** | 10 mastered, 5 otherwise |
| **Activation** | Toggle, Press, Hold |

</div>

> The souls of the world flock to you, the one who can both see and commune with the dead. Through your knowledge of the occult, harvest souls and use them to empower your attacks.

## Modes

| # | Mode |
|---|---|
| 1 | Summon Scythe |
| 2 | Carve |
| 3 | Enhance |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Summon Scythe | 500 |  |
| Carve | 500 |  |
| Enhance | 1,500 |  |
| other modes | 500 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Adjusted by scrolling while active
- Triggers when you damage a target
- Triggers on melee contact
- Triggers when you take damage

## Related

- **Items:** [Ritual Scythe](../../items/weapons/ritual-scythe.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Spiritualist.mpAcquirement` | 80,000 | Magicule Acquirement Cost. |
| `Spiritualist.summonScytheCost` | 500 | Magicule cost of the Summon Scythe mode. |
| `Spiritualist.carveCost` | 500 | Magicule cost of the Carve mode. |
| `Spiritualist.enhanceCost` | 1,500 | Magicule cost of the Enhance mode. |
| `Spiritualist.carveRange` | 5 | The Range of the Carve mode. |
| `Spiritualist.chantSpeed` | 2 | The chant speed multiplier when toggled. |

## Tags

`tensura:skills/unique_skills`
