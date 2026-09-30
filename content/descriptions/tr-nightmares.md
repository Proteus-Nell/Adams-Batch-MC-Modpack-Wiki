# TR: Nightmares: what things do

Written from the mod's code (TR: Nightmares 1.0.5.0). Each `## id` section becomes the "What it does" part of that entry's page.
Numbers marked "per level" grow with the effect level: Minecraft multiplies an effect's attribute bonus by its level.

<!-- kind: effects -->

## trnightmare:acceleration
Doubles your attack speed. While it lasts, every hit you land teleports you straight to the creature you hit.

## trnightmare:acceleration_overdrive
Speeds you up at a cost: **+5%** movement speed, **+5** attack damage and **+5%** attack speed per level. It counts as a harmful effect, and milk and other cures don't remove it.

## trnightmare:apotheosis
A large combat buff: **+20** attack damage and **+20%** movement speed at level I, plus **+15** damage and **+15%** speed for each level above that.

## trnightmare:arrogance
Per level: **+60** attack damage, **+10** armor, **+0.3** attack speed and **+0.2** knockback resistance.

The catch:
- **Mobs** with Arrogance that have no target pick a fight with the nearest living thing within 15 blocks. At level II and higher they attack their own allies too.
- **Players** pay for it at the end. Once 10 seconds or less remain, every second it takes **10%** of your max health and **10%** of your max spiritual health (it never takes you below 1).
- Hitting something while arrogant extends the effect, to at least 30 seconds or 3 seconds more than it had.

Milk and other cures don't remove it.

## trnightmare:arroganz_mirror
**+20** attack damage and **+20%** armor at level I, plus **+15** and **+15%** per extra level. While it lasts, no single hit can deal you more than **500** damage.

## trnightmare:envious_mirror
**+20** attack damage and **+20%** armor at level I, plus **+15** and **+15%** per extra level. While it lasts, no single hit can deal you more than **1,000** damage.

## trnightmare:asmodeus
Lust-style energy theft. Every time you (a player) hit a creature, you drain **30,000** energy from it into yourself. From level II up you also drain a share of its total energy: about **2%** at level II and **4.8%** at level III. Your aura and magicule can't go over your maximum from this.

Raziel blocks this effect, like other charm effects.

## trnightmare:arroganz_antiskill
Shuts off skills. While you have it, you can't use or interact with any of your skills.

## trnightmare:asmodeusd
The Asmodeus "embrace": you are held in place. Your movement speed drops to zero, you can't be knocked back and your view is locked where you were looking. Every second, the player who applied it drains your energy: **20,000** at level I, or **50%** of your energy at level II and higher.

If you applied it to yourself, it ends as soon as nothing is within 3 blocks in front of you. Raziel and CNPC Lock protect against it.

## trnightmare:assault_moded
The demon-clan transformation from Assault Mode (Coffin of Darkness also grants it for a while when it saves you from death). Per level: **+12** attack damage, **+20** armor, **+0.05** movement speed, and **double** max magicule and aura.

Every half second it spends magicule (100 per health point) to heal your missing health. When it ends, your current magicule and aura are **halved** and you get the usual transformation hangover: {{link:minecraft:weakness}} II, {{link:tensura:fragility}} II and {{link:tensura:paralysis}} I for 10 minutes. You can only have one transformation active at a time.

## trnightmare:astral_protection
**+50** armor per level. Milk and other cures don't remove it.

## trnightmare:bacchus
Bacchus Rage: **+50** armor and **+40** attack damage per level. It also builds a hidden "insanity" counter on the last creature you hit, but nothing in the mod reads that counter yet.

## trnightmare:bardic
**+50%** movement speed and **+50%** attack speed per level, and it heals **1%** of your max health every second.

## trnightmare:divine_regeneration
**+50%** movement speed and **+50%** attack speed per level, and it heals **1%** of your max health every second.

## trnightmare:beastgod
Beast God, the Nemean Lord and Eyaluth transformation. Every stat bonus is multiplied by (level + 1):

| Bonus | Level I | Level II |
|---|---|---|
| Max health | +800 | +1,200 |
| Attack damage | +50 | +75 |
| Armor | +24 | +36 |
| Movement speed | +0.2 | +0.3 |
| Knockback resistance | +1.0 | +1.5 |

It also **triples** your max magicule and aura, refills both when it starts, and lets you fly. While it lasts you regain **0.2%** of your max magicule and aura and **1** health every second. Nemean Lord's Beast Rampage pushes it to level 10 or higher.

When it ends, you lose the flight and get the transformation hangover: {{link:minecraft:weakness}} II, {{link:tensura:fragility}} II and {{link:tensura:paralysis}} I for 10 minutes. Turning Nemean Lord off early instead gives Slowness III, Weakness III and {{link:tensura:magic_interference}} II for 15 minutes.

## trnightmare:blackpara
Black Paralysis. It's labelled beneficial but works as a debuff. Per level: **-30%** movement speed, **-20%** attack speed, **-20%** armor and **-0.3** block break speed. At level II and higher it also stops you sprinting. Having Abnormal Condition Resistance toggled on lowers its level by one. Black Flame Thunder's touch attack inflicts it on mobs.

## trnightmare:cadence_white_lock
White Lock freezes a creature almost completely. It sets these to zero:
- walking, flying, swimming, lava and gliding speed
- attack damage and attack speed
- jump strength, block reach and follow range
- aura and magicule regeneration

Flyers are pulled out of the air, mobs lose their target and can't pick a new one, and the creature can't activate, toggle or scroll its skills.

Cadence (mastered) inflicts it for 30 seconds. Gabriel inflicts it too, and so do Gabriel's and Cthulhu's counter-freeze. Cthulhu's owner is immune.

## trnightmare:castle_guard
Nothing in the mod applies or checks this effect in this version. Michael's and Dominator's "Castle Guard" modes work on their own, without it.

## trnightmare:chimera_form
The chimera shape from Universal Shapeshift. You need that skill mastered, plus Gluttony, Beelzebuth or Azathoth. It gives **+30** attack damage, **+25** armor and **+0.7** movement speed, raises your max magicule and aura to **2.5×**, and makes you 1.5× bigger (you can scroll your size between 1.5× and 3.75× while in this form).

When it ends, your max energy and size go back to normal and you get {{link:tensura:paralysis}} II, {{link:tensura:fragility}} II and {{link:minecraft:weakness}} II for 10 minutes.

## trnightmare:complete_concealment
Hides your soul: analytical appraisal can't read you. It also counts as presence concealment against Battle Mode, which loses its lock on you if your concealment is higher than the attacker's presence sense. Belial's Nihilistic World strips it from anyone pulled inside.

## trnightmare:core_damage
Damage to the spiritual core. It lowers spiritual health regeneration by **25%** per level. From level II up it also dampens every change to your spiritual health, healing and damage alike, by 25% per level above I. At level V your spiritual health stops changing at all.

Forbidden magic projectiles inflict level II. So does the Ending Sealed sword for 5 seconds, when its wielder has Ending.

## trnightmare:costless
Emergency regeneration. Whenever you drop to **20%** health or lower, it heals your missing health using magicule, at the Infinite Regeneration rate: {{cfg:config/tensura/ability/skill/extra_config.toml|InfiniteRegeneration.magiculeCost}} magicule per health point, or {{cfg:config/tensura/ability/skill/extra_config.toml|InfiniteRegeneration.magiculeCostMastered}} if the source skill is mastered. At level II and higher it also refills your spiritual health, at {{cfg:config/tensura/ability/skill/extra_config.toml|InfiniteRegeneration.shpMagiculeCost}} magicule per point.

