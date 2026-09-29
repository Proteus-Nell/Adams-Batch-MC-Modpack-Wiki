# ｢ True Hero, King of Champions ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:true_hero` |
| **Modes** | 5 |
| **Acquisition cost (MP)** | 900,000 |
| **Max mastery** | 5,000 |
| **Cooldowns (s)** | 3 mastered, 5 otherwise |
| **Activation** | Toggle, Press, Hold |

</div>

> Ultimate evolution of Chosen One. Toggle the skill on to gather fallen subordinates as Memories in the Banner of the Supreme King. While in your ability slot, Hero's Boons grant you and nearby allies HOTV, Luck, crit, and dodge. Lucky Field, Haki, Charisma, and Einherjar round out the lord of heroes.

## Modes

| # | Mode |
|---|---|
| 1 | 0 |
| 2 | 1 |
| 3 | 2 |
| 4 | 3 |
| 5 | 4 |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Adjusted by scrolling while active
- Has a continuous (per-tick) effect
- Does something when first learned
- Triggers when one of your subordinates dies

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Movement Speed | -0.95 | multiply total |

## Obtaining

- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.
- Acquisition checks: [Chosen One](../../../tensura-reincarnated/abilities/unique-skills/chosen-one.md), [｢ True Hero, King of Champions ｣](true-hero.md)
- In-game message: *You have awakened True Hero, Lord of Heroes.*

## Related

- **Related skills:** [Chosen One](../../../tensura-reincarnated/abilities/unique-skills/chosen-one.md)
- **Effects:** [Ally Boost](../../../tensura-reincarnated/effects/ally-boost.md)
- **Referenced by:** [｢ Yog-Sothoth, Lord of Space-Time ｣](yog-sothoth.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `Haki.speedMultiplier` | 0.05 | Activation Speed Multiplier when activated. |
| `Haki.epAcquirement` | 100,000 | EP Requirement for Learning. |
| `Haki.magiculeCost` | 25 | Magicule Cost to activate. |
| `Haki.speedMultiplier` | 0.05 | Activation Speed Multiplier when activated. |
| `Haki.speedMultiplierMastered` | 0.1 | Activation Speed Multiplier when activated with mastery. |
| `Haki.hakiRadius` | 15 | The attack radius of the haki in blocks. |
| `Haki.epDifferenceMultiplier` | 0.25 | The EP difference multiplier for each Fear Level. |
| `Haki.fearDuration` | 200 | The duration in tick of the Fear effect when applied. |
| `Haki.cooldown` | 5 | The cooldown in second of the haki. |
| `Haki.cooldownMastered` | 3 | The cooldown in second of the haki when mastered. |

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `TrueHero.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `TrueHero.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `TrueHero.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `TrueHero.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `TrueHero.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `TrueHero.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `TrueHero.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `TrueHero.mpAcquirement` | 900,000 | Magicule cost to acquire True Hero, Lord of Heroes. |
| `TrueHero.evolutionMinEp` | 5,000,000 | Minimum EP required for courage evolution tasks. |
| `TrueHero.courageRaidWinsRequired` | 25 | Raid wins required for the first courage trial. |
| `TrueHero.courageEpMultiplier` | 2 | Enemy EP multiplier for courage trials. |
| `TrueHero.courageLowHpRatio` | 0.8 | Max HP ratio (0-1) required for the second courage trial. |
| `TrueHero.courageMaxRetreatBlocks` | 30 | Max distance (blocks) allowed from the courage target for the third trial. |
| `TrueHero.courageStandTicksRequired` | 60 | Ticks within range required to complete the third courage trial. |
| `TrueHero.trueLoveMinSubordinates` | 50 | Named subordinates required for the True Love trial. |
| `TrueHero.trueLoveNearDistanceSq` | 64 | Squared distance for True Love subordinate death. |
| `TrueHero.heroBoonsRadius` | 16 | Hero's Boons ally scan radius. |
| `TrueHero.heroBoonsHotvLevel` | 9 | Hero of the Village amplifier for Hero's Boons. |
| `TrueHero.heroBoonsLuckLevel` | 9 | Luck amplifier for Hero's Boons. |
| `TrueHero.heroBoonsCritChance` | 100 | Critical hit chance bonus for Hero's Boons. |
| `TrueHero.heroBoonsDodgeChance` | 25 | Auto-dodge chance for Hero's Boons. |
| `TrueHero.memoryStatBonusPercent` | 0.1 | Fraction of each memory stat granted as a player stat bonus. 0.10 = 10%. |
| `TrueHero.memoryMaxHealthBonus` | 750 | Maximum total HP bonus from active heroic memories. |
| `TrueHero.memoryMaxAttackDamageBonus` | 100 | Maximum total attack damage bonus from active heroic memories. |
| `TrueHero.memoryMaxArmorBonus` | 100 | Maximum total armor bonus from active heroic memories. |
| `TrueHero.luckyFieldRadius` | 16 | Lucky Field scan radius. |
| `TrueHero.luckyFieldBaseLuck` | 2 | Base luck amplifier for Lucky Field. |
| `TrueHero.luckyFieldHappyBonus` | 2 | Extra luck when the user is well-fed (happy mood proxy). |
| `TrueHero.luckyFieldAllyMinEp` | 100,000 | Minimum ally EP to receive Inspiration from Lucky Field. |
| `TrueHero.luckyFieldNullifyEpRatio` | 0.5 | Attacker EP must be below this fraction of the user's EP to nullify damage. |
| `TrueHero.enableUltimateEvolution` | true | Whether True Hero evolution is allowed. |

Set in [`config/tensura/ability/skill/unique_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `ChosenOne.blessingRadius` | 15 | The radius in block of the Hero's Blessing's effect on allies. |
| `ChosenOne.mpAcquirement` | 90,000 | Magicule Acquirement Cost. |
| `ChosenOne.magiculeCostHaki` | 25 | Magicule Cost to activate Hero Haki. |
| `ChosenOne.magiculeCostCharisma` | 200 | Magicule Cost to activate Hero's Charisma. |
| `ChosenOne.heroLevel` | 5 | The level of the Hero of the Village effect. |
| `ChosenOne.luckLevel` | 5 | The level of the Luck effect. |
| `ChosenOne.allyCritChance` | 50 | The amount of Critical Chance of the Ally Boost each level.<br>Chosen One has Ally Boost II, Villain has Ally Boost I |
| `ChosenOne.meleeDodge` | 10 | Melee Dodge Chance for the user and allies when activated. |
| `ChosenOne.projectileDodge` | 10 | Projectile Dodge Chance for the user and allies when activated. |
| `ChosenOne.blessingRadius` | 15 | The radius in block of the Hero's Blessing's effect on allies. |
| `ChosenOne.controlRadius` | 10 | The radius in block of the Hero's Charisma's effect. |
| `ChosenOne.controlDuration` | 2,400 | The duration in tick of the Mind Control effect when activating Hero's Charisma (-1 = permanent). |
| `ChosenOne.controlResistedDuration` | 1,200 | The duration in tick of the Mind Control effect when activating Hero's Charisma while the target has Spiritual Attack Resistance (-1 = permanent). |
| `ChosenOne.hpMultiplier` | 0.5 | The multiplier of Max Health when an entity is revived as Ally with Hero's Charisma. |
| `ChosenOne.shpMultiplier` | 0.5 | The multiplier of Max Spiritual Health when an entity is revived as Ally with Hero's Charisma. |
