# Divine Wisdom Core

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `trnightmare:divine_wisdom_core` |
| **Cooldowns (s)** | 5 |
| **Activation** | Press, Hold |

</div>

> A Manas core that can unite with weaker bodies, manage its host, loan skills, and still awaken deeper ego routes.

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect

## Related

- **Related skills:** [｢ Mammon, Lord of Greed ｣](../ultimate-skills/mammon.md), [Possession](../../../tensura-reincarnated/abilities/intrinsic-skills/possession.md), [｢ Alternative, Proxy Rights ｣](../ultimate-skills/alternative.md)
- **Summons / entities:** Tensura
- **Referenced by:** [Robotnic](../unique-skills/robotnic.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_intrinsic.toml`](../../configs/config-nightmare-ability-skill-nightmare-intrinsic.md).

| Option | Default | Description |
|---|---|---|
| `DivineWisdomCore.informationalDrainPercent` | 0.01 | Percent of max magicule drained every 5s while unbound (informational body). |
| `DivineWisdomCore.passiveMasteryBonus` | 14 | Passive mastery speed bonus while Divine Wisdom Core is active. |
| `DivineWisdomCore.passiveLearningBonus` | 14 | Passive learning speed bonus while Divine Wisdom Core is active. |
| `DivineWisdomCore.hostMasteryBonus` | 14 | Mastery speed granted to the host while attached. |
| `DivineWisdomCore.hostLearningBonus` | 14 | Learning speed granted to the host while attached. |
| `DivineWisdomCore.hostCastSpeedBonus` | 0.4 | Cast speed multiplier bonus for the host (chant speed attribute). |
| `DivineWisdomCore.hijackResistanceMultiplier` | 0.5 |  |
| `DivineWisdomCore.hijackHpMultiplier` | 0.35 |  |
| `DivineWisdomCore.hijackShpMultiplier` | 0.35 |  |
| `DivineWisdomCore.hijackEpMultiplier` | 0.5 |  |
| `DivineWisdomCore.hijackMaxAttack` | 5,000 |  |
| `DivineWisdomCore.hijackMaxHealth` | 5,000 |  |
| `DivineWisdomCore.hijackRange` | 12 |  |
| `DivineWisdomCore.hijackMinMinutes` | 5 |  |
| `DivineWisdomCore.hijackMaxHours` | 5 |  |
| `DivineWisdomCore.bodyDespawnTicks` | 6,000 |  |
| `DivineWisdomCore.hostRange` | 32 |  |
| `DivineWisdomCore.egoBoostCooldownSeconds` | 300 | Cooldown (seconds) after locking an ego boost before you can pick again. |
| `DivineWisdomCore.energyOptimizationMinimumMagiculePerSecond` | 500 | Minimum MP transferred per second while Energy Optimization is set to Magicule. |
| `DivineWisdomCore.energyOptimizationMagiculePercentPerSecond` | 0.01 | Percent of max MP transferred per second while Energy Optimization is set to Magicule. |
| `DivineWisdomCore.energyOptimizationMinimumAuraPerSecond` | 100 | Minimum AP transferred per second while Energy Optimization is set to Aura. |
| `DivineWisdomCore.energyOptimizationAuraPercentPerSecond` | 0.01 | Percent of max AP transferred per second while Energy Optimization is set to Aura. |
| `DivineWisdomCore.energyOptimizationSpiritronsPerSecond` | 50 | Holy Power (Spiritrons) generated per second while Energy Optimization is set to Holy Power. |
| `DivineWisdomCore.energyOptimizationNihilityPerSecond` | 100 | Nihility generated per second while Energy Optimization is set to Nihility. |
| `ConceptualExistence.unityRange` | 12 | Targeting range for Unity possession on non-player bodies. |
| `ConceptualExistence.hostRange` | 32 | Targeting range for binding to a player host. |
| `ConceptualExistence.unityResistanceMultiplier` | 0.5 | Resistance multiplier passed to Tensura possession checks for Unity. |
| `ConceptualExistence.unityHpMultiplier` | 0.35 | Health multiplier passed to Tensura possession checks for Unity. |
| `ConceptualExistence.unityShpMultiplier` | 0.35 | Spiritual-health multiplier passed to Tensura possession checks for Unity. |
| `ConceptualExistence.unityEpMultiplier` | 0.5 | EP multiplier passed to Tensura possession checks for Unity. |
| `ConceptualExistence.unityMaxAttack` | 5,000 | Maximum attack copied into a borrowed Unity body. |
| `ConceptualExistence.unityMaxHealth` | 5,000 | Maximum health copied into a borrowed Unity body. |
| `ConceptualExistence.unityMinMinutes` | 5 | Minimum Unity possession duration in minutes before mastery. |
| `ConceptualExistence.unityMaxMinutes` | 20 | Maximum Unity possession duration in minutes before mastery. |
| `ConceptualExistence.unityMinMinutesMastered` | 10 | Minimum Unity possession duration in minutes after mastery. |
| `ConceptualExistence.unityMaxMinutesMastered` | 40 | Maximum Unity possession duration in minutes after mastery. |
| `ConceptualExistence.optimizeMinimumMagiculePerSecond` | 100 | Minimum magicule transferred per second while Optimize Energy is channeled. |
| `ConceptualExistence.optimizeMagiculePercentPerSecond` | 0.01 | Additional percent of the user's max magicule transferred per second while Optimize Energy is channeled. |

## In-game messages

<details markdown><summary>Show 40 messages</summary>

- Analysis
- Imaginary Space
- Magicule Reactor
- Host needs Lucifer or Nodens for analysis storage.
- Analyzed %s.
- Host has no Azathoth or Nodens imaginary space.
- Magicule Reactor surged through %s.
- Unity
- Ego Boost
- Host Management
- Enter Mind
- Enter Mind
- Ego boost has no reachable host entity for that action.
- Cannot spectate-host another entity while ego-boosting a different host.
- That host is out of range.
- Copied sub-mode %s from %s into your ego host's Lucifer.
- Analysis copied %s onto you (Great Sage rules).
- Mind projection released — your body remains in the inner world.
- Mind projection withdrawn.
- Mind projection collapsed — Divine Wisdom Core modes locked for five minutes.
- Mind projection requires your host to be online.
- No last-known position for your mind host — wait until they are in the world once.
- Mind projection requires the Possession intrinsic.
- Mind projections cannot attack with weapons (hand items to your body clone instead).
- Alteration
- Alteration
- Ego Boost (Lucifer)
- Ego Boost (Nodens)
- Ego Boost (Azathoth)
- Ego Boost (Satanael)
- Desire Generation
- Alternative
- Scroll ability modes — %s new mode(s) unlocked.
- Use the Analysis mode (scroll wheel) to analyze targets for your host's Lucifer.
- Use the Imaginary Space mode (scroll wheel).
- Use the Magicule Reactor mode (scroll wheel).
- Alteration is only for Raphael / Raphael Wisdom ego boost.
- Ego path already locked to %s.
- Ego locked: %s.
- Host has no unique or ultimate skill to ego boost.

</details>
