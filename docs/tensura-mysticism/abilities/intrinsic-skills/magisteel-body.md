# Magisteel Body

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Magisteel Body](../../../assets/icons/mysticism/skill/magisteel_body.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `mysticism:magisteel_body` |
| **Activation** | Toggle |

</div>

> Have a body made of magisteel, making it much harder and gaining progressively stronger armor depending on your EP.

## How it works

- Can be toggled on and off

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| armor | ulate armor | add |
| toughness | ulate toughness | add |

## Obtaining

- Listed in the `intrinsicSkills` config option (config/mysticism/race/daemon_doll_config.toml): The list of intrinsic skills that the race gets.

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/intrinsic_config.toml`](../../configs/config-mysticism-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `MagisteelBody.hihiirokaneEP` | 1,000,000 | The amount of EP needed for Hihi'irokane Armor's stats. |
| `MagisteelBody.adamantiteEP` | 500,000 | The amount of EP needed for Adamantite's stats. |
| `MagisteelBody.pureMagisteelEP` | 100,000 | The amount of EP needed for Pure Magisteel's stats. |
| `MagisteelBody.highMagisteelEP` | 50,000 | The amount of EP needed for High Magisteel's stats. |

## Tags

`tensura:skills/intrinsic_skills`, `tensura:skills/no_plundering`
