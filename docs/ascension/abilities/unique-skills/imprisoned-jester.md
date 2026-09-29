# Imprisoned Jester

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Imprisoned Jester](../../../assets/icons/ascension/skill/imprisoned_jester.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `ascension:imprisoned_jester` |
| **Modes** | 2 |
| **Cooldowns (s)** | 600 |
| **Activation** | Press, Hold |

</div>

> Equipped: +20% physical and magic damage, +10% crit (+10% physical / +10% crit mastered). Toggle: reflect 25% of incoming physical damage. Forces your alignment to Chaos. Modes: Chaos Spades (white-flame Soul-damage breath scaling with EP, capped at 10M EP), Explosive Goodbye (below 25% HP, detonate for missing-HP damage to nearby enemies' HP and SHP — kills you).

## Modes

| # | Mode |
|---|---|
| 1 | Chaos Spades |
| 2 | Explosive Goodbye |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key

## Obtaining

- Listed in the `additionalUniqueSkills` config option (config/tensura/ascension-common.toml): Unique skills added to the reincarnation pool. Remove an entry to exclude that skill from random reincarnation rolls.

## Related

- **Summons / entities:** Chaos Spades

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `imprisoned_jester.enabled` | true | Enable Imprisoned Jester. |
| `imprisoned_jester.chaosEpCap` | 10,000,000 (1 to 1,000,000,000,000) | EP cap used for Chaos Spades damage scaling. EP above this value is ignored for scaling. |
| `imprisoned_jester.chaosEpFactor` | 0.001 (0 to 1) | Soul-HP damage per point of effective EP (0.001 = 10000 SHP at the 10M cap). |
| `imprisoned_jester.explodeHpThreshold` | 0.25 (0 to 1) | Max HP fraction the caster must be below to cast Explosive Goodbye (0.25 = under 25% HP). |
| `imprisoned_jester.explodeRadius` | 10 (0 to 64) | Explosive Goodbye radius in blocks. |
| `imprisoned_jester.explodeCooldownSeconds` | 600 (0 to 36,000) | Explosive Goodbye cooldown (seconds) — moot since it kills the caster, but applied for symmetry if they get revived. |
| `imprisoned_jester.physicalBonus` | 0.2 (0 to 10) | In-slot outgoing physical damage bonus, unmastered (0.20 = +20%). |
| `imprisoned_jester.physicalBonusMasteredAdd` | 0.1 (0 to 10) | Additional in-slot physical bonus added on top of base when mastered (0.10 = +10% more, total +30%). |
| `imprisoned_jester.magicBonus` | 0.2 (0 to 10) | In-slot outgoing Tensura-magic damage bonus (0.20 = +20%). |
| `imprisoned_jester.critChance` | 0.1 (0 to 1) | In-slot crit chance per hit, unmastered (0.10 = 10%). Crit deals +50% damage. |
| `imprisoned_jester.critChanceMasteredAdd` | 0.1 (0 to 1) | Additional crit chance added on top of base when mastered (0.10 = +10% more, total 20%). |
| `unbound_jester.gateSpiritDamage` | 1,000,000 (0 to 1,000,000,000,000) | Cumulative spirit damage required to qualify for the awakening (lifetime, while Imprisoned Jester is in slot). |
| `imprisoned_jester.reflectFraction` | 0.25 (0 to 10) | Fraction of incoming physical damage reflected to attacker while toggled on (0.25 = 25%). |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## In-game messages

<details markdown><summary>Show 1 messages</summary>

- You must be below 25% HP to activate Explosive Goodbye.

</details>

## Tags

`tensura:skills/unique_skills`
