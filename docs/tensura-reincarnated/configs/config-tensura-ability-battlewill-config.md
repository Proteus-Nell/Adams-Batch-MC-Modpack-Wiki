# `config/tensura/ability/battlewill_config.toml`

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Configs](index.md)</small>

## `[AuraSlash]`

| Option | Default | Range | Description |
|---|---|---|---|
| `auraCost` | 50 |  | Aura Cost to activate. |
| `attackMultiplier` | 1 |  | The damage multiplier of the projectiles compare to the user's weapon base attack damage when activated. |
| `attackMultiplierMastered` | 2 |  | The damage multiplier of the projectiles compare to the user's weapon base attack damage when activated when Mastered. |

## `[AuraSword]`

| Option | Default | Range | Description |
|---|---|---|---|
| `auraCost` | 200 |  | Aura Cost to activate. |
| `effectTime` | 1,200 |  | How long in tick that Aura Sword will stay on user after activated. |
| `attackMultiplier` | 1 |  | The bonus multiplier of the user's weapon base attack damage when activated. |

## `[EarthshatterKick]`

| Option | Default | Range | Description |
|---|---|---|---|
| `auraCost` | 150 |  | Aura Cost to activate. |
| `radius` | 5 |  | The radius of the earthquake. |
| `baseDamage` | 10 |  | The Damage the affected targets get take when activated (doubled when mastered). |

## `[HeavySlash]`

| Option | Default | Range | Description |
|---|---|---|---|
| `auraCost` | 80 |  | Aura Cost to activate. |
| `maxDistance` | 5 |  | The max distance from the target that the melee attack can be activated (doubled when mastered). |
| `meleeDamageMultiplier` | 1.5 |  | The Damage multiplier compared to the user's attack damage for the melee attack. |
| `projectileDamageMultiplier` | 0.5 |  | The Damage multiplier compared to the user's attack damage for the projectile attack. |

## `[OgreSwordGuillotine]`

| Option | Default | Range | Description |
|---|---|---|---|
| `auraCost` | 200 |  | Aura Cost to activate. |
| `effectTime` | 300 |  | How long in tick that Ogre-Sword Guillotine will stay on user after activated. |
| `effectTimeMastered` | 600 |  | How long in tick that Ogre-Sword Guillotine will stay on user after activated while mastered. |
| `attackMultiplier` | 1.5 |  | The multiplier of Attack Damage that the user gains when activated. |
| `reachMultiplier` | 1.5 |  | The multiplier of Attack Reach that the user gains when activated. |
| `attackSpeedMultiplier` | 0.8 |  | The multiplier of Attack Speed that the user gains when activated. |

## `[RoaringLionPunch]`

| Option | Default | Range | Description |
|---|---|---|---|
| `auraCost` | 10 |  | Base Aura Cost to activate. |
| `maxAuraMultiplier` | 0.1 |  | The Multiplier compared to user's Max Aura that will be used for the attack. |
| `maxAuraUsed` | 2,000 |  | The Maximum amount of Aura can be used for the attack. |
| `maxAuraUsedMastered` | 4,000 |  | The Maximum amount of Aura can be used for the attack when mastered. |

## `[FivePetalsThrust]`

| Option | Default | Range | Description |
|---|---|---|---|
| `auraCost` | 8,000 |  | Aura Cost to activate. |
| `chargingSpeed` | 0.25 |  | Speed multiplier when charging the attack. |
| `chargeTick` | 80 |  | The charge duration in tick of the attack. |
| `dashDistance` | 15 |  | The distance in block of the dash attack. |
| `dashDamage` | 100 |  | The damage of the dash attack. |
| `blossomPetal` | 5 |  | The number of petals (melee damage negation times) of the blossom. |
| `blossomDuration` | 1,200 |  | The duration in tick of the blossom after the dash attack. |
| `bonusChargeTick` | 160 |  | The bonus charge duration in tick of the attack when mastered. |
| `bonusDamage` | 25 |  | The bonus damage of the attack per each bonus charged second when mastered. |
| `bonusCost` | 1,500 |  | The bonus Aura Cost of the attack per each bonus charged second when mastered. |

## `[EightPetalsFlash]`

