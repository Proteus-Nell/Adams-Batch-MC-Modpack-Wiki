# Gatekeeper

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Gatekeeper](../../../assets/icons/mysticism/skill/gatekeeper.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:gatekeeper` |
| **Modes** | 3 |
| **Cooldowns (s)** | 20 |
| **Activation** | Press, Hold |

</div>

> Wield the authority of kings and command treasures beyond mortal reach. Summon divine armaments from the vault, binding foes in chains of judgment while asserting dominion over all.

## Modes

| # | Mode |
|---|---|
| 1 | Enkidu |
| 2 | Kings Storehouse |
| 3 | Gate Of Babylon |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Enkidu | 25,000 |  |
| Gate Of Babylon | 25,000 |  |
| other modes | 0 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect

## Related

- **Effects:** [Enkidu](../../effects/enkidu.md)
- **Summons / entities:** Gate

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Gatekeeper.mpAcquirement` | 85,000 | Magicule Acquirement Cost. |
| `Gatekeeper.enkiduRange` | 10 | The range in blocks of the Enkidu mode. |
| `Gatekeeper.enkiduCost` | 25,000 | The magicule cost of the Enkidu mode. |
| `Gatekeeper.enkiduDuration` | 120 | The duration in seconds of the Enkidu mode. |
| `Gatekeeper.enkiduDurationMastered` | 240 | The duration in seconds of the Enkidu mode when Gatekeeper is mastered. |
| `Gatekeeper.enkiduCooldown` | 20 | The cooldown of the Enkidu mode in seconds. |
| `Gatekeeper.babylonCost` | 25,000 | The initial magicule cost of the Gate of Babylon mode. |
| `Gatekeeper.babylonContinousCost` | 25,000 | The continuous magicule cost of the Gate of Babylon mode. |

## Tags

`tensura:skills/unique_skills`
