# Trash Gamer

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Trash Gamer](../../../assets/icons/ascension/skill/trash_gamer.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `ascension:trash_gamer` |
| **Modes** | 3 |
| **Cooldowns (s)** | 600, 1,800 |
| **Activation** | Press |

</div>

> Equipped: +4 to every mastery point gained on every skill. Modes: Duplication Glitch (dupe held item, costs 50%% current MP, 600s CD; 25%% MP mastered), Buff Glitch (random positive effect for 3 min at level 1–10, 60s CD; 10s mastered), Prodigy (10 min: 1 HP, +99%% dodge, +20%% speed, ×5 outgoing damage to bypass resistances; on end: paralysis 10 for 3 min and full aura/MP drain).

## Modes

| # | Mode |
|---|---|
| 1 | Duplication Glitch |
| 2 | Buff Glitch |
| 3 | Prodigy |

## How it works

- Activated by pressing the skill key

## Obtaining

- Listed in the `additionalUniqueSkills` config option (config/tensura/ascension-common.toml): Unique skills added to the reincarnation pool. Remove an entry to exclude that skill from random reincarnation rolls.

## Related

- **Effects:** [Paralysis](../../../tensura-reincarnated/effects/paralysis.md)

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `trash_gamer.duplicationBlacklist` | "minecraft:bundle", "minecraft:shulker_box", "minecraft:white_shulker_box", "minecraft:orange_shulker_box", "minecraft:magenta_shulker_box", "minecraft:light_blue_shulker_box", "minecraft:yellow_shulker_box", "minecraft:lime_shulker_box", "minecraft:pink_shulker_box", "minecraft:gray_shulker_box", "minecraft:light_gray_shulker_box", "minecraft:cyan_shulker_box", "minecraft:purple_shulker_box", "minecraft:blue_shulker_box", "minecraft:brown_shulker_box", "minecraft:green_shulker_box", "minecraft:red_shulker_box", "minecraft:black_shulker_box" | Item IDs that Duplication Glitch refuses to copy. Use full registry IDs<br>(namespace:path). Vanilla container components (bundle / shulker) are<br>ALSO blocked automatically and don't need to be listed here — this list<br>is for items that hold inventory on the stack without using the standard<br>vanilla components, e.g. modded backpacks. |
| `trash_gamer.enabled` | true | Enable Trash Gamer. |
| `trash_gamer.duplicationMpFractionMastered` | 0.25 (0 to 1) | Fraction of CURRENT magicule consumed per Duplication Glitch cast, mastered. |
| `trash_gamer.duplicationMpFraction` | 0.5 (0 to 1) | Fraction of CURRENT magicule consumed per Duplication Glitch cast, unmastered (0.50 = 50%). |
| `trash_gamer.duplicationCooldownSeconds` | 600 (0 to 36,000) | Duplication Glitch cooldown (seconds). |
| `trash_gamer.buffDurationSeconds` | 180 (1 to 7,200) | Buff Glitch effect duration (seconds). |
| `trash_gamer.buffCooldownSecondsMastered` | 10 (0 to 3,600) | Buff Glitch cooldown (seconds), mastered. |
| `trash_gamer.buffCooldownSeconds` | 60 (0 to 3,600) | Buff Glitch cooldown (seconds), unmastered. |
| `trash_gamer.prodigySpeedBonus` | 0.2 (0 to 10) | Movement-speed bonus during Prodigy (0.20 = +20%). |
| `trash_gamer.prodigyDurationSeconds` | 600 (1 to 7,200) | Prodigy duration (seconds). Default 600s = 10 minutes. |
| `trash_gamer.prodigyCooldownSeconds` | 1,800 (0 to 36,000) | Prodigy cooldown (seconds). |
| `trash_gamer.prodigyParalysisSeconds` | 180 (0 to 3,600) | Paralysis duration (seconds) applied when Prodigy ends. |
| `trash_gamer.masteryBonus` | 4 (0 to 1,000) | Flat mastery-point bonus added to every mastery gain on every skill while Trash Gamer is learned. |
| `trash_gamer.prodigyDodgeChance` | 0.99 (0 to 1) | Per-incoming-hit dodge chance during Prodigy (0.99 = 99%). |
| `trash_gamer.prodigyDamageMult` | 5 (0 to 100) | Outgoing damage multiplier during Prodigy — stand-in for 'ignore opponent resistances and nullifications'. 5.0 = 5× damage to compensate for typical resist values. |

## In-game messages

<details markdown><summary>Show 7 messages</summary>

- Hold an item to duplicate.
- Not enough magicule.
- Cannot duplicate containers.
- Rolled %1$s %2$s for 3 minutes.
- Prodigy mode online.
- Prodigy mode crashed.
- Prodigy is already active.

</details>
