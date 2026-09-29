# ｢ Samael, Lord of Deadly Poison ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:samael` |
| **Modes** | 6 |
| **Acquisition cost (MP)** | 900,000 |
| **Max mastery** | 15,000 |
| **Activation** | Toggle, Press, Hold |

</div>

> The ultimate evolution of Deadly Poison — Death World, nihility, and absolute barrier control.

## Modes

| # | Mode |
|---|---|
| 1 | Bloody Bite |
| 2 | Poison Refinement |
| 3 | Death World |
| 4 | Nihilistic Poison |
| 5 | Nihility Supply |
| 6 | Multidimensional Barrier |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers on melee contact
- Triggers when an effect is applied to you
- Does something when first learned

## Obtaining

- Listed in the `astralMasteredCreationUltimates` config option (config/nightmare/ability/skill/nightmare_ult.toml): Ultimate skill IDs only offered from Astral Light Skill Creation when Astral Light is mastered.
- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.
- Listed in the `compatibleUltimateSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Ultimate (or skill) resource ids that enable learning Spacetime Domination when possessed. Empty = unobtainable. Designer fill-in, e.g....
- Listed in the `allowedSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can be affected by Raphael-style alteration by default.
- Acquisition checks: [｢ Samael, Lord of Deadly Poison ｣](samael.md), [Deadly Poison](../unique-skills/deadly-poison.md)
- In-game message: *Deadly Poison has ripened into Samael, Lord of Deadly Poison.*

## Related

- **Related skills:** [Deadly Poison](../unique-skills/deadly-poison.md), [Spacetime Manipulation](../extra-skills/spacetime-manipulation.md)
- **Effects:** [Cursed Poison](../../effects/cursed-poison.md)
- **Referenced by:** [Alteration](../extra-skills/alteration.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Samael.mpAcquirement` | 900,000 |  |
| `Samael.maxNihility` | 25,000 |  |
| `ultMasteryConfig.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `ultMasteryConfig.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `ultMasteryConfig.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `ultMasteryConfig.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `ultMasteryConfig.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `ultMasteryConfig.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `ultMasteryConfig.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `ultMasteryConfig.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Samael.enableUltimateEvolution` | true |  |
| `Samael.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Samael.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Samael.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Samael.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Samael.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Samael.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Samael.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Samael.enableUltimateEvolution` | true |  |
| `Samael.mpAcquirement` | 900,000 |  |
| `Samael.mobKillsRequired` | 1,500 |  |
| `Samael.lethalDoseFullRequired` | 25 |  |
| `Samael.maxNihility` | 25,000 |  |
| `Samael.nihilityPerLethalDosePercent` | 1 |  |
| `Samael.nihilisticNihilityDrain` | 3.5 |  |
| `Samael.nihilisticNihilityDrainMastered` | 2 |  |
| `Samael.nihilisticTargetDoseBonus` | 5 |  |
| `Samael.nihilisticBurstSpiritual` | 200 |  |
| `Samael.nihilisticBurstNihilityFraction` | 0.1 |  |
| `Samael.nihilityPerSpatialDamage` | 20 |  |
| `Samael.barrierHealthMultiplier` | 4 |  |
| `Samael.barrierHealthMultiplierMastered` | 6 |  |
| `Samael.deathWorldDurationTicks` | 1,200 |  |
| `Samael.deathWorldSpiritualPerSecond` | 25 |  |
| `Samael.deathWorldNihilityVoidFraction` | 0.05 |  |

## In-game messages

<details markdown><summary>Show 6 messages</summary>

- +%s Nihility
- Not enough Nihility.
- Target Lethal Dose: %s%%
- Nihilistic Poison burst!
- Death World invoked.
- Death World released.

</details>

## Tags

`tensura:skills/ultimate_skills`
