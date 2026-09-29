# Snatch

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Snatch](../../../assets/icons/trnightmare/skill/snatch.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:snatch` |
| **Modes** | 3 |
| **Cooldowns (s)** | 30 or 10, 20 mastered, 40 otherwise |
| **Activation** | Toggle, Press, Hold |

</div>

> Snatch is both an Enchantment-Type and Stealth-Type Unique Skill that allows the user to rob objectsand even the abilities of otherswithout ever laying a finger on them. This intangible attack slips through barriers, armor, and defenses alike, making it lethal in the hands of someone who knows how to use it. When wielded correctly, it's less a skill and more a violation of reality.

## Modes

| # | Mode |
|---|---|
| 1 | Physical Hunt! |
| 2 | Fox Hunt! |
| 3 | Zero Sign |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect
- Triggers on melee contact
- Triggers when an effect is applied to you

## Related

- **Effects:** [Costless](../../effects/costless.md), [Chill](../../../tensura-reincarnated/effects/chill.md), [Rest](../../../tensura-reincarnated/effects/rest.md), [Sleep](../../../tensura-reincarnated/effects/sleep.md), [Fragility](../../../tensura-reincarnated/effects/fragility.md), [Strengthen](../../../tensura-reincarnated/effects/strengthen.md), [Presence Concealment](../../../tensura-reincarnated/effects/presence-concealment.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `Snatch.mpAcquirement` | 100,000 | Magicule Acquirement Cost. |
| `Snatch.presenceLevel` | 11 | Level of Presence Concealment. |
| `Snatch.foxCooldown` | 40 | Cooldown for Fox Hunt Unmastered. |
| `Snatch.foxCooldownMastered` | 20 | Cooldown for Fox Hunt Mastered. |
| `Snatch.foxRange` | 10 | Range of Fox Hunt in blocks. |
| `Snatch.maxAbsorbPercentage` | 50 | What percentage of an enemy's max magicules are absorbed when they are eaten. |
| `Snatch.multiPhysCooldown` | 30 | Cooldown for multi target Physical Hunt. |
| `Snatch.singlePhysCooldown` | 10 | Cooldown for single target Physical hunt. |
| `Snatch.physicalRange` | 20 | Range of Physical Hunt in blocks. |
| `Snatch.touchAbsorbPercentage` | 1 | What percentage of an enemy's magicules are absorbed when they are touched. |
| `Snatch.attackPercentage` | 75 | What percentage of the enemy's attack damage does the user gain from Physical Hunt. |
