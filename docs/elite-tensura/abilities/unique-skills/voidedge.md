# Void Edge

<small>[Elite Tensura](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Void Edge](../../../assets/icons/elitetensura/skill/voidedge.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `elitetensura:voidedge` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 8,000 |
| **Cooldowns (s)** | 3 mastered, 4 otherwise |
| **Activation** | Toggle, Press |

</div>

> A unique skill born from an instinctive grasp over void energy. The power feels raw and incomplete — as though it yearns to become something greater.

## Modes

| # | Mode |
|---|---|
| 1 | Void Cloak |
| 2 | Void Edge |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 800 or 0 | 0 |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| var3 | 10 | add |

## Related

- **Effects:** [Presence Concealment](../../../tensura-reincarnated/effects/presence-concealment.md)
- **Referenced by:** [Void Sovereign](../ultimate-skills/voidsovereign.md)

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/UniqueSkillConfig.toml`](../../configs/config-tensura-elitetensura-uniqueskillconfig.md).

| Option | Default | Description |
|---|---|---|
| `VoidEdge.mpAcquirement` | 8,000 |  |
| `VoidEdge.cloakAuraDrainPerTick` | 2 |  |
| `VoidEdge.cloakConcealmentLevel` | 1 |  |
| `VoidEdge.cloakConcealmentLevelMastered` | 3 |  |
| `VoidEdge.cloakDodgeBonus` | 10 |  |
| `VoidEdge.cloakChantSpeedMultiplier` | 1.4 |  |
| `VoidEdge.voidEdgeMagiculeCost` | 800 |  |
| `VoidEdge.voidEdgeDamage` | 25 |  |
| `VoidEdge.voidEdgeDamageMastered` | 50 |  |
| `VoidEdge.voidEdgeSize` | 1 |  |
| `VoidEdge.voidEdgeSizeMastered` | 1.4 |  |
| `VoidEdge.voidEdgeDuration` | 60 |  |
| `VoidEdge.voidEdgeDurationMastered` | 90 |  |
| `VoidEdge.voidEdgeCooldownSeconds` | 4 |  |
| `VoidEdge.voidEdgeCooldownMasteredSeconds` | 3 |  |

## In-game messages

<details markdown><summary>Show 1 messages</summary>

- Void Cloak has faded — insufficient aura to sustain it.

</details>

## Tags

`tensura:skills/no_plundering`, `tensura:skills/unique_skills`
