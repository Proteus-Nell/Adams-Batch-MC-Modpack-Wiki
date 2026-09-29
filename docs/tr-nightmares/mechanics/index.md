<small>[TR: Nightmares](../index.md)</small>

# Mechanics

TR: Nightmares builds on [Tensura: Reincarnated](../../tensura-reincarnated/mechanics/index.md) with Ultimate skills and several new systems. Numbers in **bold** are config or game-rule defaults. The full lists are on the [Configs](../configs/index.md) and [Commands](../commands/index.md) pages.

## Ultimate skills and God-class skills

Most of the mod's power sits in its [Ultimate Skills](../abilities/ultimate-skills/index.md). Many are reached by **evolving a Unique skill** once you meet its conditions. The in-game evolution messages are listed below.

- **God-class Ultimates** are limited: **1** owner(s) per God-class skill, and each player can hold **1** God-class skill(s). The `god_skills` game rule (default: false) and `trulygodclass` (default: false) control this.
- **Ultimate slots** (game rule `UltimateSlots`, default: false) cap how many Ultimates you can hold. You start with **1**. You earn more from reset counters, from self-naming, from awakening, and with a **0.25** chance from the sentient True Dragon and hero bosses.
- With `lose_unique_on_upgrade` (default: true), a Unique skill is used up when it evolves into its Ultimate.
- Any single hit is capped at **20,000** damage.

### Skill evolutions

These are the in-game messages you see when a skill evolves. Each one names the skills involved:

