# Corrosion

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Common Skills](index.md)</small>

<div class="infobox" markdown>

![Corrosion](../../../assets/icons/tensura/skill/corrosion.png)

| | |
|---|---|
| **Type** | Common Skill |
| **ID** | `tensura:corrosion` |
| **Activation** | Press |

</div>

> Empower your attacks with the deadly effect of Corrosion, toggleable when mastered.

## How it works

- Activated by pressing the skill key
- Triggers on melee contact

## Obtaining

- Innate to mobs: [Orc Disaster](../../mobs/orc-disaster.md), [Orc Lord](../../mobs/orc-lord.md)
- Listed in the `effectToRemove` config option (config/tensura/ability/battlewill_config.toml): The List of harmful effects that get removed upon activation.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Greater Chimera can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Golden Chimera can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Chimera Lord can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Divine Chimera can randomly receive.
- Acquisition checks: [Orc Lord](../../races/orc-lord.md), [Orc Disaster](../../races/orc-disaster.md)

## Related

- **Effects:** [Corrosion](../../effects/corrosion.md)
- **Summons / entities:** [Tempest Serpent](../../mobs/tempest-serpent.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/common_config.toml`](../../configs/config-tensura-ability-skill-common-config.md).

| Option | Default | Description |
|---|---|---|
| `Corrosion.rottenFleshAcquirement` | 100 | Rotten flesh eaten Optional Requirement for Learning. |
| `Corrosion.serpentAcquirement` | 100 | Tempest Serpent beaten Optional Requirement for Learning. |
| `Corrosion.orcAcquirement` | 1 | Orc Lord/Disaster beaten Optional Requirement for Learning. |
| `Corrosion.corrosionDuration` | 200 | The duration in tick of the Corrosion/Wither effect. |
| `Corrosion.corrosionLevel` | 1 | The level of the Corrosion/Wither effect. |

Set in [`config/tensura/ability/ability_config.toml`](../../configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/common_skills`
