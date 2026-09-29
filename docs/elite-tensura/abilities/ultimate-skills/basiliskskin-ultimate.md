# Basilisk Skin

<small>[Elite Tensura](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![Basilisk Skin](../../../assets/icons/elitetensura/skill/basiliskskin_ultimate.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `elitetensura:basiliskskin_ultimate` |
| **Acquisition cost (MP)** | 1,000 |
| **Activation** | Toggle |

</div>

> Transforms your skin into one of a Basilisk scales which become tougher as you gain more EP(Cap however easter egg)

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

- Acquisition checks: [Crocodile Skin](../unique-skills/crocodile-skin.md)

## Related

- **Related skills:** [Crocodile Skin](../unique-skills/crocodile-skin.md)

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/UltimateSkillConfig.toml`](../../configs/config-tensura-elitetensura-ultimateskillconfig.md).

| Option | Default | Description |
|---|---|---|
| `BasiliskSkin.IsEnabled` | true | Is this Skill Enabled? When false it can never be acquired. |
| `BasiliskSkin.epTierPureMagisteel` | 200,000 | Max EP at which the armour becomes Pure Magisteel (below: High Magisteel). |
| `BasiliskSkin.epTierAdamantite` | 800,000 | Max EP at which the armour becomes Adamantite. |
| `BasiliskSkin.epTierHihiirokane` | 1,000,000 | Max EP at which the armour becomes Hihiirokane. |

## Tags

`tensura:skills/no_plundering`, `tensura:skills/ultimate_skills`
