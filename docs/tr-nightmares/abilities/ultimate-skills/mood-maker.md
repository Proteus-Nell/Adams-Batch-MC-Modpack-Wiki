# ｢ Mood Maker, Lord of Psychology ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:mood_maker` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 500,000 |
| **Max mastery** | 5,000 |
| **Cooldowns (s)** | 1,200, 60, 300 |
| **Activation** | Press |

</div>

> Manipulate the moods and fate of yourself and others — twist luck, defy death, and amplify your spirit.

## Modes

| # | Mode |
|---|---|
| 1 | Destiny Alteration |
| 2 | Mood Booster |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 0 |  |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you die

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| attr | value | operation |

## Obtaining

- Listed in the `allowedSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can be affected by Raphael-style alteration by default.
- Acquisition checks: [Tuner](../../../tensura-reincarnated/abilities/unique-skills/tuner.md), [｢ Mood Maker, Lord of Psychology ｣](mood-maker.md)
- In-game message: *Your emotional resonance crystallizes — Mood Maker awakens!*

## Related

- **Related skills:** [Tuner](../../../tensura-reincarnated/abilities/unique-skills/tuner.md)
- **Effects:** [Fate Change](../../../tensura-reincarnated/effects/fate-change.md), [Strengthen](../../../tensura-reincarnated/effects/strengthen.md), [Mood](../../effects/mood.md)
- **Summons / entities:** Tensura
- **Referenced by:** [Alteration](../extra-skills/alteration.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `MoodMaker.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `MoodMaker.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `MoodMaker.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `MoodMaker.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `MoodMaker.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `MoodMaker.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `MoodMaker.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `MoodMaker.mpAcquirement` | 500,000 | Magicule cost to acquire Mood Maker (evolution from Tuner). |
| `MoodMaker.destinyChangeUsesRequired` | 100 | Number of times Destiny Change must have been used to unlock evolution. |
| `MoodMaker.enableUltimateEvolution` | true | Whether Mood Maker evolution is allowed. |
| `MoodMaker.destinyAlterationCooldown` | 300 | Cooldown in seconds for Destiny Alteration (manual revive). |
| `MoodMaker.moodBoosterCooldown` | 60 | Cooldown in seconds for Mood Booster active. |
| `MoodMaker.moodBoosterDuration` | 600 | Duration in ticks for Mood Booster effect. |
| `MoodMaker.moodBoosterMaxStacks` | 5 | Max Mood Booster stacks. |
| `MoodMaker.unexpectedManipulationHpThreshold` | 0.3 | HP threshold ratio (0-1) for Unexpected Manipulation buffs. |
| `MoodMaker.unexpectedManipulationHpThresholdMid` | 0.49 | Middle HP threshold ratio (0-1) for Unexpected Manipulation buffs. |
| `MoodMaker.unexpectedManipulationHpThresholdHigh` | 0.74 | High HP threshold ratio (0-1) for Unexpected Manipulation buffs. |
| `MoodMaker.unexpectedManipulationDamageAmplifier` | 3 | Damage buff amplifier from Unexpected Manipulation. |
| `MoodMaker.unexpectedManipulationSpeedAmplifier` | 2 | Speed buff amplifier from Unexpected Manipulation. |
| `MoodMaker.unexpectedManipulationResistanceAmplifier` | 1 | Resistance buff amplifier from Unexpected Manipulation. |
| `ultMasteryConfig.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |
