# Void Sovereign

<small>[Elite Tensura](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![Void Sovereign](../../../assets/icons/elitetensura/skill/voidsovereign.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `elitetensura:voidsovereign` |
| **Modes** | 4 |
| **Acquisition cost (MP)** | 50,000 |
| **Cooldowns (s)** | 1, 20 mastered, 30 otherwise, 260 or 400 |
| **Activation** | Toggle, Press, Hold |

</div>

> An ultimate skill granting absolute dominion over existence, space, and life-force. Those who wield it become sovereign over the void itself.

## Modes

| # | Mode |
|---|---|
| 1 | Void Domain |
| 2 | Null Slash |
| 3 | Event Horizon |
| 4 | Soul Collapse |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Null Slash | 1,500 | 3,000 or 0 |
| Soul Collapse | 5,000 |  |
| other modes | 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| var3 | 25 | add |
| var4 | 3 | add |

## Obtaining

- Acquisition checks: [Void Edge](../unique-skills/voidedge.md)

## Related

- **Related skills:** [Void Edge](../unique-skills/voidedge.md)
- **Effects:** [Presence Concealment](../../../tensura-reincarnated/effects/presence-concealment.md), [Severance Blade](../../../tensura-reincarnated/effects/severance-blade.md)
- **Summons / entities:** Severance Cutter, Tensura

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/UltimateSkillConfig.toml`](../../configs/config-tensura-elitetensura-ultimateskillconfig.md).

| Option | Default | Description |
|---|---|---|
| `VoidSovereign.IsEnabled` | true | Is this Skill Enabled? |
| `VoidSovereign.mpAcquirement` | 50,000 | Magicule Acquirement Cost. |
| `VoidSovereign.domainAuraDrainPerTick` | 5 |  |
| `VoidSovereign.domainConcealmentLevel` | 3 |  |
| `VoidSovereign.domainConcealmentLevelMastered` | 5 |  |
| `VoidSovereign.domainDodgeBonus` | 25 |  |
| `VoidSovereign.domainDodgeInvulnerabilityBonus` | 3 |  |
| `VoidSovereign.domainChantSpeedMultiplier` | 2 |  |
| `VoidSovereign.domainPassiveDamage` | 8 |  |
| `VoidSovereign.domainPassiveDamageMastered` | 16 |  |
| `VoidSovereign.nullSlashMagiculeCost` | 1,500 |  |
| `VoidSovereign.nullSlashDamage` | 150 |  |
| `VoidSovereign.nullSlashDamageMastered` | 300 |  |
| `VoidSovereign.nullSlashSize` | 1.4 |  |
| `VoidSovereign.nullSlashSizeMastered` | 2 |  |
| `VoidSovereign.nullSlashDuration` | 80 |  |
| `VoidSovereign.nullSlashDurationMastered` | 120 |  |
| `VoidSovereign.nullSlashCooldownSeconds` | 1 |  |
| `VoidSovereign.nullSlashCooldownMasteredSeconds` | 1 |  |
| `VoidSovereign.eventHorizonAuraCost` | 3,000 |  |
| `VoidSovereign.eventHorizonRange` | 20 |  |
| `VoidSovereign.eventHorizonRangeMastered` | 35 |  |
| `VoidSovereign.eventHorizonDamageBonus` | 100 |  |
| `VoidSovereign.eventHorizonDamageBonusMastered` | 555 |  |
| `VoidSovereign.eventHorizonDebuffDuration` | 120 |  |
| `VoidSovereign.eventHorizonCooldown` | 30 |  |
| `VoidSovereign.eventHorizonCooldownMastered` | 20 |  |
| `VoidSovereign.soulCollapseMagiculeCost` | 5,000 |  |
| `VoidSovereign.soulCollapseBaseDamage` | 60 |  |
| `VoidSovereign.soulCollapseBaseDamageMastered` | 100 |  |
| `VoidSovereign.soulCollapseChargeMultiplier` | 1.5 |  |
| `VoidSovereign.soulCollapseChargeMultiplierMastered` | 2.5 |  |
| `VoidSovereign.soulCollapseMaxChargeTicks` | 60 |  |
| `VoidSovereign.soulCollapseHitRadius` | 3 |  |
| `VoidSovereign.soulCollapseHitRadiusMastered` | 5 |  |
| `VoidSovereign.soulCollapseCooldown` | 400 |  |
| `VoidSovereign.soulCollapseCooldownMastered` | 260 |  |
| `VoidSovereign.friendlyFire` | false | If true, Event Horizon and Soul Collapse also hit players in the user's own nation or hunt party. |

## Tags

`tensura:skills/no_plundering`, `tensura:skills/ultimate_skills`
