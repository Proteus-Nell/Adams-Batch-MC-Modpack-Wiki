# Mediation

<small>[Elite Tensura](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Mediation](../../../assets/icons/tensura/skill/sage.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `elitetensura:meditation` |
| **Modes** | 1 |
| **Acquisition cost (MP)** | 0 |
| **Cooldowns (s)** | 60 |
| **Activation** | Toggle |

</div>

> Helps regenerate Aura, Magic, and SHP faster when toggled

## Modes

| # | Mode |
|---|---|
| 1 | Default |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Default | 20 | 0 |
| other modes | 0 |  |

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| var3 | 0.5 | add |
| var4 | 0.5 | add |
| var5 | 0.5 | add |

## Related

- **Summons / entities:** Tensura
- **Referenced by:** [Stillness](../unique-skills/stillness.md)

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/ExtraSkillConfig.toml`](../../configs/config-tensura-elitetensura-extraskillconfig.md).

| Option | Default | Description |
|---|---|---|
| `MeditationSkill.enabled` | true | True/False Disable this skill? |
| `MeditationSkill.epAcquirement` | 500 | EP Requirement for Learning Meditation. |
| `MeditationSkill.magiculeCost` | 20 | Magicule Cost to activate . |
| `MeditationSkill.auraRegenRate` | 0.5 | Aura Regen rate. |
| `MeditationSkill.manaRegenRate` | 0.5 | Mana Regen rate |
| `MeditationSkill.shpRegenRate` | 0.5 | SHP Regen rate |

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

`tensura:skills/extra_skills`
