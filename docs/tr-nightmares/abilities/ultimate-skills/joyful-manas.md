# Joyful Manas

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:joyful_manas` |
| **Acquisition cost (MP)** | 900,000 |
| **Max mastery** | 3,000 |
| **Activation** | Toggle, Press, Hold |

</div>

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | *set by config (base cost (ego ultimate cost))* |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Does something when first learned

## Obtaining

- Acquisition checks: [｢ Raguel, Lord of Charity ｣](raguel.md)
- In-game message: *You have awakened Raguel, Lord of Charity.*

## Related

- **Related skills:** [｢ Raguel, Lord of Charity ｣](raguel.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Raguel.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Raguel.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Raguel.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Raguel.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Raguel.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Raguel.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Raguel.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Raguel.mpAcquirement` | 900,000 | Magicule obtainment cost. |
| `Raguel.maxMastery` | 3,000 | Max mastery. |
| `Raguel.parallelMaxClones` | 3 | Parallel mode max clones. |
| `Raguel.parallelCooldownSeconds` | 5 | Parallel mode cooldown (Tensura seconds). |
| `Raguel.cardinalDashSpeed` | 1.6 | Cardinal dash speed (not mastered). |
| `Raguel.cardinalDashSpeedMastered` | 2.2 | Cardinal dash speed (mastered). |
| `Raguel.cardinalCooldownSeconds` | 5 | Cardinal mode cooldown after release (Tensura seconds). |
| `Raguel.cardinalMasteryTickInterval` | 20 | Cardinal mastery tick interval while channeling (ticks). |
| `Raguel.cardinalBeamFlameDamage` | 250 | Cardinal beam flame damage (not mastered). |
| `Raguel.cardinalBeamFlameDamageMastered` | 350 | Cardinal beam flame damage (mastered). |
| `Raguel.cardinalBeamEnergyCost` | 50 | Cardinal beam energy cost per tick pair second value. |
| `Raguel.cardinalBeamThickness` | 0.5 | Cardinal beam thickness. |
| `Raguel.cardinalBeamDurationTicks` | 21 | Cardinal beam duration ticks. |
| `Raguel.cardinalBeamRange` | 105 | Cardinal beam range. |
| `Raguel.cardinalBeamInaccuracy` | 0 | Cardinal beam inaccuracy. |
| `Raguel.cardinalDashFlameDamage` | 350 | Cardinal dash bonus flame damage (not mastered). |
| `Raguel.cardinalDashFlameDamageMastered` | 500 | Cardinal dash bonus flame damage (mastered). |
| `Raguel.cardinalDashHitboxRadius` | 2.5 | Cardinal dash hitbox inflate radius. |
| `Raguel.cardinalMoveSpeedBaseline` | 0.1 | Movement speed baseline used for cardinal speed scaling. |
| `Raguel.cardinalSpeedBonusPerTenth` | 0.2 | Cardinal speed scaling bonus per tenth over baseline. |
| `Raguel.evolutionRaidWins` | 25 | Raid wins required to evolve Endorse into Raguel. |
| `Raguel.evolutionCuredZombieVillagers` | 1 | Cured zombie villagers required to evolve Endorse into Raguel. |
| `Raguel.enableUltimateEvolution` | true | Whether Raguel evolution is allowed. |

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `endorse.mpAcquirement` | 90,000 | Magicule obtainment cost. |
| `endorse.mpAcquirement` | 90,000 | Magicule obtainment cost. |
| `endorse.maxMastery` | 1,000 | Max mastery. |
| `endorse.stockpileCooldownSeconds` | 5 | Stockpile mode cooldown (Tensura seconds). |
