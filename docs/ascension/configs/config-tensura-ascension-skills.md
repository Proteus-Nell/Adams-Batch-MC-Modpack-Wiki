# `config/tensura/ascension-skills.toml`

<small>[Ascension](../index.md) &rsaquo; [Configs](index.md)</small>

## `[Skills.sharpened_claws]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Sharpened Claws. |
| `damage` | 10 | 0 to 1,000 | Unarmed damage while toggled, unmastered. |
| `damageMastered` | 15 | 0 to 1,000 | Unarmed damage while toggled, mastered. |

## `[Skills.angel_wings]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Angel Wings. |
| `durationSeconds` | 60 | 1 to 3,600 | Unmastered effect duration (seconds). |
| `cooldownSeconds` | 70 | 0 to 3,600 | Unmastered cooldown (seconds). |

## `[Skills.blood_frenzy]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Blood Frenzy. |
| `attackDamageBonus` | 3 | 0 to 1,000 | Flat attack-damage bonus while toggled, unmastered. |
| `attackDamageBonusMastered` | 5 | 0 to 1,000 | Flat attack-damage bonus while toggled, mastered. |
| `attackSpeedBonus` | 0.4 | 0 to 10 | Flat attack-speed bonus while toggled, unmastered. |
| `attackSpeedBonusMastered` | 0.6 | 0 to 10 | Flat attack-speed bonus while toggled, mastered. |
| `auraDrainFraction` | 0.003 | 0 to 1 | Fraction of max aura drained per tick, unmastered. |
| `auraDrainFractionMastered` | 0.0015 | 0 to 1 | Fraction of max aura drained per tick, mastered. |
| `auraRestoreOnKill` | 0.1 | 0 to 1 | Fraction of max aura restored on kill, unmastered. |
| `auraRestoreOnKillMastered` | 0.15 | 0 to 1 | Fraction of max aura restored on kill, mastered. |

## `[Skills.intimidating_roar]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Intimidating Roar. |
| `radius` | 8 | 0 to 64 | AoE radius in blocks. |
| `durationSeconds` | 6 | 1 to 600 | Effect duration, unmastered (seconds). |
| `durationSecondsMastered` | 10 | 1 to 600 | Effect duration, mastered (seconds). |
| `cooldownSeconds` | 20 | 0 to 3,600 | Cooldown (seconds). |

## `[Skills.toxic_skin]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Toxic Skin. |
| `poisonDurationSeconds` | 5 | 1 to 600 | Poison duration, unmastered (seconds). |
| `poisonDurationSecondsMastered` | 10 | 1 to 600 | Poison duration, mastered (seconds). |

## `[Skills.energy_charge]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Energy Charge (and block its EP auto-unlock when false). |
| `auraRestorePerSec` | 0.05 | 0 to 10 | Fraction of max aura restored per second, unmastered. |
| `auraRestorePerSecMastered` | 0.07 | 0 to 10 | Fraction of max aura restored per second, mastered. |
| `magiculeCostPerSec` | 0.03 | 0 to 10 | Fraction of max magicule consumed per second. |
| `slownessAmplifier` | 1 | 0 to 127 | Slowness amplifier applied while channeling. 0 = Slowness I, 1 = Slowness II, ... |
| `maxHeldSeconds` | 5 | 1 to 300 | Maximum seconds the skill can be channeled before it force-releases and goes on cooldown. |
| `cooldownSeconds` | 5 | 0 to 600 | Cooldown (seconds) applied on release — both force-release at the cap and early release. |

## `[Skills.maximum_charge]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Maximum Charge (and block its EP auto-unlock when false). |
| `auraRestorePerSec` | 0.1 | 0 to 10 | Fraction of max aura restored per second, unmastered. |
| `auraRestorePerSecMastered` | 0.15 | 0 to 10 | Fraction of max aura restored per second, mastered. |
| `magiculeCostPerSec` | 0.06 | 0 to 10 | Fraction of max magicule consumed per second. |
| `slownessAmplifier` | 3 | 0 to 127 | Slowness amplifier applied while channeling. 0 = Slowness I, 1 = Slowness II, ... |
| `maxHeldSeconds` | 5 | 1 to 300 | Maximum seconds the skill can be channeled before it force-releases and goes on cooldown. |
| `cooldownSeconds` | 5 | 0 to 600 | Cooldown (seconds) applied on release — both force-release at the cap and early release. |

