# Elder Soul

<small>[Elite Tensura](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Elder Soul](../../../assets/icons/elitetensura/skill/elder_soul.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `elitetensura:elder_soul` |
| **Modes** | 1 |
| **Acquisition cost (MP)** | 1,000 |
| **Cooldowns (s)** | 60 |
| **Activation** | Toggle |

</div>

> A primordial soul in full bloom. A 40-block aura grants allies Strength III, Regeneration III and Resistance II, Soul Sight reaches further — and every enemy inside the aura is outlined for all your allies to see.

## Modes

| # | Mode |
|---|---|
| 1 | Aura of the Elder |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 4 |  |

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect
- Does something when first learned

## Related

- **Related skills:** [Ancient Soul](../extra-skills/ancient-soul.md)

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/UniqueSkillConfig.toml`](../../configs/config-tensura-elitetensura-uniqueskillconfig.md).

| Option | Default | Description |
|---|---|---|
| `ElderSoul.enabled` | true | Master enable. When false the skill can never be acquired. |
| `ElderSoul.epAcquirement` | 100,000 | Max EP required to evolve Ancient Soul into Elder Soul. |
| `ElderSoul.bossKillsRequired` | 5 | Total boss kills required (Tensura bossesCounter bosses + world calamities). |
| `ElderSoul.magiculeDrainPerTick` | 4 | Magicule drained per tick while the aura is toggled on (Ancient Soul is 2). |
| `ElderSoul.buffRadius` | 40 | Ally-buff aura radius in blocks (Ancient Soul is 25). |
| `ElderSoul.buffRadiusMastered` | 50 | Ally-buff aura radius when mastered. |
| `ElderSoul.soulSightRadius` | 50 | Soul Sight ESP radius in blocks for the holder (covers the mastered aura). |
| `ElderSoul.strengthAmplifier` | 2 | Aura Strength amplifier (2 = Strength III). |
| `ElderSoul.regenAmplifier` | 2 | Aura Regeneration amplifier (2 = Regeneration III). |
| `ElderSoul.resistanceAmplifier` | 1 | Aura Resistance amplifier (1 = Resistance II; Ancient Soul gives I). |
| `ElderSoul.effectDurationTicks` | 120 | Duration in ticks of each aura effect application. Keep &gt;= 100: ManasCore refreshes toggle skills every 100 game ticks. |
| `ElderSoul.refreshIntervalTicks` | 120 | Revealing Presence: glow lease per sweep = this + revealLingerTicks (sweeps run every 100-tick skill tick). |
| `ElderSoul.revealLingerTicks` | 40 | Revealing Presence: ticks an enemy keeps glowing after leaving the aura. |

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
