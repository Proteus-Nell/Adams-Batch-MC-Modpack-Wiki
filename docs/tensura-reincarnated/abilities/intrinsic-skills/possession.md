# Possession

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Possession](../../../assets/icons/tensura/skill/possession.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `tensura:possession` |
| **Activation** | Press |

</div>

> Possess a weakened material body to gain access to a whole new world.

## How it works

- Activated by pressing the skill key

## Obtaining

- Intrinsic skill of: [Demon Slime](../../races/demon-slime.md), [God Slime](../../races/god-slime.md), [Lesser Daemon](../../races/lesser-daemon.md), [Greater Daemon](../../races/greater-daemon.md), [Arch Daemon](../../races/arch-daemon.md), [Daemon Lord](../../races/daemon-lord.md), [Devil Lord](../../races/devil-lord.md), [Perfect Doppelganger](../../../tr-nightmares/races/perfect-doppelganger.md), [Eidolon](../../../tr-nightmares/races/eidolon.md), [Thought Leech](../../../tr-nightmares/races/thought-leech.md), [Shadow Mimic](../../../tr-nightmares/races/shadow-mimic.md), [Lesser Mimic](../../../tr-nightmares/races/lesser-mimic.md), [Lesser Elemental](../../../tensura-mysticism/races/lesser-elemental.md), [Medium Elemental](../../../tensura-mysticism/races/medium-elemental.md), [Greater Elemental](../../../tensura-mysticism/races/greater-elemental.md), [Elemental Lord](../../../tensura-mysticism/races/elemental-lord.md), [Majin Elemental Lord](../../../tensura-mysticism/races/majin-lord.md), [Divine Majin Elemental](../../../tensura-mysticism/races/divine-majin-elemental.md), [Divine Elemental](../../../tensura-mysticism/races/divine-elemental.md), [Fallen Angel](../../../ascension/races/fallen-angel.md), [Chaotic Deity](../../../ascension/races/chaotic-deity.md), [Mindwitness](../../../ascension/races/mindwitness.md), [Gauth](../../../ascension/races/gauth.md), [Beholder](../../../ascension/races/beholder.md), [Death Tyrant](../../../ascension/races/death-tyrant.md)
- Innate to mobs: [Arch Daemon](../../mobs/arch-daemon.md), [Greater Daemon](../../mobs/greater-daemon.md), [Lesser Daemon](../../mobs/lesser-daemon.md)
- Listed in the `intrinsicSkills` config option (config/mysticism/race/phantom_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/forgotten_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/angel_config.toml): The list of intrinsic skills that the race gets.
- Acquisition checks: [Possession](../aspectual-magic/possession-magic.md)

## Related

- **Related skills:** [Possession](../aspectual-magic/possession-magic.md), [Spiritual Attack Nullification](../resistance-skills/spiritual-attack-nullification.md), [Spiritual Attack Resistance](../resistance-skills/spiritual-attack-resistance.md)
- **Effects:** [Energy Blockade](../../effects/energy-blockade.md)
- **Referenced by:** [Divine Wisdom Core](../../../tr-nightmares/abilities/intrinsic-skills/divine-wisdom-core.md), [Relapse](../../../tensura-mysticism/abilities/intrinsic-skills/relapse.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `Possession.range` | 5 | The possession range in block. |
| `Possession.hpMultiplier` | 0.1 | The multiplier of the maximum Health that a target needs to be under to be possessed. |
| `Possession.shpMultiplier` | 0.1 | The multiplier of the maximum Spiritual Health that a target needs to be under to be possessed. |
| `Possession.epMultiplier` | 0.25 | The multiplier of the user's maximum EP that a target needs to be under to be possessed. |
| `Possession.resistanceMultiplier` | 0.5 | The multiplier of the possession requirement multipliers when the target has Spiritual Attack Resistance. |
| `Possession.maxHealth` | 1,000 | The maximum amount of HP the user can get from possessing an entity. |
| `Possession.maxAttack` | 100 | The maximum amount of Attack Damage the user can get from possessing an entity. |
| `Possession.bodyDespawnTick` | 300 | The number of seconds that Possession Bodies will despawn. (0 = instant despawn, -1 = doesn't despawn) |

## Tags

`tensura:skills/intrinsic_skills`
