# Titanification

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Titanification](../../../assets/icons/tensura/skill/titanification.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `tensura:titanification` |
| **Cooldowns (s)** | 420, 300 |
| **Activation** | Press, Hold |

</div>

> Grow into a towering titan to massively increase your strength, defense, and reach while gaining immunity to magic from weaker foes.

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Adjusted by scrolling while active
- Has a continuous (per-tick) effect
- Triggers when you are attacked
- Triggers when you take damage

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| scale | size ÷ 2 | add |
| armor | 20 | add |
| step | max(size, 0) ÷ 2 | add |
| speed | max(size, 0) × 0.02 | add |
| jump | max(size, 0) × 0.1 | add |
| fall | max(size, 0) | add |
| entityRange | max(size × range, 0) | add |
| blockRange | max(size × range, 0) | add |

## Obtaining

- Intrinsic skill of: [Divine Giant](../../races/divine-giant.md), [Cosmic Deity](../../../ascension/races/cosmic-deity.md), [Chaotic Deity](../../../ascension/races/chaotic-deity.md), [Frog Monarch](../../../ascension/races/frog-monarch.md), [Progenitor Bloodfiend](../../../ascension/races/progenitor-bloodfiend.md), [Primordial Djinn](../../../ascension/races/primordial-djinn.md), [Ascended Djinn](../../../ascension/races/ascended-djinn.md), [Sovereign Djinn](../../../ascension/races/sovereign-djinn.md), [Infinite Djinn](../../../ascension/races/infinite-djinn.md), [Omniversal Djinn](../../../ascension/races/omniversal-djinn.md), [Abyssal Dragonewt](../../../ascension/races/abyssal-dragonewt.md), [Chaos Dragon](../../../ascension/races/chaos-dragon.md), [Death Tyrant](../../../ascension/races/death-tyrant.md), [Sun Wukong](../../../ascension/races/sun-wukong.md)
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Divine Chimera can randomly receive.

## Related

- **Effects:** [Anti-Skill](../../effects/anti-skill.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `Titanification.damage` | 60 | The attack damage buff the user gains when activated. |
| `Titanification.armor` | 20 | The armor buff the user gains when activated. |
| `Titanification.maxSize` | 6 | The maximum size change in block when activated. |
| `Titanification.minSize` | 0 | The minimum size change in block when activated with Mastery. |
| `Titanification.rangeMultiplier` | 1.75 | The interaction range multiplier to apply with size when activated. |
| `Titanification.duration` | 120 | The duration in second that Titanification effect lasts once activated. |
| `Titanification.cooldown` | 300 | The cooldown in second once the effect runs out or deactivated. |

Set in [`config/tensura/ability/skill/resistance_config.toml`](../../configs/config-tensura-ability-skill-resistance-config.md).

| Option | Default | Description |
|---|---|---|
| `nullificationDamageMultiplier` | 0 | The multiplier that will be applied on incoming damage when the damage went through Nullifications |
| `hpDamageBypassResistance` | 0.5 | How many times of current HP that incoming damage value needs to be higher to deal damage to the user with Resistances<br>-1 = always applied regardless of HP |
| `resistanceDamageMultiplier` | 0.5 | The multiplier that will be applied on incoming damage when the damage went through Resistances |
| `hpDamageBypassNullification` | -1 | How many times of current HP that incoming damage value needs to be higher to deal damage to the user with Nullifications<br>-1 = always applied regardless of HP |
| `nullificationDamageMultiplier` | 0 | The multiplier that will be applied on incoming damage when the damage went through Nullifications |
| `damagePointMultiplier` | 10 | The multiplier of learning point requirement for damage points that the skill to reach for 1 learning point |

Set in [`config/tensura/ability/ability_config.toml`](../../configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/intrinsic_skills`
