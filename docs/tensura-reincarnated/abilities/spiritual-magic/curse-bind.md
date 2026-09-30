# Curse Bind

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Curse Bind](../../../assets/icons/tensura/skill/curse_bind.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:curse_bind` |
| **Element** | Necromancy |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Cooldowns (s)** | 1 mastered, 3 otherwise |
| **Activation** | Hold |

</div>

> Call forth spirits of the death to bind and corrode targets.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 80,000 |  |

## How it works

- Triggers when the held key is released

## Obtaining

- Can appear in rare tomes in rotted wizard towers

## Related

- **Related skills:** [Curse](curse.md)
- **Effects:** [Paralysis](../../effects/paralysis.md), [Corrosion](../../effects/corrosion.md)
- **Summons / entities:** Curse Bind Hands
- **Referenced by:** [Curse](curse.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `CurseBind.castTime` | 120 | Cast time in tick. |
| `CurseBind.castTimeMastered` | 100 | Cast time in tick when mastered. |
| `CurseBind.magiculeCost` | 80,000 | Magicule Cost to cast. |
| `CurseBind.range` | 20 | The range in block of the magic. |
| `CurseBind.paralysisLevel` | 3 | The level of the Paralysis effect to apply on trapped targets. |
| `CurseBind.damageInterval` | 40 | The damage interval in tick of the Curse Bind. |
| `CurseBind.bindDamage` | 100 | The amount of Magic damage dealt on trapped targets. |
| `CurseBind.bindDamageMastered` | 150 | The amount of Magic damage dealt on trapped targets. |
| `CurseBind.curseInterval` | 100 | The curse interval in tick of the Curse Bind. |
| `CurseBind.curseLevel` | 1 | The level of the Curse effect to add/increase on trapped targets every curse interval. |
| `CurseBind.curseDuration` | 600 | The duration in tick of the Curse effect to add/increase on trapped targets every curse interval. |
| `CurseBind.corrosionLevel` | 1 | The level of the Corrosion effect to add/increase on trapped targets every curse interval. |
| `CurseBind.bindDuration` | 400 | The duration of the Curse Bind. |
| `CurseBind.cooldown` | 3 | The cooldown in second of the magic. |
| `CurseBind.cooldownMastered` | 1 | The cooldown in second of the magic when mastered. |

Set in [`config/tensura/ability/ability_config.toml`](../../configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Learning.learningFailCooldown` | 3 | The number of seconds of cooldown when a new ability fails to gain a learning point. |
| `Learning.learningPoint` | 1 | The base value of how many learning points the player gains when learning an ability. |
| `Learning.minBonus` | 0 | The min bonus learning points the player can gain when learning an ability. |
| `Learning.maxBonus` | 4 | The max bonus learning points the player can gain when learning an ability. |
| `Learning.learningCostMultiplier` | 5 | The multiplier of energy cost compared to normal cost when learning a new ability. |
| `Learning.learningPointRequirement` | 100 | The number of learning points a new ability need to get to become fully learnt. |
| `Learning.learningCooldown` | 10 | The number of seconds of cooldown when a new ability gains a learning point. |
| `Learning.learningFailCooldown` | 3 | The number of seconds of cooldown when a new ability fails to gain a learning point. |
| `Learning.failingPenaltyChance` | 0.1 | The chance to the failing penalty to apply. |
| `Learning.failingPenaltyLevel` | 1 | The level of the misfire status effect when failing penalty applies. |
| `Learning.failingPenaltyDuration` | 200 | The duration in ticks of the misfire status effect when failing penalty applies. |
| `Learning.failingPenaltyMin` | 1 | The min learning points the player can lose when failing to learn an ability. |
| `Learning.failingPenaltyMax` | 3 | The max learning points the player can lose when failing to learn an ability. |
| `battlewillManualList` | "tensura:aura_slash", "tensura:aura_sword", "tensura:earthshatter_kick", "tensura:ogre_sword_guillotine", "tensura:roaring_lion_punch", "tensura:dark_eight_palms", "tensura:elephant_stampede", "tensura:magic_bullet", "tensura:ogre_flame", "tensura:air_flight", "tensura:aura_shield", "tensura:battlewill", "tensura:diamond_path", "tensura:formhide", "tensura:instant_move", "tensura:violent_break" | List of Battlewills that can be randomly obtained from using the Battlewill Manual. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `SpiritualMagic.masteryLesser` | 100 | The max amount of mastery point for Lesser Spiritual Magic. |
| `SpiritualMagic.masteryLesser` | 100 | The max amount of mastery point for Lesser Spiritual Magic. |
| `SpiritualMagic.masteryMedium` | 500 | The max amount of mastery point for Medium Spiritual Magic. |
| `SpiritualMagic.masteryGreater` | 1,000 | The max amount of mastery point for Greater Spiritual Magic. |
| `SpiritualMagic.masteryLord` | 10,000 | The max amount of mastery point for Lord Spiritual Magic. |

## Tags

`tensura:skills/necromancy_magic`, `tensura:skills/rare_tome_rotted_wizard_tower`, `tensura:skills/spiritual_magic`
