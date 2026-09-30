# Absorb &amp; Dissolve

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Absorb &amp; Dissolve](../../../assets/icons/tensura/skill/absorb_and_dissolve.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `tensura:absorb_and_dissolve` |
| **Activation** | Press |

</div>

> Dissolve specific items to instantly consume them.

## How it works

- Activated by pressing the skill key

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| width | new width | add |
| health | amount ÷ bonus × 5 | add |

## Obtaining

- Intrinsic skill of: [Slime](../../races/slime.md), [Metal Slime](../../races/metal-slime.md), [Demon Slime](../../races/demon-slime.md), [God Slime](../../races/god-slime.md), [Lesser Saiyan](../../../elite-tensura/races/lesser-saiyan.md), [Medium Class Saiyan](../../../elite-tensura/races/medium-saiyan.md), [High Class Saiyan](../../../elite-tensura/races/high-saiyan.md), [Divine Saiyan](../../../elite-tensura/races/divine-saiyan.md)
- Innate to mobs: [Metal Slime](../../mobs/metal-slime.md), [Slime](../../mobs/slime.md), [Supermassive Slime](../../mobs/supermassive-slime.md)
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Lesser Chimera can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Greater Chimera can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Golden Chimera can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Chimera Lord can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Divine Chimera can randomly receive.
- Listed in the `intrinsicSkills` config option (config/nightmare/race/axolotl/salamander_config.toml): List of skills obtained by this race.
- Listed in the `intrinsicSkills` config option (config/nightmare/race/axolotl/axolotl_config.toml): List of skills obtained by this race.

## Related

- **Items:** [Slime Core](../../items/materials/slime-core.md)
- **Summons / entities:** Tensura

## Stats (config defaults)

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `AbsorbDissolve.magiculeMultiplier` | 1 | The multiplier of magicule gained from dissolving items. |
| `AbsorbDissolve.healthMultiplier` | 1 | The multiplier of health healed from dissolving items. |
| `AbsorbDissolve.bonusHP` | 5 | The bonus max HP that Slime players can get from each Slime Core used to increase their size. |
| `AbsorbDissolve.bonusSize` | 0.1 | The bonus max size that Slime players can get from each Slime Core used to increase their size. |
| `AbsorbDissolve.maxSize` | 0.75 | The max bonus size that Slime players can get from consuming Slime Cores. |

## Tags

`tensura:skills/intrinsic_skills`