## `[Skills.magicule_attunement]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Magicule Attunement. |
| `bonus` | 0.05 | 0 to 10 | Regen multiplier bonus while toggled, unmastered. |
| `bonusMastered` | 0.1 | 0 to 10 | Regen multiplier bonus while toggled, mastered. |

## `[Skills.magicule_resonance]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Magicule Resonance. |
| `bonus` | 0.1 | 0 to 10 | Regen multiplier bonus while toggled, unmastered. |
| `bonusMastered` | 0.2 | 0 to 10 | Regen multiplier bonus while toggled, mastered. |

## `[Skills.magicule_dominion]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Magicule Dominion. |
| `bonus` | 0.25 | 0 to 10 | Regen multiplier bonus while toggled, unmastered. |
| `bonusMastered` | 0.5 | 0 to 10 | Regen multiplier bonus while toggled, mastered. |

## `[Skills.blood_manipulation]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Blood Manipulation. |
| `bonus` | 0.2 | 0 to 10 | Outgoing blood-damage multiplier bonus while toggled, unmastered (0.20 = +20%). |
| `bonusMastered` | 0.4 | 0 to 10 | Outgoing blood-damage multiplier bonus while toggled, mastered. |

## `[Skills.blood_domination]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Blood Domination. |
| `bonus` | 0.6 | 0 to 10 | Outgoing blood-damage multiplier bonus while toggled, unmastered. |
| `bonusMastered` | 1 | 0 to 10 | Outgoing blood-damage multiplier bonus while toggled, mastered. |

## `[Skills.prickly_hands]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Prickly Hands. |
| `tier` | 1 | 1 to 10 | Bleeding tier applied on melee hit, unmastered (1 = 0.5 dmg/s). |
| `tierMastered` | 2 | 1 to 10 | Bleeding tier applied on melee hit, mastered. |
| `durationSeconds` | 5 | 1 to 600 | Bleeding duration, unmastered (seconds). |
| `durationSecondsMastered` | 10 | 1 to 600 | Bleeding duration, mastered (seconds). |

## `[Skills.blood_blade]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Blood Blade. |
| `damage` | 10 | 0 to 1,000 | Damage dealt to target on hit. |
| `healthCost` | 1 | 0 to 100 | HP cost paid by the caster per cast. |
| `speed` | 3 | 0.1 to 20 | Projectile flight speed multiplier. |

## `[Skills.magicule_nourishment]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Magicule Nourishment. |
| `costFraction` | 0.15 | 0 to 1 | Fraction of max magicule consumed per cast, unmastered. |
| `costFractionMastered` | 0.075 | 0 to 1 | Fraction of max magicule consumed per cast, mastered. |
| `cooldownSeconds` | 10 | 0 to 3,600 | Cooldown, unmastered (seconds). |
| `cooldownSecondsMastered` | 5 | 0 to 3,600 | Cooldown, mastered (seconds). |

## `[Skills.magnetized_vacuum]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Magnetized Vacuum (also skips the Iron Golem skill grant when false). |
| `durationSeconds` | 5 | 1 to 600 | Aura duration, unmastered (seconds). |
| `durationSecondsMastered` | 10 | 1 to 600 | Aura duration, mastered (seconds). |
| `radius` | 8 | 0 to 64 | Pull radius in blocks, unmastered. |
| `radiusMastered` | 12 | 0 to 64 | Pull radius in blocks, mastered. |
| `cost` | 2,000 | 0 to 1,000,000,000 | Flat magicule cost per activation, unmastered. |
| `costMastered` | 1,000 | 0 to 1,000,000,000 | Flat magicule cost per activation, mastered. |
| `cooldownSeconds` | 20 | 0 to 3,600 | Cooldown, unmastered (seconds). |
| `cooldownSecondsMastered` | 10 | 0 to 3,600 | Cooldown, mastered (seconds). |

## `[Skills.great_mage]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Great Mage. |
| `passiveBonus` | 0.19 | 0 to 100 | Learning/mastery attribute bonus while toggled. |
| `cooldownSeconds` | 120 | 0 to 3,600 | Study cooldown, unmastered (seconds). |
| `cooldownSecondsMastered` | 60 | 0 to 3,600 | Study cooldown, mastered (seconds). |
| `tomeXpCost` | 5 | 0 to 1,000 | Vanilla XP levels consumed per tome crafted via Create Tome mode. |
| `chantXpCost` | 10 | 0 to 1,000 | Vanilla XP levels consumed per Magic Chant cast. |
| `chantCooldownSeconds` | 600 | 0 to 3,600 | Magic Chant cooldown, unmastered (seconds). |
| `chantCooldownSecondsMastered` | 300 | 0 to 3,600 | Magic Chant cooldown, mastered (seconds). |
| `tomeCooldownSeconds` | 1 | 0 to 3,600 | Create Tome cooldown (seconds). Short anti-spam gate — the real cost is the XP charged inside the tome GUI. |

