# Hecate

<small>[Elite Tensura](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Hecate](../../../assets/icons/elitetensura/skill/hecate.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `elitetensura:hecate` |
| **Modes** | 1 |
| **Acquisition cost (MP)** | 0 |
| **Cooldowns (s)** | 60 |
| **Activation** | Toggle |

</div>

> The goddess of magic. While held, the magicule cost of nearly every spell is floored to its minimum (Reincarnation excluded). Toggle on for chant annulment, thought acceleration, +1 learning &amp; mastery, and bonus damage with all spells.

## Modes

| # | Mode |
|---|---|
| 1 | Default |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 50 |  |

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect
- Triggers when you damage a target

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| var3 | 1 | add |
| var4 | 1 | add |

## Related

- **Summons / entities:** Tensura

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/UniqueSkillConfig.toml`](../../configs/config-tensura-elitetensura-uniqueskillconfig.md).

| Option | Default | Description |
|---|---|---|
| `Hecate.inSlotCostMultiplier` | 0.1 | In-slot passive: multiplier applied to every spell's magicule cost (0.0 = floored to free/minimum). Blacklisted spells (see costFloorBlacklist) keep their normal cost. |
| `Hecate.costFloorBlacklist` | "tensura:reincarnation" | Spell registry IDs excluded from the in-slot cost floor (kept at full cost). |
| `Hecate.magiculeCostPerTick` | 50 | Magicule drained per tick while the toggle is active. |
| `Hecate.learningPoint` | 1 | Bonus learning gain (ADD_VALUE) while toggled. |
| `Hecate.masteryPoint` | 1 | Bonus mastery gain (ADD_VALUE) while toggled. |
| `Hecate.passiveLearningBonus` | 1 | In-slot passive: flat bonus to learning-point gain for Magic (spells) only, always active while Hecate is slotted (stacks with the toggle's learningPoint bonus). |
| `Hecate.passiveMasteryBonus` | 1 | In-slot passive: flat bonus to mastery-point gain for Magic (spells) only, always active while Hecate is slotted (stacks with the toggle's masteryPoint bonus). |
| `Hecate.spellDamageBonus` | 30 | Flat bonus damage added to all spell (magic) damage while toggled. |
| `Hecate.spellDamageBonusMastered` | 75 | Flat bonus spell damage while toggled, when Hecate is mastered. |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/no_plundering`, `tensura:skills/unique_skills`
