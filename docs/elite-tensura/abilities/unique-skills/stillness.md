# Stillness

<small>[Elite Tensura](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Stillness](../../../assets/icons/elitetensura/skill/stillness.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `elitetensura:stillness` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 1,000 |
| **Cooldowns (s)** | 60, 180 or 300 |
| **Activation** | Toggle, Press |

</div>

> Meditation perfected. Serenity regenerates aura, magicules and spiritual health at twice the rate; Inner Calm instantly restores a portion of your maximum pools on a long cooldown.

## Modes

| # | Mode |
|---|---|
| 1 | Serenity |
| 2 | Inner Calm |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 30 or 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| var0 | var1 | add |

## Related

- **Related skills:** [Mediation](../extra-skills/meditation.md)

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/UniqueSkillConfig.toml`](../../configs/config-tensura-elitetensura-uniqueskillconfig.md).

| Option | Default | Description |
|---|---|---|
| `Stillness.enabled` | true | Master enable. When false the skill can never be acquired. |
| `Stillness.epAcquirement` | 50,000 | Max EP required to evolve Meditation into Stillness. |
| `Stillness.bossKillsRequired` | 3 | Total boss kills required (Tensura bossesCounter bosses + world calamities). |
| `Stillness.magiculeCost` | 30 | Magicule drained per tick while Serenity is toggled on. |
| `Stillness.regenRate` | 1 | Aura/magicule/SHP regeneration added while Serenity is active (Meditation is 0.5). |
| `Stillness.regenRateMastered` | 1.5 | Serenity regeneration when mastered. |
| `Stillness.restorePercent` | 25 | Inner Calm: percent of MAX magicule and aura restored instantly (0-100). |
| `Stillness.restorePercentMastered` | 40 | Inner Calm restore percent when mastered. |
| `Stillness.calmCooldownSeconds` | 300 | Inner Calm cooldown in SECONDS. |
| `Stillness.calmCooldownMasteredSeconds` | 180 | Inner Calm cooldown in SECONDS when mastered. |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## In-game messages

<details markdown><summary>Show 1 messages</summary>

- Inner Calm — your energies surge back.

</details>

## Tags

`tensura:skills/no_plundering`, `tensura:skills/unique_skills`
