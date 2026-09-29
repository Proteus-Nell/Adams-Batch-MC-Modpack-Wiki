# Demon Dominate

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Demon Dominate](../../../assets/icons/tensura/skill/demon_dominate.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:demon_dominate` |
| **Element** | Mental |
| **Max mastery** | 1,500 |
| **Activation** | Press, Hold |

</div>

> Dominate over any targets up to the Calamity level.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 100,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Can appear in rare tomes in buried wizard towers
- Can appear in rare tomes in burnt wizard towers
- Can appear in rare tomes in frozen wizard towers
- Can appear in rare tomes in rotted wizard towers
- Can appear in rare tomes in ruined wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Related

- **Related skills:** [Dominate](dominate.md), [Spiritual Attack Resistance](../resistance-skills/spiritual-attack-resistance.md)
- **Referenced by:** [Demon Marionette](demon-marionette.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `DemonDominate.castTime` | 100 | Cast time in tick. |
| `DemonDominate.magiculeCost` | 100,000 | Magicule Cost to cast. |
| `DemonDominate.range` | 10 | The range in block of the magic. |
| `DemonDominate.epRequirement` | 200,000 | The amount of EP that the target needs to have below to be controlled. |
| `DemonDominate.resistedRequirement` | 100,000 | The amount of EP that the target needs to have below to be controlled when having Spiritual Attack Resistance toggled. |
| `DemonDominate.controlDuration` | 12,000 | The duration in tick of the Mind Control effect (-1 = permanent). |
| `DemonDominate.controlDurationMastered` | -1 | The duration in tick of the Mind Control effect when mastered (-1 = permanent). |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

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

## Tags

`tensura:skills/aspectual_magic`, `tensura:skills/rare_tome_buried_wizard_tower`, `tensura:skills/rare_tome_burnt_wizard_tower`, `tensura:skills/rare_tome_frozen_wizard_tower`, `tensura:skills/rare_tome_rotted_wizard_tower`, `tensura:skills/rare_tome_ruined_wizard_tower`
