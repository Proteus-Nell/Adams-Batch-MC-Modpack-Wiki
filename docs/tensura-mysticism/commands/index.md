# Commands

<small>[Tensura: Mysticism](../index.md)</small>

`<value>` is a required argument, `[value]` is optional. The permission column shows who can run it by default.

## `/mysticism edit`

| Syntax | Permission |
|---|---|
| `/mysticism edit stat <selector> soulEnergy current add <amount>` | Operator (level 2) |
| `/mysticism edit stat <selector> soulEnergy current set <amount>` | Operator (level 2) |
| `/mysticism edit stat <selector> soulEnergy max add <amount>` | Operator (level 2) |
| `/mysticism edit stat <selector> soulEnergy max add <amount> <resetCurrent>` | Operator (level 2) |
| `/mysticism edit stat <selector> soulEnergy max set <amount>` | Operator (level 2) |
| `/mysticism edit stat <selector> soulEnergy max set <amount> <resetCurrent>` | Operator (level 2) |

## `/mysticism get`

| Syntax | Permission |
|---|---|
| `/mysticism get stat <selector> soulEnergy current` | Moderator |
| `/mysticism get stat <selector> soulEnergy max` | Moderator |
| `/mysticism get stat soulEnergy current` | Everyone |
| `/mysticism get stat soulEnergy max` | Everyone |

## `/mysticism reset`

| Syntax | Permission |
|---|---|
| `/mysticism reset <selector> soulEnergy` | Operator (level 2) |

## Game rules

Change these with `/gamerule <name> <value>`.

| Game rule | Default | Description |
|---|---|---|
| `uniqueSECost` | true | Will Unique Skills cost Soul Energy |

## Command feedback messages

<details markdown><summary>Show 5 messages</summary>

| Key | Message |
|---|---|
| `mysticism.command.soul_energy.get` | %s's soul energy is currently %s. |
| `mysticism.command.soul_energy.get_max` | %s's Base amount of Max soul energy is currently %s. |
| `mysticism.command.soul_energy.reset` | %s's soul energy has been reset to %s. |
| `mysticism.command.soul_energy.set` | %s's soul energy has been set to %s. |
| `mysticism.command.soul_energy.set_max` | %s's Base amount of Max soul energy has been set to %s. |

</details>
