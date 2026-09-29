# Thought Acceleration

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Thought Acceleration](../../../assets/icons/tensura/skill/thought_acceleration.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:thought_acceleration` |
| **Activation** | Toggle |

</div>

> Increase the speed at which you think to cast magic more quickly as well as to increase your reaction speed.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| chantSpeed | 2 | add |
| invulnerability | 1 | add |
| speed | 0.02 mastered, 0.01 otherwise | add |
| attackSpeed | 0.4 mastered, 0.2 otherwise | add |

## Obtaining

- Can be learned by: [Cosmic Deity](../../../ascension/races/cosmic-deity.md), [Chaotic Deity](../../../ascension/races/chaotic-deity.md), [Bog Ancient](../../../ascension/races/bog-ancient.md), [Frog Monarch](../../../ascension/races/frog-monarch.md), [6 Tailed Fox](../../../ascension/races/six-tail-fox.md), [9 Tailed Fox](../../../ascension/races/nine-tail-fox.md), [Divine Kitsune](../../../ascension/races/divine-kitsune.md), [Royal Djinn](../../../ascension/races/royal-djinn.md), [Wishbound Djinn](../../../ascension/races/wishbound-djinn.md), [Primordial Djinn](../../../ascension/races/primordial-djinn.md), [Ascended Djinn](../../../ascension/races/ascended-djinn.md), [Sovereign Djinn](../../../ascension/races/sovereign-djinn.md), [Infinite Djinn](../../../ascension/races/infinite-djinn.md), [Omniversal Djinn](../../../ascension/races/omniversal-djinn.md), [Davy Jones](../../../ascension/races/davy-jones.md), [Abyssal Dragonewt](../../../ascension/races/abyssal-dragonewt.md), [Chaos Dragon](../../../ascension/races/chaos-dragon.md), [Spectator](../../../ascension/races/spectator-gazer.md), [Mindwitness](../../../ascension/races/mindwitness.md), [Gauth](../../../ascension/races/gauth.md), [Beholder](../../../ascension/races/beholder.md), [Death Tyrant](../../../ascension/races/death-tyrant.md), [Monkey King](../../../ascension/races/monkey-king.md), [Divine King](../../../ascension/races/divine-king.md), [Sun Wukong](../../../ascension/races/sun-wukong.md), [Mage Skeleton](../../../ascension/races/mage-skeleton.md), [Elder Lich](../../../ascension/races/elder-lich.md), [Lich](../../../ascension/races/lich.md), [Lich King](../../../ascension/races/lich-king.md)
- Innate to mobs: [Kyoya Tachibana](../../mobs/kyoya-tachibana.md)

## Related

- **Summons / entities:** Tensura
- **Referenced by:** [｢ Hastur, Lord of Starwind ｣](../../../tr-nightmares/abilities/ultimate-skills/hastur.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `ThoughtAcceleration.epAcquirement` | 8,000 | EP Requirement for Learning. |
| `ThoughtAcceleration.chantSpeed` | 2 | The chant speed multiplier when activated. |
| `ThoughtAcceleration.movementSpeed` | 0.01 | The bonus movement speed when activated. |
| `ThoughtAcceleration.movementSpeedMastered` | 0.02 | The bonus movement speed when activated with mastery. |
| `ThoughtAcceleration.attackSpeed` | 0.2 | The bonus movement speed when activated. |
| `ThoughtAcceleration.attackSpeedMastered` | 0.4 | The bonus movement speed when activated with mastery. |
| `ThoughtAcceleration.dodgeInvulnerability` | 1 | The bonus dodge invulnerability when toggled. |

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

`tensura:skills/extra_skills`
