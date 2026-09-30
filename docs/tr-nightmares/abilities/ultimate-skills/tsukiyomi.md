# ｢ Tsukiyomi, Lord of Moonshadow ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![｢ Tsukiyomi, Lord of Moonshadow ｣](../../../assets/icons/trnightmare/skill/tsukiyomi.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:tsukiyomi` |
| **Modes** | 6 |
| **Acquisition cost (MP)** | 600,000 |
| **Max mastery** | 5,000 |
| **Cooldowns (s)** | 6 mastered, 12 otherwise, 5 |
| **Activation** | Toggle, Press, Hold |

</div>

> Striking out from the unknown has always been one of your talents, and now even the laws of the world itself find it hard to see your attacks from the dark side of the moon.

## Modes

| # | Mode |
|---|---|
| 1 | Instant Kill |
| 2 | Ultraspeed Action |
| 3 | Eye Of The Moon |
| 4 | Assassinate |
| 5 | Thousand Shadow Deaths |
| 6 | Parallel Existence |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Instant Kill | 30,000 | 500 |
| Ultraspeed Action | 12,000 | *set by config (base aura cost)* |
| other modes | *set by config (base cost)* |  |
| Assassinate | 15,000 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers when an effect is applied to you

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| dodgeB | 0.5 | add |
| dodge | 0.8 | add |

## Obtaining

- Listed in the `astralMasteredCreationUltimates` config option (config/nightmare/ability/skill/nightmare_ult.toml): Ultimate skill IDs only offered from Astral Light Skill Creation when Astral Light is mastered.
- Listed in the `allowedSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can be affected by Raphael-style alteration by default.
- Acquisition checks: [Shadow Striker](../../../tensura-reincarnated/abilities/unique-skills/shadow-striker.md), [｢ Tsukiyomi, Lord of Moonshadow ｣](tsukiyomi.md)
- In-game message: *The world is having difficulties locating you, there is no stopping your progression, become one with the night, and let the night come to you... Moonshadow.*

## Related

- **Related skills:** [Shadow Striker](../../../tensura-reincarnated/abilities/unique-skills/shadow-striker.md)
- **Effects:** [Mind Control](../../../tensura-reincarnated/effects/mind-control.md), [Presence Concealment](../../../tensura-reincarnated/effects/presence-concealment.md), [Movement Interference](../../../tensura-reincarnated/effects/movement-interference.md)
- **Summons / entities:** Tensura, Shadow Bind Hands
- **Referenced by:** [Alteration](../extra-skills/alteration.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Tsukiyomi.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Tsukiyomi.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Tsukiyomi.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Tsukiyomi.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Tsukiyomi.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Tsukiyomi.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Tsukiyomi.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Tsukiyomi.mpAcquirement` | 600,000 | Magicule cost required to acquire Tsukiyomi. |
| `Tsukiyomi.killMagiculeCost` | 30,000 | Magicule cost of Instant Kill. |
| `Tsukiyomi.killDamage` | 2,500 | Instant Kill damage (unmastered). |
| `Tsukiyomi.killDamageMastered` | 5,000 | Instant Kill damage (mastered). |
| `Tsukiyomi.killCooldown` | 12 | Instant Kill cooldown (ticks). |
| `Tsukiyomi.killCooldownMastered` | 6 | Instant Kill cooldown when mastered (ticks). |
| `Tsukiyomi.ultraMagiculeCost` | 12,000 | Magicule cost of Ultraspeed Action. |
| `Tsukiyomi.ultraDistance` | 10 | Ultraspeed Action range (unmastered). |
| `Tsukiyomi.ultraDistanceMastered` | 14 | Ultraspeed Action range (mastered). |
| `Tsukiyomi.ultraDamage` | 100 | Ultraspeed Action bonus damage (unmastered). |
| `Tsukiyomi.ultraDamageMastered` | 370 | Ultraspeed Action bonus damage (mastered). |
| `Tsukiyomi.eyeAuraCost` | 500 | Aura cost per tick while Eye of the Moon is toggled. |
| `Tsukiyomi.eyeDodgeStrength` | 0.8 | Dodge chance bonus while Eye of the Moon is active. |
| `Tsukiyomi.eyeDodgeInvulnerability` | 0.5 | Dodge bypass while Eye of the Moon is active. |
| `Tsukiyomi.eyeConcealmentLevel` | 0 | Optional concealment level while Eye of the Moon is active. |
| `Tsukiyomi.eyeRange` | 16 | Maximum range for shadow shift while Eye of the Moon is active. |
| `Tsukiyomi.assassinateMagiculeCost` | 15,000 | Magicule cost of Assassinate. |
| `Tsukiyomi.assassinateRequiredUses` | 500 | Instant Kill uses required to unlock Assassinate. |
| `Tsukiyomi.assassinateDamage` | 2,000 | Assassinate damage (unmastered). |
| `Tsukiyomi.assassinateDamageMastered` | 4,000 | Assassinate damage (mastered). |
| `Tsukiyomi.assassinateLightPenalty` | 0.5 | Damage multiplier when target is in natural light. |
| `Tsukiyomi.assassinateConcealmentLevel` | 3 | Concealment level while charging Assassinate. |
| `Tsukiyomi.assassinateChargeTime` | 40 | Ticks required to fully charge Assassinate. |
| `Tsukiyomi.shadowDeathShpDamage` | 250 | Shadow Death SHP damage. |
| `Tsukiyomi.shadowDeathDarknessDamage` | 250 | Shadow Death Darkness damage. |
| `Tsukiyomi.shadowDeathDuration` | 60 | Shadow Death bind duration . |
| `Tsukiyomi.enableUltimateEvolution` | true | Enable evolution from Shadow Striker to Tsukiyomi. |
| `Tsukiyomi.tsukiMobs` | 500 | Mobs slain for Tsukiyomi |
| `Tsukiyomi.tsukiHealth` | 50 | Health Percentage for Tsukiyomi |
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

## Tags

`tensura:skills/ultimate_skills`