- Abaddon, King of Destruction has awakened.
- The nether's flames crown you. Agni awakens.
- Astral Light ascends into Akashic Records.
- Understood, General, your people need you just as you need them. Fight with the might of the Flame Dragon's Magic, and victory is assured.
- The forge sings with a thousand perfected forms. Godly Craftsman has evolved into Amatsumara, Lord of Crafts.
- Imitator has evolved into Artist.
- Heaven and Sloth merge. Astaroth, King of Fallen, awakens.
- Designer ascends. Astarte, Lord of Heaven, awakens.
- The Odd Laguna recognizes your strength and grants you further gifts to use for both yourself and others. This cannot be rejected.
- The Unique Skill Creator resonates with Astral Light: you have obtained the Ultimate Skill %s.
- The void recognizes you. Azathoth awakens.
- Tempter and Seeker unite. Azazel awakens.
- Gluttony and Guardian merge — Beelzebub, Lord of Gourmet awakens!
- The underworld acknowledges you. Belial awakens.
- Sloth surrenders to sleep. Belphegor, Lord of Sloth, awakens.
- The King of Divine Flames awakens — you have obtained Cthugha.
- Evolving unique into Ultimate
- Your pursuit of truth deepens until knowledge itself bends to your will. [ Ultimate Skill: Faust, Lord of Investigation ] has been obtained.
- Cadence has stilled itself completely. Your Unique Skill has evolved into the Ultimate Skill: Gabriel, Lord of Patience.
- The world acknowledges your heroism. Sunshine is reforged into Galatine.
- Gilgamesh has become God of Myth.
- Gilgamesh has ascended as King of Uruk.
- Babylon has evolved into Gilgamesh, Lord of Treasures.
- Your Unique Skill Gluttony is full, yet your Hunger is not yet sated... Attempting Evolution of the Unique Skill: Gluttony... The Unique Skill: Gluttony has evolved into the Ultimate Skill: Beelzebuth by consuming the Unique Skill: Merciless.
- Your Gourmet has evolved through Guardian's protection!
- Notice: The Unique Skill: Great Sage has collected enough data to attempt Skill Evolution. Attempting Skill Evolution into Ultimate Skill: Raphael... Attempting.... Failure.... Attempting.... Failure.... Great Sage has sacrificed the Extra Skill: Sage and the Extra Skill: Chant Annulment to evolve the Unique Skill: Great Sage into the Ultimate Skill: Raphael
- Requesting evolution of Great Sage. Confirmed. Request from Unique Skill: Great Sage. accepted. 'Great Sage'. Attempting evolution. -Failed. Re-executing. -Failed. Re-executing. -Failed. Re-executing. -Failed. Re-executing. -Failed. Re-executing. -Failed. Re-executing. -Failed. Re-executing. -Failed. Re-executing. -Failed. Re-executing. -Failed. Re-executing. -Successful. Unique Skill Great Sage has evolved into Ultimate Skill: Raphael, Lord of Wisdom
- Evolution complete: Grimoire has awakened.
- Your Guardian has evolved through Gourmet's consumption!
- Praise be, the graciousness of the world has granted unto you a powerful and holy blessing, Glorious is evolving into Haniel. To what extent will you shine now?
- The cheers of your subordinates empower you, your acts of heroism have garned many people to believe in you, you have taken a vow to protect them... Your Unique Skill: Infinity Prison has evolved into the Ultimate Skill: Uriel
- Your Elegy has evolved into Lilith, Lord of Heresy.
- Your Deluge has evolved into Livyatan, Lord of Floods.
- In the heat of battle, when prayers must be answered, evil must be cleaned, order must be maintained through the separation of powers, you find yourself glowing in Holy Light. [ Ultimate Skill: Metatron, Lord of Purity ] has been obtained.
- Evolution complete: Michael has awakened.
- Your emotional resonance crystallizes — Mood Maker awakens!
- Evolution complete: Nyarla has awakened.
- Evolution complete: Pazuzu has awakened.
- You have awakened Raguel, Lord of Charity.
- Your soul feels heavier - %s is ready to be obtained. &lt; Press %s to open the Evolution Menu. &gt;
- Deadly Poison has ripened into Samael, Lord of Deadly Poison.
- Evolution complete: Sariel has awakened.
- Evolution complete: Satanael has awakened.
- Your Tempter has ripened into Seeker.
- Uriel's vow becomes harvest — Shub-Niggurath awakens.
- Ultimate slot cap reached for %s. The evolution was queued. &lt; Press %s to reopen the Evolution Menu once a slot opens. &gt;
- Under extreme circumstances, order must be maintained, Purity and Chastity must remain untainted by the Domination of a Moral Justice. Metatron, Lord of Purity has evolved into [ Ultimate Skill: Surya, King of Brilliance ].
- Error- The Unique Skill: "Cook" has attempted evolution. This is considered dangerous, are you sure you wish to continue? Understood. The Unique Skill: "Cook" has begun to undergo evolution into the Ultimate Skill: "Susanoo, Lord of Tyranny".... Er-
- Your Seeker has ripened into Tempter.
- Your soul ascends to godhood — Tenebrosum awakens.
- You have awakened True Hero, Lord of Heroes.
- The world is having difficulties locating you, there is no stopping your progression, become one with the night, and let the night come to you... Moonshadow.
- Nightmare Ultimates are disabled on this world (gamerule nightmare_ultimates).
- The Unique Skill Time Traveler has evolved into the Ultimate Skill Yog-Sothoth, Lord of Spacetime.
- Astraea answers your heroic trials. Faith God, Zehirete awakens.

### Demonic, Angelic and Virtue skills

Consuming **Demon Essence** can create one of the Demonic skills, and **Holy Essence** one of the Angelic skills. The exact lists are the `DemonicSkillsList` and `AngelicSkillsList` options in [`nightmare_mechanics.toml`](../configs/serverconfig-nightmare-mechanic-nightmare-mechanics.md).

## Egos and personalities

Some skills awaken an **Ego**, a personality that lives in the skill, talks to you and reacts to what you do. Egos range from the Seven Sins to characters like Ciel and Michael, and they can be friendly or hostile. You can dispose of an ego, after which that skill can never awaken one again. Ego behaviour is set in [`personality_config.toml`](../configs/config-nightmare-ability-skill-ego-personality-config.md) and [`general_config.toml`](../configs/config-nightmare-ability-skill-ego-general-config.md).

## True Dragons, friendship and Dragon Bond

The True Dragons (Veldanava, Veldora, Velzard and Velgrynd) are sentient bosses. They can replace a **Leech Lizard** as a rare spawn: Veldora 1 in **10,000**, Velzard and Velgrynd 1 in **10,000**. Once befriended, you raise **Friendship**, **Loyalty** and **Bond** through interactions. High bond lets you summon the dragon for 20 minutes, or analyse it to gain its Ultimate.

