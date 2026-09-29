# `config/tensura/EliteTensura/WalpurgisConfig.toml`

<small>[Elite Tensura](../index.md) &rsaquo; [Configs](index.md)</small>

## `[WalpurgisCore]`

| Option | Default | Range | Description |
|---|---|---|---|
| `MIN_CONVENERS` | 3 |  | How many players does it take to call Walpurgis |
| `CONVENE_WINDOW_MINS` | 10 |  | Pending invitation stays open before expiring in Minutes |
| `AGENDA_PHASE_MINS` | 5 |  | The agenda-submission phase in Minutes |
| `VOTE_PHASE_MINS` | 5 |  | Deliberation/voting phase in Minutes |
| `VOTE_EXTENSION_MINS` | 2 |  | Extra Minutes granted per extension while votes are still missing |
| `VOTE_HARD_CAP_MINS` | 15 |  | Hard cap in Minutes a single motion may stay in deliberation before it resolves regardless of missing votes |
| `COOLDOWN_MINS` | 150 |  | Cooldown for the Walpurgis in Minutes (150 = 2.5 hours) |
| `DUEL_INVITE_SECONDS` | 60 |  | The council waits for a Combat Clause challenge after a tied vote |
| `ACCEPT_WINDOW_SECONDS` | 30 |  | The timer for the defender to accept or deny the challenge |
| `MAX_DUEL_MINS` | 5 |  | duel may run before timing out at said Minutes |

## `[Seal]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enableBuffs` | true |  | Enable the Walpurgis Seal passive regen buffs while carried |
| `magiculeRegenBonus` | 0.1 |  | Magicule regeneration multiplier bonus added while carrying the Seal |
| `auraRegenBonus` | 0.1 |  | Aura regeneration multiplier bonus added while carrying the Seal |
| `voteWeight` | 2 |  | How many votes a Seal-holder's ballot counts as in deliberation |
