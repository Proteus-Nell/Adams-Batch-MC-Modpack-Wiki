# Universal Shapeshift

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `trnightmare:universal_shapeshift` |
| **Modes** | 5 |
| **Cooldowns (s)** | 1,200 |
| **Activation** | Press, Hold |

</div>

> A mastered form of Mimicry that grants full control over one's shape and presence.

## Modes

| # | Mode |
|---|---|
| 1 | Form Manipulation |
| 2 | Discover |
| 3 | Shapeshift |
| 4 | Size Manipulation |
| 5 | Chimera Transformation |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| scaleAttr | mod | multiply total |

## Related

- **Related skills:** [Gluttony](../../../tensura-reincarnated/abilities/unique-skills/gluttony.md), [Mimicry](mimicry.md), [｢ Beelzebuth, Lord of Gluttony ｣](../ultimate-skills/beelzebuth.md), [｢ Azathoth, God of The Void ｣](../ultimate-skills/azathoth.md)
- **Effects:** [Chimera Form](../../effects/chimera-form.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_extra.toml`](../../configs/config-nightmare-ability-skill-nightmare-extra.md).

| Option | Default | Description |
|---|---|---|
| `UniversalShapeshift.learnRequired` | 5 | Learn-progress required per discover pulse. |
| `UniversalShapeshift.allowUniqueAndUltimate` | false | Whether unique/ultimate skills can be copied. |
| `UniversalShapeshift.chimeraDuration` | 6,000 | Chimera Transformation duration in ticks (non-mastered). |
| `UniversalShapeshift.chimeraDurationMastered` | 7,200 | Chimera Transformation duration in ticks (mastered). |
| `UniversalShapeshift.chimeraCooldown` | 24,000 | Chimera Transformation cooldown in ticks. |

## In-game messages

<details markdown><summary>Show 6 messages</summary>

- Chimera Transformation activated!
- Chimera Transformation is on cooldown.
- Requires mastery and Gluttony, Beelzebuth, or Azathoth.
- Scale set to %s%%
- Form Manipulation: ON
- Form Manipulation: OFF

</details>

## Tags

`tensura:skills/no_plundering`
