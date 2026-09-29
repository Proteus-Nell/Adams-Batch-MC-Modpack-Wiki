# `config/tensura/entity/effect_config.toml`

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Configs](index.md)</small>

## Top level

| Option | Default | Range | Description |
|---|---|---|---|
| `maxFear` | 20 |  | The max level of Fear can be applied legally in game. |

## `[Rampage]`

| Option | Default | Range | Description |
|---|---|---|---|
| `replenishEach` | 60 |  | The duration in tick of rampage that affected entities get replenished to each time damaging or getting hurt. |
| `replenishDamage` | 600 |  | The maximum duration of rampage that affected entities get replenished to when damaging another entity. |
| `replenishHurt` | 1,200 |  | The maximum duration of rampage that affected entities get replenished to after getting hurt by another entity. |
| `mobAggroRadius` | 15 |  | The radius in block for affected mobs to find targets to attack. |
| `playerDamageDuration` | 200 |  | The duration in tick of the effect that affected players need to have below to start taking damage. |
| `playerDamageHP` | 0.1 |  | The max health multiplier that affected players lose every second when the effect's duration is too low. |
| `playerDamageSHP` | 0.1 |  | The max spiritual health multiplier that affected players lose every second when the effect's duration is too low. |
