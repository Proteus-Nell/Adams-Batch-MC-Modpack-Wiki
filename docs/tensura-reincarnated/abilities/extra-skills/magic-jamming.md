# Magic Jamming

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Magic Jamming](../../../assets/icons/tensura/skill/magic_jamming.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:magic_jamming` |
| **Activation** | Toggle |

</div>

> Interferes with skills, magics, flight and transformation with mastery.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 100 |  |

## How it works

- Can be toggled on and off
- Has a continuous (per-tick) effect
- Triggers on melee contact

## Obtaining

- Intrinsic skill of: [Harpy](../../races/harpy.md), [Harpy Queen](../../races/harpy-queen.md), [Spirit Bird](../../races/spirit-bird.md), [Divine Bird](../../races/divine-bird.md)
- Can be learned by: [Mindwitness](../../../ascension/races/mindwitness.md), [Gauth](../../../ascension/races/gauth.md), [Beholder](../../../ascension/races/beholder.md), [Death Tyrant](../../../ascension/races/death-tyrant.md)
- Innate to mobs: [Charybdis](../../mobs/charybdis.md), [Megalodon](../../mobs/megalodon.md)
- Listed in the `charybdisCoreSkills` config option (config/tensura/block_config.toml): List of Skills that can be obtained from right-clicking Inert Charybdis Core.
- Listed in the `charybdisCoreFusingSkills` config option (config/tensura/block_config.toml): List of Skills that can be obtained from fusing with Inert Charybdis Core using Degenerate and similar abilities.
- Listed in the `intrinsicSkills` config option (config/nightmare/race/scholar_config.toml): List of skills obtained by this race.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/direwolf/direwolf_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/beetle_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/wasp_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Effects:** [Magic Interference](../../effects/magic-interference.md)
- **Summons / entities:** Tensura, [Charybdis](../../mobs/charybdis.md)
- **Referenced by:** [Mana Manipulation](mana-manipulation.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `MagicJamming.magiculeCost` | 100 | Base Magicule Cost to activate. |
| `MagicJamming.epMultiplier` | 3.5 | The multiplier of the user's EP that the target needs to be higher to ignore the effect of this skill. |
| `MagicJamming.inputDamageMitigation` | 0.5 | The multiplier of input skill/magic/art damage that the user takes less when toggled. |
| `MagicJamming.inputDamageMitigationMastered` | 0.67 | The multiplier of input skill/magic/art damage that the user takes less when toggled with mastery. |
| `MagicJamming.jammingDuration` | 600 | The duration in tick of the Jamming effect when a target is physically attacked by this skill. |
| `MagicJamming.jammingRadius` | 10 | The radius of the Jamming area. |
| `MagicJamming.jammingRadiusMastered` | 15 | The radius of the Jamming area when mastered. |
| `MagicJamming.jammingArenaDuration` | 120 | The duration in tick of the Jamming effect when a target is in the Jamming Arena. |

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

`tensura:skills/extra_skills`