## `[Skills.timeless_mage]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Timeless Mage. |
| `passiveBonus` | 29 | 0 to 100 | Mastery-gain attribute bonus while toggled (+29 = 30x faster total). |
| `zoltraakCooldownSeconds` | 20 | 0 to 3,600 | Zoltraak cooldown (seconds), unmastered. |
| `zoltraakCooldownSecondsMastered` | 5 | 0 to 3,600 | Zoltraak cooldown (seconds), mastered. |
| `zoltraakHpFraction` | 0.1 | 0 to 1 | Fraction of target's max HP dealt per Zoltraak damage tick (every 0.5s). |
| `zoltraakInstakillRatio` | 1.5 | 1 to 100 | Caster Max EP must exceed target Max EP × this ratio to instakill via Zoltraak. |
| `dominateCooldownSeconds` | 20 | 0 to 3,600 | Magic Dominate cooldown (seconds), unmastered. |
| `dominateCooldownSecondsMastered` | 10 | 0 to 3,600 | Magic Dominate cooldown (seconds), mastered. |

## `[Skills.eye_of_mind]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Eye of Mind. |
| `passiveBonus` | 9 | 0 to 100 | Learning/mastery attribute bonus while toggled (+9 = 10x faster total). |
| `rayMagiculePerSec` | 0.02 | 0 to 1 | Fraction of max magicule drained per second while Ray of Death is held. |

## `[Skills.king_of_curses]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable King of Curses. |
| `meleeBonus` | 0.15 | 0 to 10 | Melee damage bonus while toggled (fraction). |
| `auraDrainPerSec` | 0.002 | 0 to 1 | Fraction of max aura drained per second while toggled. |
| `costDismantle` | 0.02 | 0 to 1 | Dismantle magicule cost (fraction of max). |
| `costCleave` | 0.04 | 0 to 1 | Cleave magicule cost (fraction of max). |
| `costFuga` | 0.1 | 0 to 1 | Fuga magicule cost (fraction of max). |
| `costShrine` | 0.25 | 0 to 1 | Malevolent Shrine magicule cost (fraction of max). |

## `[Skills.sealer]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Sealer. |
| `passiveSpiritHp` | 100 | 0 to 100,000 | Max spiritual HP bonus while toggled. |
| `sealRange` | 16 | 1 to 128 | Seal raycast range in blocks. |
| `sealEpThreshold` | 1.5 | 1 to 100 | Caster-EP / target-EP ratio required to Seal (1.5 = 1.5x as strong). |
| `sealCooldownSeconds` | 30 | 0 to 3,600 | Seal cooldown, unmastered (seconds). |
| `sealCooldownSecondsMastered` | 20 | 0 to 3,600 | Seal cooldown, mastered (seconds). |
| `suppressFraction` | 0.1 | 0 to 1 | Fraction of max aura AND max magicule each removed on Suppress (0.10 = 10% from each, total 20% of max EP). |
| `suppressCooldownSeconds` | 30 | 0 to 3,600 | Suppress cooldown, unmastered (seconds). |
| `suppressCooldownSecondsMastered` | 20 | 0 to 3,600 | Suppress cooldown, mastered (seconds). |
| `strengthPerStack` | 0.2 | 0 to 100 | Attack-damage added per Stored Strength activation, unmastered. |
| `strengthPerStackMastered` | 0.2 | 0 to 100 | Attack-damage added per Stored Strength activation, mastered. |
| `strengthCap` | 20 | 0 to 1,000 | Total attack-damage cap for Stored Strength, unmastered. |
| `strengthCapMastered` | 40 | 0 to 1,000 | Total attack-damage cap for Stored Strength, mastered. |
| `strengthCooldownSeconds` | 20 | 0 to 3,600 | Stored Strength cooldown, unmastered (seconds). |
| `strengthCooldownSecondsMastered` | 10 | 0 to 3,600 | Stored Strength cooldown, mastered (seconds). |

