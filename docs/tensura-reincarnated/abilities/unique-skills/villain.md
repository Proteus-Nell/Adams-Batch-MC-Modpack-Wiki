# Villain

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Villain](../../../assets/icons/tensura/skill/villain.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:villain` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 60,000 |
| **Cooldowns (s)** | 3 mastered, 5 otherwise |
| **Activation** | Toggle, Press, Hold |

</div>

> Embody malice and fight on the side of evil. Gain increased power from killing your foes, manipulate your enemies into joining your side and empower your allies.

## Modes

| # | Mode |
|---|---|
| 1 | Demon Lord's Haki |
| 2 | Villain's Charisma |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Demon Lord's Haki | 25 |  |
| Villain's Charisma | 200 |  |
| other modes | 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Adjusted by scrolling while active
- Has a continuous (per-tick) effect

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Movement Speed | -0.95 | multiply total |
| aura | 1.5 | add |
| magicule | 1.5 | add |
| negate | 0.25 | add |

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Related

- **Related skills:** [Spiritual Attack Resistance](../resistance-skills/spiritual-attack-resistance.md)
- **Effects:** [Haki Coat](../../effects/haki-coat.md), [Ally Boost](../../effects/ally-boost.md), [Mind Control](../../effects/mind-control.md)
- **Summons / entities:** Tensura
- **Referenced by:** [｢ Tantalous, King of Evil ｣](../../../tr-nightmares/abilities/ultimate-skills/tantalus.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Villain.mpAcquirement` | 60,000 | Magicule Acquirement Cost. |
| `Villain.magiculeCostHaki` | 25 | Magicule Cost to activate Hero Haki. |
| `Villain.magiculeCostCharisma` | 200 | Magicule Cost to activate Hero's Charisma. |
| `Villain.intimidationRadius` | 15 | The radius in block of the Villain's Intimidation's effect on allies. |
| `Villain.controlRadius` | 10 | The radius in block of the Villain's Charisma's effect. |
| `Villain.controlDuration` | 2,400 | The duration in tick of the Mind Control effect when activating Villain's Charisma (-1 = permanent). |
| `Villain.controlResistedDuration` | 1,200 | The duration in tick of the Mind Control effect when activating Villain's Charisma while the target has Spiritual Attack Resistance (-1 = permanent). |
| `Villain.majinPercentage` | 100 | The percentage to become Majin when dying of Magicule Poison while having this skill. |
| `Villain.auraPercentage` | 1.5 | The bonus Aura percentage the user gains when toggled on. |
| `Villain.magiculePercentage` | 1.5 | The bonus Magicule percentage the user gains when toggled on. |
| `Villain.dodgeNegateChance` | 0.25 | The bonus Dodge negate chance the user gains when toggled on. |

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `Haki.speedMultiplier` | 0.05 | Activation Speed Multiplier when activated. |
| `Haki.epAcquirement` | 100,000 | EP Requirement for Learning. |
| `Haki.magiculeCost` | 25 | Magicule Cost to activate. |
| `Haki.speedMultiplier` | 0.05 | Activation Speed Multiplier when activated. |
| `Haki.speedMultiplierMastered` | 0.1 | Activation Speed Multiplier when activated with mastery. |
| `Haki.hakiRadius` | 15 | The attack radius of the haki in blocks. |
| `Haki.epDifferenceMultiplier` | 0.25 | The EP difference multiplier for each Fear Level. |
| `Haki.fearDuration` | 200 | The duration in tick of the Fear effect when applied. |
| `Haki.cooldown` | 5 | The cooldown in second of the haki. |
| `Haki.cooldownMastered` | 3 | The cooldown in second of the haki when mastered. |

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

`tensura:skills/has_magicule_rich_haki`, `tensura:skills/unique_skills`
