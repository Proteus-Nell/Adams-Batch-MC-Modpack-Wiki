# Tempter

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:tempter` |
| **Modes** | 5 |
| **Acquisition cost (MP)** | 90,000 |
| **Max mastery** | 15,000 |
| **Cooldowns (s)** | 1,200, 500, 15 |
| **Activation** | Press |

</div>

> Unique temptation — Charm, Temptation World, Reality Exchange, Solicitation, and End of World.

## Modes

| # | Mode |
|---|---|
| 1 | Charm |
| 2 | Temptation World |
| 3 | Reality Exchange |
| 4 | Solicitation |
| 5 | End of World |

## How it works

- Activated by pressing the skill key
- Triggers when you are attacked

## Obtaining

- Listed in the `astralExtraUniqueSkills` config option (config/nightmare/ability/skill/nightmare_ult.toml): Extra unique skill IDs merged into Astral Light Skill Creation (after Tensura Creator).
- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.

## Related

- **Referenced by:** [Alteration](../extra-skills/alteration.md), [｢ Azazel, Lord of Temptation ｣](../ultimate-skills/azazel.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `Tempter.mpAcquirement` | 90,000 |  |
| `Tempter.seekerMasteredSkills` | 50 |  |
| `Tempter.tempterMasteredSpells` | 50 |  |
| `Tempter.solicitationLearnPoints` | 300 |  |
| `Tempter.endOfWorldLearnPoints` | 500 |  |
| `Tempter.copyChance` | 35 |  |
| `Tempter.copyChanceMastered` | 75 |  |
| `Tempter.copyCooldown` | 15 |  |

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `ultMasteryConfig.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `ultMasteryConfig.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `ultMasteryConfig.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `ultMasteryConfig.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `ultMasteryConfig.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `ultMasteryConfig.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `ultMasteryConfig.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `ultMasteryConfig.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
