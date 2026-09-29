# Profaned Prominence

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Profaned Prominence](../../../assets/icons/mysticism/skill/profaned_prominence.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `mysticism:profaned_prominence` |
| **Modes** | 2 |
| **Cooldowns (s)** | 10 mastered, 20 otherwise |
| **Activation** | Toggle, Press, Hold |

</div>

> Command your absolute authority over Acceleration, allowing you to inflict all enemies with fire and spew superheated flames. Additionally, melt the surroundings into magma.

## Modes

| # | Mode |
|---|---|
| 1 | Fire Breath |
| 2 | Providence |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Fire Breath | 500 |  |
| Providence | 1,000 |  |
| other modes | 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers on melee contact

## Obtaining

- Listed in the `intrinsicSkills` config option (config/mysticism/race/wyrm_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/direwolf/special_direwolf_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Related skills:** [Flame Breath](../../../tensura-reincarnated/abilities/intrinsic-skills/flame-breath.md)

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/extra_config.toml`](../../configs/config-mysticism-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `ProfanedProminence.fireBreathMPCost` | 500 | Magicule cost for Fire Breath. |
| `ProfanedProminence.damage` | 16 | The damage each second of the Fire Breath. |
| `ProfanedProminence.damageMastered` | 32 | The damage each second of the Fire Breath when mastered. |
| `ProfanedProminence.providenceMPCost` | 1,000 | Magicule cost for Providence. |
| `ProfanedProminence.radius` | 8 | The radius of Providence. |
| `ProfanedProminence.providenceCooldownMastered` | 10 | The cooldown of Providence when it's mastered. |
| `ProfanedProminence.providenceCooldown` | 20 | The cooldown of Providence. |
| `ProfanedProminence.profanedProminenceBoost` | 1.5 | The Fire Damage Boost when Profaned Prominence is toggled. |
| `ProfanedProminence.prominenceBurnTick` | 300 | How long in tick that the target will be set on fire when attacked with Prominence's Toggle (doubled with Mastery). |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

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
