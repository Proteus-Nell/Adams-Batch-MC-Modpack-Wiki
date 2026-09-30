# All-seeing Eye

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![All-seeing Eye](../../../assets/icons/tensura/skill/all_seeing_eye.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:all_seeing_eye` |
| **Activation** | Toggle, Press, Hold |

</div>

> Go into a 3rd person mode, with your increased POV you gain movement and action buffs as well as an upgrade to Presence Sense.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 10 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Attack Speed | 0.1 | add |
| Movement Speed | 0.02 | add |
| Block Break Speed | 0.02 | add |
| Swim Speed Multiplier | 0.5 | add |
| Presence Sense | 1 | add |
| Presence Sense Radius | 10 | add |
| melee | 10 | add |
| projectile | 10 | add |
| invulnerability | 1 | add |

## Obtaining

- Can be learned by: [Lich King](../../../ascension/races/lich-king.md)
- Innate to mobs: [Kyoya Tachibana](../../mobs/kyoya-tachibana.md)

## Related

- **Summons / entities:** Tensura

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `AllSeeingEye.epAcquirement` | 5,000 | EP Requirement for Learning. |
| `AllSeeingEye.attackSpeed` | 0.1 | The Attack Speed Boost when activated. |
| `AllSeeingEye.movementSpeed` | 0.02 | The Movement Speed Boost when activated. |
| `AllSeeingEye.swimSpeed` | 0.5 | The Swim Speed Multiplier Boost when activated. |
| `AllSeeingEye.miningSpeed` | 0.02 | The Mining Speed Boost when activated. |
| `AllSeeingEye.presenceSense` | 1 | The Presence Sense Boost when activated. |
| `AllSeeingEye.presenceRadius` | 10 | The Presence Sense Radius Boost when activated. |
| `AllSeeingEye.boostMultiplierMastered` | 2 | The Boost Multiplier when mastered. |
| `AllSeeingEye.meleeDodge` | 10 | The Melee Dodge Chance when mastered. |
| `AllSeeingEye.projectileDodge` | 10 | The Projectile Dodge Chance when mastered. |
| `AllSeeingEye.dodgeInvulnerability` | 1 | The bonus dodge invulnerability when toggled. |

Set in [`config/tensura/ability/ability_config.toml`](../../configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/extra_skills`
