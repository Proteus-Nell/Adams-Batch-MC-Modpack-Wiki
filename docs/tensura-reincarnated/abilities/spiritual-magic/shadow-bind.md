# Shadow Bind

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Shadow Bind](../../../assets/icons/tensura/skill/shadow_bind.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:shadow_bind` |
| **Element** | Darkness |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Activation** | Hold |

</div>

> If the target is standing in shadows, bind them and deal spiritual damage.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 1,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Removed and re-rolled when you change race

## Related

- **Related skills:** [Darkness Attack Nullification](../resistance-skills/darkness-attack-nullification.md), [Darkness Attack Resistance](../resistance-skills/darkness-attack-resistance.md)
- **Effects:** [Movement Interference](../../effects/movement-interference.md)
- **Referenced by:** [Witch of Envy, Satella](../../../tensura-more-skills/abilities/ultimate-skills/witch-of-envy-satella.md), [Satella](../../../tensura-more-skills/abilities/unique-skills/satella.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `ShadowBind.castTime` | 40 | Cast time in tick. |
| `ShadowBind.castTimeMastered` | 40 | Cast time in tick when mastered. |
| `ShadowBind.magiculeCost` | 1,000 | Magicule Cost to cast. |
| `ShadowBind.range` | 10 | The range in block of the magic. |
| `ShadowBind.bindLevel` | 10 | The level of the Movement Interference effect when the hands catch a target (-10% speed each level). |
| `ShadowBind.bindLevelResisted` | 2 | The level of the Movement Interference effect when the hands catch a target with Darkness Attack Resistance. |
| `ShadowBind.bindDamage` | 10 | The amount of Spiritual damage dealt on targets when applied with the Shadow Bind effect. |
| `ShadowBind.bindDamageMastered` | 0.01 | The bonus multiplier of the target's Spiritual damage dealt when mastered. |
| `ShadowBind.bindDuration` | 200 | The duration of the Shadow Bind effect. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `SpiritualMagic.masteryLesser` | 100 | The max amount of mastery point for Lesser Spiritual Magic. |
| `SpiritualMagic.masteryLesser` | 100 | The max amount of mastery point for Lesser Spiritual Magic. |
| `SpiritualMagic.masteryMedium` | 500 | The max amount of mastery point for Medium Spiritual Magic. |
| `SpiritualMagic.masteryGreater` | 1,000 | The max amount of mastery point for Greater Spiritual Magic. |
| `SpiritualMagic.masteryLord` | 10,000 | The max amount of mastery point for Lord Spiritual Magic. |

## Tags

`tensura:skills/reset_with_race`, `tensura:skills/spiritual_magic`