| Interaction | Details |
|---|---|
| Ask / Follow | Ask them to follow you around. |
| Ask / Free | Let them roam and act on their own. |
| Ask / Stay | Ask them to wait at this spot. |
| Gii / Address Formally | Greet Gii with proper formality. |
| Gii / Discuss Strategy | Discuss plans and battle strategy. |
| Gii / Offer Information | Share useful intelligence. |
| Gii / Show Power | Display your strength with confidence. |
| Masayuuki / Ask Ally | Ask Masayuuki to stand beside you as an ally. |
| Masayuuki / Ask Collect Memories | Offer the required essences to unlock Rudra's Memory. |
| Masayuuki / Ask Follow | Ask Masayuuki to follow you. |
| Masayuuki / Ask Grow Stronger | Offer essences to awaken Masayuuki's true hero power. |
| Masayuuki / Ask Stay | Ask Masayuuki to stay at this spot. |
| Masayuuki / Mention Eyes | Mention the striking look in his eyes. |
| Masayuuki / Show Spoils | Show him the spoils of your adventures. |
| Masayuuki / Talk Another World | Speak with him about another world. |
| Masayuuki / Talk Encourage | Encourage Masayuuki and strengthen your bond. |
| Masayuuki / Talk Past | Ask Masayuuki about the past. |
| Milim / Ask / Ally | Ask Milim to become your ally. |
| Milim / Ask / Awaken | Ask Milim to awaken into a True Demon Lord. |
| Milim / Ask / Follow | Ask Milim to follow you. |
| Milim / Ask / Soul Count | Ask Milim how many soul points she has stored. |
| Milim / Ask / Stay | Ask Milim to stay where she is. |
| Milim / Gift Dragon Knuckles | Give Milim two Dragon Knuckles to equip in both hands. |
| Milim / Grow Stronger | Push Milim toward awakening by increasing her strength and reserves. |
| Milim / Insult | Say something rude to Milim. |
| Milim / Offer Cake | Give Milim 1 cake. |
| Milim / Offer Cocoa Beans | Give Milim 16 cocoa beans. |
| Milim / Offer Cookies | Give Milim 16 cookies. |
| Milim / Offer Dubious Food | Give Milim dubious food. |
| Milim / Offer Honey | Offer 16 honey bottles to calm Milim for 10 minutes. |
| Milim / Offer Honey Bottles | Give Milim 16 honey bottles. |
| Milim / Offer Pumpkin Pie | Give Milim 2 pumpkin pies. |
| Milim / Offer Stew | Give Milim ordinary stew. |
| Milim / Offer Sugar | Give Milim 16 sugar. |
| Milim / Offer Suspicious Stew | Give Milim suspicious stew. |
| Milim / Pat Head | Pat Milim on the head once she trusts you enough. |
| Milim / Return Dragon Knuckles | Ask Milim to hand back her Dragon Knuckles. |
| Milim / Spar | Challenge Milim to a friendly spar. |
| Milim / Talk | Chat with Milim. It may help or hurt your friendship. |
| Milim / Tell Joke | Tell Milim a joke and see how she reacts. |
| Veldanava / Ask Guidance | Request wisdom from the one who remembers everything. |
| Veldanava / Offer Reverence | Show your respect to the First Dragon. |
| Veldanava / Talk | A quiet conversation with the creator of the world. |
| Veldora / Analyze Veldora | Requires 500 Friendship, 300 Loyalty, and 850 Bond. Chance to gain Veldora's ultimate. |
| Veldora / Ask About Past | Requires 125 Friendship and 125 Bond. Grants Veldora Investigator. |
| Veldora / Ask For Training | Requires 50 Friendship and 90 Bond. Grants Veldora Black Lightning. |
| Veldora / Ask To Grow Stronger | Requires 500 Friendship, 500 Loyalty, and 1,000 Bond. Faust replaces Veldora's Investigator. |
| Veldora / Chat | +5 Friendship, +1 Loyalty, +1 Bond. |
| Veldora / Evolve Faust | Requires 500 Friendship, 500 Loyalty, 1,000 Bond, Alteration, and 1,550,000 EP. Grants Veldora Nyarlathotep. |
| Veldora / Give Treat | +5 Friendship, +10 Loyalty, +5 Bond. Costs 16 Cookies. |
| Veldora / Hang Out With | Requires 200 Friendship, 100 Loyalty, and 80 Bond. Chance to gain Divide. |
| Veldora / Investigate | +5 Friendship, +5 Loyalty, +15 Bond. Costs 25 levels. |
| Veldora / Nerd Out With | +20 Friendship, +20 Loyalty, +20 Bond. Costs 24 Books, 32 Cookies, and 50 levels. |
| Veldora / Read Manga | +15 Friendship, +5 Loyalty, +5 Bond. Costs 12 Books. |
| Veldora / Summon Veldora | Requires 100 Friendship, 100 Loyalty, and 100 Bond. Summons your bonded Veldora for 20 minutes. |
| Velgrynd / Analyze Velgrynd | Requires 500 Friendship, 300 Loyalty, and 850 Bond. Chance to gain Velgrynd's ultimate. |
| Velgrynd / Chat | +5 Friendship, +1 Loyalty, +1 Bond. |
| Velgrynd / Gift A Drink | +15 Friendship, +5 Loyalty, +5 Bond. Costs 4 Lava Buckets. |
| Velgrynd / Give Dinner | +5 Friendship, +10 Loyalty, +5 Bond. Costs 64 Cooked Chicken. |
| Velgrynd / Hang Out With | Requires 200 Friendship, 100 Loyalty, and 80 Bond. Chance to gain Acceleration. |
| Velgrynd / Help Grow | Requires 500 Friendship, 500 Loyalty, 1,000 Bond, Alteration, Uriel Oath/Vow, Raguel, and 2,400,000 EP. Evolves Velgrynd into Cthugha and grants you Shub Niggurath. |
| Velgrynd / Spend Time | +20 Friendship, +20 Loyalty, +20 Bond. Costs 8 Lava Buckets, 128 Cooked Chicken, and 8 Cakes. |
| Velgrynd / Spoil | +5 Friendship, +5 Loyalty, +15 Bond. Costs 4 Cakes. |
| Velgrynd / Summon Velgrynd | Requires 100 Friendship, 100 Loyalty, and 100 Bond. Summons your bonded Velgrynd for 20 minutes. |
| Velzard / Analyze Velzard | Requires 500 Friendship, 300 Loyalty, and 850 Bond. Chance to gain Velzard's ultimate. |
| Velzard / Chat | +5 Friendship, +1 Loyalty, +1 Bond. |
| Velzard / Chat About Others | Requires 125 Friendship and 125 Bond. On the 10th use, Velzard challenges you. |
| Velzard / Empower | Requires 500 Friendship, 500 Loyalty, 1,000 Bond, Alteration, and 3,000,000 EP. Grants Velzard Cthulhu and removes her Leviathan/Gabriel. |
| Velzard / Gift Flowers | +15 Friendship, +5 Loyalty, +5 Bond. Costs 12 Hipokute Flowers. |
| Velzard / Give Dinner | +5 Friendship, +10 Loyalty, +5 Bond. Costs 16 Golden Carrots. |
| Velzard / Hang Out With | Requires 200 Friendship, 100 Loyalty, and 80 Bond. Chance to gain Cessation. |
| Velzard / Relax With | +5 Friendship, +5 Loyalty, +15 Bond. Costs 12 Dragon Essence or 12 Ice Essence. |
| Velzard / Spend Time | +20 Friendship, +20 Loyalty, +20 Bond. Costs 24 Hipokute Flowers, 32 Golden Carrots, and 24 Dragon Essence or 24 Ice Essence. |
| Velzard / Summon Velzard | Requires 100 Friendship, 100 Loyalty, and 100 Bond. Summons your bonded Velzard for 20 minutes. |
| Yuuki / Ask Ally | Ask Yuuki to stand beside you as an ally. |
| Yuuki / Ask Follow | Ask Yuuki to follow you. |
| Yuuki / Ask Grow Greed | Offer daemon essence and awaken Yuuki's Greed. |
| Yuuki / Ask Overwhelming Greed | Channel immense power into Yuuki and evolve Greed into Mammon. |
| Yuuki / Ask Stay | Ask Yuuki to hold position here. |
| Yuuki / Spoil Series | Reveal a story spoiler to Yuuki and see how she reacts. |
| Yuuki / Talk Dragons | Discuss dragon battles with Yuuki and earn her respect. |
| Yuuki / Talk Manga | Discuss manga with Yuuki and strengthen your bond. |
| Yuuki / Threaten Him | Throw a threat at Yuuki and provoke a hostile response. |
| Yuuki / Toss Coin | Offer a coin to curry favor with Yuuki. |

