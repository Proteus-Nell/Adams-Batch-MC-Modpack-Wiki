# ｢ Uriel, Lord of Vows ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![｢ Uriel, Lord of Vows ｣](../../../assets/icons/trnightmare/skill/uriel_lord_of_vow.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:uriel_lord_of_vow` |
| **Modes** | 4 |
| **Acquisition cost (MP)** | 1,750,000 |
| **Max mastery** | 5,000 |
| **Cooldowns (s)** | 15, 3, 20 |
| **Activation** | Press |

</div>

> True Uriel awakened from Infinity Prison. It grants believer scaling, absolute guard, imprisoning authority, severing force, and a bound Imaginary Space that stores blocked energy.

## Modes

| # | Mode |
|---|---|
| 1 | Imprison |
| 2 | Absolute End |
| 3 | Nova Break |
| 4 | Imaginary Space |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | *set by config (base cost (ego ultimate cost))* |  |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you take damage
- Triggers when an effect is applied to you

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| learning | capped count | add |
| mastery | capped count | add |

## Obtaining

- Listed in the `virtueDominionSkills` config option (config/nightmare/ability/skill/nightmare_ult.toml): Virtue skills that Ultimate Dominion can copy from targets.
- Acquisition checks: [Infinity Prison](../../../tensura-reincarnated/abilities/unique-skills/infinity-prison.md), [｢ Uriel, Lord of Vows ｣](uriel-lord-of-vow.md)
- In-game message: *The cheers of your subordinates empower you, your acts of heroism have garned many people to believe in you, you have taken a vow to protect them... Your Unique Skill: Infinity Prison has evolved into the Ultimate Skill: Uriel*

## Related

- **Related skills:** [Infinity Prison](../../../tensura-reincarnated/abilities/unique-skills/infinity-prison.md)
- **Effects:** [Infinite Imprisonment](../../../tensura-reincarnated/effects/infinite-imprisonment.md), [Holy Damage](../../../tensura-reincarnated/effects/holy-damage.md), [Magic Interference](../../../tensura-reincarnated/effects/magic-interference.md), [Anti-Skill](../../../tensura-reincarnated/effects/anti-skill.md)
- **Summons / entities:** [Severance](../../../tensura-reincarnated/enchantments/severance.md)
- **Referenced by:** [｢ Uriel, Lord of Oaths ｣](uriel-lord-of-oath.md), [Paladin Manas](paladin-manas.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `UrielVow.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `UrielVow.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `UrielVow.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `UrielVow.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `UrielVow.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `UrielVow.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `UrielVow.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `UrielVow.mpAcquirement` | 1,750,000 | Magicule cost to acquire Uriel Lord of Vow. |
| `UrielVow.guardMpPerDamage` | 15 | Absolute Guard MP cost per 1 blocked damage. |
| `UrielVow.guardBypassEpRatio` | 0.8 | Attackers with EP &gt;= owner EP \* this can bypass Absolute Guard. |
| `UrielVow.imprisonCost` | 50,000 | Imprison MP cost. |
| `UrielVow.imprisonRange` | 16 | Imprison range. |
| `UrielVow.imprisonDuration` | 600 | Imprison duration in seconds. |
| `UrielVow.imprisonDurationMastered` | 1,200 | Imprison duration in seconds when mastered. |
| `UrielVow.imprisonCooldown` | 15 | Imprison cooldown in seconds. |
| `UrielVow.imprisonMissCooldown` | 15 | Imprison miss cooldown in seconds. |
| `UrielVow.imprisonMissCooldownMastered` | 10 | Imprison miss cooldown in seconds when mastered. |
| `UrielVow.imprisonDrainPerPulse` | 500 | Magicules drained from imprisoned targets every 10 ticks. |
| `UrielVow.absoluteEndCost` | 50,000 | Absolute End MP cost. |
| `UrielVow.absoluteEndDamage` | 350 | Absolute End damage. |
| `UrielVow.absoluteEndDamageMastered` | 450 | Absolute End damage when mastered. |
| `UrielVow.absoluteEndSize` | 8 | Absolute End cutter size. |
| `UrielVow.absoluteEndSizeMastered` | 12 | Absolute End cutter size when mastered. |
| `UrielVow.absoluteEndCooldown` | 3 | Absolute End cooldown in seconds. |
| `UrielVow.novaBreakCost` | 175,000 | Nova Break MP cost. |
| `UrielVow.novaBreakSpaceDamage` | 200 | Nova Break space damage. |
| `UrielVow.novaBreakHolyDamage` | 200 | Nova Break holy damage. |
| `UrielVow.novaBreakSeveranceDamage` | 200 | Nova Break severance damage. |
| `UrielVow.novaBreakRange` | 16 | Nova Break range. |
| `UrielVow.novaBreakLength` | 20 | Nova Break ground break length. |
| `UrielVow.novaBreakHalfWidth` | 1 | Nova Break half-width for the ground slash. |
| `UrielVow.novaBreakCooldown` | 20 | Nova Break cooldown in seconds. |
| `UrielVow.imaginarySpaceSlots` | 108 | Imaginary Space slot count (27 = one chest page). |
| `UrielVow.imaginarySpaceStack` | 999 | Imaginary Space max stack size. |
| `UrielVow.believerRange` | 128 | Radius to scan loaded subordinates. |
| `UrielVow.believerMaxBonus` | 12 | Maximum bonus cap for Believer system (+Learning and +Mastery per subordinate). |
| `UrielVow.urielRaidCount` | 25 | Raids to obtain Uriel. |
| `UrielVow.urielSubCount` | 50 | Subs to obtain Uriel. |
| `UrielVow.enableUltimateEvolution` | true | Whether Uriel evolution is allowed. |

## Tags

`tensura:skills/paladin`, `tensura:skills/ultimate_skills`