If you run out of magicule it heals what it can, and the skill that gave it switches off. In this version it only heals while you also have Tensura's Instant Regeneration effect, because it reads the source skill from that effect.

Given by Vehement, Snatch, Glitcher (Kindness Heal), Ocean (in rain or water), Tornado (while airborne), Sunshine Grace and Escanor (in sunlight), and Tyche's roll of 100.

## trnightmare:courage
**+25%** attack damage and **+2** armor at level I, plus **+15%** and **+1** per extra level. Camael's Total Combat Zone gives it to the caster for 10 minutes.

## trnightmare:coward
**-35%** attack damage and **-10%** movement speed at level I, plus **-15%** and **-5%** per extra level. Camael's Total Combat Zone gives Coward II for a minute to anyone caught in the zone who leaves it.

## trnightmare:cthulhu_drain
Consumes the soul. Every 0.4 seconds it deals **350** spiritual damage (+25 per extra level), and applies Slowness II or higher and Weakness. Milk and other cures don't remove it.

## trnightmare:cthulhu_inferior
Cthulhu's "Inferior" form: **+200** attack damage, **+100** armor and **+500** max health (these don't change with level). While it lasts, no single hit deals you more than **500** damage, and your own physical hits are capped at **1,000** damage.

## trnightmare:cursed_poison
Every second it deals **2** damage per level, and from level III up it also causes Nausea. Milk and other cures don't remove it. If a creature dies while it has Cursed Poison, the player who killed it gains **{{cfg:config/nightmare/ability/skill/nightmare_unique.toml|DeadlyPoison.cursedKillEpBonusFraction}}×** their own current EP as a bonus.

Deadly Poison applies it: Bloody Bite inflicts levels II to IV depending on your lethal dose, and the mastered Cursed Poison mode inflicts level I for 5 minutes. Samael's Death World gives it to every guest (level III, refreshed while they stay), and Samael's owner is immune.

## trnightmare:daemon_omen
A raid trigger. Killing an Arch Daemon (30% chance) or a Greater Daemon (2%) gives it for 30 seconds. If you walk into a **dwarf village** that still has dwarves while you have it, a **daemon raid** starts: 5, 7 or 10 waves on Easy, Normal or Hard. Starting the raid uses up the omen.

## trnightmare:dire_omen
A raid trigger. Killing an alpha direwolf has a 5% chance to give it for 30 seconds. If you walk into a **goblin village** that still has goblins while you have it, a **direwolf raid** starts. Starting the raid uses up the omen.

## trnightmare:falmuth_omen
A raid trigger. Killing Folgen gives it for 30 seconds: a 50% chance, or always if you are Majin. If you walk into an **orc village** while you have it, a **human (Falmuth army) raid** starts: 5, 7 or 10 waves on Easy, Normal or Hard. Starting the raid uses up the omen.

## trnightmare:monster_omen
A raid trigger. Killing an Orc (2% chance) or an Orc Lord (52%) gives it for 30 seconds, and killing an Orc Disaster always does. Vanilla Bad Omen also turns into Monster Omen when you enter one of these villages. If you walk into a **lizardman village** while you have it, a **monster raid** starts, and the omen is used up. It also stops vanilla raids from starting while you carry it.

## trnightmare:demon_burned
Hellblaze: black flames that deal **1** damage per level every second, and **stop you from healing at all** while they burn. A Bucket of Cattledeer Milk or a Silver Apple cures it. Coffin of Darkness sets touched enemies ablaze for 10 seconds.

## trnightmare:deus
Deus Ex Machina's Chaotic Barrier (15 seconds). It gives **+8** armor and a multilayer barrier that grows by 10 layers every second. All damage you take is cut to **75%**, and players take a further 30% less on top of that (about **52%** in total). While it's up, your attacks also flip type: physical hits land as holy (magic) damage and magic hits land as physical damage.

## trnightmare:dragonmaddness
Dragon Madness, the fear a true dragon's presence causes. Per level: **-25%** max health and **-5%** movement speed. It also grounds you: you can't fly unless you are in Creative, in spiritual form, in bat mode, a Lesser Daemon, or wearing the full Holy Armaments set. Milk and other cures don't remove it.

Higher levels get worse. The checks run every 2 seconds:
- **Level IV+:** a curse hit equal to your max health. If it leaves a non-Majin player below 5% health while still on a starting race, they turn into a **Wight** (and become Majin).
- **Level V+:** players within 7 blocks of whoever caused it take insanity damage.
- **Level X+:** fear damage too. If the source is using Demon Lord Haki (or Villain's haki mode), players may turn Majin.

Having Abnormal Condition Resistance toggled on counts the effect as 2 levels lower.

## trnightmare:ending
A marker effect with soul particles. The Ending Unsealed sword applies it for 5 seconds when its wielder has the Ending skill. Nothing else reads it in this version.

## trnightmare:ending_soul
A marker effect with soul particles. Cthulhu's Whiteout Absorb puts it on its target (level V, 5 seconds). Nothing else reads it in this version.

## trnightmare:enkidu_bind
Enkidu's golden chains (from TR: Nightmares' Tensura: Mysticism compat) bind the target. It sets these to zero:
- walking, flying and swimming speed
- attack damage and attack speed
- jump strength and block reach
- aura and magicule regeneration
- melee and projectile dodge chance

Flyers are pulled down. While bound you can't learn skills, your race abilities stop working, and your other skills are locked to what your race limit allows.

## trnightmare:envied
Leviathan's and Cthulhu's "Crushing Jealousy" mark. It lands on a creature that has more magicule or aura than the attacker. While it's marked, the attacker's hits drain a share of its magicule or aura (picked at random) into the attacker. If the attacker has more energy instead, the target gets {{link:trnightmare:stolen_luck}}.

## trnightmare:freezing_burn
A paradox flame that burns cold. It gives **-50%** movement speed per level and keeps you covered in {{link:tensura:frost}}. It also puts out and blocks normal fire. Every second it deals **10** ice damage plus **10** flame-breath damage, and this damage can't be dodged.

Freezing Flame's white-flame hits inflict it for 10 seconds (level II when mastered), and so do Paradox flames. Creatures with Spiritual Attack Nullification or Thermal Fluctuation Nullification toggled on are immune.

## trnightmare:gabriel_heat_death
Left behind by Gabriel's and Cthulhu's Heat Death. That attack instantly kills everything in its area unless the target has Thermal Fluctuation Nullification and at least 70% of the caster's EP. Survivors get this effect, and while it lasts, **cold and spatial damage deal 75% more** to them.

## trnightmare:giant_dance
The giant races' transformation, from the Giant Dance skill. It only works on giant-line races. Per level: **+10** attack damage, **+12** attack speed and effectively full knockback immunity.

When it ends, your current magicule and aura are **halved**, and you get {{link:minecraft:weakness}} II, {{link:tensura:fragility}} II and {{link:tensura:paralysis}} II for 10 minutes. You can only have one transformation active at a time.

## trnightmare:glorious_regen
Glorious' and Haniel's regeneration. Every half second it heals all your missing health, paying **100** magicule per health point. Toggling Glorious on halves that cost at level I, and Haniel halves it at level II. At level II (from Haniel or Hamiel) it also refills your spiritual health, at **240** magicule per point (Haniel ×{{cfg:config/nightmare/ability/skill/nightmare_ult.toml|Haniel.regenCostMultiplier}}, Hamiel ×{{cfg:config/nightmare/ability/skill/nightmare_ult.toml|Hamiel.regenCostMultiplier}}).