## `[Skills.one_who_seals]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable One Who Seals. |
| `killBonusPerKill` | 0.5 | 0 to 1,000 | Max Spiritual HP gained per kill (passive). |
| `killBonusCap` | 20,000 | 0 to 1,000,000 | Cap on the cumulative kill-bonus Max Spiritual HP. |
| `range` | 16 | 1 to 128 | Targeting raycast range for Suppress (sneak-target) and Enough is Enough (blocks). |
| `sealCooldownSeconds` | 30 | 0 to 3,600 | Seal cooldown, unmastered (seconds). |
| `sealCooldownSecondsMastered` | 20 | 0 to 3,600 | Seal cooldown, mastered (seconds). |
| `suppressFraction` | 0.2 | 0 to 1 | Fraction of Max EP suppressed into a stone, unmastered (0.20 = 20%). |
| `suppressFractionMastered` | 0.3 | 0 to 1 | Fraction of Max EP suppressed into a stone, mastered (0.30 = 30%). |
| `suppressCooldownSeconds` | 60 | 0 to 3,600 | Suppress cooldown, unmastered (seconds). |
| `suppressCooldownSecondsMastered` | 60 | 0 to 3,600 | Suppress cooldown, mastered (seconds). |
| `enoughCooldownSeconds` | 60 | 0 to 3,600 | Enough is Enough cooldown, unmastered (seconds). |
| `enoughCooldownSecondsMastered` | 10 | 0 to 3,600 | Enough is Enough cooldown, mastered (seconds). |
| `enoughEpRatio` | 2 | 1 to 100 | Caster-EP / target-EP ratio required to seal an ordinary skill. |
| `enoughEpRatioUnique` | 3 | 1 to 100 | Caster-EP / target-EP ratio required to seal a UNIQUE-tier skill. |

## `[Skills.bubble_majin]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Bubble Majin. |
| `reflectSpeedMultiplier` | 1.5 | 0 to 100 | Speed multiplier applied to reflected projectiles. |
| `reflectDamageMultiplier` | 1.5 | 0 to 100 | Damage multiplier applied to reflected Tensura projectiles. |
| `candyBeamRange` | 30 | 1 to 256 | Candy Beam targeting range in blocks. |
| `candyEpThreshold` | 2 | 1 to 100 | Caster-EP / target-EP ratio required for Candy Beam to transmute (2.0 = 2x as strong). |
| `candyEpRetained` | 0.1 | 0 to 1 | Fraction of the target's EP stored in the resulting candy (0.10 = 10%). |
| `candyAllowPlayers` | false |  | When true, Candy Beam can target other players (subject to the EP threshold). PvP servers only — leave false for co-op. |
| `candyCooldownSeconds` | 30 | 0 to 3,600 | Candy Beam cooldown, unmastered (seconds). |
| `candyCooldownSecondsMastered` | 10 | 0 to 3,600 | Candy Beam cooldown, mastered (seconds). |
| `regenAuraCost` | 0.05 | 0 to 1 | Regeneration aura cost (fraction of max aura). |
| `regenCooldownSeconds` | 8 | 0 to 3,600 | Regeneration cooldown, unmastered (seconds). |
| `regenCooldownSecondsMastered` | 4 | 0 to 3,600 | Regeneration cooldown, mastered (seconds). |

## `[Skills.evil_majin]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable The Evil Majin. |
| `reflectSpeedMultiplier` | 1.5 | 0 to 100 | Reflected projectile speed multiplier. |
| `reflectDamageMultiplier` | 2 | 0 to 100 | Reflected Tensura projectile damage multiplier. |
| `candyEpRetained` | 0.2 | 0 to 1 | Fraction of each victim's EP rolled into the merged candy. |
| `candyAllowPlayers` | false |  | If true, players inside the AOE may be candied. PvP opt-in. |
| `candyCooldownSeconds` | 20 | 0 to 3,600 | Candy AOE cooldown, unmastered (seconds). |
| `candyCooldownSecondsMastered` | 5 | 0 to 3,600 | Candy AOE cooldown, mastered (seconds). |
| `hungerDamage` | 8 | 0 to 1,000,000 | Per-tick predation damage applied by the Hunger mist. |
| `hungerRange` | 16 | 1 to 128 | Range of the Hunger mist (blocks). |
| `hungerSize` | 1.5 | 0.1 to 10 | Mist visual/hit size. |
| `hungerCooldownSeconds` | 20 | 0 to 3,600 | Hunger cooldown applied on key release, unmastered (seconds). |
| `hungerCooldownSecondsMastered` | 5 | 0 to 3,600 | Hunger cooldown applied on key release, mastered (seconds). |

