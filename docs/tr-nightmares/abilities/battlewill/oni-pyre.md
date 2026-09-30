# Oni Pyre

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `trnightmare:oni_pyre` |
| **Cooldowns (s)** | 30 |
| **Activation** | Hold |

</div>

> After charging, erupt pillars of flame beneath nearby enemies.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | *set by config (base aura cost)* | 15,000 or 300 |

## How it works

- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Acquisition checks: [Ogre Flame](../../../tensura-reincarnated/abilities/battlewill/ogre-flame.md), [Flame Domination](../../../tensura-reincarnated/abilities/extra-skills/flame-domination.md)

## Related

- **Related skills:** [Ogre Flame](../../../tensura-reincarnated/abilities/battlewill/ogre-flame.md), [Flame Domination](../../../tensura-reincarnated/abilities/extra-skills/flame-domination.md), [Flare Circle](../../../tensura-reincarnated/abilities/spiritual-magic/flare-circle.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/battlewill/nightmare_battlewill.toml`](../../configs/config-nightmare-ability-battlewill-nightmare-battlewill.md).

| Option | Default | Description |
|---|---|---|
| `OniPyre.epAcquirement` | 1,500,000 | EP required to learn Oni Pyre. |
| `OniPyre.learningAuraCost` | 15,000 | Aura point cost used while learning Oni Pyre. |
| `OniPyre.auraCostPerPillar` | 300 | Aura cost per pillar. |
| `OniPyre.chargeTimeTicks` | 100 | Charge time in ticks. |
| `OniPyre.pillarDamage` | 150 | Pillar damage per second. |
| `OniPyre.pillarRadius` | 2 | Pillar radius. |
| `OniPyre.durationTicks` | 100 | Duration in ticks while unmastered. |
| `OniPyre.durationMasteredTicks` | 200 | Duration in ticks while mastered. |
| `OniPyre.range` | 15 | Target search range. |
| `OniPyre.cooldownSeconds` | 30 | Cooldown in seconds after release. |
