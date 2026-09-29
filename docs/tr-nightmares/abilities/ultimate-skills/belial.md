# ｢ Belial, Lord of The Dead ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![｢ Belial, Lord of The Dead ｣](../../../assets/icons/trnightmare/skill/belial.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:belial` |
| **Modes** | 4 |
| **Acquisition cost (MP)** | 900,000 |
| **Max mastery** | 15,000 |
| **Cooldowns (s)** | 50, 60, 10, 2 |
| **Activation** | Press, Hold |

</div>

> Ultimate underworld flame: All of Creation, spacetime, soul bank, nihilistic world, white flare, and nihility.

## Modes

| # | Mode |
|---|---|
| 1 | Nihilistic World |
| 2 | White Flare |
| 3 | Nihility Supply |
| 4 | Nihilistic End |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Nihilistic World | 100,000 |  |
| White Flare | 25,000 |  |
| other modes | 0 |  |
| Nihilistic End | 125,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when you damage a target
- Does something when first learned

## Obtaining

- Listed in the `astralMasteredCreationUltimates` config option (config/nightmare/ability/skill/nightmare_ult.toml): Ultimate skill IDs only offered from Astral Light Skill Creation when Astral Light is mastered.
- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.
- Listed in the `allowedSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can be affected by Raphael-style alteration by default.
- Acquisition checks: [Freezing Flame](../unique-skills/freezing-flame.md), [｢ Belial, Lord of The Dead ｣](belial.md)
- In-game message: *The underworld acknowledges you. Belial awakens.*

## Related

- **Related skills:** [Freezing Flame](../unique-skills/freezing-flame.md)
- **Referenced by:** [Alteration](../extra-skills/alteration.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Belial.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Belial.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Belial.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Belial.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Belial.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Belial.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Belial.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Belial.enableUltimateEvolution` | true |  |
| `Belial.mpAcquirement` | 900,000 |  |
| `Belial.maxNihility` | 25,000 |  |
| `Belial.whiteFlareLearnPoints` | 500 |  |
| `Belial.nihilisticEndLearnPoints` | 1,000 |  |
| `Belial.nihilisticEndMaxNuclear` | 1,000 |  |
| `Belial.nihilisticEndMaxVoid` | 1,000 |  |
| `Belial.nihilisticEndCooldown` | 60 |  |
| `Belial.mobKillsRequired` | 4,500 |  |
| `Belial.flameSkillsMastered` | 5 |  |
| `Belial.subordinatesRequired` | 15 |  |
| `Belial.magiculeCostNihilisticWorld` | 100,000 |  |
| `Belial.magiculeCostWhiteFlarePerTick` | 2,500 |  |
| `Belial.magiculeCostNihilisticEnd` | 125,000 |  |
| `Belial.whiteFlareRadius` | 4 |  |
| `Belial.whiteFlareRadiusMastered` | 6 |  |
| `Belial.whiteFlareRange` | 32 |  |
| `Belial.whiteFlareRangeMastered` | 48 |  |
| `ultMasteryConfig.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `ultMasteryConfig.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `ultMasteryConfig.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `ultMasteryConfig.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `ultMasteryConfig.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `ultMasteryConfig.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `ultMasteryConfig.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `ultMasteryConfig.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |

## Tags

`tensura:skills/ultimate_skills`
