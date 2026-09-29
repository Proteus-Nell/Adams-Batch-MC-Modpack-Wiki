<small>[Tensura: Reincarnated](../index.md)</small>

# Mechanics

A guide to how Tensura: Reincarnated works. Numbers in **bold** are the mod's config defaults (or this pack's value when a pack note applies). Follow the links for the full config tables.

## Existence Points, Aura and Magicules

Every living thing has two energy pools:

- **Magicules (MP)** fuel skills and magic.
- **Aura (AP)** fuels battlewill arts and some skills.

Together they make up your **Existence Points (EP)**, the number that measures how strong you are. The Status Menu shows your HP, spiritual HP (SHP), aura, magicules, EP, souls and evolution progress.

- Killing something gives you part of its EP: between **1%** and **10%** of it as magicules, and the same range as aura.
- Aura regenerates by **5** every half second. Magicules are drawn from the chunk you stand in: each half second you absorb **0.01%** of the chunk's current magicules.
- If your MP hits 0 you fall into **Sleep Mode** for **180** seconds. When you wake up naturally you recover part of your max MP and AP.
- Holding more aura than your maximum causes **Insanity**, and holding more magicules than your maximum causes **Magicule Poison**. Every extra 25% over the cap adds a level.
- Game rules scale the EP of mobs: `tensuraEP` (default: 100%), `vanillaEP` (default: 100%), `moddedEP` (default: 100%) and `spawnerEP` (default: 10%). `epDeathPenalty` (default: 5) controls how much EP you lose on death.

### Area magicules

Each chunk has its own magicule level, starting at **500** and regenerating **10** per second, up to **1,000,000**. Mobs only spawn where a chunk has at least **10** magicules. A **Magic Engine** block drains **1,000** from surrounding chunks. Check a chunk with `/tensura worldData areaMagicule`.

## Abilities

Tensura has three families of abilities. See [Abilities](../abilities/index.md) for all of them.

| Family | Uses | Tiers |
|---|---|---|
| **Skills** | MP (sometimes AP) | Resistance, Intrinsic, Common, Extra, Unique, Ultimate |
| **Magic** | MP, with a chant (cast time) | Aspectual (elemental), Spiritual (from spirits), Summoning |
| **Battlewill** | AP | Melee, projectile and utility arts |

### Getting a new ability

Many abilities first have to be **learned**. Using an ability you are still learning costs **5x** its normal energy. Each successful use gives **1** learning point (plus a random bonus of up to **4**). You need **100** points to learn it fully. A failed attempt can apply the Misfire effect and cost you a few learning points.

Acquiring a skill outright also costs magicules. The base costs are **100** MP for Common, **100** for Intrinsic, **100** for Resistance, **1,000** for Nullification and **1,000** for Extra skills. Unique skills set their own cost, listed on each skill page. The `mpSkillCost` game rule (default: 100%) scales these.

Other ways to get abilities:

- **Reincarnation.** You start with a random Unique skill from the reincarnation pool (see below).
- **Race intrinsics.** Every race grants its intrinsic skills and can learn a set of others. Each race page lists both.
- **Tomes, manuals and dwarf traders.** Wizard-tower tomes, battlewill manuals and dwarf traders hand out abilities. Each ability page says where it can drop.
- **Taking skills from others.** Skills such as Predator can take abilities from mobs. Mob pages list each mob's innate skills.

### Mastery

Using an ability earns **mastery points**. You gain more when it hits (**x2**) or kills (**x2**). A mastered ability usually becomes stronger or cheaper; the "mastered" values are on each ability page.

| Skill tier | Mastery points to master |
|---|---|
| Intrinsic / Common / Resistance | **100** |
| Extra | **500** |
| Unique | **1,000** (Sin skills: **1,500**) |
| Ultimate | **10,000** |

Skill cooldowns count down in seconds. Passive effects that tick run every 5 seconds.

## Races and evolution

You pick a race when you first join (or roll a random one). See [Races](../races/index.md) for the full list with evolution trees. Each race has:

- a **difficulty** and an **alignment**
- an **aura and magicule range** you start in
- stat bonuses
- intrinsic skills

When you meet a race's requirements, the evolution bar in the Status Menu fills up. Each requirement is worth a share of the bar. The most common one is reaching a set EP, which by default is the target race's minimum aura plus its minimum magicule. At 100% you can **evolve**. Some races branch, and their race page shows each option.

### True Demon Lord and True Hero

- **Demon Lord Seed.** You become a Demon Lord Seed at **200,000** EP. To awaken as a **True Demon Lord** you need **10,000** souls. Killing things adds **50%** of their EP to your soul points. Awakening starts the **Harvest Festival**, which lasts **3,600** ticks. It multiplies your EP by **3** and also evolves your subordinates within **30** blocks.
- **Hero Egg.** You become a Hero Egg by gathering spirits: **1** Hero spirit (Light or Darkness) plus **5** others, each at level **3** or higher. The egg hatches into a **True Hero** while you fight a boss that is below **0.25** of its health. That multiplies your EP by **3**.
- Being named can make you lose your Seed or Egg, and you can't be both a Demon Lord and a Hero. Several races have a special **awakening evolution** listed on their page.

## Naming

You can name a monster that has less than **25%** of its health and less of your EP than you. Naming costs magicules and gives the target EP and often an evolution. There are three options:

| Option | EP multiplier for the target | Chance you permanently lose max MP |
|---|---|---|
| Subdue | x**0.5** | **0%** |
| Evolve | x**1.5** | **20%** |
| Endow | x**9** | **50%** |

A named creature becomes your subordinate. Mass Naming unlocks after **25** raids or **1,000** human kills.

## Reincarnation and reset scrolls

- Your first Unique skill is rolled from the reincarnation pool (`Skills.startingSkills` in [`reincarnation_config.toml`](../configs/config-tensura-reincarnation-config.md)). You get **1** of them. The addons in this pack add their own Unique skills to this pool.
- **Race, Skill and Character Reset Scrolls** let you start over. The **Reset Counter** rewards full runs: final race evolution, awakening, and defeating Orc Disaster, Ifrit, Charybdis, the Elemental Colossus, Hinata Sakaguchi and Gazel Dwargo.
- With the `trulyUnique` game rule (default: false), each Unique skill can only be owned by one player at a time.

## Spirits

Pray inside the Labyrinth for **200** ticks to get a spirit (the cooldown is **1,200** seconds):

| Spirit | Chance |
|---|---|
| Lesser Spirit | **40%** |
| Medium Spirit | **30%** |
| Greater Spirit | **20%** |
| Spirit Lord | **1%** |

Spirits unlock Spiritual Magic of their element and count toward the Hero Egg.

## Dwarf reputation

Trading with and helping dwarves raises your reputation with them (from **-100** to **100**). Hurting or killing them in front of witnesses lowers it. Each positive point gives a **0.005** price discount. At **-50**, dwarves stop trading and guards attack.

## Game rules

Tensura's game rules (EP scaling, griefing, naming, Truly Unique and more) are listed on the [Commands](../commands/index.md) page.
