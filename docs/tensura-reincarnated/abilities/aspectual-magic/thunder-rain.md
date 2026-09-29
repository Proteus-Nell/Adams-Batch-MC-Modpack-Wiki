# Thunder Rain

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Thunder Rain](../../../assets/icons/tensura/skill/thunder_rain.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `tensura:thunder_rain` |
| **Element** | Lightning |
| **Modes** | 2 |
| **Max mastery** | 1,500 |
| **Cooldowns (s)** | 10 |
| **Activation** | Hold |

</div>

> Call forth a wide area of thunder clouds that strike all enemies.

## Modes

| # | Mode |
|---|---|
| 1 | Coating |
| 2 | Rain |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 70,000 |  |

## How it works

- Triggers when the held key is released
- Triggers when you damage a target

## Obtaining

- Sold by dwarf traders (high upgraded tome)
- Can appear in rare tomes in ruined wizard towers
- Listed in the `learnableMagics` config option (config/tensura/race/daemon_config.toml): List of Magics that players automatically get as learnable.

## Related

- **Related skills:** [Thunder](thunder.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/aspectual_config.toml`](../../configs/config-tensura-ability-magic-aspectual-config.md).

| Option | Default | Description |
|---|---|---|
| `ThunderRain.castTime` | 160 | Cast time in tick. |
| `ThunderRain.castTimeMastered` | 100 | Cast time in tick when mastered. |
| `ThunderRain.magiculeCost` | 70,000 | Magicule Cost to cast. |
| `ThunderRain.radius` | 17.5 | The radius in block of the rain. |
| `ThunderRain.thunderDamage` | 300 | The magic damage of each thunder strike. |
| `ThunderRain.thunderInterval` | 80 | The interval in tick between each times thunders struck. |
| `ThunderRain.duration` | 600 | The duration in tick of the rain. |
| `ThunderRain.coatDamage` | 100 | The magic damage of each melee attack from the caster when Coating Mode is casted. |
| `ThunderRain.coatNumber` | 5 | The number of melee attacks will be coated in thunder when Coating Mode is casted. |
| `ThunderRain.cooldown` | 10 | The cooldown in second when casted. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/high_upgraded_tome_dwarf_trade`, `tensura:skills/rare_tome_ruined_wizard_tower`
