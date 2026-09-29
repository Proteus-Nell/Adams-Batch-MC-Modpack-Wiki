# Skill Storage

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `trnightmare:skill_storage` |
| **Modes** | 3 |
| **Activation** | Press |

</div>

> View and manage your learned skills; destroy to unlearn and store for later recreation.

## Modes

| # | Mode |
|---|---|
| 1 | Skill Creation |
| 2 | Skill Update |
| 3 | Skill Duplication |

## How it works

- Activated by pressing the skill key
- Does something when first learned

## Obtaining

- Listed in the `blacklistedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that are banned from being transferred through Food Chain.

## Related

- **Referenced by:** [｢ Shub-Niggurath, King of Harvest ｣](../ultimate-skills/shub-niggurath.md), [｢ Nodens, God of Abyss ｣](../ultimate-skills/nodens.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_extra.toml`](../../configs/config-nightmare-ability-skill-nightmare-extra.md).

| Option | Default | Description |
|---|---|---|
| `SkillStorage.excludedSkillIds` | "trnightmare:shub-niggurath", "trnightmare:nodens", "trnightmare:ultimate_arroganz" | Skill ids that Skill Storage will NOT store when obtained (blacklist). |
| `SkillStorage.allowedSkillIds` | [] (empty) | Skill ids that are allowed to be stored (empty = allow all not in exclusion list). |

## In-game messages

<details markdown><summary>Show 1 messages</summary>

- Update Stored Mastery

</details>

## Tags

`tensura:skills/no_plundering`
