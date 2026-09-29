# Charm

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Charm](../../../assets/icons/tensura/skill/charm.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `tensura:charm` |
| **Activation** | Press |

</div>

> Use your inherent power to turn your opponents neutral or to temporarily dominate weak opponents.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 80 |  |

## How it works

- Activated by pressing the skill key

## Obtaining

- Intrinsic skill of: [Vampire](../../races/vampire.md), [Vampire Overcomer](../../races/vampire-overcomer.md), [Vampire Lord](../../races/vampire-lord.md), [Divine Vampire](../../races/divine-vampire.md), [Sacred qTree sChild](../../../tr-nightmares/races/sacred-tree-child.md), [Fairy Druid](../../../tr-nightmares/races/fairy-druid.md), [Medium Class Saiyan](../../../elite-tensura/races/medium-saiyan.md), [High Class Saiyan](../../../elite-tensura/races/high-saiyan.md), [Divine Saiyan](../../../elite-tensura/races/divine-saiyan.md), [Kitsune](../../../ascension/races/kitsune.md), [3 Tailed Fox](../../../ascension/races/three-tail-fox.md), [6 Tailed Fox](../../../ascension/races/six-tail-fox.md), [9 Tailed Fox](../../../ascension/races/nine-tail-fox.md), [Divine Kitsune](../../../ascension/races/divine-kitsune.md), [Blood Noble](../../../ascension/races/blood-noble.md), [Elder Bloodfiend](../../../ascension/races/elder-bloodfiend.md), [Progenitor Bloodfiend](../../../ascension/races/progenitor-bloodfiend.md), [Whisper Djinn](../../../ascension/races/whisper-djinn.md), [Trickster Djinn](../../../ascension/races/trickster-djinn.md), [Phantom Djinn](../../../ascension/races/phantom-djinn.md), [Royal Djinn](../../../ascension/races/royal-djinn.md), [Wishbound Djinn](../../../ascension/races/wishbound-djinn.md), [Primordial Djinn](../../../ascension/races/primordial-djinn.md), [Ascended Djinn](../../../ascension/races/ascended-djinn.md), [Sovereign Djinn](../../../ascension/races/sovereign-djinn.md), [Infinite Djinn](../../../ascension/races/infinite-djinn.md), [Omniversal Djinn](../../../ascension/races/omniversal-djinn.md), [Gazer](../../../ascension/races/gazer.md), [Spectator](../../../ascension/races/spectator-gazer.md), [Mindwitness](../../../ascension/races/mindwitness.md), [Gauth](../../../ascension/races/gauth.md), [Beholder](../../../ascension/races/beholder.md), [Death Tyrant](../../../ascension/races/death-tyrant.md)

## Related

- **Related skills:** [Spiritual Attack Resistance](../resistance-skills/spiritual-attack-resistance.md), [Spiritual Attack Nullification](../resistance-skills/spiritual-attack-nullification.md)
- **Effects:** [Mind Control](../../effects/mind-control.md), [Rampage](../../effects/rampage.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `Charm.magiculeCost` | 80 | Base Magicule Cost to activate. |
| `Charm.cooldown` | 5 | The Cooldown in second after activation. |
| `Charm.range` | 5 | The range in block for targeting an entity. |
| `Charm.fullMultiplier` | 0.25 | The multiplier of the user's EP that the target's EP needs to be below for full mind control. |
| `Charm.neutralMultiplier` | 0.5 | The multiplier of the user's EP that the target's EP needs to be below to become neutral toward the user. |
| `Charm.resistedMultiplier` | 0.2 | The multiplier of the user's EP that the target's Spiritual Attack Resistance reduces onto the EP requirement. |
| `Charm.controlDuration` | 6,000 | The duration in tick of the Mind Control effect (-1 = permanent). |
| `Charm.controlDurationMastered` | 12,000 | The duration in tick of the Mind Control effect when mastered (-1 = permanent). |

## Tags

`tensura:skills/intrinsic_skills`