### Inner World

A True Dragon can live inside your clone (**Inner World**). There you can talk to it (5-minute cooldown between conversations), learn its techniques by chance, and awaken its Lord power.

## Noble Phantasms

Noble Phantasms are legendary weapons and relics with unique effects:

| Noble Phantasm | Details |
|---|---|
| Angra Mainyu | Imparts a random curse on hit. |
| Avalon | Quarter-cost ultra speed regeneration and clears negative status. |
| Avalon Lionheart | Massively increases speed and dodge chance. |
| Balmung | Massive damage against draconic targets. |
| Excalibur Lionheart | Buffs and damage scale with nearby hostiles. |
| Excalibur Phantasm | Multiplied damage vs undead, majin, and true dragons. |
| Fragarach | Teleports behind attackers and counter-strikes. |
| Gae Bolg | Guaranteed hits that inflict bleeding. |
| Gae Buidhe | Wounds resist all healing until spear returns or wielder dies. |
| Gae Dearg | Ignores defense, barriers, and nullifications. |
| God Force | Damage scales with AP. |
| Harpe | Death bypasses revival and death evasion. |
| Holy Grail | Absorbs EP from nearby kills to revive the wielder. |
| Jeweled Sword Zelretch | Infinite MP regeneration while held. |
| Lord Camelot | Protects allies while granting defensive buffs. |
| Muramasa Phantasm | Randomly severs movement, sight, skills, casting, regen, and more. |
| Rho Aias | Seven shield layers with stored retaliation. |
| Rule Breaker | Severs contracts and applies anti-magic on hit. |
| True Nine Lives | Projectile splits into nine independent attacks. |