## `[Skills.dragon_slayer]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Dragon Slayer. |
| `essenceMaxHpPer` | 20 | 0 to 1,000 | Permanent max-HP bonus added per Dragon Essence eaten (no cap, reset on death). |
| `infusionEpGain` | 20,000 | 0 to 1,000,000,000 | EP granted per Dragon Heart consumed via Dragon Infusion, unmastered. |
| `infusionEpGainMastered` | 40,000 | 0 to 1,000,000,000 | EP granted per Dragon Heart consumed via Dragon Infusion, mastered. |
| `infusionCooldownSeconds` | 5 | 0 to 3,600 | Dragon Infusion cooldown (seconds), unmastered. |
| `infusionCooldownSecondsMastered` | 2 | 0 to 3,600 | Dragon Infusion cooldown (seconds), mastered. |
| `rageAmplifier` | 9 | 0 to 127 | Strength amplifier applied by Dragon Rage, unmastered (9 = Strength X). |
| `rageAmplifierMastered` | 14 | 0 to 127 | Strength amplifier applied by Dragon Rage, mastered (14 = Strength XV). |
| `rageDurationSeconds` | 30 | 1 to 3,600 | Dragon Rage strength duration (seconds), unmastered. |
| `rageDurationSecondsMastered` | 60 | 1 to 3,600 | Dragon Rage strength duration (seconds), mastered. |
| `rageCooldownSeconds` | 60 | 0 to 3,600 | Dragon Rage cooldown (seconds), unmastered. |
| `rageCooldownSecondsMastered` | 30 | 0 to 3,600 | Dragon Rage cooldown (seconds), mastered. |

## `[Skills.slayer_of_dragons]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable The Slayer of Dragons. |
| `essenceMaxHpPer` | 30 | 0 to 1,000 | Permanent max-HP bonus per Dragon Essence / dragon flesh eaten while toggled on (no cap, reset on death). |
| `killEpBonus` | 50,000 | 0 to 1,000,000,000 | Permanent Max EP granted per dragon kill while toggled on. Split 50/50 across MAX_AURA + MAX_MAGICULE. |
| `killArmorBonus` | 1 | 0 to 100 | Permanent ARMOR granted per dragon kill while toggled on (stacks via a single growing modifier). |
| `infusionEpGain` | 40,000 | 0 to 1,000,000,000 | EP granted per Dragon Heart consumed via Dragon Infusion, unmastered. |
| `infusionEpGainMastered` | 50,000 | 0 to 1,000,000,000 | EP granted per Dragon Heart consumed via Dragon Infusion, mastered. |
| `infusionCooldownSeconds` | 10 | 0 to 3,600 | Dragon Infusion cooldown (seconds). |
| `rageDurationSeconds` | 300 | 1 to 3,600 | Draconic Rage duration (seconds). |
| `rageCooldownSeconds` | 300 | 0 to 3,600 | Draconic Rage cooldown (seconds). |
| `rageStrengthAmp` | 19 | 0 to 127 | Strength amplifier applied by Draconic Rage (19 = Strength XX). |
| `rageStrengthenAmp` | 4 | 0 to 127 | Tensura Strengthen amplifier applied by Draconic Rage (4 = Strengthen V; +6 attack damage per level). |
| `rageResistanceAmp` | 2 | 0 to 127 | Resistance amplifier applied by Draconic Rage (2 = Resistance III). |
| `roarCooldownSeconds` | 30 | 0 to 3,600 | Dragon King Roar cooldown applied on key release (seconds). |
| `roarDamage` | 25 | 0 to 1,000,000 | Per-hit damage for each breath stream while Dragon King Roar is held, unmastered. Overrides Tensura's base breath damage. Tensura's elemental Domination toggle (FLAME/WATER/LIGHTNING_BOOST) scales this multiplicatively via the DamagingHandler attribute lookup; with no toggle on the corresponding element this is the raw landed damage. |
| `roarDamageMastered` | 50 | 0 to 1,000,000 | Per-hit damage for each breath stream while Dragon King Roar is held, mastered. |
| `roarSizeMultiplier` | 0.6 | 0.1 to 5 | Cone-width multiplier applied to roar-spawned breath entities (0.6 = 40% narrower). Lower = tighter, more focused beam. Set 1.0 for vanilla width. |
| `roarLengthMultiplier` | 2 | 1 to 10 | Range multiplier applied to roar-spawned breath entities (2.0 = 2x reach). |

