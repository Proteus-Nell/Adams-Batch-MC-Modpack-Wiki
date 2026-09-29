# Strengthen Body

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Strengthen Body](../../../assets/icons/tensura/skill/strengthen_body.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:strengthen_body` |
| **Activation** | Toggle |

</div>

> Strengthen your body to better protect yourself against attacks.

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect
- Triggers when you take damage

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| armor | 5 | add |

## Obtaining

- Intrinsic skill of: [Giant](../../races/giant.md), [Ancient Giant](../../races/ancient-giant.md), [Divine Giant](../../races/divine-giant.md)
- Can be learned by: [Monkey Warrior](../../../ascension/races/monkey-warrior.md), [Monkey Martial Artist](../../../ascension/races/monkey-martial-artist.md), [Monkey King](../../../ascension/races/monkey-king.md), [Divine King](../../../ascension/races/divine-king.md), [Sun Wukong](../../../ascension/races/sun-wukong.md), [Skeleton Warrior](../../../ascension/races/skeleton-warrior.md), [Death Knight](../../../ascension/races/death-knight.md), [Dullahan](../../../ascension/races/dullahan.md), [Dark Lord Dullahan](../../../ascension/races/dark-lord-dullahan.md)
- Innate to mobs: [Folgen](../../mobs/folgen.md), [Mark Lauren](../../mobs/mark-lauren.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `StrengthenBody.epAcquirement` | 15,000 | EP Requirement for Learning. |
| `StrengthenBody.bonusArmor` | 5 | The bonus armor amount when activated. |
| `StrengthenBody.inputMultiplier` | 0.8 | The input damage multiplier that the user takes when activated. |

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
