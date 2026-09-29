# Crocodile Skin

<small>[Elite Tensura](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Crocodile Skin](../../../assets/icons/elitetensura/skill/crocodile_skin.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `elitetensura:crocodile_skin` |
| **Acquisition cost (MP)** | 1,000 |
| **Activation** | Toggle |

</div>

> Transforms your skin into one of crocodile scales which become tougher as you gain more EP (Has a Cap)

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| var3 | var2 (a) | add |
| var4 | var2 (b) | add |

## Obtaining

- Acquisition checks: [Dragon Skin](../../../tensura-reincarnated/abilities/intrinsic-skills/dragon-skin.md)

## Related

- **Related skills:** [Dragon Skin](../../../tensura-reincarnated/abilities/intrinsic-skills/dragon-skin.md)
- **Referenced by:** [Basilisk Skin](../ultimate-skills/basiliskskin-ultimate.md)

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/UniqueSkillConfig.toml`](../../configs/config-tensura-elitetensura-uniqueskillconfig.md).

| Option | Default | Description |
|---|---|---|
| `CrocodileSkin.IsEnabled` | true | Is this Skill Enabled? When false it can never be acquired. |
| `CrocodileSkin.epTierPureMagisteel` | 100,000 | Max EP at which the armour becomes Pure Magisteel (below: High Magisteel). |
| `CrocodileSkin.epTierAdamantite` | 500,000 | Max EP at which the armour becomes Adamantite. |
| `CrocodileSkin.epTierHihiirokane` | 900,000 | Max EP at which the armour becomes Hihiirokane. |

## Tags

`tensura:skills/no_plundering`, `tensura:skills/unique_skills`