## `[Skills.imprisoned_jester]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Imprisoned Jester. |
| `physicalBonus` | 0.2 | 0 to 10 | In-slot outgoing physical damage bonus, unmastered (0.20 = +20%). |
| `physicalBonusMasteredAdd` | 0.1 | 0 to 10 | Additional in-slot physical bonus added on top of base when mastered (0.10 = +10% more, total +30%). |
| `magicBonus` | 0.2 | 0 to 10 | In-slot outgoing Tensura-magic damage bonus (0.20 = +20%). |
| `critChance` | 0.1 | 0 to 1 | In-slot crit chance per hit, unmastered (0.10 = 10%). Crit deals +50% damage. |
| `critChanceMasteredAdd` | 0.1 | 0 to 1 | Additional crit chance added on top of base when mastered (0.10 = +10% more, total 20%). |
| `reflectFraction` | 0.25 | 0 to 10 | Fraction of incoming physical damage reflected to attacker while toggled on (0.25 = 25%). |
| `chaosEpCap` | 10,000,000 | 1 to 1,000,000,000,000 | EP cap used for Chaos Spades damage scaling. EP above this value is ignored for scaling. |
| `chaosEpFactor` | 0.001 | 0 to 1 | Soul-HP damage per point of effective EP (0.001 = 10000 SHP at the 10M cap). |
| `chaosCooldownSeconds` | 15 | 0 to 3,600 | Chaos Spades cooldown (seconds). |
| `explodeHpThreshold` | 0.25 | 0 to 1 | Max HP fraction the caster must be below to cast Explosive Goodbye (0.25 = under 25% HP). |
| `explodeRadius` | 10 | 0 to 64 | Explosive Goodbye radius in blocks. |
| `explodeCooldownSeconds` | 600 | 0 to 36,000 | Explosive Goodbye cooldown (seconds) — moot since it kills the caster, but applied for symmetry if they get revived. |
| `chaosFireDamage` | 1 | 0 to 1,000 | Flat Soul-HP damage dealt per tick-interval while standing in Chaos Fire. |
| `chaosFireTickInterval` | 10 | 1 to 1,200 | Ticks between Chaos Fire damage applications (20 ticks = 1 second). |
| `chaosFireBurnoutTicks` | 300 | 1 to 72,000 | Ticks a Chaos Fire block survives before self-extinguishing (20 ticks = 1 second). |

