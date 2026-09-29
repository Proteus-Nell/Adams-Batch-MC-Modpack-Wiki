# ｢ Shub-Niggurath, King of Harvest ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:shub_niggurath` |
| **Modes** | 1 |
| **Acquisition cost (MP)** | 1,200,000 |
| **Max mastery** | 5,000 |
| **Activation** | Press |

</div>

> Harvest of every skill you have owned. Store memories, recreate lost arts, craft new ones, duplicate mastered creations, and gift analyzed skills to allies.

## Modes

| # | Mode |
|---|---|
| 1 | Skill Gifting |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Does something when first learned

## Obtaining

- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.
- Listed in the `skillEngraveBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skills that cannot be engraved through Amatsumara skill engrave.
- In-game message: *%s has reached its final threshold. &lt; Press %s to open the Evolution Menu and obtain Shub Niggurath. &gt;*

## Related

- **Related skills:** [Skill Storage](../extra-skills/skill-storage.md)
- **Referenced by:** [｢ Tenebrosum, God of Souls ｣](tenebrosum.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `ShubNiggurath.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `ShubNiggurath.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `ShubNiggurath.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `ShubNiggurath.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `ShubNiggurath.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `ShubNiggurath.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `ShubNiggurath.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `ShubNiggurath.mpAcquirement` | 1,200,000 | Magicule obtainment cost. |
| `ShubNiggurath.destroyMasteryCommon` | 25 | Shub mastery rewarded when destroying a common skill memory. |
| `ShubNiggurath.destroyMasteryUnique` | 300 | Shub mastery rewarded when destroying a unique skill memory. |
| `ShubNiggurath.destroyMasteryUltimate` | 1,000 | Shub mastery rewarded when destroying an ultimate skill memory. |
| `ShubNiggurath.duplicateThreshold` | 1 | Creation count required before duplication unlocks. |
| `ShubNiggurath.creationCooldownHighSeconds` | 600 | Creation cooldown for unique/ultimate copies (Tensura seconds). |
| `ShubNiggurath.creationCooldownLowSeconds` | 2 | Creation cooldown for common skill copies (Tensura seconds). |
| `ShubNiggurath.enableUltimateEvolution` | true | Whether Shub evolution is allowed. |

## Tags

`tensura:skills/paladin`, `tensura:skills/ultimate_skills`
