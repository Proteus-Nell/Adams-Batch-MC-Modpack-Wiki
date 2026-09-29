# `config/tensura/EliteTensura/EventHandlerConfig.toml`

<small>[Elite Tensura](../index.md) &rsaquo; [Configs](index.md)</small>

## `[Blacklist]`

| Option | Default | Range | Description |
|---|---|---|---|
| `Blacklist` | "tensura:slime", "tensura:hound_dog", "tensura:barghest", "tensura:leech_lizard", "tensura:hover_lizard", "tensura:direwolf", "tensura:giant_ant", "tensura:metal_slime" |  | Blacklist mobs. These entity types are blocked from spawning in the spawn region. Everything else is allowed. |

## `[PICKUP_BLACKLIST]`

| Option | Default | Range | Description |
|---|---|---|---|
| `items` | [] (empty) |  | Item ids (namespace:path) that players can never pick up. Existing copies are removed from player inventories and Curios slots. Empty = disabled. |

## `[DEBUG]`

| Option | Default | Range | Description |
|---|---|---|---|
| `debug` | false |  | T/F Is this debug enabled? |

## `[Naming]`

| Option | Default | Range | Description |
|---|---|---|---|
| `namingEpLossPercent` | 0.15 |  | Fraction of the namer's MAX EP permanently transferred to the named player when one player names another. Requires gamerule ETPlayerNamingEpLoss. Default 0.15 = 15%. |

## `[SubordinateEpShare]`

| Option | Default | Range | Description |
|---|---|---|---|
| `sharePercent` | 0.1 |  | Fraction of a subordinate's kill-EP also granted to its owner when the owner is within rangeBlocks. Requires gamerule ETSubordinateEpShare. Default 0.10 = 10%. |
| `rangeBlocks` | 20 |  | Max distance (blocks) between subordinate and owner for the EP share to apply. Default 20. |

## `[HuntParty]`

| Option | Default | Range | Description |
|---|---|---|---|
| `sharePercent` | 0.2 |  | Fraction of a party member's kill-EP granted on-top to EACH other qualifying party member. Requires gamerule ETPartySystem. Default 0.20 = 20%. |
| `rangeBlocks` | 32 |  | Max distance (blocks) between the killer and a party member for the EP share to apply. Default 32. |
| `maxMembers` | 5 |  | Maximum party size, enforced when an invite is accepted. Default 5. |
| `inviteExpirySeconds` | 60 |  | Seconds before a pending party invite expires (checked lazily on accept). Default 60. |
| `hudIntervalTicks` | 20 |  | Ticks between live party roster pushes (member HP + position for the party HUD and screen). Roster changes always push immediately. Clamped 10-100. Default 20. |
