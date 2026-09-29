# ｢ Abaddon, King of Destruction ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:abaddon` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 750,000 |
| **Max mastery** | 5,000 |
| **Activation** | Toggle, Press, Hold |

</div>

> A King-class ultimate skill that embodies total destruction and catastrophic force.

## Modes

| # | Mode |
|---|---|
| 1 | Bullet Break Storm |
| 2 | Limitless World |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers when you take damage
- Triggers when an effect is applied to you
- Does something when first learned

## Obtaining

- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.
- Acquisition checks: [｢ Abaddon, King of Destruction ｣](abaddon.md), [Breaker](../unique-skills/breaker.md), [｢ Sandalphon, Lord of Judgement ｣](sandalphon-judgment.md)
- In-game message: *Abaddon, King of Destruction has awakened.*

## Related

- **Related skills:** [Breaker](../unique-skills/breaker.md), [｢ Sandalphon, Lord of Judgement ｣](sandalphon-judgment.md), [Spacetime Manipulation](../extra-skills/spacetime-manipulation.md)
- **Effects:** [Spatial Blockade](../../../tensura-reincarnated/effects/spatial-blockade.md), [Mystic Aura](../../effects/mystic-aura.md)
- **Summons / entities:** Bouncing Aura Bullet

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Abaddon.mpAcquirement` | 750,000 | Magicule cost to acquire Abaddon, King of Destruction. |
| `Abaddon.maxNihility` | 25,000 | Max nihility granted while Nihility Supply is active. |
| `Abaddon.enableUltimateEvolution` | true | Whether Abaddon can be obtained naturally |
| `Abaddon.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Abaddon.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Abaddon.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Abaddon.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Abaddon.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Abaddon.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Abaddon.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Abaddon.mpAcquirement` | 750,000 | Magicule cost to acquire Abaddon, King of Destruction. |
| `Abaddon.mobKillsRequired` | 1,500 | Mob kills required (minecraft:global mob_kills stat). |
| `Abaddon.humanKillsRequired` | 250 | Human kills required (Tensura existence human kill counter). |
| `Abaddon.maxNihility` | 25,000 | Max nihility granted while Nihility Supply is active. |
| `Abaddon.nihilityOverloadThreshold` | 10,000 | Nihility overload threshold (void damage per second above this). |
| `Abaddon.nihilityVoidPerSecond` | 50 | Void damage per second while above overload threshold. |
| `Abaddon.nihilityPerSpatialDamage` | 10 | Spatial damage dealt required per 1 nihility generated. |
| `Abaddon.limitBreakerMpRegenMulti` | 30 | Limit Breaker MP/AP regen multiplier. |
| `Abaddon.limitBreakerApRegenMulti` | 30 |  |
| `Abaddon.limitBreakerMpCapMultiplier` | 2.5 | Limit Breaker max MP cap as multiplier of base max (2.5 = 250%). |
| `Abaddon.limitBreakerOverflowThreshold` | 0.99 | Start MP overflow generation when current MP &gt;= this fraction of max. |
| `Abaddon.limitBreakerOverflowRatePerSecond` | 0.03 | MP overflow per skill-second while above threshold (fraction of max). |
| `Abaddon.raptureNihilityDrainPerSecond` | 100 | Rapture nihility drain per skill-second. |
| `Abaddon.raptureDurationSeconds` | 120 | Rapture duration before backlash (skill-seconds). |
| `Abaddon.raptureSkillCooldownSeconds` | 600 | Whole-skill cooldown after rapture backlash (skill-seconds). |
| `Abaddon.raptureDebuffDurationSeconds` | 1,800 | Dragon-style debuff duration after rapture (skill-seconds). |
| `Abaddon.raptureAuraRadius` | 8 | Rapture aura radius for judgment-style debuffs on nearby foes. |
| `Abaddon.enableUltimateEvolution` | true | Whether Abaddon can be obtained naturally |

## Tags

`tensura:skills/ultimate_skills`
