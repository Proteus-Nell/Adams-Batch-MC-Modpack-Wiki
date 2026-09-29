# Mechanics

TR: Nightmares builds on [Tensura: Reincarnated](@/tensura-reincarnated/mechanics/index.md) with Ultimate skills and several new systems. Numbers in **bold** are config or game-rule defaults. The full lists are on the [Configs](@/tr-nightmares/configs/index.md) and [Commands](@/tr-nightmares/commands/index.md) pages.

## Ultimate skills and God-class skills

Most of the mod's power sits in its [Ultimate Skills](@/tr-nightmares/abilities/ultimate-skills/index.md). Many are reached by **evolving a Unique skill** once you meet its conditions. The in-game evolution messages are listed below.

- **God-class Ultimates** are limited: **{{cfg:serverconfig/nightmare/mechanic/nightmare_mechanics.toml|godOwnerAmount.GodOwnerAmount}}** owner(s) per God-class skill, and each player can hold **{{cfg:serverconfig/nightmare/mechanic/nightmare_mechanics.toml|godSkillsOwned.GodSkillsOwned}}** God-class skill(s). The `god_skills` game rule (default: {{gamerule:god_skills}}) and `trulygodclass` (default: {{gamerule:trulygodclass}}) control this.
- **Ultimate slots** (game rule `UltimateSlots`, default: {{gamerule:UltimateSlots}}) cap how many Ultimates you can hold. You start with **{{cfg:serverconfig/nightmare/mechanic/UltimateSlotConfig.toml|ultimateSlotSettings.DefaultUltimateSlot}}**. You earn more from reset counters, from self-naming, from awakening, and with a **{{cfg:serverconfig/nightmare/mechanic/UltimateSlotConfig.toml|ultimateSlotSettings.UltimateSlotRewardChance}}** chance from the sentient True Dragon and hero bosses.
- With `lose_unique_on_upgrade` (default: {{gamerule:lose_unique_on_upgrade}}), a Unique skill is used up when it evolves into its Ultimate.
- Any single hit is capped at **{{cfg:serverconfig/nightmare/mechanic/nightmare_mechanics.toml|damageCapSettings.UniversalDamageCap}}** damage.

### Skill evolutions

These are the in-game messages you see when a skill evolves. Each one names the skills involved:

{{langlist:trnightmare\.evolution\.[a-z_]+}}

### Demonic, Angelic and Virtue skills

Consuming **Demon Essence** can create one of the Demonic skills, and **Holy Essence** one of the Angelic skills. The exact lists are the `DemonicSkillsList` and `AngelicSkillsList` options in [`nightmare_mechanics.toml`](@/tr-nightmares/configs/serverconfig-nightmare-mechanic-nightmare-mechanics.md).

## Egos and personalities

Some skills awaken an **Ego**, a personality that lives in the skill, talks to you and reacts to what you do. Egos range from the Seven Sins to characters like Ciel and Michael, and they can be friendly or hostile. You can dispose of an ego, after which that skill can never awaken one again. Ego behaviour is set in [`personality_config.toml`](@/tr-nightmares/configs/config-nightmare-ability-skill-ego-personality-config.md) and [`general_config.toml`](@/tr-nightmares/configs/config-nightmare-ability-skill-ego-general-config.md).

## True Dragons, friendship and Dragon Bond

The True Dragons (Veldanava, Veldora, Velzard and Velgrynd) are sentient bosses. They can replace a **Leech Lizard** as a rare spawn: Veldora 1 in **{{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.veldoraRarity}}**, Velzard and Velgrynd 1 in **{{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.velzardRarity}}**. Once befriended, you raise **Friendship**, **Loyalty** and **Bond** through interactions. High bond lets you summon the dragon for 20 minutes, or analyse it to gain its Ultimate.

{{langtable:trnightmare\.friendship\.(.+)\.desc|Interaction}}

### Inner World

A True Dragon can live inside your clone (**Inner World**). There you can talk to it (5-minute cooldown between conversations), learn its techniques by chance, and awaken its Lord power.

## Noble Phantasms

Noble Phantasms are legendary weapons and relics with unique effects:

{{langtable:trnightmare\.phantasm\.(.+)\.effect|Noble Phantasm}}

## Souls and soul traits

With `nightmareSoulType` (default: {{gamerule:nightmareSoulType}}) and `nightmareSoulTraits` (default: {{gamerule:nightmareSoulTraits}}) on, every soul has a type and **soul traits**. Traits evolve once you reach a set EP and have consumed enough Elder Essence. Elemental souls grant a physique bolster, and some traits awaken skills (for example the Time trait grants Spacetime Manipulation).

## Other bosses

Rare boss replacements (1 in X chance, from `nightmare_bosses.toml`):

| Boss | Replaces | Chance |
|---|---|---|
| Crimson | a Daemon | 1 in **{{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.crimsonRarity}}** |
| Agera | a Daemon | 1 in **{{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.ageraRarity}}** |
| Ancient Daemon | a Lesser Daemon | 1 in **{{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.ancientDaemonRarity}}** |
| Primordial Daemon aspect | a daemon in Hell | 1 in **{{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.primordialDaemonAspectRarity}}** |
| Milim (Wrath) | an Otherworlder | 1 in **{{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.milimWrathRarity}}** |
| Yuuki (Desire) | an Otherworlder | 1 in **{{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.yuukiRarity}}** |
| Mariabell Rosso | an Otherworlder | 1 in **{{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.mariabellRarity}}** |
| Glenda / Arios | an Otherworlder | 1 in **{{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.glendaAriosRarity}}** |
| Lucius / Raymond | an Otherworlder | 1 in **{{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.luciusRaymondRarity}}** |
| Frey | a Phantom | 1 in **{{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.freyPhantomRarity}}** |

## Faith and Grace

Players can found a faith. A world allows **{{cfg:serverconfig/nightmare/mechanic/faith_grace.toml|faith_and_grace.maxGods}}** gods or faith leaders. Each faith can have up to **{{cfg:serverconfig/nightmare/mechanic/faith_grace.toml|faith_and_grace.maxFollowersPerFaith}}** followers, including up to **{{cfg:serverconfig/nightmare/mechanic/faith_grace.toml|faith_and_grace.maxPriestsPerFaith}}** priests.

## Families, titles and deals

- **Families:** create one with `/trnightmare family create <name>` and add players with `/trnightmare family invite <player>`. They join with `/trnightmare family accept`.
- **Titles:** some titles have a holder limit, so only a set number of players can hold them.
- **Deals (Deal Maker):** a contract system that can, among other things, force a naming (subdue, evolve, endow or custom) without the usual conditions. `maxDealMakerUsers` (default: {{gamerule:maxDealMakerUsers}}) limits who can use it.

## Entity awakening

With `EntityAwakening` (default: {{gamerule:EntityAwakening}}), mobs can awaken the way players do once they have at least **{{gamerule:entityAwakeningMinEp}}** EP and **{{gamerule:entityAwakeningSoulPointsRaw}}** soul points.
