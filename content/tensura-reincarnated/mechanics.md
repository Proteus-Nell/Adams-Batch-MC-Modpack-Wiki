# Mechanics

A guide to how Tensura: Reincarnated works. Numbers in **bold** are the mod's config defaults (or this pack's value when a pack note applies). Follow the links for the full config tables.

## Existence Points, Aura and Magicules

Every living thing has two energy pools:

- **Magicules (MP)** fuel skills and magic.
- **Aura (AP)** fuels battlewill arts and some skills.

Together they make up your **Existence Points (EP)**, the number that measures how strong you are. The Status Menu shows your HP, spiritual HP (SHP), aura, magicules, EP, souls and evolution progress.

- Killing something gives you part of its EP: between **{{cfg:config/tensura/energy_config.toml|baseMagiculeGain}}%** and **{{cfg:config/tensura/energy_config.toml|maxMagiculeGain}}%** of it as magicules, and the same range as aura.
- Aura regenerates by **{{cfg:config/tensura/energy_config.toml|baseAuraRegen}}** every half second. Magicules are drawn from the chunk you stand in: each half second you absorb **{{cfg:config/tensura/energy_config.toml|areaMagiculeRegen}}%** of the chunk's current magicules.
- If your MP hits 0 you fall into **Sleep Mode** for **{{cfg:config/tensura/energy_config.toml|sleepModeTick}}** seconds. When you wake up naturally you recover part of your max MP and AP.
- Holding more aura than your maximum causes **Insanity**, and holding more magicules than your maximum causes **Magicule Poison**. Every extra 25% over the cap adds a level.
- Game rules scale the EP of mobs: `tensuraEP` (default: {{gamerule:tensuraEP}}%), `vanillaEP` (default: {{gamerule:vanillaEP}}%), `moddedEP` (default: {{gamerule:moddedEP}}%) and `spawnerEP` (default: {{gamerule:spawnerEP}}%). `epDeathPenalty` (default: {{gamerule:epDeathPenalty}}) controls how much EP you lose on death.

### Area magicules

Each chunk has its own magicule level, starting at **{{cfg:config/tensura/area_magicule_config.toml|baseMagicule}}** and regenerating **{{cfg:config/tensura/area_magicule_config.toml|baseMagiculeRegeneration}}** per second, up to **{{cfg:config/tensura/area_magicule_config.toml|maximumMagicule}}**. Mobs only spawn where a chunk has at least **{{cfg:config/tensura/area_magicule_config.toml|minimalMagiculeSpawn}}** magicules. A **Magic Engine** block drains **{{cfg:config/tensura/area_magicule_config.toml|magicEngineReduction}}** from surrounding chunks. Check a chunk with `/tensura worldData areaMagicule`.

## Abilities

Tensura has three families of abilities. See [Abilities](@/tensura-reincarnated/abilities/index.md) for all of them.

| Family | Uses | Tiers |
|---|---|---|
| **Skills** | MP (sometimes AP) | Resistance, Intrinsic, Common, Extra, Unique, Ultimate |
| **Magic** | MP, with a chant (cast time) | Aspectual (elemental), Spiritual (from spirits), Summoning |
| **Battlewill** | AP | Melee, projectile and utility arts |

### Getting a new ability

Many abilities first have to be **learned**. Using an ability you are still learning costs **{{cfg:config/tensura/ability/ability_config.toml|Learning.learningCostMultiplier}}x** its normal energy. Each successful use gives **{{cfg:config/tensura/ability/ability_config.toml|Learning.learningPoint}}** learning point (plus a random bonus of up to **{{cfg:config/tensura/ability/ability_config.toml|Learning.maxBonus}}**). You need **{{cfg:config/tensura/ability/ability_config.toml|Learning.learningPointRequirement}}** points to learn it fully. A failed attempt can apply the Misfire effect and cost you a few learning points.