If you run out of magicule, the skill that gave it switches off. With Haniel or Hamiel toggled on it can also save you from a killing blow, unless the damage bypasses invulnerability or pierces barriers at level 1.75 or higher. {{link:trnightmare:necrotic}} strips it.

## trnightmare:godspeed_regeneration
Godspeed Regeneration's heal. Every half second it heals missing health for **80** magicule per point (**40** when mastered) and missing spiritual health for **240** magicule per point (**290** when mastered). It stays while the skill is toggled on.

## trnightmare:holy_ascension
**+50** attack damage per level, and you glow. You take **half damage** from everything, and spiritual damage is cut by a further 30%. Every hit you land teleports you to your target. Every second it heals **1** health and **1** spiritual health per level, costing players **20** magicule per point healed. If you run out of magicule, the effect ends.

## trnightmare:hopes_gift
Sariel's and Yog-Sothoth's gift to themselves and their subordinates, refreshed while the skill is toggled on. It gives **+100%** critical hit chance, and **+25%** automatic melee and projectile dodge chance.

## trnightmare:inked
Raziel's ink. Each physical hit from Raziel adds one level, up to {{cfg:config/nightmare/ability/skill/nightmare_ult.toml|Raziel.inkCap}}, and the effect lasts 30 seconds.
- At level {{cfg:config/nightmare/ability/skill/nightmare_ult.toml|Raziel.renameThreshold}} the target is temporarily renamed.
- At level {{cfg:config/nightmare/ability/skill/nightmare_ult.toml|Raziel.antiSkillThreshold}} it gets Anti-Skill for 20 seconds.
- At level {{cfg:config/nightmare/ability/skill/nightmare_ult.toml|Raziel.eraseThreshold}} Raziel can **erase** it.

## trnightmare:intangible
You can't be hurt at all while it lasts, and you glow. Love Locomotive's "Faded Desire" grants it for 5 to 10 seconds. Arelkos' Cowardice grants it for 30 seconds, along with Speed II.

## trnightmare:isolate
Isolate holy magic cuts the target off from spiritual recovery. It lowers spiritual health regeneration by **25%** per level. The spell inflicts level III (**-75%**) for 60 seconds, or level IV (**-100%**, no regeneration at all) when mastered.

## trnightmare:jealous
Leviathan's envy. It stops the target's magicule and aura regeneration completely. Level II also lowers their max magicule and aura by **1.5%**, and level III or higher by **5%**.

Leviathan applies it to everything within 20 blocks while it's in a slot (Violent Envy), and at level II from Power Siphon, level III from Envy Festival, and sometimes on hit (Serpent's Jealousy). Cthulhu applies it too.

## trnightmare:kinetic
**-10%** movement speed per level. Nothing in TR: Nightmares applies it in this version, so you'll only see it from commands.

## trnightmare:knight_fury
Mad Knight's fury, kept up while the skill is toggled on. It gives **+30%** movement speed and **+50%** attack damage, but **-20%** armor (all based on your base stats). Milk and other cures don't remove it.

## trnightmare:knight_resolve
Mad Knight's will to survive. When a hit leaves you at **30%** health or lower, Mad Knight heals you for **10%** of your max health and gives Knight's Resolve for 10 seconds: **+40%** critical hit chance and **+40%** attack speed (based on your base stats). It recharges after about 24 seconds.

## trnightmare:leonidas
**+50** max health, **+25** attack damage, **+0.1** movement speed and **+5** swim speed per level. A tamed mob with it walks to wherever its owner is looking, unless it was ordered to stay. Nothing in TR: Nightmares applies it in this version.

## trnightmare:liberation
A huge transformation, only obtainable through commands in this version (no skill applies it). Its bonuses are multiplied by (level + 1): **+20,000** max health, **+450** attack damage, **+300** armor, **+0.1** movement speed and **+0.5** knockback resistance at each step.

It also triples your max magicule and aura, refills both, and lets you fly. When it ends, you get the transformation hangover: {{link:minecraft:weakness}} II, {{link:tensura:fragility}} II and {{link:tensura:paralysis}} I for 10 minutes.

## trnightmare:magicule_reactor
Satanael's Magicule Reactor: **+{{cfg:config/nightmare/ability/skill/nightmare_ult.toml|Satanael.reactorAttack}}** attack damage, **+{{cfg:config/nightmare/ability/skill/nightmare_ult.toml|Satanael.reactorArmor}}** armor and **+{{cfg:config/nightmare/ability/skill/nightmare_ult.toml|Satanael.reactorKnockbackResist}}** knockback resistance per level, plus small boosts to attack, movement, swim and lava speed.

