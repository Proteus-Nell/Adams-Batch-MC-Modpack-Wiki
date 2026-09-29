# `config/tensura/ability/magic/summoning_config.toml`

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Configs](index.md)</small>

## `[SummonMediumElemental]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 100 |  | Cast time in tick. |
| `castTimeMastered` | 60 |  | Cast time in tick when mastered. |
| `magiculeCost` | 500 |  | Magicule Cost to cast. |
| `magiculeCostSecond` | 50 |  | Magicule Cost each second to keep the Spirit alive. |
| `spiritDuration` | 600 |  | How long in second will the summoned Spirit will stay. |
| `cooldown` | 600 |  | The cooldown in second of the magic. |
| `cooldownMastered` | 300 |  | The cooldown in second of the magic when mastered. |

## `[SummonGreaterElemental]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 100 |  | Cast time in tick. |
| `castTimeMastered` | 60 |  | Cast time in tick when mastered. |
| `magiculeCost` | 3,000 |  | Magicule Cost to cast. |
| `magiculeCostSecond` | 300 |  | Magicule Cost each second to keep the Spirit alive. |
| `spiritDuration` | 600 |  | How long in second will the summoned Spirit will stay. |
| `attackMultiplier` | 0.5 |  | The multiplier of Attack damage for the summoned Greater Spirit compared to the wild Boss version. |
| `healthMultiplier` | 0.5 |  | The multiplier of Health for the summoned Greater Spirit compared to the wild Boss version. |
| `cooldown` | 600 |  | The cooldown in second of the magic. |
| `cooldownMastered` | 300 |  | The cooldown in second of the magic when mastered. |

## `[SummonBasilisk]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 100 |  | Cast time in tick. |
| `castTimeMastered` | 60 |  | Cast time in tick when mastered. |
| `magiculeCost` | 500 |  | Magicule Cost to cast. |
| `magiculeCostSecond` | 100 |  | Magicule Cost each second to keep the Basilisk alive. |
| `summonDuration` | 600 |  | How long in second will the summoned Basilisk will stay. |
| `cooldown` | 600 |  | The cooldown in second of the magic. |
| `cooldownMastered` | 300 |  | The cooldown in second of the magic when mastered. |

## `[SummonDaemon]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 300 |  | Cast time in tick. |
| `costMultiplier` | 2 |  | The EP multiplier of the summoned daemon to be counted as Magicule Cost. |
| `obeyMultiplier` | 3 |  | The EP multiplier of the summoned daemon that the summoner needs have to be able to control the daemon when its Negotiable. |
| `obeyMultiplierWhimsical` | 5 |  | The EP multiplier of the summoned daemon that the summoner needs have to be able to control the daemon when its Whimsical. |
| `obeyMultiplierNonNegotiable` | 10 |  | The EP multiplier of the summoned daemon that the summoner needs have to be able to control the daemon when its Non-Negotiable. |
| `archChance` | 0.1 |  | The chance for the magic to summon an Arch Daemon when using Random mode. |
| `greaterChance` | 0.3 |  | The chance for the magic to summon a Greater Daemon when using Random mode. |
| `lesserEP` | 0 |  | The minimal amount of EP that a daemon player needs to have to be qualified for Lesser Daemon mode. |
| `greaterEP` | 10,000 |  | The minimal amount of EP that a daemon player needs to have to be qualified for Greater Daemon mode (and maximum for Lesser Daemon mode). |
| `archEP` | 140,000 |  | The minimal amount of EP that a daemon player needs to have to be qualified for Arch Daemon mode (and maximum for Greater Daemon mode). |
| `archEPMax` | 10,000,000 |  | The maximum amount of EP that a daemon player can be summoned by the Arch Daemon mode. |
| `sacrificeRadius` | 3 |  | The radius in block from the magic circle center that mobs can be used as sacrifices. |
| `sacrificeHP` | 0.25 |  | The multiplier of max HP that an entity needs to have below to be qualified for Sacrificing. |
| `sacrificeSHP` | 0.25 |  | The multiplier of max SHP that an entity needs to have below to be qualified for Sacrificing. |
| `sacrificeEP` | 0.25 |  | The multiplier of the summoned daemon's EP that an entity needs to have below to be qualified for Sacrificing. |
| `sacrificeEPBoost` | 0.5 |  | The multiplier of the total EP sacrificed will be added onto the summoned Daemon. |
| `summonDuration` | 600 |  | How long in second will the summoned Daemon will stay. |
| `cooldown` | 600 |  | The cooldown in second of the magic. |
| `cooldownMastered` | 300 |  | The cooldown in second of the magic when mastered. |

## `[SummonHoundDog]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castTime` | 100 |  | Cast time in tick. |
| `castTimeMastered` | 60 |  | Cast time in tick when mastered. |
| `magiculeCost` | 50 |  | Magicule Cost to cast. |
| `magiculeCostSecond` | 10 |  | Magicule Cost each second to keep the Hound Dog alive. |
| `summonDuration` | 600 |  | How long in second will the summoned Hound Dog will stay. |
| `cooldown` | 600 |  | The cooldown in second of the magic. |
| `cooldownMastered` | 300 |  | The cooldown in second of the magic when mastered. |

## `[SummonOtherworlder]`

| Option | Default | Range | Description |
|---|---|---|---|
| `castInterval` | 60 |  | Cast time in tick each time the magic circle can be provided with Magicule. |
| `castRange` | 8 |  | Cast range in block of the magic. |
| `magiculeCostTotal` | 3,000,000 |  | Magicule Cost total to summon an otherworlder. |
| `magiculeCostInterval` | 50,000 |  | Magicule Cost the magic circle takes each cast interval. |
| `magiculeCostIntervalMastered` | 100,000 |  | Magicule Cost the magic circle takes each cast interval when mastered. |
| `failChance` | 0.5 |  | The chance to fail summon an otherworlder. |
| `failChanceMastered` | 0.3 |  | The chance to fail summon an otherworlder when mastered. |
| `circleDuration` | 600 |  | How long in second will the magic circle stay each time it is provided with Magicule. |
| `cooldown` | 1,200 |  | The cooldown in second of the magic. |
