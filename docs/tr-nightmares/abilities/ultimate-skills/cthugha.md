# ｢ Cthugha, King of Divine Flame ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:cthugha` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 2,400,000 |
| **Cooldowns (s)** | 5 |
| **Activation** | Toggle, Press, Hold |

</div>

> Ultimate flame charity — Spacetime Manipulation, stronger Amplification, Encore, Stockpile, Parallel Existence, Cardinal Acceleration, Multidimensional Barrier, and Scorch Excitation.

## Modes

| # | Mode |
|---|---|
| 1 | Multidimensional Barrier |
| 2 | Scorch Excitation |

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
- Triggers when you take damage
- Triggers when an effect is applied to you
- Does something when first learned

## Obtaining

- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.
- Listed in the `skillEngraveBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skills that cannot be engraved through Amatsumara skill engrave.
- Listed in the `allowedSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can be affected by Raphael-style alteration by default.
- Acquisition checks: [｢ Raguel, Lord of Charity ｣](raguel.md), [｢ Cthugha, King of Divine Flame ｣](cthugha.md)
- In-game message: *The King of Divine Flames awakens — you have obtained Cthugha.*

## Related

- **Related skills:** [｢ Raguel, Lord of Charity ｣](raguel.md), [Spacetime Manipulation](../extra-skills/spacetime-manipulation.md)
- **Referenced by:** [Alteration](../extra-skills/alteration.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Cthugha.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Cthugha.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Cthugha.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Cthugha.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Cthugha.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Cthugha.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Cthugha.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Cthugha.mpAcquirement` | 2,400,000 | Magicule obtainment cost. |
| `Cthugha.barrierHealthMultiplier` | 4 | Multidimensional Barrier max-health multiplier when not mastered. |
| `Cthugha.barrierHealthMultiplierMastered` | 6 | Multidimensional Barrier max-health multiplier when mastered. |
| `Cthugha.barrierToggleCooldownSeconds` | 5 | Multidimensional Barrier toggle cooldown (Tensura seconds). |
| `Cthugha.scorchRadius` | 12 | Scorch Excitation ally search radius. |
| `Cthugha.scorchSelfMagiculeOvercapRate` | 0.15 | Scorch Excitation magicule overcap rate when self-only. |
| `Cthugha.scorchAllyMagiculeOvercapRate` | 0.1 | Scorch Excitation magicule overcap rate when affecting allies. |
| `Cthugha.scorchMasteryTickStep` | 100 | Scorch Excitation mastery gain interval (ticks). |
| `Cthugha.scorchAllyBoostBaseDuration` | 240 | Scorch Excitation ally boost base duration. |
| `Cthugha.scorchInsanityBaseDuration` | 600 | Scorch Excitation insanity base duration. |
| `Cthugha.scorchAllyBoostTickStep` | 200 | Scorch Excitation ally boost progression interval. |
| `Cthugha.scorchInsanityTickStepAllies` | 300 | Scorch Excitation insanity progression interval for allies. |
| `Cthugha.scorchInsanityTickStepSelf` | 400 | Scorch Excitation insanity progression interval for self-only mode. |
| `Cthugha.evolutionMinMagiculeCap` | 2,400,000 | Minimum max magicules required to evolve Raguel into Cthugha. |
| `Cthugha.evolutionMasayuukiDefeats` | 1 | Masayuuki defeats required to evolve Raguel into Cthugha. |
| `Cthugha.enableUltimateEvolution` | true | Whether Cthugha evolution is allowed. |
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

## In-game messages

<details markdown><summary>Show 1 messages</summary>

- Stockpile  ▶  Charge: %1$s%% / %2$s%%

</details>

## Tags

`tensura:skills/joyful`, `tensura:skills/ultimate_skills`