While Satanael is toggled on, the reactor keeps refilling your magicule (a share of your max, scaled by Satanael's output). Each pulse also has a chance to raise this effect's level. Above the output threshold, Satanael's output turns it into Tensura's Rampage instead.

At a high enough level it also acts as "Stampede": a death that would kill you is cancelled at the cost of some levels, on a cooldown.

## trnightmare:mammon_flare
Mammon's greed flame. It only does anything from level II up. From then on, every 0.75 seconds it deals **70** spiritual damage plus **2** corrosion damage per level, and wears down **every piece of equipment** by 15 durability per level. It also gives **-5%** movement speed and **-0.3** mining speed per level.

- **Level V+:** players within 7 blocks of whoever cast it take insanity damage.
- **Level X+:** fear damage too, and players it hits may turn Majin.

If the flame kills its target, the caster gains EP equal to the target's EP × the EP gain gamerule ÷ 2.25, added straight to their base magicule and aura. Milk and other cures don't remove it.

## trnightmare:metal_mode
Heavy Metal, the giant races' iron-body transformation. It gives **+10** attack damage, **+30** armor and full knockback immunity, and the skill adds Resistance on top. When it ends, your current magicule and aura are **halved** and you get {{link:minecraft:weakness}} II, {{link:tensura:fragility}} II and {{link:tensura:paralysis}} II for 10 minutes. You can only have one transformation active at a time.

## trnightmare:mind_projection
You are projecting your mind out of your body. Your ghostly form passes through blocks and creatures, can't be hurt and can fly, but it stays leashed to your host body. The projection ends if the host dies or can't be found. It is shown as a translucent tint on your character.

## trnightmare:monk_speed
Monk Speed Blitz: **+200%** attack speed per level (three times as fast at level I).

## trnightmare:mood
Mood Maker's Mood Booster: **+1** luck and **+10%** critical damage per level. Each cast adds a level (up to {{cfg:config/nightmare/ability/skill/nightmare_ult.toml|MoodMaker.moodBoosterMaxStacks}}), and it lasts 30 seconds. When Mood Maker saves you from death, the boost is used up.

## trnightmare:mystic_aura
Mystic Aura wraps your attacks in "mystic" energy. Each melee hit you land strikes a second time as mystic damage based on your attack damage. Once the skill is mastered, damage from your skills is also converted into mystic damage.

Mystic damage is halved against targets with an active Anti-Skill. The skill keeps it up while toggled on (30 seconds when cast unmastered). Breaker's and Abaddon's bonus physical damage doesn't stack with it.

## trnightmare:necrotic
Stops all healing over time. Every second it removes Regeneration, Instant Regeneration, Self Regeneration, {{link:trnightmare:slowheal}}, {{link:trnightmare:glorious_regen}} and {{link:trnightmare:divine_regeneration}}, and it shuts off your magicule regeneration while it lasts.

## trnightmare:nihilistic_vision
The distorted vision of anyone pulled into Belial's Nihilistic World or a Tempter's temptation world (about 62 seconds). It has no effect of its own beyond marking and showing that the creature is caught in that world, and it's removed when the session ends.

## trnightmare:overclock
Processor's Overclock: it strengthens Processor's thread bonuses (chant speed, and dodge invulnerability once mastered) by **{{cfg:config/nightmare/ability/skill/nightmare_unique.toml|Processor.clockBuffPerc}}%**, or by 5/3 of that with Heat Nullification or a boost clock. You need Heat Resistance or Heat Nullification toggled on to start it. It lasts 40 to 60 seconds depending on the mode.

When it ends, Processor **burns out**: it switches off and goes on cooldown ({{cfg:config/nightmare/ability/skill/nightmare_unique.toml|Processor.clockCooldown}} seconds, or a third less with Heat Nullification or the time clock).

## trnightmare:overheat
**-10** attack damage per level. Azathoth's Soul Nucleation inflicts it for 10 seconds, together with Black Burn, Chill and Anti-Skill.

## trnightmare:projection_glass
Projection Sorcery freezes the target in a frame of glass. It sets these to zero:
- walking, flying, swimming, lava and gliding speed
- attack damage and attack speed
- jump strength, block reach and follow range
- aura and magicule regeneration
- all dodge chances

Race abilities stop working, and skills are locked to the race limit. Any single hit of more than **25** damage **shatters** the glass: that hit deals **triple damage**, knocks the target back and ends the effect.

Projection Sorcery's Breaker mode applies it, and so can a random hit while the skill is toggled on. The catch: with the skill toggled on, taking damage can freeze **you** as well (less often with Pain Resistance or Pain Nullification).

## trnightmare:reflection
Love Locomotive's Reflective Love Shield (30 seconds). You glow, and you heal **25** health (+5 per extra level) every second. All damage to you is cancelled, and the attacker takes **1.5×** that damage back as thorns. Projectiles that hit you bounce back at 1.5× speed and now count as yours.

## trnightmare:rotting
Death God's rot. Every second it removes Instant Regeneration and Self Regeneration, and switches off the target's Ultraspeed Regeneration, Self-Regeneration and Infinite Regeneration skills. The mod also sets a "healing disabled" flag, but nothing reads that flag in this version, so other healing still works.

Death God's physical hits stack it (+1 level per hit, 10 seconds). Pressing the skill **detonates** it on every rotting enemy within 8 blocks, dealing **150** corrosion damage plus **150** spiritual damage per level. A corrosion dragon's Dragon Factor Haki also inflicts it, briefly locking regeneration.

## trnightmare:salvation
Azrael's mark. Each physical hit from Azrael has a **{{cfg:config/nightmare/ability/skill/nightmare_ult.toml|Azrael.retributionChance}}** chance ({{cfg:config/nightmare/ability/skill/nightmare_ult.toml|Azrael.retributionChanceMastered}} mastered) to add 2 levels, up to {{cfg:config/nightmare/ability/skill/nightmare_ult.toml|Azrael.salvationCap}} ({{cfg:config/nightmare/ability/skill/nightmare_ult.toml|Azrael.salvationCapMastered}} mastered). The mark lasts 30 seconds.

Azrael's Retribution and Purgatory attacks go after marked targets: Retribution deals {{cfg:config/nightmare/ability/skill/nightmare_ult.toml|Azrael.retributionDamagePerLevel}} damage per level, and each Purgatory slash removes some levels.

## trnightmare:simple
Soul Shrine's and Izanagi's "Simple" mode. Casting it fully heals you and refills your magicule and aura. While it lasts (30 seconds, 60 when mastered):
- direct attacks have a **50%** chance to miss you, unless they can't be dodged
- magic and spiritual damage is cut to **{{cfg:config/nightmare/ability/skill/nightmare_unique.toml|SoulShrine.simpleResistance}}%**

## trnightmare:slowheal
A slow, costly heal. Every second it heals **2%** of max health at level I, and less at higher levels (2% ÷ level, at least 0.1%). Players pay magicule for each heal, and the effect stops when they run out. From level II up it also restores a little spiritual health.

Enemies use it as a debuff: Leviathan's Envy Festival, Chrono Leech (15% on hit) and Muramasa's sever all inflict it, and it keeps draining the target's magicule. {{link:trnightmare:necrotic}} strips it.

## trnightmare:soul_protect
While it lasts, you can't take **spiritual damage** at all. Alternative's Soul Protect passive grants it in 30-second windows with a 10-second cooldown, and each window also cleanses mind effects.

## trnightmare:spatial_lock
Nothing in the mod applies or reads this effect in this version.

## trnightmare:stasis_fixed_state
Stasis' and Cadence's "Fixed State". When you cast it, your current magicule and aura are recorded, and while it lasts they can't drop below those amounts. In effect you can spend energy for free during the window.

## trnightmare:stolen_luck
Leviathan's and Cthulhu's Crushing Jealousy mark for a target that has **less** energy than the attacker. It lowers automatic melee and projectile dodge chance by **50%** per level, and lowers magic interference resistance the same way.

## trnightmare:survival
You take **half damage** from everything, and spiritual damage is halved again (a quarter in total).

## trnightmare:temptation_magic_jamming
Azazel's jamming inside a temptation world. It marks creatures caught in an Azazel temptation session, is refreshed while they stay in that inner world, and is removed when the session ends. Nothing else in the mod reads it in this version.

## trnightmare:temptation_marked
A Tempter's mark (about 62 seconds). Tempter and Azazel mark charmed or frightened creatures around them. The next temptation cast pulls every marked creature within 16 blocks into the caster's inner world. The mark is removed when the session ends or the creature is sent back.

## trnightmare:time_stop
Frozen in stopped time. Every tick your motion is set to zero and mobs lose their pathfinding. While it lasts you can't use or interact with skills, attack, or right-click blocks and items. Time Stop pulses from skills also freeze projectiles in mid-air.

## trnightmare:true_dragon_body
Pseudo Dragon Body's true-dragon form. While it's active, your base max health becomes **{{cfg:config/nightmare/ability/skill/nightmare_ult.toml|TrueDragon.dragonBodyHp}}**, attack **{{cfg:config/nightmare/ability/skill/nightmare_ult.toml|TrueDragon.dragonBodyAttack}}**, armor **{{cfg:config/nightmare/ability/skill/nightmare_ult.toml|TrueDragon.dragonBodyArmor}}** and max spiritual health **{{cfg:config/nightmare/ability/skill/nightmare_ult.toml|TrueDragon.dragonBodyShp}}**. You're fully healed and your max EP is **quadrupled**.

It drains **{{cfg:config/nightmare/ability/skill/nightmare_extra.toml|PseudoDragonBody.mpDrainPerTick}}** magicule every tick. When your magicule runs out or you turn the skill off, your old stats come back. It can't be used together with Tensura's Dragon Mode.

## trnightmare:ultimate_shield
**+25%** attack damage and **+5** armor at level I, plus **+15%** and **+3** for each extra level. The Ultimate Shield skill gives level II (**+40%** and **+8**) for 60 seconds (120 when mastered), and refills your magicule and aura.

## trnightmare:unlimited_void
Unlimited Void traps you in an endless void. Movement, attack damage, attack speed, luck, reach, swim speed and jump strength all drop to zero, and you're pulled out of the air. You can't use or interact with skills.

Every half second it drains **500** magicule per level from players, or EP from mobs. Milk and other cures don't remove it.

## trnightmare:white_flame
Freezing Flame's white coating (15 seconds, level II when mastered). While coated you move **20%** slower, attack **15%** slower and have **10%** less armor. In return, every half second it heals almost all of your missing health (10% less per extra level), and at level II it heals spiritual health too.

Players pay a lot of magicule for that healing (80 per point of current health), and the effect stops when they run out. Level II also stops you sprinting. The skill adds flat attack damage while you're coated, and your hits inflict {{link:trnightmare:freezing_burn}}.

## trnightmare:witches_curse
A curse counter from **Witch's Envy**. It lasts 5 hours, and its level is the number of stacks.
- **Gaining stacks:** if someone kills a Witch's Envy user (skill in a slot), the killer gets curse stacks. Once the skill is mastered, anyone who hits its user also has a chance to gain a stack.
- **Using them:** the user's **Witch's Wrath** consumes every stack on the targeted creature, dealing corrosion damage plus the same amount of spiritual damage for each stack.

It has no effect of its own besides counting stacks.

## trnightmare:zone
Soul Shrine's and Izanagi's "Zone", entered through Flash strikes. While the skill is toggled on, each physical hit has a small chance (**{{cfg:config/nightmare/ability/skill/nightmare_unique.toml|SoulShrine.flashChance}}%**, or {{cfg:config/nightmare/ability/skill/nightmare_unique.toml|SoulShrine.flashChanceMastered}}% mastered) to become a **Flash**. A Flash deals **{{cfg:config/nightmare/ability/skill/nightmare_unique.toml|SoulShrine.flashMultiplier}}×** damage and puts you in the Zone for 50 seconds.

While you're in the Zone, Flash chance goes up by {{cfg:config/nightmare/ability/skill/nightmare_unique.toml|SoulShrine.flashZoneChance}}%. At levels II to IV the Zone gives **+120%** base attack damage and attack speed; from level V up only **+20%**, because of how the formula rounds.


<!-- kind: -->

## trnightmare:domicile
The template for the personal pocket worlds made by the {{link:skill/trnightmare:domicile}} skill. Every player who uses it gets two of their own: a **Homestead** (a house) and a **Shop**. They are built from a saved structure the first time you enter, then stay as you leave them.

**Getting in:** look at any door or trapdoor within 5 blocks and use the skill. The door turns into a {{link:trnightmare:domicile_door}} (or {{link:trnightmare:domicile_trapdoor}}) linked to you, and you step inside: Homestead mode for the house, Shopkeeper mode for the shop. Linking a new door reverts your old one to a plain oak door. After that, **anyone** who walks through the open linked door is taken to your domicile. Use the skill again inside, or open the door inside, to go back out through your linked door.

**Inside:**

- Nothing can take damage.
- Only you, your allies and your subordinates can place or break blocks, and only you can open chests, barrels, furnaces, hoppers and other containers. The linked doors can't be broken.
- The chunk you stand in stays loaded while the skill is active.
- In the shop, Shopkeeper mode summons an invulnerable Domicile Shopkeeper that sells what you stock in its chests and barrel (Shift + use on it to remove it). If you have {{link:skill/trnightmare:the_warden}}, it gains mastery for every visitor in your shop and every door you convert.

**Commands:** `/domicile` (Homestead) and `/domicilestore` (Shop) let the owner kick a player, or everyone not on their whitelist, back to world spawn. The whitelist only matters for that kick: the blacklist, lock and safety settings are saved, but nothing reads them in this version, so they don't keep anyone out. Operators can rebuild someone's Homestead or Shop with `/resetdomicile <players> base|shop`.

## trnightmare:inner_world
The template for each player's own Inner World, a flat, dark world where time stands still at noon. Beds and respawn anchors don't work.

**Getting in:**

- The {{link:skill/trnightmare:inner_world}} skill takes you in if you have at least **90%** of your health and magicule. A hollow "echo" of you (your health, no gear, almost no EP) stays behind where you stood and keeps its chunk loaded. Use the skill again to leave and rejoin the echo. If the echo is killed while you're inside, you're thrown back out to where it fell.
- Sleeping in a bed while holding a completed {{link:trnightmare:ancient_history_book}} pulls you into your Inner World to meet Veldanava.
- Other skills can visit someone else's Inner World as a guest, such as {{link:skill/trnightmare:conceptual_existence}}'s and {{link:skill/trnightmare:pazuzu}}'s Enter Mind (Pazuzu only reaches players you have a deal with).
- Several skills use it as a battlefield or prison, such as Abaddon, Samael's Death World and Temptation.

True Dragons you've bonded with (Veldora, Velzard, Velgrynd, Velgaia) live in your Inner World and add extra modes to the skill.

## trnightmare:imaginary_space
The template for each player's own Imaginary Space, a flat, dark world where time stands still at noon. Beds and respawn anchors don't work.

**Getting in:** the Imaginary Space mode of {{link:skill/trnightmare:azathoth}} (and of {{link:skill/trnightmare:nodens}}, which borrows it). Pressing the skill opens your spatial storage; **Shift + press** enters and drags every living thing within **6 blocks** in with you.

**Inside:**

- Look at a creature within 8 blocks and press to throw it back out.
- Shift + press to leave, taking everything within 6 blocks of you along.
- Mobs you leave behind are saved and put back the next time you enter, so it doubles as a prison.
- Azathoth's Imaginary Blade can cut enemies straight into your Imaginary Space, and a {{link:skill/trnightmare:divine_wisdom_core}} can follow its host in.

<!-- kind: items -->

## class:com.github.hvnbael.trnightmare.main.weapon.GenesisSwordItem, class:com.github.hvnbael.trnightmare.main.weapon.ArkSwordItem
One of the divine-tier **Genesis** swords. It has no ability of its own: it's a stat weapon with long reach, a strong sweep and a 20% critical chance (see the stats box), and 10,000 durability.

{{auto}}

## trnightmare:memory
**Memory**, a Genesis sword with the same stats as the others. {{link:skill/trnightmare:astral_light}} forges it (its fifth mode) if you have a named Amnesiac ego. Only one Memory exists per world: copies that don't match the world's forged Memory are deleted from inventories.

{{auto}}

## trnightmare:gilgamesh_ea
**Ea**, Gilgamesh's Genesis sword, summoned by the Gilgamesh skills. It has the Genesis sword stats, plus:

- **Enuma Elish:** use it (right-click) to fire a beam that reaches 96 blocks and deals **2,000** damage. It costs **1,500,000** magicule and **1,500,000** aura and has a 2-minute cooldown.
- Its hits do nothing to a target with more than **twice your EP**.

{{auto}}

## trnightmare:gilgamesh_marduk_axe
**Marduk**, Gilgamesh's Genesis axe, summoned by the Gilgamesh skills. It's a divine-tier axe with no ability of its own (see the stats box).

{{auto}}

## trnightmare:mystic_code_book
A spellbook summoned by the Gilgamesh skills. Held in either hand it gives **+5** chant speed.

{{auto}}

## trnightmare:divine_axe_rhitta
Escanor's divine axe. Holding it in either hand powers up {{link:skill/trnightmare:sunshine}}: Sunshine's bonus to physical, light, fire and heat damage rises from **{{cfg:config/nightmare/ability/skill/nightmare_unique.toml|Sunshine.noRhittaDamagePercentage}}%** to **{{cfg:config/nightmare/ability/skill/nightmare_unique.toml|Sunshine.hasRhittaDamagePercentage}}%**, and you keep Fire Resistance while Sunshine is on. The axe never breaks, can't be repaired, doesn't burn and can't be put in shulker boxes or bundles.

{{auto}}

## trnightmare:lostvayne_sword, trnightmare:zeldris_sword, trnightmare:galand_halberd, trnightmare:dragon_seal
A treasure weapon with no ability of its own (see the stats box). It never breaks, can't be repaired, doesn't burn and can't be put in shulker boxes or bundles.

{{auto}}

## trnightmare:excalibur, trnightmare:caliburn, trnightmare:the_asura
A divine-tier sword with no ability of its own: a stat weapon (see the stats box) with 10,000 durability.

{{auto}}

## trnightmare:the_world
A divine-tier sword (see the stats box). While a player holds it in either hand, their attacks go straight through {{link:skill/tensura:infinity_prison}}'s protection. {{link:skill/trnightmare:nodens}} can upgrade it into {{link:trnightmare:nodens_the_world}}.

{{auto}}

## trnightmare:terrablade
Despite the name, the Terrablade is a **shovel** (Sacred Treasure tier, 10,000 durability) with no special ability.

{{auto}}

## trnightmare:ending_sealed_sword
The sealed form of the {{link:skill/trnightmare:ending}} skill's sword; the skill creates it. If you have Ending, every hit gives the target {{link:effect/trnightmare:core_damage}} II for 5 seconds. If you don't, trying to use it destroys it. Repair it with Daemon Essence.

{{auto}}

## trnightmare:ending_unsealed_sword
The unsealed form of the {{link:skill/trnightmare:ending}} skill's sword. If you have Ending, every hit gives the target {{link:effect/trnightmare:ending}} for 5 seconds, and holding it in your main hand fully masters Ending (mastery 1,500). If you don't have Ending, trying to use it destroys it. Repair it with Daemon Essence.

{{auto}}

## trnightmare:evil_attribute_stick
A testing stick that raises **every** attribute in the game (vanilla, ManasCore and Tensura) while held: **+0.08** flat, **+3%** of base and **+3%** of total in the main hand, or +0.06, +2.5% and +2.5% in the off hand. (It also lists bonuses for armor slots, but a stick can't be worn.)

{{auto}}

## trnightmare:life_essence
Life energy gathered from crops: bone-mealing a crop that's still growing has a **50%** chance to drop one, and harvesting a fully grown crop a **10%** chance. It can also be a raid reward. Fairy races have to eat it to evolve, and some skills count how many you've eaten.

{{auto}}

## trnightmare:ruined_history_book
A history book found in Ancient City chests. Its pages are too damaged to read; craft it with essence to restore it into the {{link:trnightmare:ancient_history_book}}.

{{auto}}

## trnightmare:skill_crystal
A skill sealed in crystal. {{link:skill/trnightmare:pazuzu}} can crystallize one of its user's skills (the user forgets it). Whoever eats the crystal learns that skill without paying its learning cost. An empty crystal does nothing.

{{auto}}

<!-- kind: mobs -->

## trnightmare:sentient_boss_gii_crimson
**Primordial Rouge**, a demonic sentient boss: it attacks players and mobs that aren't majin (monster races).

**Spawning:** in Hell biomes, each time a Lesser, Greater or Arch Daemon spawns there's a 1 in {{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.crimsonRarity}} chance it's replaced by this boss.

**Stats:** 850 health, 5,500 spiritual health, 40 armor, 15 attack damage, 1,500,000 to 6,666,666 EP.

**Rewards:** killing it raises your max magicule and aura by about **10% of 6,666,666** (scaled by your alignment and the EP gain gamerule); it drops {{link:tensura:daemon_essence}} (1 to 3) and a 50% chance of {{link:trnightmare:elder_essence}}, and a Magic Tome with a random elemental spell; it can teach {{link:skill/tensura:pride}} (the chance is set by `otherworlderSkillDrop`, which is **0** in this pack, so it doesn't happen here).

It takes at most **500** damage from any one hit.

Sentient bosses only appear through natural spawns, never inside pillager outposts, never within 500 blocks of another of the same boss, and never within 500 blocks of a spot where any sentient boss appeared in the last 3 minutes. On the surface (under open sky or above sea level) they're 4 times as likely as the rate below, underground 4 times less likely.

{{auto}}

## trnightmare:sentient_boss_ancient_daemon
An **Ancient Daemon**, a demonic sentient boss: it attacks players and mobs that aren't majin.

**Spawning:** in Hell biomes, each time a Lesser Daemon spawns there's a 1 in {{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.ancientDaemonRarity}} chance it's replaced by this boss.

**Stats:** 650 health, 2,450 spiritual health, 10 armor, 10 attack damage, 400,000 to 850,000 EP.

**Rewards:** killing it raises your max magicule and aura by about **10% of 850,000** (scaled by your alignment and the EP gain gamerule); it drops {{link:tensura:daemon_essence}} (1 to 3) and a Magic Tome with a random elemental spell.

It takes at most **500** damage from any one hit.

Sentient bosses only appear through natural spawns, never inside pillager outposts, never within 500 blocks of another of the same boss, and never within 500 blocks of a spot where any sentient boss appeared in the last 3 minutes. On the surface (under open sky or above sea level) they're 4 times as likely as the rate below, underground 4 times less likely.

{{auto}}

## trnightmare:sentient_boss_agera
**Agera**, a sentient boss swordsman.

**Spawning:** in Hell biomes, each time a Lesser, Greater or Arch Daemon spawns there's a 1 in {{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.ageraRarity}} chance it's replaced by this boss.

**Stats:** 5,000 health, 8,000 spiritual health, 0 armor, 55 attack damage, 2,100,000 EP.

**Rewards:** it drops {{link:tensura:daemon_essence}} (1 to 3) and a 5% chance of {{link:trnightmare:elder_essence}}.

Sentient bosses only appear through natural spawns, never inside pillager outposts, never within 500 blocks of another of the same boss, and never within 500 blocks of a spot where any sentient boss appeared in the last 3 minutes. On the surface (under open sky or above sea level) they're 4 times as likely as the rate below, underground 4 times less likely.

{{auto}}

## trnightmare:sentient_boss_primordial_daemon
A **Primordial Daemon**, a demonic sentient boss: it attacks players and mobs that aren't majin.

**Spawning:** it isn't in the natural spawn rules in this version.

**Stats:** 850 health, 5,500 spiritual health, 40 armor, 15 attack damage, 1,500,000 to 6,666,666 EP.

**Rewards:** killing it raises your max magicule and aura by about **10% of 6,666,666** (scaled by your alignment and the EP gain gamerule); it drops {{link:tensura:daemon_essence}} (1 to 3) and a 50% chance of {{link:trnightmare:elder_essence}}, and a Magic Tome with a random elemental spell.

It takes at most **500** damage from any one hit.

{{auto}}

## trnightmare:sentient_boss_milim_wrath
**Milim Nava, the Dragon Princess**, a sentient boss.

**Spawning:** in otherworlder biomes, each time a human-like mob spawns there's a 1 in {{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.milimWrathRarity}} chance it's replaced by this boss.

**Stats:** 10,000 health, 18,000 spiritual health, 15 armor, 75 attack damage, 7,000,000 to 7,600,000 EP.

**Rewards:** killing it raises your max magicule and aura by about **10% of 7,000,000** (scaled by your alignment and the EP gain gamerule); it drops a 50% chance of {{link:tensura:dragon_essence}} (1 to 3) and a 45% chance of {{link:trnightmare:elder_essence}}; it can teach {{link:skill/tensura:wrath}} (the chance is set by `otherworlderSkillDrop`, which is **0** in this pack, so it doesn't happen here).

It takes at most **500** damage from any one hit.

Sentient bosses only appear through natural spawns, never inside pillager outposts, never within 500 blocks of another of the same boss, and never within 500 blocks of a spot where any sentient boss appeared in the last 3 minutes. On the surface (under open sky or above sea level) they're 4 times as likely as the rate below, underground 4 times less likely.

{{auto}}

## trnightmare:sentient_boss_yuuki_desire
**Yuuki, the Grandmaster**, a sentient boss.

**Spawning:** in otherworlder biomes, each time a human-like mob spawns there's a 1 in {{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.yuukiRarity}} chance it's replaced by this boss.

**Stats:** 4,000 health, 6,000 spiritual health, 0 armor, 45 attack damage, 3,500,000 to 4,500,000 EP.

**Rewards:** killing it raises your max magicule and aura by about **10% of 2,100,000** (scaled by your alignment and the EP gain gamerule); it can teach Creator (the chance is set by `otherworlderSkillDrop`, which is **0** in this pack, so it doesn't happen here).

Sentient bosses only appear through natural spawns, never inside pillager outposts, never within 500 blocks of another of the same boss, and never within 500 blocks of a spot where any sentient boss appeared in the last 3 minutes. On the surface (under open sky or above sea level) they're 4 times as likely as the rate below, underground 4 times less likely.

{{auto}}

## trnightmare:sentient_boss_mariabell_rosso
**Mariabell Rosso**, a sentient boss.

**Spawning:** in otherworlder biomes, each time a human-like mob spawns there's a 1 in {{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.mariabellRarity}} chance it's replaced by this boss.

**Stats:** 500 health, 1,500 spiritual health, 0 armor, 12 attack damage, 200,000 to 500,000 EP.

**Rewards:** it can teach {{link:skill/tensura:greed}} (the chance is set by `otherworlderSkillDrop`, which is **0** in this pack, so it doesn't happen here).

Sentient bosses only appear through natural spawns, never inside pillager outposts, never within 500 blocks of another of the same boss, and never within 500 blocks of a spot where any sentient boss appeared in the last 3 minutes. On the surface (under open sky or above sea level) they're 4 times as likely as the rate below, underground 4 times less likely.

{{auto}}

## trnightmare:sentient_boss_glenda
**Glenda**, a sentient boss.

**Spawning:** in otherworlder biomes, each time a human-like mob spawns there's a 1 in {{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.glendaAriosRarity}} chance it's replaced by this boss. (Glenda or Arios, 50/50)

**Stats:** 500 health, 650 spiritual health, 0 armor, 14 attack damage, 150,000 EP.

**Rewards:** it can teach Sniper (the chance is set by `otherworlderSkillDrop`, which is **0** in this pack, so it doesn't happen here).

Sentient bosses only appear through natural spawns, never inside pillager outposts, never within 500 blocks of another of the same boss, and never within 500 blocks of a spot where any sentient boss appeared in the last 3 minutes. On the surface (under open sky or above sea level) they're 4 times as likely as the rate below, underground 4 times less likely.

{{auto}}

## trnightmare:sentient_boss_arios
**Arios**, a sentient boss. Killing Arios while you have {{link:skill/trnightmare:abaddon}} teaches you the Murderer unique skill.

**Spawning:** in otherworlder biomes, each time a human-like mob spawns there's a 1 in {{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.glendaAriosRarity}} chance it's replaced by this boss. (Glenda or Arios, 50/50)

**Stats:** 900 health, 1,400 spiritual health, 0 armor, 18 attack damage, 450,000 EP.

Sentient bosses only appear through natural spawns, never inside pillager outposts, never within 500 blocks of another of the same boss, and never within 500 blocks of a spot where any sentient boss appeared in the last 3 minutes. On the surface (under open sky or above sea level) they're 4 times as likely as the rate below, underground 4 times less likely.

{{auto}}

## trnightmare:sentient_boss_lucius
**Lucius**, a sentient boss.

**Spawning:** in otherworlder biomes, each time a human-like mob spawns there's a 1 in {{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.luciusRaymondRarity}} chance it's replaced by this boss. (Lucius or Raymond, 50/50)

**Stats:** 300 health, 400 spiritual health, 0 armor, 8 attack damage, 40,000 EP.

**Rewards:** it can teach Fusionist (the chance is set by `otherworlderSkillDrop`, which is **0** in this pack, so it doesn't happen here).

Sentient bosses only appear through natural spawns, never inside pillager outposts, never within 500 blocks of another of the same boss, and never within 500 blocks of a spot where any sentient boss appeared in the last 3 minutes. On the surface (under open sky or above sea level) they're 4 times as likely as the rate below, underground 4 times less likely.

{{auto}}

## trnightmare:sentient_boss_raymond
**Raymond**, a sentient boss.

**Spawning:** in otherworlder biomes, each time a human-like mob spawns there's a 1 in {{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.luciusRaymondRarity}} chance it's replaced by this boss. (Lucius or Raymond, 50/50)

**Stats:** 300 health, 400 spiritual health, 0 armor, 10 attack damage, 40,000 EP.

**Rewards:** it can teach Fighter (the chance is set by `otherworlderSkillDrop`, which is **0** in this pack, so it doesn't happen here).

Sentient bosses only appear through natural spawns, never inside pillager outposts, never within 500 blocks of another of the same boss, and never within 500 blocks of a spot where any sentient boss appeared in the last 3 minutes. On the surface (under open sky or above sea level) they're 4 times as likely as the rate below, underground 4 times less likely.

{{auto}}

## trnightmare:sentient_boss_kokuyou
**Kokuyou**, a sentient boss.

**Spawning:** in otherworlder biomes, any natural spawn there has a 1 in {{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.kokuyouExtraChance}} chance to bring Kokuyou along.

**Stats:** 2,800 health, 5,000 spiritual health, 55 armor, 38 attack damage, 900,000 to 1,500,000 EP.

Sentient bosses only appear through natural spawns, never inside pillager outposts, never within 500 blocks of another of the same boss, and never within 500 blocks of a spot where any sentient boss appeared in the last 3 minutes. On the surface (under open sky or above sea level) they're 4 times as likely as the rate below, underground 4 times less likely.

{{auto}}

## trnightmare:sentient_boss_frey
**Frey**, a flying sentient boss.

**Spawning:** anywhere, each time a Phantom spawns there's a 1 in {{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.freyPhantomRarity}} chance it's replaced by Frey.

**Stats:** 3,500 health, 5,000 spiritual health, 45 armor, 40 attack damage, 1,948,734 to 2,000,000 EP.

**Rewards:** it can teach Reflector (the chance is set by `otherworlderSkillDrop`, which is **0** in this pack, so it doesn't happen here).

Sentient bosses only appear through natural spawns, never inside pillager outposts, never within 500 blocks of another of the same boss, and never within 500 blocks of a spot where any sentient boss appeared in the last 3 minutes. On the surface (under open sky or above sea level) they're 4 times as likely as the rate below, underground 4 times less likely.

{{auto}}

## trnightmare:sentient_boss_veldora
**Veldora**, the Storm Dragon, a sentient boss.

**Spawning:** in mountains or villages, each time a Leech Lizard spawns there's a 1 in {{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.veldoraRarity}} chance it's replaced by Veldora.

**Stats:** 10,000 health, 20,000 spiritual health, 60 armor, 90 attack damage, 30,000,000 to 40,000,000 EP.

**Rewards:** killing it raises your max magicule and aura by about **10% of 30,000,000** (scaled by your alignment and the EP gain gamerule); it drops a 50% chance of {{link:tensura:dragon_essence}} (3 to 13) and an 80% chance of {{link:trnightmare:elder_essence}}; it can teach Investigator (the chance is set by `otherworlderSkillDrop`, which is **0** in this pack, so it doesn't happen here).

It takes at most **500** damage from any one hit.

Sentient bosses only appear through natural spawns, never inside pillager outposts, never within 500 blocks of another of the same boss, and never within 500 blocks of a spot where any sentient boss appeared in the last 3 minutes. On the surface (under open sky or above sea level) they're 4 times as likely as the rate below, underground 4 times less likely.

{{auto}}

## trnightmare:sentient_boss_velzard
**Velzard**, the Ice Dragon, a sentient boss.

**Spawning:** in snowy or icy biomes or villages, each time a Leech Lizard spawns there's a 1 in {{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.velzardRarity}} chance it's replaced by Velzard.

**Stats:** 12,000 health, 25,000 spiritual health, 65 armor, 95 attack damage, 30,000,000 to 60,000,000 EP.

**Rewards:** killing it raises your max magicule and aura by about **10% of 30,000,000** (scaled by your alignment and the EP gain gamerule); it drops a 50% chance of {{link:tensura:dragon_essence}} (3 to 13) and an 80% chance of {{link:trnightmare:elder_essence}}; it can teach Stasis and {{link:skill/tensura:envy}} (the chance is set by `otherworlderSkillDrop`, which is **0** in this pack, so it doesn't happen here).

It takes at most **500** damage from any one hit.

Sentient bosses only appear through natural spawns, never inside pillager outposts, never within 500 blocks of another of the same boss, and never within 500 blocks of a spot where any sentient boss appeared in the last 3 minutes. On the surface (under open sky or above sea level) they're 4 times as likely as the rate below, underground 4 times less likely.

{{auto}}

## trnightmare:sentient_boss_velgrynd
**Velgrynd**, the Scorch Dragon, a sentient boss.

**Spawning:** in savannas, badlands or villages, each time a Leech Lizard spawns there's a 1 in {{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.velgryndRarity}} chance it's replaced by Velgrynd.

**Stats:** 12,000 health, 25,000 spiritual health, 65 armor, 100 attack damage, 30,000,000 to 60,000,000 EP.

**Rewards:** killing it raises your max magicule and aura by about **10% of 30,000,000** (scaled by your alignment and the EP gain gamerule); it drops a 50% chance of {{link:tensura:dragon_essence}} (3 to 13) and an 80% chance of {{link:trnightmare:elder_essence}}; it can teach Endorse (the chance is set by `otherworlderSkillDrop`, which is **0** in this pack, so it doesn't happen here).

It takes at most **500** damage from any one hit.

Sentient bosses only appear through natural spawns, never inside pillager outposts, never within 500 blocks of another of the same boss, and never within 500 blocks of a spot where any sentient boss appeared in the last 3 minutes. On the surface (under open sky or above sea level) they're 4 times as likely as the rate below, underground 4 times less likely.

{{auto}}

## trnightmare:sentient_boss_masayuuki
**Masayuki, the Lightspeed Chosen Hero**, a sentient boss wielding a Hihi'irokane long sword. Killing him while you have the Gift or Astraea skill teaches you Hero Banner Blessing.

**Spawning:** he isn't in the natural spawn rules in this version.

**Stats:** 800 health, 4,500 spiritual health, 80 armor, 15 attack damage, 400,000 EP.

**Rewards:** killing it raises your max magicule and aura by about **10% of 10,000,000** (scaled by your alignment and the EP gain gamerule); it drops a 50% chance of {{link:trnightmare:holy_essence}} (2 to 10); it can teach Absolute Severance (the chance is set by `otherworlderSkillDrop`, which is **0** in this pack, so it doesn't happen here).

It takes at most **500** damage from any one hit.

{{auto}}

## trnightmare:sentient_boss_veldanava
**Veldanava, the Star Dragon.** He doesn't spawn in the world: sleeping in a bed with a completed {{link:trnightmare:ancient_history_book}} takes you into your Inner World to meet him. There he is invulnerable and doesn't move.

**Stats:** 99,999 health, 99,999 spiritual health, 20 armor, 99 attack damage, 90,000,000 to 99,999,999 EP.

{{auto}}

## trnightmare:sentient_boss_vert, trnightmare:sentient_boss_bleu, trnightmare:sentient_boss_jaune, trnightmare:sentient_boss_blanc, trnightmare:sentient_boss_violet, trnightmare:sentient_boss_noir, trnightmare:sentient_boss_nior
One of the six **Primordial** demons (Vert, Bleu, Jaune, Blanc, Violet and Noir), demonic sentient bosses that attack players and mobs that aren't majin.

**Spawning:** in Hell biomes, each time a Lesser, Greater or Arch Daemon spawns there's a 1 in {{cfg:serverconfig/nightmare/mechanic/spawns/nightmare_bosses.toml|boss_spawn_rates.primordialDaemonAspectRarity}} chance it's replaced by one of the six, picked at random.

**Stats:** 850 health, 5,500 spiritual health, 40 armor, 15 attack damage, 1,500,000 to 6,666,666 EP.

Sentient bosses only appear through natural spawns, never inside pillager outposts, never within 500 blocks of another of the same boss, and never within 500 blocks of a spot where any sentient boss appeared in the last 3 minutes. On the surface (under open sky or above sea level) they're 4 times as likely as the rate below, underground 4 times less likely.

{{auto}}

## trnightmare:dragon_clone_veldora, trnightmare:dragon_clone_velzard, trnightmare:dragon_clone_velgrynd
A True Dragon's body in human form, for a True Dragon living in your {{link:dimension/trnightmare:inner_world}}. Once your bond with the dragon is strong enough, the {{link:skill/trnightmare:inner_world}} skill can let it inhabit a clone that fights beside you.

{{auto}}

<!-- kind: blocks -->

## trnightmare:cadence_accel_glass
The marker for **Block Acceleration**, a mode of {{link:skill/trnightmare:cadence}} and {{link:skill/trnightmare:gabriel}}. Using the mode on a block places this glass and speeds up time in an 8×8 area around it (from 2 blocks below to 3 above): every tick, plants and other randomly-ticking blocks get **{{cfg:config/nightmare/ability/skill/nightmare_unique.toml|cadence.blockAccelBonusRandomTicks}}** extra growth ticks, and furnaces and other machines run {{cfg:config/nightmare/ability/skill/nightmare_unique.toml|cadence.blockAccelBonusRandomTicks}} extra times, so crops grow and smelting finishes about 20 times faster. The zone lasts until the glass is broken (it breaks very easily) or you sneak and use the mode to clear your zones. Cooldown: {{cfg:config/nightmare/ability/skill/nightmare_unique.toml|cadence.blockAccelCooldownSeconds}} s with Cadence, {{cfg:config/nightmare/ability/skill/nightmare_ult.toml|Gabriel.blockAccelCooldownSeconds}} s with Gabriel.

{{auto}}

## trnightmare:domicile_door, trnightmare:domicile_trapdoor
A door or trapdoor linked to someone's {{link:dimension/trnightmare:domicile}}, made when they use the {{link:skill/trnightmare:domicile}} skill on an ordinary door or trapdoor. **Walk through it while it's open** to enter the owner's Homestead or Shop (anyone can, with a 2-second cooldown between trips). Opening the door from inside takes you back out through it. Linking a new door turns the old one back into a plain oak door, and the linked doors can't be broken from inside.

{{auto}}

## trnightmare:gabriel_snow_crystal
Unbreakable ice crystal made by {{link:skill/trnightmare:cessation}} and {{link:skill/trnightmare:gabriel}}. While you hold their ice abilities it forms either a hollow **shell** around you that moves with you, or an **ice wall** in front of you (5 wide, {{cfg:config/nightmare/ability/skill/nightmare_unique.toml|cessation.iceWallHeight}} high and {{cfg:config/nightmare/ability/skill/nightmare_unique.toml|cessation.iceWallThickness}} thick with Cessation). It only fills empty space and disappears as soon as you let go.

{{auto}}
