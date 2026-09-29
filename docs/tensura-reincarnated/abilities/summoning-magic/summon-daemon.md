# Summon Daemon

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Summoning Magic](index.md)</small>

<div class="infobox" markdown>

![Summon Daemon](../../../assets/icons/tensura/skill/summon_daemon.png)

| | |
|---|---|
| **Type** | Summoning Magic |
| **ID** | `tensura:summon_daemon` |
| **Modes** | 4 |
| **Max mastery** | 200 |
| **Activation** | Press, Hold |

</div>

> Summon a Daemon from hell to fight for you.

## Modes

| # | Mode |
|---|---|
| 1 | Mode 1 |
| 2 | Mode 2 |
| 3 | Mode 3 |
| 4 | Mode 4 |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when one of your subordinates dies

## Obtaining

- Can appear in epic tomes from wizard towers
- Can appear in Hell treasure tomes

## Related

- **Effects:** [Rampage](../../effects/rampage.md)
- **Summons / entities:** Tensura, Summoning Beam, [Clone](../../mobs/clone.md)

## Stats (config defaults)

Set in [`config/tensura/ability/magic/summoning_config.toml`](../../configs/config-tensura-ability-magic-summoning-config.md).

| Option | Default | Description |
|---|---|---|
| `SummonDaemon.castTime` | 300 | Cast time in tick. |
| `SummonDaemon.costMultiplier` | 2 | The EP multiplier of the summoned daemon to be counted as Magicule Cost. |
| `SummonDaemon.obeyMultiplier` | 3 | The EP multiplier of the summoned daemon that the summoner needs have to be able to control the daemon when its Negotiable. |
| `SummonDaemon.obeyMultiplierWhimsical` | 5 | The EP multiplier of the summoned daemon that the summoner needs have to be able to control the daemon when its Whimsical. |
| `SummonDaemon.obeyMultiplierNonNegotiable` | 10 | The EP multiplier of the summoned daemon that the summoner needs have to be able to control the daemon when its Non-Negotiable. |
| `SummonDaemon.archChance` | 0.1 | The chance for the magic to summon an Arch Daemon when using Random mode. |
| `SummonDaemon.greaterChance` | 0.3 | The chance for the magic to summon a Greater Daemon when using Random mode. |
| `SummonDaemon.lesserEP` | 0 | The minimal amount of EP that a daemon player needs to have to be qualified for Lesser Daemon mode. |
| `SummonDaemon.greaterEP` | 10,000 | The minimal amount of EP that a daemon player needs to have to be qualified for Greater Daemon mode (and maximum for Lesser Daemon mode). |
| `SummonDaemon.archEP` | 140,000 | The minimal amount of EP that a daemon player needs to have to be qualified for Arch Daemon mode (and maximum for Greater Daemon mode). |
| `SummonDaemon.archEPMax` | 10,000,000 | The maximum amount of EP that a daemon player can be summoned by the Arch Daemon mode. |
| `SummonDaemon.sacrificeRadius` | 3 | The radius in block from the magic circle center that mobs can be used as sacrifices. |
| `SummonDaemon.sacrificeHP` | 0.25 | The multiplier of max HP that an entity needs to have below to be qualified for Sacrificing. |
| `SummonDaemon.sacrificeSHP` | 0.25 | The multiplier of max SHP that an entity needs to have below to be qualified for Sacrificing. |
| `SummonDaemon.sacrificeEP` | 0.25 | The multiplier of the summoned daemon's EP that an entity needs to have below to be qualified for Sacrificing. |
| `SummonDaemon.sacrificeEPBoost` | 0.5 | The multiplier of the total EP sacrificed will be added onto the summoned Daemon. |
| `SummonDaemon.summonDuration` | 600 | How long in second will the summoned Daemon will stay. |
| `SummonDaemon.cooldown` | 600 | The cooldown in second of the magic. |
| `SummonDaemon.cooldownMastered` | 300 | The cooldown in second of the magic when mastered. |

Set in [`config/tensura/ability/magic_config.toml`](../../configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

## Tags

`tensura:skills/epic_tome_wizard_tower`, `tensura:skills/hell_treasure_tome`, `tensura:skills/summoning_magic`
