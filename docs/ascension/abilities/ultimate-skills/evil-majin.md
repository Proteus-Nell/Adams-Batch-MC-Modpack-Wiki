# The Evil Majin

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![The Evil Majin](../../../assets/icons/ascension/skill/evil_majin.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `ascension:evil_majin` |
| **Modes** | 3 |
| **Max mastery** | 100 |
| **Cooldowns (s)** | 2, 5 mastered, 20 otherwise |
| **Activation** | Press, Hold |

</div>

> Ultimate awakening of Bubble Majin. Toggle: full HP heal every 10s, cleanse all negative effects every 5s, reflect basic projectiles. Modes: Storage, Candy for me! (12-block AOE — turns every entity you're 2x stronger than (5x for bosses) into a single merged Majin Candy that lands in your inventory; copies all skills except ultimates), Hunger (held — pink Gluttony-style predation mist, no corrosion DOT, cost-free).

## Modes

| # | Mode |
|---|---|
| 1 | Storage |
| 2 | Candy for me! |
| 3 | Hunger |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when a projectile hits you

## Related

- **Summons / entities:** Evil Majin Hunger

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `evil_majin.enabled` | true | Enable The Evil Majin. |
| `evil_majin.reflectSpeedMultiplier` | 1.5 (0 to 100) | Reflected projectile speed multiplier. |
| `evil_majin.reflectDamageMultiplier` | 2 (0 to 100) | Reflected Tensura projectile damage multiplier. |
| `evil_majin.candyEpRetained` | 0.2 (0 to 1) | Fraction of each victim's EP rolled into the merged candy. |
| `evil_majin.candyAllowPlayers` | false | If true, players inside the AOE may be candied. PvP opt-in. |
| `evil_majin.candyCooldownSecondsMastered` | 5 (0 to 3,600) | Candy AOE cooldown, mastered (seconds). |
| `evil_majin.candyCooldownSeconds` | 20 (0 to 3,600) | Candy AOE cooldown, unmastered (seconds). |
| `evil_majin.hungerRange` | 16 (1 to 128) | Range of the Hunger mist (blocks). |
| `evil_majin.hungerDamage` | 8 (0 to 1,000,000) | Per-tick predation damage applied by the Hunger mist. |
| `evil_majin.hungerCooldownSecondsMastered` | 5 (0 to 3,600) | Hunger cooldown applied on key release, mastered (seconds). |
| `evil_majin.hungerCooldownSeconds` | 20 (0 to 3,600) | Hunger cooldown applied on key release, unmastered (seconds). |

## In-game messages

<details markdown><summary>Show 3 messages</summary>

- Nothing in range is weak enough to candy.
- %s victims candied for %s EP.
- %s was candied by %s.

</details>