Acquiring a skill outright also costs magicules. The base costs are **{{cfg:config/tensura/ability/skill_config.toml|mpAcquirementCommon}}** MP for Common, **{{cfg:config/tensura/ability/skill_config.toml|mpAcquirementIntrinsic}}** for Intrinsic, **{{cfg:config/tensura/ability/skill_config.toml|mpAcquirementResistance}}** for Resistance, **{{cfg:config/tensura/ability/skill_config.toml|mpAcquirementNullification}}** for Nullification and **{{cfg:config/tensura/ability/skill_config.toml|mpAcquirementExtra}}** for Extra skills. Unique skills set their own cost, listed on each skill page. The `mpSkillCost` game rule (default: {{gamerule:mpSkillCost}}%) scales these.

Other ways to get abilities:

- **Reincarnation.** You start with a random Unique skill from the reincarnation pool (see below).
- **Race intrinsics.** Every race grants its intrinsic skills and can learn a set of others. Each race page lists both.
- **Tomes, manuals and dwarf traders.** Wizard-tower tomes, battlewill manuals and dwarf traders hand out abilities. Each ability page says where it can drop.
- **Taking skills from others.** Skills such as Predator can take abilities from mobs. Mob pages list each mob's innate skills.

### Mastery

Using an ability earns **mastery points**. You gain more when it hits (**x{{cfg:config/tensura/ability/ability_config.toml|Mastery.masteryHitMultiplier}}**) or kills (**x{{cfg:config/tensura/ability/ability_config.toml|Mastery.masteryKillMultiplier}}**). A mastered ability usually becomes stronger or cheaper; the "mastered" values are on each ability page.

| Skill tier | Mastery points to master |
|---|---|
| Intrinsic / Common / Resistance | **{{cfg:config/tensura/ability/skill_config.toml|Mastery.masteryIntrinsic}}** |
| Extra | **{{cfg:config/tensura/ability/skill_config.toml|Mastery.masteryExtra}}** |
| Unique | **{{cfg:config/tensura/ability/skill_config.toml|Mastery.masteryUnique}}** (Sin skills: **{{cfg:config/tensura/ability/skill_config.toml|Mastery.masteryUniqueSin}}**) |
| Ultimate | **{{cfg:config/tensura/ability/skill_config.toml|Mastery.masteryUltimate}}** |

Skill cooldowns count down in seconds. Passive effects that tick run every 5 seconds.

## Races and evolution

You pick a race when you first join (or roll a random one). See [Races](@/tensura-reincarnated/races/index.md) for the full list with evolution trees. Each race has:

- a **difficulty** and an **alignment**
- an **aura and magicule range** you start in
- stat bonuses
- intrinsic skills

When you meet a race's requirements, the evolution bar in the Status Menu fills up. Each requirement is worth a share of the bar. The most common one is reaching a set EP, which by default is the target race's minimum aura plus its minimum magicule. At 100% you can **evolve**. Some races branch, and their race page shows each option.

### True Demon Lord and True Hero

- **Demon Lord Seed.** You become a Demon Lord Seed at **{{gamerule:demonLordSeed}}** EP. To awaken as a **True Demon Lord** you need **{{gamerule:demonLordAwaken}}** souls. Killing things adds **{{cfg:config/tensura/race/race_config.toml|epToSoulRate}}%** of their EP to your soul points. Awakening starts the **Harvest Festival**, which lasts **{{cfg:config/tensura/race/race_config.toml|DemonLord.harvestFestivalTick}}** ticks. It multiplies your EP by **{{cfg:config/tensura/race/race_config.toml|DemonLord.epMultiplierDemonLord}}** and also evolves your subordinates within **{{cfg:config/tensura/race/race_config.toml|DemonLord.harvestFestivalRange}}** blocks.
- **Hero Egg.** You become a Hero Egg by gathering spirits: **{{cfg:config/tensura/race/race_config.toml|Hero.heroSpiritNumber}}** Hero spirit (Light or Darkness) plus **{{cfg:config/tensura/race/race_config.toml|Hero.heroCommonSpiritNumber}}** others, each at level **{{cfg:config/tensura/race/race_config.toml|Hero.heroSpiritLevel}}** or higher. The egg hatches into a **True Hero** while you fight a boss that is below **{{cfg:config/tensura/race/race_config.toml|Hero.bossHPMultiplier}}** of its health. That multiplies your EP by **{{cfg:config/tensura/race/race_config.toml|Hero.epMultiplierHero}}**.
- Being named can make you lose your Seed or Egg, and you can't be both a Demon Lord and a Hero. Several races have a special **awakening evolution** listed on their page.

