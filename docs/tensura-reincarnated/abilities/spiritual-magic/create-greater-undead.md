# Create Greater Undead

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Spiritual Magic](index.md)</small>

<div class="infobox" markdown>

![Create Greater Undead](../../../assets/icons/tensura/skill/create_greater_undead.png)

| | |
|---|---|
| **Type** | Spiritual Magic |
| **ID** | `tensura:create_greater_undead` |
| **Element** | Necromancy |
| **Modes** | 3 |
| **Max mastery** | 100 / 500 / 1,000 / 10,000 |
| **Activation** | Press, Hold |

</div>

> Call forth armed undead from the ground to aid the caster.

## Modes

| # | Mode |
|---|---|
| 1 | Zombie |
| 2 | Skeleton |
| 3 | Random Undead |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 8,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Can be learned by: [Elder Lich](../../../ascension/races/elder-lich.md), [Lich](../../../ascension/races/lich.md), [Lich King](../../../ascension/races/lich-king.md)
- Can appear in uncommon tomes in rotted wizard towers

## Related

- **Related skills:** [Create Lesser Undead](create-lesser-undead.md)
- **Summons / entities:** [Zombie](../../mobs/zombie.md), [Skeleton](../../mobs/skeleton.md)
- **Referenced by:** [Create Lesser Undead](create-lesser-undead.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/spiritual_config.toml`](../../configs/config-tensura-ability-magic-spiritual-config.md).

| Option | Default | Description |
|---|---|---|
| `CreateGreaterUndead.castTime` | 120 | Cast time in tick. |
| `CreateGreaterUndead.magiculeCost` | 8,000 | Magicule Cost to create each undead. |
| `CreateGreaterUndead.undeadDuration` | 300 | How long in second will the summoned undead will stay. |
| `CreateGreaterUndead.undeadNumber` | 1 | The number of undead getting summoned by the magic. |
| `CreateGreaterUndead.undeadNumberSneak` | 3 | The number of undead getting summoned by the magic when sneaking. |
| `CreateGreaterUndead.undeadNumberSneakMastered` | 6 | The number of undead getting summoned by the magic when sneaking with Mastery. |
| `CreateGreaterUndead.undeadHP` | 100 | The HP that each undead created has. |
| `CreateGreaterUndead.undeadAttack` | 5 | The attack damage that each undead created has. |
| `CreateGreaterUndead.undeadEpBoost` | 5,000 | The EP boost that each undead created has. |
| `CreateGreaterUndead.undeadSharpness` | 1 | The Sharpness level of created Zombie's sword. |
| `CreateGreaterUndead.undeadPower` | 2 | The Power level of created Skeleton's bow. |
| `CreateGreaterUndead.cooldown` | 10 | The cooldown in second of the magic. |
| `CreateGreaterUndead.cooldownMastered` | 5 | The cooldown in second of the magic when mastered. |

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

`tensura:skills/necromancy_magic`, `tensura:skills/spiritual_magic`, `tensura:skills/uncommon_tome_rotted_wizard_tower`