## Souls and soul traits

With `nightmareSoulType` (default: true) and `nightmareSoulTraits` (default: true) on, every soul has a type and **soul traits**. Traits evolve once you reach a set EP and have consumed enough Elder Essence. Elemental souls grant a physique bolster, and some traits awaken skills (for example the Time trait grants Spacetime Manipulation).

## Other bosses

Rare boss replacements (1 in X chance, from `nightmare_bosses.toml`):

| Boss | Replaces | Chance |
|---|---|---|
| Crimson | a Daemon | 1 in **10,000** |
| Agera | a Daemon | 1 in **1,000** |
| Ancient Daemon | a Lesser Daemon | 1 in **1,000** |
| Primordial Daemon aspect | a daemon in Hell | 1 in **1,000** |
| Milim (Wrath) | an Otherworlder | 1 in **1,000** |
| Yuuki (Desire) | an Otherworlder | 1 in **1,000** |
| Mariabell Rosso | an Otherworlder | 1 in **1,000** |
| Glenda / Arios | an Otherworlder | 1 in **1,000** |
| Lucius / Raymond | an Otherworlder | 1 in **1,000** |
| Frey | a Phantom | 1 in **50** |

## Faith and Grace

Players can found a faith. A world allows **3** gods or faith leaders. Each faith can have up to **20** followers, including up to **4** priests.

## Families, titles and deals

- **Families:** create one with `/trnightmare family create <name>` and add players with `/trnightmare family invite <player>`. They join with `/trnightmare family accept`.
- **Titles:** some titles have a holder limit, so only a set number of players can hold them.
- **Deals (Deal Maker):** a contract system that can, among other things, force a naming (subdue, evolve, endow or custom) without the usual conditions. `maxDealMakerUsers` (default: 1) limits who can use it.

## Entity awakening

With `EntityAwakening` (default: true), mobs can awaken the way players do once they have at least **200,000** EP and **10,000,000** soul points.
