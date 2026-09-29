# Nuclear Flame

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Other Magic](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Other Magic |
| **ID** | `trnightmare:nuclear_flame` |
| **Max mastery** | 700 |
| **Activation** | Hold |

</div>

> A nuclear magic that unleashes extreme heat and destructive flame pressure.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | max(1, charge) × 15,000 |  |

## How it works

- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Can appear in epic tomes from wizard towers
- Can be found in skill tomes

## Related

- **Related skills:** [Chant Annulment](../../../tensura-reincarnated/abilities/extra-skills/chant-annulment.md)
- **Summons / entities:** Nuclear Flame Projectile

## Stats (config defaults)

Set in [`config/nightmare/ability/magic/nuclear.toml`](../../configs/config-nightmare-ability-magic-nuclear.md).

| Option | Default | Description |
|---|---|---|
| `NuclearFlame.maxChargeLevels` | 8 | Maximum charge levels. |
| `NuclearFlame.castTime` | 14 | Cast time in seconds for non-daemons. |
| `NuclearFlame.castTimeMastered` | 7 | Cast time in seconds for non-daemons with mastery. |
| `NuclearFlame.castTimeAnnuled` | 7 | Cast time in seconds for non-daemons with chant annulment. |
| `NuclearFlame.castTimeBoth` | 4 | Cast time in seconds for non-daemons with both mastery and annulment. |
| `NuclearFlame.daemonCastTime` | 10 | Cast time in seconds for daemon lords. |
| `NuclearFlame.daemonCastTimeMastered` | 5 | Cast time in seconds for daemon lords with mastery. |
| `NuclearFlame.daemonCastTimeAnnuled` | 5 | Cast time in seconds for daemon lords with chant annulment. |
| `NuclearFlame.daemonCastTimeBoth` | 2 | Cast time in seconds for daemon lords with both mastery and annulment. |
| `NuclearFlame.magiculeCost` | 15,000 | Magicule Cost to cast per level. |
| `NuclearFlame.explosionRadius` | 5 | The explosion radius in blocks of the fireball. |
| `NuclearFlame.nuclearDamage` | 125 | The nuclear damage of the strike per level. |
| `NuclearFlame.chargeTicksPerLevel` | 40 | Charge level increases per 2 seconds of holding after cast time. |
| `NuclearFlame.maxChargeLevels` | 8 | Maximum charge levels. |

Set in [`config/tensura/ability/magic_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

## In-game messages

<details markdown><summary>Show 1 messages</summary>

- Nuclear Flame  ▶  Charge: %1$s / %2$s  (%3$s dmg)

</details>

## Tags

`tensura:skills/epic_tome_wizard_tower`, `tensura:skills/found_in_tome`, `tensura:skills/magic`