## Naming

You can name a monster that has less than **{{cfg:config/tensura/entity/player_config.toml|Naming.lowHPToName}}%** of its health and less of your EP than you. Naming costs magicules and gives the target EP and often an evolution. There are three options:

| Option | EP multiplier for the target | Chance you permanently lose max MP |
|---|---|---|
| Subdue | x**{{cfg:config/tensura/entity/player_config.toml|Naming.subdueGain}}** | **{{cfg:config/tensura/entity/player_config.toml|Naming.subdueLostChance}}%** |
| Evolve | x**{{cfg:config/tensura/entity/player_config.toml|Naming.evolveGain}}** | **{{cfg:config/tensura/entity/player_config.toml|Naming.evolveLostChance}}%** |
| Endow | x**{{cfg:config/tensura/entity/player_config.toml|Naming.endowGain}}** | **{{cfg:config/tensura/entity/player_config.toml|Naming.endowLostChance}}%** |

A named creature becomes your subordinate. Mass Naming unlocks after **{{cfg:config/tensura/race/race_config.toml|massNamingRaid}}** raids or **{{cfg:config/tensura/race/race_config.toml|massNamingHuman}}** human kills.

## Reincarnation and reset scrolls

- Your first Unique skill is rolled from the reincarnation pool (`Skills.startingSkills` in [`reincarnation_config.toml`](@/tensura-reincarnated/configs/config-tensura-reincarnation-config.md)). You get **{{cfg:config/tensura/reincarnation_config.toml|Skills.skillNumber}}** of them. The addons in this pack add their own Unique skills to this pool.
- **Race, Skill and Character Reset Scrolls** let you start over. The **Reset Counter** rewards full runs: final race evolution, awakening, and defeating Orc Disaster, Ifrit, Charybdis, the Elemental Colossus, Hinata Sakaguchi and Gazel Dwargo.
- With the `trulyUnique` game rule (default: {{gamerule:trulyUnique}}), each Unique skill can only be owned by one player at a time.

## Spirits

Pray inside the Labyrinth for **{{cfg:config/tensura/race/race_config.toml|Spirit.prayingTime}}** ticks to get a spirit (the cooldown is **{{cfg:config/tensura/race/race_config.toml|Spirit.prayingCooldown}}** seconds):

| Spirit | Chance |
|---|---|
| Lesser Spirit | **{{cfg:config/tensura/race/race_config.toml|Spirit.lesserSpiritPercentage}}%** |
| Medium Spirit | **{{cfg:config/tensura/race/race_config.toml|Spirit.mediumSpiritPercentage}}%** |
| Greater Spirit | **{{cfg:config/tensura/race/race_config.toml|Spirit.greaterSpiritPercentage}}%** |
| Spirit Lord | **{{cfg:config/tensura/race/race_config.toml|Spirit.lordSpiritPercentage}}%** |

Spirits unlock Spiritual Magic of their element and count toward the Hero Egg.

## Dwarf reputation

Trading with and helping dwarves raises your reputation with them (from **{{cfg:config/tensura/entity/player_config.toml|Reputation.minReputation}}** to **{{cfg:config/tensura/entity/player_config.toml|Reputation.maxReputation}}**). Hurting or killing them in front of witnesses lowers it. Each positive point gives a **{{cfg:config/tensura/entity/player_config.toml|Reputation.discountPercentage}}** price discount. At **{{cfg:config/tensura/entity/player_config.toml|Reputation.hostileReputation}}**, dwarves stop trading and guards attack.

## Game rules

Tensura's game rules (EP scaling, griefing, naming, Truly Unique and more) are listed on the [Commands](@/tensura-reincarnated/commands/index.md) page.
