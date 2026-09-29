# Ultimate Arroganz

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:ultimate_arroganz` |
| **Max mastery** | 15,000 |
| **Activation** | Press, Hold |

</div>

> Powerful toolkit for Arroganz-related skill creation, duplication and storage.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | *set by config (base cost (ego ultimate cost))* |  |
| Always | var14 (ego ultimate cost) |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Adjusted by scrolling while active
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers on melee contact
- Triggers when you are attacked
- Triggers when you take damage
- Triggers when an effect is applied to you
- Triggers when a projectile hits you
- Triggers when you die
- Triggers when you respawn
- Does something when first learned

## Obtaining

- Listed in the `blacklistedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that are banned from being transferred through Food Chain.
- Listed in the `excludedSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that Skill Storage will NOT store when obtained (blacklist).
- Acquisition checks: [｢ Lucifer, Lord of Pride ｣](lucifer.md)
- In-game message: *The Unique Skill Pride has evolved into the Ultimate Skill. Lucifer, Lord of Pride.*

## Related

- **Related skills:** [｢ Lucifer, Lord of Pride ｣](lucifer.md), [Material Creation](../intrinsic-skills/material-creation.md)
- **Referenced by:** [｢ Nodens, God of Abyss ｣](nodens.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_extra.toml`](../../configs/config-nightmare-ability-skill-nightmare-extra.md).

| Option | Default | Description |
|---|---|---|
| `UltimateArroganz.allowedSkillIds` | [] (empty) | Skill ids or options related to Ultimate Arroganz. Empty = default behavior. |

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Lucifer.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Lucifer.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Lucifer.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Lucifer.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Lucifer.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Lucifer.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Lucifer.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Lucifer.mpAcquirement` | 1,700,000 | The Cost for the Ultimate Skill: Lucifer. |
| `Lucifer.copyChance` | 20 | The skill copy chance when attacked (Arroganz). Matches Tensura Pride defaults. |
| `Lucifer.copyChanceMastered` | 100 | The skill copy chance when attacked with mastery. |
| `Lucifer.copyMastery` | 0.0004 | Mastery gained per magicule cost of a successfully copied ability. |
| `Lucifer.copyMasteryFail` | 0 | Multiplier of mastery gained per magicule cost of a failed copy attempt. |
| `Lucifer.copyCooldown` | 45 | Cooldown in seconds per mastery gained from a successful copy. |
| `Lucifer.copyCooldownFail` | 4.5 | Cooldown in seconds per mastery gained from a failed copy. |
| `Lucifer.ocularAnalysisCooldown` | 0 | Cooldown ticks applied to Ocular Analysis (mode 1) after attempts. Arroganz uses copyCooldown \* mastery on slot 0. |
| `Lucifer.LuciferMastered` | 100 | Number of mastered skills required for Lucifer evolution. |
| `Lucifer.LuciferHPPercentage` | 0.4 | HP percentage threshold for Lucifer evolution. |
| `Lucifer.enableUltimateEvolution` | true | Whether Lucifer evolution is allowed. If false, Pride cannot evolve into Lucifer. |
| `Lucifer.copyRanged` | 25 | This is the range of the projectile copying of Lucifer. |
| `Lucifer.copyRange` | 5 | This is the range of the normal copying of Lucifer. |

## Tags

`tensura:skills/no_plundering`