| Option | Default | Range | Description |
|---|---|---|---|
| `auraCost` | 10,000 |  | Aura Cost to activate. |
| `chargingSpeed` | 0.25 |  | Speed multiplier when charging the attack. |
| `chargeTick` | 80 |  | The charge duration in tick of the attack. |
| `dashDistance` | 20 |  | The distance in block of the dash attack. |
| `dashDamage` | 200 |  | The damage of the dash attack. |
| `blossomPetal` | 8 |  | The number of petals (melee damage negation times) of the blossom. |
| `blossomDuration` | 1,200 |  | The duration in tick of the blossom after the dash attack. |
| `bonusChargeTick` | 160 |  | The bonus charge duration in tick of the attack when mastered. |
| `bonusDamage` | 50 |  | The bonus damage of the attack per each bonus charged second when mastered. |
| `bonusCost` | 2,500 |  | The bonus Aura Cost of the attack per each bonus charged second when mastered. |
| `dashPetal` | 4 |  | The number of petals to consume to reperform the dash attack when mastered. |

## `[DarkEightPalms]`

| Option | Default | Range | Description |
|---|---|---|---|
| `auraCost` | 200 |  | Base Aura Cost to activate. |
| `maxMultiplier` | 8 |  | The Max Multiplier of the Attack Power. |
| `holdTime` | 20 |  | The Time the user need to hold down to increase 1 Power level. |
| `holdTimeMastered` | 10 |  | The Time the user need to hold down to increase 1 Power level with Mastery. |
| `baseDamage` | 100 |  | The Base Damage of each Aura Bullet. |

## `[DeathMarchDance]`

| Option | Default | Range | Description |
|---|---|---|---|
| `auraCost` | 100 |  | Base Aura Cost to activate. |
| `range` | 50 |  | The range in block of the bullets when homing. |
| `maxMultiplier` | 5 |  | The Max Multiplier of the Attack Power. |
| `maxMultiplierMastered` | 10 |  | The Max Multiplier of the Attack Power when Mastered. |
| `holdTime` | 40 |  | The Time the user need to hold down to increase 1 Power level. |
| `holdTimeMastered` | 20 |  | The Time the user need to hold down to increase 1 Power level with Mastery. |
| `baseDamage` | 25 |  | The Base Damage of each Aura Bullet. |

## `[ElephantStampede]`

| Option | Default | Range | Description |
|---|---|---|---|
| `auraCost` | 100 |  | Base Aura Cost to activate. |
| `holdTime` | 20 |  | The Time the user need to hold down to do each time of attack. |
| `baseDamage` | 25 |  | The Damage of each aura bullet (doubled with Mastery). |
| `bulletNumber` | 8 |  | The Number of aura bullets each time activated. |

## `[MagicBullet]`

| Option | Default | Range | Description |
|---|---|---|---|
| `auraCost` | 25 |  | Base Aura Cost to activate. |
| `maxMultiplier` | 10 |  | The Max Multiplier of the Attack Power. |
| `maxMultiplierMastered` | 20 |  | The Max Multiplier of the Attack Power when Mastered. |
| `holdTime` | 30 |  | The Time the user need to hold down to increase 1 Power level. |
| `holdTimeMastered` | 20 |  | The Time the user need to hold down to increase 1 Power level with Mastery. |
| `baseDamage` | 10 |  | The Base Damage before Power Level calculation. |

## `[MaximumMagicBullet]`

| Option | Default | Range | Description |
|---|---|---|---|
| `auraCost` | 100 |  | Base Aura Cost to activate. |
| `maxMultiplier` | 15 |  | The Max Multiplier of the Attack Power. |
| `maxMultiplierMastered` | 30 |  | The Max Multiplier of the Attack Power when Mastered. |
| `holdTime` | 30 |  | The Time the user need to hold down to increase 1 Power level. |
| `holdTimeMastered` | 20 |  | The Time the user need to hold down to increase 1 Power level with Mastery. |
| `baseDamage` | 25 |  | The Base Damage before Power Level calculation. |

## `[OgreFlame]`

| Option | Default | Range | Description |
|---|---|---|---|
| `auraCost` | 200 |  | Base Aura Cost to activate. |
| `castTime` | 100 |  | The Cast Time in tick to activate. |
| `maxTime` | 100 |  | The Max Time in tick for the Ogre Flame to stay after activation (doubled when Mastered). |
| `maxDistance` | 15 |  | The Max Distance away from the user to spawn Ogre Flame. |
| `flameDamage` | 50 |  | The Ogre Flame's damage each second. |
| `flameRadius` | 4 |  | The Ogre Flame's radius. |

## `[OgreSwordCannon]`

