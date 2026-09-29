# Sunshine

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Sunshine](../../../assets/icons/trnightmare/skill/sunshine.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:sunshine` |
| **Modes** | 4 |
| **Acquisition cost (MP)** | 100,000 |
| **Activation** | Toggle, Press |

</div>

> Sunshine is a Unique Skill of the Destruction and Enchantment Types. It radiates overwhelming heat and light, empowering the user as the sun rises, reaching its peak at noon. During this time, the user's destructive power and enchanted abilities surge to their maximum potential, turning them into an unstoppable force under the daylight.

> [!NOTE]
> **Pack note:** this pack changes the defaults below.
> - `Sunshine.Roar.magiculeCost` is **50** (mod default: 35)
> - `Sunshine.Roar.cooldownTicks` is **100** (mod default: 3)
> - `Sunshine.Sun.magiculeCost` is **80** (mod default: 60)
> - `Sunshine.Sun.cooldownTicks` is **160** (mod default: 5)
> - `Sunshine.FireStorm.magiculeCost` is **100** (mod default: 75)
> - `Sunshine.FireStorm.cooldownTicks` is **200** (mod default: 8)
> - `Sunshine.Spiral.magiculeCost` is **150** (mod default: 110)
> - `Sunshine.Spiral.cooldownTicks` is **800** (mod default: 25)

## Modes

| # | Mode |
|---|---|
| 1 | Solar Burst |
| 2 | Cruel Sun |
| 3 | Burn To Ash |
| 4 | Spiral of Creation |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Solar Burst | 0 |  |
| Cruel Sun | 0 |  |
| Burn To Ash | 0 |  |
| Spiral of Creation | 0 |  |
| other modes | 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you take damage

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| inst | amount | op |

## Related

- **Items:** [Divine Axe Rhitta](../../items/weapons/divine-axe-rhitta.md)
- **Referenced by:** [｢ Galatine, Sword of the Sun ｣](../ultimate-skills/galatine.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | This pack | Description |
|---|---|---|---|
| `Sunshine.epAcquirement` | 100,000 | | EP / magicule obtainment cost to acquire Sunshine. |
| `Sunshine.stormLearnThreshold` | 100 | | Learn threshold for Fire Storm. |
| `Sunshine.stormMasteryThreshold` | 200 | | Mastery threshold for Fire Storm. |
| `Sunshine.stormRange` | 30 | | Maximum targeting range for Storm mode. |
| `Sunshine.stormHitInterval` | 10 | | Ticks between each Fire Storm hit. |
| `Sunshine.stormSurgeInterval` | 20 | | Ticks between each Fire Storm surge. |
| `Sunshine.stormMagicDamage` | 10 | | Secondary magic damage per Fire Storm hit. |
| `Sunshine.stormFireSurgeDamage` | 30 | | Fire Storm surge damage. |
| `Sunshine.stormMagicSurgeDamage` | 15 | | Secondary surge magic damage. |
| `Sunshine.stormBurnTicks` | 100 | | Burn ticks applied by Storm. |
| `Sunshine.spiralHeight` | 5 | | Spiral barrier height. |
| `Sunshine.attackBonusSunrise` | 4 | | Attack bonus: sunrise |
| `Sunshine.attackBonusDay` | 6 | | Attack bonus: day |
| `Sunshine.attackBonusNoon` | 10 | | Attack bonus: noon |
| `Sunshine.attackBonusAfternoon` | 6 | | Attack bonus: afternoon |
| `Sunshine.attackBonusMoonrise` | -2 | | Attack bonus: moonrise |
| `Sunshine.attackBonusNight` | -4 | | Attack bonus: night |
| `Sunshine.speedBonusSunrise` | 0.05 | | Speed bonus (ADD_MULTIPLIED_TOTAL): sunrise |
| `Sunshine.speedBonusDay` | 0.1 | | Speed bonus: day |
| `Sunshine.speedBonusNoon` | 0.2 | | Speed bonus: noon |
| `Sunshine.speedBonusAfternoon` | 0.1 | | Speed bonus: afternoon |
| `Sunshine.speedBonusMoonrise` | -0.05 | | Speed bonus: moonrise |
| `Sunshine.speedBonusNight` | -0.1 | | Speed bonus: night |
| `Sunshine.healthBonusSunrise` | 4 | | Max health bonus: sunrise |
| `Sunshine.healthBonusDay` | 8 | | Max health bonus: day |
| `Sunshine.healthBonusNoon` | 16 | | Max health bonus: noon |
| `Sunshine.healthBonusAfternoon` | 8 | | Max health bonus: afternoon |
| `Sunshine.healthBonusMoonrise` | -2 | | Max health bonus: moonrise |
| `Sunshine.healthBonusNight` | -4 | | Max health bonus: night |
| `Sunshine.armorBonusSunrise` | 2 | | Armor bonus: sunrise |
| `Sunshine.armorBonusDay` | 4 | | Armor bonus: day |
| `Sunshine.armorBonusNoon` | 6 | | Armor bonus: noon |
| `Sunshine.armorBonusAfternoon` | 4 | | Armor bonus: afternoon |
| `Sunshine.armorBonusMoonrise` | -1 | | Armor bonus: moonrise |
| `Sunshine.armorBonusNight` | -2 | | Armor bonus: night |
| `Sunshine.rhittaFireResistDuration` | 1,400 | | Fire resistance duration when toggled on (ticks). |
| `Sunshine.rhittaFireResistRefresh` | 600 | | Fire resistance refresh duration (ticks). |
| `Sunshine.glowingDuration` | 500 | | Glowing duration (ticks). |
| `Sunshine.noRhittaDamagePercentage` | 10 | | Damage boost percent to Heat, Light and Fire while toggled (no Rhitta). |
| `Sunshine.hasRhittaDamagePercentage` | 25 | | Damage boost percent with Rhitta. |
| `Roar.magiculeCost` | 35 | 50 | Current MP (magicule) cost to use this mode or segment. |
| `Roar.durationTicks` | 0 | | Duration in ticks (effects, zones, projectiles) when applicable. |
| `Roar.level` | 0 | | Effect amplifier level (0 = I) when applicable. |
| `Roar.cooldownTicks` | 3 | 100 | Cooldown in ticks after this mode activates. |
| `Roar.damage` | 20 | | Primary damage when this mode deals damage. |
| `Roar.damageMastered` | 0 | | Damage when mastered; if 0, 'damage' is used for both. |
| `Roar.scalar` | 2 | | Extra scalar: explosion radius, AoE radius, etc. when applicable. |
| `Roar.scalar2` | 0 | | Second scalar (e.g. secondary radius) when applicable. |
| `Sun.magiculeCost` | 60 | 80 | Current MP (magicule) cost to use this mode or segment. |
| `Sun.durationTicks` | 0 | | Duration in ticks (effects, zones, projectiles) when applicable. |
| `Sun.level` | 0 | | Effect amplifier level (0 = I) when applicable. |
| `Sun.cooldownTicks` | 5 | 160 | Cooldown in ticks after this mode activates. |
| `Sun.damage` | 40 | | Primary damage when this mode deals damage. |
| `Sun.damageMastered` | 0 | | Damage when mastered; if 0, 'damage' is used for both. |
| `Sun.scalar` | 5 | | Extra scalar: explosion radius, AoE radius, etc. when applicable. |
| `Sun.scalar2` | 0 | | Second scalar (e.g. secondary radius) when applicable. |
| `FireStorm.magiculeCost` | 75 | 100 | Current MP (magicule) cost to use this mode or segment. |
| `FireStorm.durationTicks` | 200 | | Duration in ticks (effects, zones, projectiles) when applicable. |
| `FireStorm.level` | 0 | | Effect amplifier level (0 = I) when applicable. |
| `FireStorm.cooldownTicks` | 8 | 200 | Cooldown in ticks after this mode activates. |
| `FireStorm.damage` | 20 | | Primary damage when this mode deals damage. |
| `FireStorm.damageMastered` | 0 | | Damage when mastered; if 0, 'damage' is used for both. |
| `FireStorm.scalar` | 6 | | Extra scalar: explosion radius, AoE radius, etc. when applicable. |
| `FireStorm.scalar2` | 8 | | Second scalar (e.g. secondary radius) when applicable. |
| `Spiral.magiculeCost` | 110 | 150 | Current MP (magicule) cost to use this mode or segment. |
| `Spiral.durationTicks` | 0 | | Duration in ticks (effects, zones, projectiles) when applicable. |
| `Spiral.level` | 0 | | Effect amplifier level (0 = I) when applicable. |
| `Spiral.cooldownTicks` | 25 | 800 | Cooldown in ticks after this mode activates. |
| `Spiral.damage` | 200 | | Primary damage when this mode deals damage. |
| `Spiral.damageMastered` | 0 | | Damage when mastered; if 0, 'damage' is used for both. |
| `Spiral.scalar` | 4.5 | | Extra scalar: explosion radius, AoE radius, etc. when applicable. |
| `Spiral.scalar2` | 0 | | Second scalar (e.g. secondary radius) when applicable. |

Set in [`config/nightmare/ability/skill/nightmare_intrinsic.toml`](../../configs/config-nightmare-ability-skill-nightmare-intrinsic.md).

| Option | Default | Description |
|---|---|---|
| `hellFlarePlasma.magiculeCost` | 0 | Current MP (magicule) cost to use this mode or segment. |
| `breath.magiculeCost` | 50 | Current MP (magicule) cost to use this mode or segment. |
| `breath.durationTicks` | 0 | Duration in ticks (effects, zones, projectiles) when applicable. |
| `breath.level` | 0 | Effect amplifier level (0 = I) when applicable. |
| `breath.cooldownTicks` | 0 | Cooldown in ticks after this mode activates. |
| `breath.damage` | 10 | Primary damage when this mode deals damage. |
| `breath.damageMastered` | 20 | Damage when mastered; if 0, 'damage' is used for both. |
| `breath.scalar` | 0 | Extra scalar: explosion radius, AoE radius, etc. when applicable. |
| `breath.scalar2` | 0 | Second scalar (e.g. secondary radius) when applicable. |
| `ball.magiculeCost` | 100 | Current MP (magicule) cost to use this mode or segment. |
| `ball.durationTicks` | 0 | Duration in ticks (effects, zones, projectiles) when applicable. |
| `ball.level` | 0 | Effect amplifier level (0 = I) when applicable. |
| `ball.cooldownTicks` | 0 | Cooldown in ticks after this mode activates. |
| `ball.damage` | 50 | Primary damage when this mode deals damage. |
| `ball.damageMastered` | 0 | Damage when mastered; if 0, 'damage' is used for both. |
| `ball.scalar` | 1 | Extra scalar: explosion radius, AoE radius, etc. when applicable. |
| `ball.scalar2` | 0 | Second scalar (e.g. secondary radius) when applicable. |
| `hellFlareArea.magiculeCost` | 0 | Current MP (magicule) cost to use this mode or segment. |
| `hellFlareArea.durationTicks` | 60 | Duration in ticks (effects, zones, projectiles) when applicable. |
| `hellFlareArea.level` | 0 | Effect amplifier level (0 = I) when applicable. |
| `hellFlareArea.cooldownTicks` | 0 | Cooldown in ticks after this mode activates. |
| `hellFlareArea.damage` | 750 | Primary damage when this mode deals damage. |
| `hellFlareArea.damageMastered` | 0 | Damage when mastered; if 0, 'damage' is used for both. |
| `hellFlareArea.scalar` | 15 | Extra scalar: explosion radius, AoE radius, etc. when applicable. |
| `hellFlareArea.scalar2` | 0 | Second scalar (e.g. secondary radius) when applicable. |
| `limitedHellFlare.magiculeCost` | 0 | Current MP (magicule) cost to use this mode or segment. |
| `limitedHellFlare.durationTicks` | 60 | Duration in ticks (effects, zones, projectiles) when applicable. |
| `limitedHellFlare.level` | 0 | Effect amplifier level (0 = I) when applicable. |
| `limitedHellFlare.cooldownTicks` | 0 | Cooldown in ticks after this mode activates. |
| `limitedHellFlare.damage` | 2,500 | Primary damage when this mode deals damage. |
| `limitedHellFlare.damageMastered` | 0 | Damage when mastered; if 0, 'damage' is used for both. |
| `limitedHellFlare.scalar` | 2.5 | Extra scalar: explosion radius, AoE radius, etc. when applicable. |
| `limitedHellFlare.scalar2` | 0 | Second scalar (e.g. secondary radius) when applicable. |
| `hellFlarePlasma.magiculeCost` | 0 | Current MP (magicule) cost to use this mode or segment. |
| `hellFlarePlasma.durationTicks` | 0 | Duration in ticks (effects, zones, projectiles) when applicable. |
| `hellFlarePlasma.level` | 0 | Effect amplifier level (0 = I) when applicable. |
| `hellFlarePlasma.cooldownTicks` | 0 | Cooldown in ticks after this mode activates. |
| `hellFlarePlasma.damage` | 50 | Primary damage when this mode deals damage. |
| `hellFlarePlasma.damageMastered` | 125 | Damage when mastered; if 0, 'damage' is used for both. |
| `hellFlarePlasma.scalar` | 0 | Extra scalar: explosion radius, AoE radius, etc. when applicable. |
| `hellFlarePlasma.scalar2` | 0 | Second scalar (e.g. secondary radius) when applicable. |
