# ｢ Galatine, Sword of the Sun ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![｢ Galatine, Sword of the Sun ｣](../../../assets/icons/trnightmare/skill/galatine.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:galatine` |
| **Modes** | 4 |
| **Acquisition cost (MP)** | 4,500,000 |
| **Max mastery** | 5,000 |
| **Cooldowns (s)** | 8, 30, 15 |
| **Activation** | Press, Hold |

</div>

> An Ultimate Enchantment granted by the world for true heroism. Its power waxes and wanes with the sun — Pinnacle of Creation, Sun Cleaver, Cruel Sun, Solar Charged, and Crazy Prominence.

## Modes

| # | Mode |
|---|---|
| 1 | Sun Cleaver |
| 2 | Cruel Sun |
| 3 | Solar Charged |
| 4 | Crazy Prominence |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Sun Cleaver | 5,000 |  |
| Cruel Sun | 20,000 |  |
| other modes | 0 |  |
| Crazy Prominence | 10,000 |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Triggers when you damage a target

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| inst | amount | add |

## Obtaining

- Acquisition checks: [｢ Galatine, Sword of the Sun ｣](galatine.md), [Sunshine](../unique-skills/sunshine.md)
- In-game message: *The world acknowledges your heroism. Sunshine is reforged into Galatine.*

## Related

- **Related skills:** [Sunshine](../unique-skills/sunshine.md), [Fire Ball](../../../tensura-reincarnated/abilities/aspectual-magic/fire-ball.md)
- **Summons / entities:** Flame Orb

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Galatine.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Galatine.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Galatine.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Galatine.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Galatine.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Galatine.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Galatine.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Galatine.mpAcquirement` | 4,500,000 | Magicule cost to acquire Galatine. |
| `Galatine.enableUltimateEvolution` | true | Whether Sunshine can evolve into Galatine. |
| `Galatine.evolutionMinEp` | 3,000,000 | Minimum max EP required to evolve Sunshine into Galatine. |
| `Galatine.trueDemonLordEntities` | "trnightmare:sentient_boss_gii_crimson", "trnightmare:sentient_boss_milim_wrath" | Entity ids that count as a True Demon Lord when slain (any entity whose existence is a True Demon Lord also counts). |
| `Galatine.attackSunrise` | 10 | Pinnacle of Creation attack damage: sunrise |
| `Galatine.attackDay` | 20 | Pinnacle of Creation attack damage: day |
| `Galatine.attackNoon` | 50 | Pinnacle of Creation attack damage: noon |
| `Galatine.attackAfternoon` | 20 | Pinnacle of Creation attack damage: afternoon |
| `Galatine.attackSunset` | 10 | Pinnacle of Creation attack damage: sunset |
| `Galatine.attackNight` | -50 | Pinnacle of Creation attack damage: night |
| `Galatine.healthSunrise` | 50 | Pinnacle of Creation max health: sunrise |
| `Galatine.healthDay` | 100 | Pinnacle of Creation max health: day |
| `Galatine.healthNoon` | 500 | Pinnacle of Creation max health: noon |
| `Galatine.healthAfternoon` | 100 | Pinnacle of Creation max health: afternoon |
| `Galatine.healthSunset` | 50 | Pinnacle of Creation max health: sunset |
| `Galatine.healthNight` | -500 | Pinnacle of Creation max health: night |
| `Galatine.armorSunrise` | 15 | Pinnacle of Creation armor: sunrise |
| `Galatine.armorDay` | 30 | Pinnacle of Creation armor: day |
| `Galatine.armorNoon` | 60 | Pinnacle of Creation armor: noon |
| `Galatine.armorAfternoon` | 30 | Pinnacle of Creation armor: afternoon |
| `Galatine.armorSunset` | 15 | Pinnacle of Creation armor: sunset |
| `Galatine.armorNight` | -50 | Pinnacle of Creation armor: night |
| `Galatine.cleaverSunrise` | 3 | Sun Cleaver attack-damage multiplier: sunrise |
| `Galatine.cleaverDay` | 5 | Sun Cleaver attack-damage multiplier: day |
| `Galatine.cleaverNoon` | 12 | Sun Cleaver attack-damage multiplier: noon |
| `Galatine.cleaverAfternoon` | 5 | Sun Cleaver attack-damage multiplier: afternoon |
| `Galatine.cleaverSunset` | 2 | Sun Cleaver attack-damage multiplier: sunset |
| `Galatine.cleaverNight` | 0.5 | Sun Cleaver attack-damage multiplier: night |
| `Galatine.cleaverMpCost` | 5,000 | Sun Cleaver magicule cost. |
| `Galatine.cleaverCooldown` | 8 | Sun Cleaver cooldown (seconds). |
| `Galatine.cruelSunPowerScale` | 10 | Cruel Sun power scale outside Noon / Night. |
| `Galatine.cruelSunPowerScaleNoon` | 20 | Cruel Sun power scale at Noon. |
| `Galatine.cruelSunPowerScaleNight` | 1 | Cruel Sun power scale at Night. |
| `Galatine.cruelSunDamagePerScale` | 50 | Cruel Sun fire damage per power scale. |
| `Galatine.cruelSunChargeTicks` | 60 | Ticks Cruel Sun must be held to reach full charge. |
| `Galatine.cruelSunMpCost` | 20,000 | Cruel Sun magicule cost. |
| `Galatine.cruelSunCooldown` | 30 | Cruel Sun cooldown (seconds). |
| `Galatine.solarMaxCharge` | 1,200 | Solar Charged: ticks of daylight stored at full charge (1200 = one minute). |
| `Galatine.solarDayStateTicks` | 1,200 | Solar Charged: ticks the stored daylight grants Day state when released outside daytime. |
| `Galatine.solarNoonHoldTicks` | 100 | Solar Charged: ticks held (at sunrise/day, fully charged) to enter Noon state. |
| `Galatine.solarNoonStateTicks` | 200 | Solar Charged: ticks of Noon state granted. |
| `Galatine.prominenceSunrise` | 4 | Crazy Prominence fireballs: sunrise |
| `Galatine.prominenceDay` | 8 | Crazy Prominence fireballs: day |
| `Galatine.prominenceNoon` | 12 | Crazy Prominence fireballs: noon |
| `Galatine.prominenceAfternoon` | 8 | Crazy Prominence fireballs: afternoon |
| `Galatine.prominenceSunset` | 4 | Crazy Prominence fireballs: sunset |
| `Galatine.prominenceNight` | 1 | Crazy Prominence fireballs: night |
| `Galatine.prominenceDamage` | 125 | Crazy Prominence flame damage per fireball. |
| `Galatine.prominenceMpCost` | 10,000 | Crazy Prominence magicule cost. |
| `Galatine.prominenceCooldown` | 15 | Crazy Prominence cooldown (seconds). |

## In-game messages

<details markdown><summary>Show 5 messages</summary>

- No target in reach.
- You must stand in direct sunlight to store daylight.
- Storing daylight... %s%%
- Stored daylight released — Galatine burns as if it were day.
- The sun reaches its zenith — Noon state!

</details>

## Tags

`tensura:skills/ultimate_skills`
