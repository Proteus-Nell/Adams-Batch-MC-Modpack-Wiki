# Black Lightning

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Black Lightning](../../../assets/icons/tensura/skill/black_lightning.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:black_lightning` |
| **Modes** | 5 |
| **Cooldowns (s)** | 5, 3, 7 |
| **Activation** | Press, Hold |

</div>

> Shoot black lightning at varying strength, or summon a massive storm which attacks any non-allied mobs. A short range plasma blast can also be used to melt even the strongest of foes.

## Modes

| # | Mode |
|---|---|
| 1 | Default Power |
| 2 | Decreased Power |
| 3 | Increased Power |
| 4 | Blast |
| 5 | Death Storm |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Decreased Power | 100 |  |
| Increased Power | 1,000 |  |
| Blast | 100 |  |
| Death Storm | 5,000 |  |
| other modes | 500 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect
- Triggers when you die

## Obtaining

- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Chimera Lord can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Divine Chimera can randomly receive.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/direwolf/special_direwolf_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Related skills:** [Molecular Manipulation](molecular-manipulation.md), [Wind Domination](wind-domination.md), [Wind Manipulation](wind-manipulation.md)
- **Summons / entities:** Black Lightning Blast, Black Lightning Bolt, Death Tornado
- **Referenced by:** [Black Flame](black-flame.md), [Black Flame Thunder](../../../tr-nightmares/abilities/intrinsic-skills/black-flame-thunder.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `BlackLightning.magiculeCost` | 500 | Magicule Cost to activate Default Mode. |
| `BlackLightning.magiculeCostWeak` | 100 | Magicule Cost to activate Weak Mode. |
| `BlackLightning.magiculeCostStrong` | 1,000 | Magicule Cost to activate Strong Mode. |
| `BlackLightning.magiculeCostBlast` | 100 | Magicule Cost to activate Blast Mode. |
| `BlackLightning.magiculeCostStorm` | 5,000 | Magicule Cost to activate Death Storm. |
| `BlackLightning.defaultLightningDamage` | 45 | How much Lightning damage that Default Mode does when activated. |
| `BlackLightning.defaultMagicDamage` | 5 | How much Magic damage that Default Mode does when activated. |
| `BlackLightning.defaultRange` | 8 | The range for damage that Default Mode does when activated. |
| `BlackLightning.defaultCooldown` | 5 | The cooldown in second of the Default Mode does when activated. |
| `BlackLightning.weakLightningDamage` | 22.5 | How much Lightning damage that Weak Mode does when activated. |
| `BlackLightning.weakMagicDamage` | 2.5 | How much Magic damage that Weak Mode does when activated. |
| `BlackLightning.weakRange` | 5 | The range for damage that Weak Mode does when activated. |
| `BlackLightning.weakCooldown` | 3 | The cooldown in second of the Weak Mode does when activated. |
| `BlackLightning.strongLightningDamage` | 135 | How much Lightning damage that Strong Mode does when activated. |
| `BlackLightning.strongMagicDamage` | 15 | How much Magic damage that Strong Mode does when activated. |
| `BlackLightning.strongRange` | 12 | The range for damage that Strong Mode does when activated. |
| `BlackLightning.strongCooldown` | 7 | The cooldown in second of the Strong Mode does when activated. |
| `BlackLightning.blastLightningDamage` | 22.5 | How much Lightning damage that Blast Mode does each second. |
| `BlackLightning.blastMagicDamage` | 2.5 | How much Magic damage that Weak Mode does when activated. |
| `BlackLightning.blastRange` | 30 | The range in block of Blast Mode. |
| `BlackLightning.stormStrikes` | 30 | The number of strikes that the Death Storm will create when activated (5s each strike). |
| `BlackLightning.stormRadius` | 30 | The radius of attack of the Death Storm when activated. |
| `BlackLightning.stormBoltDamage` | 90 | The Lightning damage of the bolt from the Death Storm. |
| `BlackLightning.stormBoltMagicDamage` | 10 | The Magic damage of the bolt from the Death Storm. |
| `BlackLightning.stormBoltRange` | 4 | The damage range of the bolt from the Death Storm. |
| `BlackLightning.stormBoltDistance` | 10 | The distance in block away from other lightning bolts from the Death Storm. |
| `BlackLightning.stormBoltNumber` | 10 | The maximum number of new lightning bolts to spawn each time. |
| `BlackLightning.stormTornadoDamage` | 45 | The Wind damage of the Tornado from the Death Storm. |
| `BlackLightning.stormTornadoMagicDamage` | 5 | The Magic damage of the Tornado from the Death Storm. |
| `BlackLightning.stormTornadoSize` | 4 | The size of the Tornado from the Death Storm. |
| `BlackLightning.stormTornadoDistance` | 20 | The distance in block away from other tornadoes from the Death Storm. |
| `BlackLightning.stormTornadoNumber` | 5 | The maximum number of new tornadoes to spawn each time. |

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

`tensura:skills/extra_skills`, `tensura:skills/lightning_skills`