## `[Skills.unbound_jester]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable The Unbound Jester. |
| `gateSpiritDamage` | 1,000,000 | 0 to 1,000,000,000,000 | Cumulative spirit damage required to qualify for the awakening (lifetime, while Imprisoned Jester is in slot). |
| `physicalBonus` | 0.5 | 0 to 10 | In-slot outgoing physical damage bonus (0.50 = +50%). |
| `magicBonus` | 0.5 | 0 to 10 | In-slot outgoing magic damage bonus (0.50 = +50%). |
| `critChance` | 0.3 | 0 to 1 | In-slot crit chance per hit (0.30 = 30%). |
| `critDamage` | 1 | 0 to 100 | Crit damage bonus (1.00 = +100% on crit). |
| `reflectFraction` | 0.25 | 0 to 1 | Fraction of all incoming damage reflected to the attacker while toggled (0.25 = 25%). |
| `theaterRadius` | 8 | 1 to 64 | Chaos Theater AOE radius (blocks). |
| `theaterEpCap` | 10,000,000 | 0 to 1,000,000,000,000 | Caster EP cap used for Chaos Theater damage scaling. |
| `theaterEpFactor` | 0.0001 | 0 to 1 | EP-to-damage factor for Chaos Theater (1.5× Chaos Spades' default; was 2.0× before the -25% nerf). |
| `theaterAuraFraction` | 0.05 | 0 to 1 | Fraction of caster's max aura consumed per Chaos Theater cast (0.05 = 5%). |
| `theaterCooldownSeconds` | 30 | 0 to 600 | Chaos Theater cooldown (seconds, unmastered). |
| `theaterCooldownSecondsMastered` | 10 | 0 to 600 | Chaos Theater cooldown (seconds, mastered). |
| `curtainRadius` | 16 | 1 to 64 | Curtain Call AOE radius (blocks). |
| `curtainCooldownSeconds` | 60 | 0 to 3,600 | Curtain Call cooldown (seconds). |
| `punishRange` | 16 | 1 to 128 | Final Punishment targeting range (blocks). |
| `punishEpRatio` | 1.5 | 1 to 100 | Caster-EP / target-EP ratio required to apply Sentence. |
| `punishDurationSeconds` | 10 | 1 to 600 | Sentence effect duration (seconds). |
| `punishHpFraction` | 0.05 | 0 to 1 | Fraction of target's max HP dealt per second by Sentence (0.05 = 5%). |
| `punishEpAbsorb` | 0.25 | 0 to 1 | Fraction of target's EP absorbed by caster on death during Sentence (0.25 = 25%). |
| `punishCooldownSeconds` | 60 | 0 to 3,600 | Final Punishment cooldown, unmastered (seconds). |
| `punishCooldownSecondsMastered` | 10 | 0 to 3,600 | Final Punishment cooldown, mastered (seconds). |

## `[Skills.blockade]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Blockade. |
| `durationSeconds` | 10 | 1 to 600 | Regen Suppression duration applied to the target, unmastered (seconds). |
| `durationSecondsMastered` | 20 | 1 to 600 | Regen Suppression duration applied to the target, mastered (seconds). |
| `cooldownSeconds` | 30 | 0 to 3,600 | Blockade cooldown (seconds). |
| `vexKillsRequired` | 30 | 0 to 10,000 | Vex kills required for Blockade auto-unlock (in addition to Magic Jamming being mastered). |

## `[Skills.deus_sanguis]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Deus Sanguis. |
| `bleedTier` | 6 | 1 to 32 | Bleed-on-melee tier applied while toggled, unmastered (1 = amplifier 0). |
| `bleedTierMastered` | 10 | 1 to 32 | Bleed tier when mastered. |
| `bleedDurationSeconds` | 4 | 1 to 60 | Bleed duration on melee hit (seconds). |
| `biteDamage` | 20 | 0 to 1,000 | Bite damage (HP), unmastered. |
| `biteDamageMastered` | 25 | 0 to 1,000 | Bite damage (HP), mastered. |
| `biteCooldownSeconds` | 3 | 0 to 3,600 | Bite cooldown (seconds). |
| `shiftCooldownSeconds` | 20 | 0 to 3,600 | Shift cooldown (seconds), unmastered. Press cycles in OR out and consumes the cooldown either way. |
| `shiftCooldownSecondsMastered` | 10 | 0 to 3,600 | Shift cooldown (seconds), mastered. |
| `drainFraction` | 0.1 | 0 to 1 | Health Drain: fraction of each enemy's CURRENT HP drained per second, unmastered (0.10 = 10%). |
| `drainFractionMastered` | 0.2 | 0 to 1 | Health Drain fraction per second, mastered. |
| `drainCooldownSeconds` | 30 | 0 to 3,600 | Health Drain cooldown (seconds), unmastered. Set on press so a tap still consumes the full cooldown. |
| `drainCooldownSecondsMastered` | 10 | 0 to 3,600 | Health Drain cooldown (seconds), mastered. |

## `[Skills.hell_passage]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Hell Passage (and block its auto-unlock when false). |
| `magiculeFraction` | 0.1 | 0 to 1 | Fraction of CURRENT magicule consumed per cast (0.10 = 10%). |
| `cooldownSeconds` | 30 | 0 to 3,600 | Cooldown (seconds), unmastered. |
| `cooldownSecondsMastered` | 10 | 0 to 3,600 | Cooldown (seconds), mastered. |
| `portalLifetimeSeconds` | 10 | 1 to 600 | How long the spawned portal entity persists before despawning (seconds). |
| `masteryPerCast` | 5 | 0 to 500 | Mastery points awarded per successful cast.<br>EXTRA-tier mastery cap is 500, so 5/cast = 100 casts to master.<br>Set to 1 for the slow Tensura default; higher = faster mastery. |

## `[Skills.hyperbolic_passage]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Hyperbolic Passage (and block its auto-unlock when false). |
| `magiculeFraction` | 0.1 | 0 to 1 | Fraction of CURRENT magicule consumed per cast (0.10 = 10%). |
| `cooldownSeconds` | 30 | 0 to 3,600 | Cooldown (seconds), unmastered. |
| `cooldownSecondsMastered` | 10 | 0 to 3,600 | Cooldown (seconds), mastered. |
| `portalLifetimeSeconds` | 10 | 1 to 600 | How long the spawned portal entity persists before despawning (seconds). |
| `masteryPerCast` | 5 | 0 to 500 | Mastery points awarded per successful cast.<br>EXTRA-tier mastery cap is 500, so 5/cast = 100 casts to master.<br>Set to 1 for the slow Tensura default; higher = faster mastery. |

## `[Skills.image_training]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Image Training Battlewill. |
| `lifespanSeconds` | 120 | 1 to 3,600 | How long the spawned clone persists before despawning (seconds). Default 120 = 2 minutes. |
| `cooldownSeconds` | 300 | 0 to 36,000 | Cooldown between casts (seconds). Default 300 = 5 minutes. |
| `epMultiplier` | 0.1 | 0 to 100 | Bonus EP awarded on killing the clone, expressed as a multiplier of the player's CURRENT EP.<br>0.10 = +10% of current EP per kill. Set to 0 to disable the bonus. |
| `masteryPerCast` | 5 | 0 to 500 | Mastery points awarded per successful cast. |
| `damageScale` | 0.5 | 0 to 10 | Multiplier applied to the summoner's attack damage when copying onto the clone.<br>0.5 = clone hits for half the player's damage. Compensates for the<br>no-resist truth-damage bypass — every hit lands unmitigated, so even a<br>small fraction of player damage adds up to meaningful pressure. Set higher<br>(e.g. 1.0 / 2.0+) for tougher / punishment-style training dummies, or lower<br>(0.10 / 0.25) for a sparring-pace partner. |

## `[Skills.trash_gamer]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Enable Trash Gamer. |
| `masteryBonus` | 4 | 0 to 1,000 | Flat mastery-point bonus added to every mastery gain on every skill while Trash Gamer is learned. |
| `duplicationMpFraction` | 0.5 | 0 to 1 | Fraction of CURRENT magicule consumed per Duplication Glitch cast, unmastered (0.50 = 50%). |
| `duplicationMpFractionMastered` | 0.25 | 0 to 1 | Fraction of CURRENT magicule consumed per Duplication Glitch cast, mastered. |
| `duplicationCooldownSeconds` | 600 | 0 to 36,000 | Duplication Glitch cooldown (seconds). |
| `buffDurationSeconds` | 180 | 1 to 7,200 | Buff Glitch effect duration (seconds). |
| `buffCooldownSeconds` | 60 | 0 to 3,600 | Buff Glitch cooldown (seconds), unmastered. |
| `buffCooldownSecondsMastered` | 10 | 0 to 3,600 | Buff Glitch cooldown (seconds), mastered. |
| `prodigyDurationSeconds` | 600 | 1 to 7,200 | Prodigy duration (seconds). Default 600s = 10 minutes. |
| `prodigyCooldownSeconds` | 1,800 | 0 to 36,000 | Prodigy cooldown (seconds). |
| `prodigyParalysisSeconds` | 180 | 0 to 3,600 | Paralysis duration (seconds) applied when Prodigy ends. |
| `prodigyDodgeChance` | 0.99 | 0 to 1 | Per-incoming-hit dodge chance during Prodigy (0.99 = 99%). |
| `prodigySpeedBonus` | 0.2 | 0 to 10 | Movement-speed bonus during Prodigy (0.20 = +20%). |
| `prodigyDamageMult` | 5 | 0 to 100 | Outgoing damage multiplier during Prodigy — stand-in for 'ignore opponent resistances and nullifications'. 5.0 = 5× damage to compensate for typical resist values. |
| `duplicationBlacklist` | "minecraft:bundle", "minecraft:shulker_box", "minecraft:white_shulker_box", "minecraft:orange_shulker_box", "minecraft:magenta_shulker_box", "minecraft:light_blue_shulker_box", "minecraft:yellow_shulker_box", "minecraft:lime_shulker_box", "minecraft:pink_shulker_box", "minecraft:gray_shulker_box", "minecraft:light_gray_shulker_box", "minecraft:cyan_shulker_box", "minecraft:purple_shulker_box", "minecraft:blue_shulker_box", "minecraft:brown_shulker_box", "minecraft:green_shulker_box", "minecraft:red_shulker_box", "minecraft:black_shulker_box" |  | Item IDs that Duplication Glitch refuses to copy. Use full registry IDs<br>(namespace:path). Vanilla container components (bundle / shulker) are<br>ALSO blocked automatically and don't need to be listed here — this list<br>is for items that hold inventory on the stack without using the standard<br>vanilla components, e.g. modded backpacks. |