| Option | Default | Range | Description |
|---|---|---|---|
| `auraCost` | 200 |  | Base Aura Cost to activate. |
| `maxMultiplier` | 5 |  | The Max Multiplier of the Attack Power. |
| `maxMultiplierMastered` | 10 |  | The Max Multiplier of the Attack Power when Mastered. |
| `holdTime` | 40 |  | The Time the user need to hold down to increase 1 Power level. |
| `holdTimeMastered` | 20 |  | The Time the user need to hold down to increase 1 Power level with Mastery. |
| `baseMultiplier` | 1.5 |  | The Base Damage multiplier compared to the user's attack damage. |
| `bonusMultiplier` | 0.5 |  | The Bonus Damage multiplier compared to the user's attack damage each Power Level. |

## `[AirFlight]`

| Option | Default | Range | Description |
|---|---|---|---|
| `auraCost` | 15 |  | Aura Cost to activate. |
| `magiculeCost` | 15 |  | Magicule Cost to activate. |
| `forwardBoost` | 0.2 |  | The boost power of the user's forward movement when activated. |
| `forwardBoostMastered` | 0.4 |  | The boost power of the user's forward movement when activated with Mastery. |

## `[AuraShield]`

| Option | Default | Range | Description |
|---|---|---|---|
| `auraCost` | 1,000 |  | Aura Cost to activate. |
| `size` | 3 |  | The size in blocks of the created shield gets. |
| `health` | 100 |  | How much Health that the created shield gets. |
| `cooldown` | 5 |  | The cooldown in second of the battlewill. |
| `cooldownMastered` | 3 |  | The cooldown in second of the battlewill when mastered. |

## `[Battlewill]`

| Option | Default | Range | Description |
|---|---|---|---|
| `auraCost` | 200 |  | Aura Cost to learn (before multiplier). |
| `percentage` | 1 |  | How much percentage of Magicule gets converted into Aura each 30 ticks (doubled when Mastered). |

## `[DiamondPath]`

| Option | Default | Range | Description |
|---|---|---|---|
| `auraCost` | 150 |  | Aura Cost to activate. |
| `effectTime` | 1,200 |  | How long in tick that Diamond Path will stay on user after activated. |
| `effectTimeMastered` | 3,600 |  | How long in tick that Diamond Path will stay on user after activated while mastered. |
| `damageBoost` | 10 |  | How much attack damage that the user gains after activated (doubled when Mastered). |
| `knockBackResistanceBoost` | 0.4 |  | How much knockback resistance that the user gains after activated (doubled when Mastered). |

## `[Formhide]`

| Option | Default | Range | Description |
|---|---|---|---|
| `auraCost` | 15 |  | Aura Cost to activate. |
| `concealment` | 1 |  | The Presence Concealment level when activated. |

## `[Haze]`

| Option | Default | Range | Description |
|---|---|---|---|
| `auraCost` | 20 |  | Aura Cost to activate. |
| `concealment` | 2 |  | The Presence Concealment level when activated. |

## `[InstantMove]`

| Option | Default | Range | Description |
|---|---|---|---|
| `auraCost` | 50 |  | Aura Cost to activate. |
| `distance` | 6 |  | How far ahead the user will instant move toward (doubled when Mastered). |
| `dodgeStrength` | 0.1 |  | The bonus dodge strength when toggled. |
| `dodgeInvulnerability` | 1 |  | The bonus dodge invulnerability when toggled. |

## `[ViolentBreak]`

| Option | Default | Range | Description |
|---|---|---|---|
| `auraCost` | 150 |  | Aura Cost to activate. |
| `holdTime` | 60 |  | The Hold Time in Tick to activate. |
| `strengthenTime` | 1,200 |  | The Strengthen Time in Tick when activated. |
| `strengthenLevel` | 1 |  | The Strengthen Level when activated (doubled when Mastered). |
| `effectToRemove` | "minecraft:bad_omen", "minecraft:nausea", "minecraft:weakness", "minecraft:blindness", "minecraft:hunger", "minecraft:poison", "minecraft:darkness", "minecraft:mining_fatigue", "minecraft:levitation", "minecraft:slowness", "minecraft:unluck", "minecraft:wither", "tensura:burden", "tensura:chill", "tensura:fragility", "tensura:silence", "tensura:corrosion", "tensura:fatal_poison", "tensura:infection", "tensura:paralysis" ... (21 total) |  | The List of harmful effects that get removed upon activation. |
