# Tensura: Reincarnated: what things do

Written from the mod's code (Tensura: Reincarnated 2.0.1.3). Each `## id` section becomes the "What it does" part of that entry's page.
"Per level" means the value grows with the effect level: Minecraft multiplies an effect's attribute bonus by its level.

<!-- kind: effects -->

## tensura:ally_boost
The hero's blessing, from Chosen One, True Hero, Villain and similar skills. It gives **+{{cfg:config/tensura/ability/skill/unique_config.toml|ChosenOne.allyCritChance}}%** critical hit chance per level. From level II up it also gives **+{{cfg:config/tensura/ability/skill/unique_config.toml|ChosenOne.meleeDodge}}%** melee and **+{{cfg:config/tensura/ability/skill/unique_config.toml|ChosenOne.projectileDodge}}%** projectile dodge chance per level above I.

When something you kill while boosted can be mind-controlled (not undead, not an ally, not a summon), it doesn't die. It gets back up at half health and half spiritual health as a **subordinate of whoever gave you the boost**.

## tensura:anti_magic
You can't cast magic while it lasts. Summoning and aspectual spells fail, daemons can't cast, and Escape Magic won't auto-trigger. A mastered spell still works if you have Law Degradation. Anti-Magic Area and Holy Field inflict it on everything inside.

## tensura:anti_shock
Physical hits can't deal you more than **{{cfg:config/tensura/ability/magic/aspectual_config.toml|AntiShockArea.antiShockDamage}}** damage each. Anti-Shock Area (aspectual magic) gives it to everything inside the area.

## tensura:anti_skill
Seals your skills. While it lasts, skills count as blocked by a status effect and won't activate, and ridden mounts can't use their mount abilities. Many skills inflict it, including Anti-Skill's touch, prisons (Uriel, Yog-Sothoth), Merlin, Raziel's ink and Elyon. Some ultimates and Manas are immune.

## tensura:auditory_sense
Hearing boost: **+5** presence-sense radius. Ultrasonic Waves (sense mode) and Exploiter grant it.

## tensura:aura_sword
Aura Sword (battlewill). Each physical hit you make adds your **weapon damage** again as a bonus (×{{cfg:config/tensura/ability/battlewill_config.toml|AuraSword.attackMultiplier}}), and your weapon hits count as **battlewill damage**, which some ki and chi releases need. It lasts 60 seconds from a press, or stays up while the art is toggled on.

## tensura:bats_mode
The vampire's bat form. You shrink to half size, gain **+1** presence concealment and can fly, but your armor and armor toughness drop to **zero**. While you're a swarm of bats you can't interact with things, and your skills are limited to what your race limit allows. It ends if something stops you jumping, or, with the Hardcore Race gamerule, if a vampire is caught in sunlight.

## tensura:beast_transformation
Beast Transformation (level I) and Royal Beast (level II). Per level: **+15** attack damage, **+10** armor and **+0.04** movement speed. It also **doubles** your max magicule and aura (not per level) and refills both when it starts. Royal Beast (level II) also lets you fly.

When it ends, your current magicule and aura are **halved**, and you get the transformation hangover: {{link:minecraft:weakness}} II, {{link:tensura:fragility}} II and {{link:tensura:paralysis}} I for 10 minutes. Only one transformation can be active at a time.

## tensura:black_burn
Black flames. Every second they deal **{{cfg:config/tensura/ability/skill/extra_config.toml|BlackFlame.blackBurnDamage}}** flame damage per level. This damage can't be dodged and is split between physical and elemental. At **level II or higher**, the burning creature **can't heal**, unless it has Instant Regeneration II or higher.

Black Flame's touch, black fire blocks, Hell Flare, black-flame breath and many addon skills inflict it.

## tensura:burden
Extra gravity. Per level: **+50%** gravity (you fall faster and jump lower), **+50%** fall damage and **+0.1** knockback resistance. Flying mobs are pulled out of the sky unless they have full gravity control.

Gravity Attack Nullification, Abnormal Condition Resistance and Abnormal Condition Nullification make you immune. Reverser turns it into Slow Falling. Earth Jail, Magma Surge, the Burden/gravity spells, Oppressor and Earth Transform all inflict it.

## tensura:chill
Numbing cold. Per level: **-20%** movement speed, **-20%** attack speed and **-0.2** mining speed. It also keeps you frozen, like standing in powder snow: the freeze gets stronger at higher levels.

Physical Barrier, Magic Barrier and Diamond Path remove it. Cold Resistance, Cold Nullification and the Thermal Fluctuation resistances make you immune. Ice Lance deals bonus damage to chilled targets. Potions of Chill exist (45 or 90 seconds, or Chill II).

## tensura:confusion
**-15%** movement speed per level. Every second it also gives vanilla Nausea and Darkness at the same level. Confusion magic inflicts it on everything within 10 blocks (level {{cfg:config/tensura/ability/magic/aspectual_config.toml|Confusion.confusionLevel}}+, up to {{cfg:config/tensura/ability/magic/aspectual_config.toml|Confusion.confusionMaxLevel}}).

## tensura:corrosion
Acid. Every second it deals **2** damage per level, which can't be dodged, and wears down **every equipped item** by 15 durability per level.

Corrosion Nullification makes you immune (it also blocks Wither), and so does being an Orc Disaster. Reverser turns it into Regeneration II. Acid Shell, Curse Bind, Starved, Corrosion, orc lords' hits and several gluttony skills inflict it. Potions of Corrosion exist.

## tensura:curse
A curse on the body. Per level: **-20%** max health. While cursed you **can't heal**, unless you have Instant Regeneration II or higher. Aura Healing is blocked too.

At **level V or higher**, every second it hits you for your full max health. If that kills a non-Majin player who is still on a starting race, there's a 5% chance they come back as a **Wight**.

Curse magic and Curse Bind inflict it. In miasmic biomes, too much ambient magicule curses anyone who isn't undead. Abnormal Condition Resistance and Abnormal Condition Nullification make you immune.


## tensura:diamond_path
Diamond Path Art (battlewill). Per level: **+{{cfg:config/tensura/ability/battlewill_config.toml|DiamondPath.damageBoost}}** armor and **+{{cfg:config/tensura/ability/battlewill_config.toml|DiamondPath.knockBackResistanceBoost}}** knockback resistance. Pressing the art gives level I for {{secs:config/tensura/ability/battlewill_config.toml|DiamondPath.effectTime}} s, or level II for {{secs:config/tensura/ability/battlewill_config.toml|DiamondPath.effectTimeMastered}} s once mastered. It removes {{link:tensura:chill}} every second.

It also works like an elemental resistance: fire, water, wind, earth, space, gravity, lightning, light, dark, heat, cold and corrosion damage is **blocked**, unless the hit is at least {{pct:config/tensura/ability/skill/resistance_config.toml|hpDamageBypassResistance}} of your current health (then it goes through, reduced to that same percentage). Hits that bypass resistances, or come from an attacker with Resistance Degradation, get through normally.

## tensura:disintegrating
Holy disintegration. Every half second it deals **100** holy damage per level, plus the same amount as spiritual damage. It pierces barriers and can't be dodged. Hinata Sakaguchi's Melt Slash inflicts it for 5 seconds. Angels such as Michael and Feldway's angels, and skills like Solomon, Camael, Sunshine Grace, Tornado and Vehement, make you immune.

## tensura:dragon_mode
Dragon Mode, a transformation. Per level: **+12** attack damage, **+20** armor and **+0.05** movement speed. It also **doubles** your max magicule and max aura (this part doesn't grow with level).

The Dragon Mode skill gives it for {{secs:config/tensura/ability/skill/intrinsic_config.toml|DragonMode.transformationDuration}} s ({{secs:config/tensura/ability/skill/intrinsic_config.toml|DragonMode.transformationDurationMastered}} s mastered). Flame Dragon's Blazing Wings gives **level II** for 3 minutes (6 mastered) and refills your magicule and aura. When it ends, your current magicule and aura are **halved**, and you get the transformation hangover: {{link:minecraft:weakness}} II, {{link:tensura:fragility}} II and {{link:tensura:paralysis}} I for 10 minutes. Only one transformation can be active at a time, and TR: Nightmares' Pseudo Dragon Body can't be used alongside it.

## tensura:drowsiness
Overwhelming sleepiness. Per level: **-25%** movement speed, **-4** attack damage, **-10%** attack speed and **-25%** jump, swim, lava and glide speed. Everything that hits you deals **+20%** damage per level.

At **level V or higher** it becomes lethal: every quarter second it deals "drowsy death" damage equal to your **current health**, which can't be dodged.

Sloth, Dreamer and Dream Manipulation raise its level the longer they're held on you. Belphegor, Astaroth, Dark Passenger's World of Darkness and some addon skills and bosses also inflict it. Several angelic skills (Solomon, Camael, Sunshine Grace, Tornado) make you immune.

## tensura:earth_lock
Stone armor that roots you in place. Per level: **+{{cfg:config/tensura/ability/magic/aspectual_config.toml|EarthLock.knockbackResistance}}** knockback resistance and the same explosion knockback resistance. You're shown covered in stone while it lasts. Earth Lock magic gives it for {{secs:config/tensura/ability/magic/aspectual_config.toml|EarthLock.knockbackResistanceDuration}} s, and Lesser Daemons give it to themselves when they fire stone shots.

## tensura:enemy_search
The buff from Search Enemy magic ({{secs:config/tensura/ability/magic/aspectual_config.toml|SearchEnemy.searchDuration}} s, or kept up while its mastered "constant" mode is held). It adds **+0.1** to your presence sense radius, which is tiny next to the 30-block base, so on its own it barely changes what you can sense. While it lasts, Search Enemy gains mastery. Pressing the spell again ends it early.

## tensura:energy_blockade
Blocks your energy. Per level: **-20%** magicule and aura regeneration. While you have it, Possession, Dragon Possession and Goddess Incarnation fail to activate, and TR: Nightmares' teleport abilities (such as Reticence, Judicator and Dark Passenger) can't move you.

Holy Fields put level V on intruders. Clones from Doppelganger, Mirage and Body Double carry level V so they don't regenerate. Istaroth's banishment and Asmoday's prison also apply it. Angelic skills (Solomon, Camael, Sunshine Grace, Tornado, Vehement) make you immune.

## tensura:engorgement
The Engorger unique skill's growth form. Per level: **+{{cfg:config/tensura/ability/skill/unique_config.toml|Engorger.attack}}** attack damage, **+{{cfg:config/tensura/ability/skill/unique_config.toml|Engorger.armor}}** armor, **+{{cfg:config/tensura/ability/skill/unique_config.toml|Engorger.attackKnock}}** attack knockback, **+{{cfg:config/tensura/ability/skill/unique_config.toml|Engorger.knockResistance}}** knockback resistance, **+{{cfg:config/tensura/ability/skill/unique_config.toml|Engorger.speed}}** movement and swim speed, **+{{cfg:config/tensura/ability/skill/unique_config.toml|Engorger.jumpBoost}}** jump strength, **+{{cfg:config/tensura/ability/skill/unique_config.toml|Engorger.range}}** reach and +1 step height. You also grow to **{{cfg:config/tensura/ability/skill/unique_config.toml|Engorger.size}}×** size.

Every second it feeds you (players) or heals you (mobs). Engorger keeps it on while toggled.

## tensura:falsifier
The Falsifier skill's concealment. It gives **+2** presence concealment, and every quarter second, mobs within 40 blocks that are targeting you lose track of you unless their presence sense is higher than your concealment. While it's active, Falsifier's other modes ignore their cooldowns.

## tensura:fatal_poison
A deadly poison. Every second it deals **2** damage per level, which can't be dodged.

Poison Nullification, Abnormal Condition Nullification, Survivor and Mammon make you immune. Mastered Antidote magic lowers its level by {{cfg:config/tensura/ability/magic/aspectual_config.toml|Antidote.fatalLevel}} and shortens it. Reverser turns it into Regeneration II. Potions of Fatal Poison exist (45 or 90 seconds, or Fatal Poison II).

It comes from poisonous monsters (hound dogs, giant ants, army wasps, aqua frogs, phantaspores, Undine and more), the Spider Dagger, mastered Poison and Lethal Poison, Snake Eye, Acid Rain, poison breath and Disaster (level X).

## tensura:fate_change
The luck buff from Tuner (also given by Mood Maker and Phoenix while they're active, and for 10 minutes by Yog-Sothoth's Courage). Per level: **+{{cfg:config/tensura/ability/skill/unique_config.toml|Tuner.bonusAttack}}** attack damage, **+{{cfg:config/tensura/ability/skill/unique_config.toml|Tuner.bonusAttackSpeed}}** attack speed, **+{{cfg:config/tensura/ability/skill/unique_config.toml|Tuner.bonusSpeed}}** movement speed, **+{{cfg:config/tensura/ability/skill/unique_config.toml|Tuner.bonusSwim}}** swim speed, and **+{{cfg:config/tensura/ability/skill/unique_config.toml|Tuner.bonusMeleeDodge}}%** melee and **+{{cfg:config/tensura/ability/skill/unique_config.toml|Tuner.bonusProjectileDodge}}%** projectile dodge chance.

## tensura:fear
Terror. From level II it slows you by **5%** per level. Higher levels get dangerous (Abnormal Condition Resistance, while toggled on, counts your Fear as 2 levels lower for these):

- **Level V+:** a mob this afraid won't pick targets (unless it's in a Rampage), and every 2 seconds a feared player within 7 blocks of whoever scared them takes **2 × (level − 4)** fear damage.
- **Level X+:** every 2 seconds it also deals **3 × (level − 9)** fear damage no matter where you are.

Fear matters for other abilities too: a mob that fears you can be named even if it's stronger than you, mobs flee from what they fear, and Heart Eat (Gourmand), Merciless and several soul skills work on targets that are afraid enough.

Haki and Sacred Haki (Coercion), direwolves' howl and many demon lord skills inflict it. Spiritual Attack Nullification makes you immune.

## tensura:flashed_blindness
A blinding flash. Your view **whites out**: the fog turns white and closes in, so you can only see a short distance. Solar Flare, Mental Crush and magic explosions inflict it.

## tensura:fragility
You take **+20%** damage per level from every source.

It's the second part of the transformation hangover (Fragility II for 10 minutes after Beast Transformation, Dragon Mode and similar forms). Vampire races get it on new-moon nights, and Wight and spirit skeleton races in sunlight. Earth Jail, Mental Crush, Shrink, Snatch, Disaster, giant ants and more inflict it. Potions of Fragility exist (45 or 90 seconds, or Fragility II).

Abnormal Condition Resistance, Abnormal Condition Nullification, Survivor and Mammon make you immune. Reverser turns it into Resistance.

## tensura:frost
Frozen solid. Your movement, swim speed, jump and reach all drop to **zero**, your view is locked where it was, flying stops, and you **can't heal** (unless you have Instant Regeneration II or higher). It shatters with a glass sound when it ends.

Ice Wall (when broken), TR: Nightmares' Freezing Burn and several ice skills inflict it. An Ice Lance hitting a frozen target deals bonus damage per Frost level and breaks the ice. Cold Nullification and Thermal Fluctuation Nullification make you immune.

## tensura:future_vision
Seeing a moment ahead. It gives **+100%** melee dodge, projectile dodge, dodge-negation and critical hit chance, so you dodge almost everything and every hit crits.

Seer gives it for {{secs:config/tensura/ability/skill/unique_config.toml|Seer.visionDuration}} s ({{secs:config/tensura/ability/skill/unique_config.toml|Seer.visionDurationMastered}} s mastered), and Seer ignores its cooldown while it lasts. Ultimate Eye's Perfect Action gives it for 60 s. While you have it, Magical Eye also dodges every direct hit and projectile.

## tensura:guarded
A guardian's protection. Per level: **+{{cfg:config/tensura/ability/skill/unique_config.toml|Guardian.protectionArmor}}** armor and **+{{cfg:config/tensura/ability/skill/unique_config.toml|Guardian.protectionBarrier}}** multilayer barrier. The Guardian skill gives it to allies within {{cfg:config/tensura/ability/skill/unique_config.toml|Guardian.protectionRadius}} blocks for {{secs:config/tensura/ability/skill/unique_config.toml|Guardian.protectionDuration}} s. Beelzebub and Michael also grant it.

## tensura:haki_coat
Your haki or aura wrapped around your body. It gives **+1** physical resistance degradation, so your physical hits ignore physical resistances. It also lets physical attacks hurt beings that normally shrug them off (magic elementals and some bosses take only 1% from plain physical hits): **half** damage with Haki Coat I, **full** damage with Haki Coat II or higher.

Sacred Haki and Demon Lord Haki toggle it ({{secs:config/tensura/ability/skill/extra_config.toml|SacredHaki.coatDuration}} s), Villain keeps it on while active, and bosses such as Gazel Dwargo, Luminous Valentine and Carrion have level II.

## tensura:healthcare
Healthcare magic's regeneration. Every 2 seconds it heals **{{cfg:config/tensura/ability/magic/aspectual_config.toml|Healthcare.healthRegeneration}}** health per level (the spell gives level II), unless something is stopping your healing. The spell lasts {{secs:config/tensura/ability/magic/aspectual_config.toml|Healthcare.careDuration}} s, or {{secs:config/tensura/ability/magic/aspectual_config.toml|Healthcare.careDurationMastered}} s once mastered.

## tensura:holy_damage
Holy burning. Every quarter second it deals **2** holy damage per level, which can't be dodged, but only to monsters and creatures whose alignment is weak to holy power. Anything else is unharmed. TensuraMoreSkills' Arthur and Avalon holy auras apply it.

## tensura:hypnosis
A dazed trance. Every quarter second there's a **5%** chance per level that you suddenly turn to face a random direction.

Baffledil flowers, phantaspores and Potions of Hypnosis inflict it. Abnormal Condition Nullification and Mammon make you immune. Reverser turns it into {{link:tensura:illusion_boost}}.

## tensura:illusion_boost
Strengthens illusion magic. Per level: **+0.3** illusion boost, which lengthens Mirage clones, Confusion and Invisible magic, and makes Possession magic stronger. Potions of Hypnotic Efficiency give it.

## tensura:infection
A spreading disease that gets worse over time. Undead and spiritual beings can't catch it. It checks every 3 seconds:

| Level | What happens | Worsens after |
|---|---|---|
| I | Nothing yet | 30 s |
| II | 2 damage every 3 s | 15 s |
| III | 4 damage every 3 s, plus Nausea | 9 s |
| IV | 6 damage every 3 s, Nausea and {{link:tensura:fragility}} II | 9 s |
| V | Damage equal to your **max health** every 3 s | |

From level II it also slows you and weakens your attacks, a little more at each level (about **-15%** speed and **-20%** attack damage per step).

While infected by the Healer skill, every creature you hit, and every creature that hits you, catches Infection I. Shinji Tanimura spreads it, the Healer skill can cure it, and some raw monster meat has a small chance to infect you. Angels and angelic skills make you immune.

## tensura:infinite_imprisonment
A sealing prison. While it lasts your movement, flight, jumping, swimming, reach, attack damage and attack speed, dodge chances, and magicule and aura regeneration all drop to **zero**. Every half second it also drains **500** magicule per level, and it knocks you out of flight.

You can't heal (not even with Instant Regeneration), use skills or race abilities, learn skills, cast from slotted items, be teleported, or travel to another dimension. Imprisoned mobs lose their target.

Yog-Sothoth's Infinity Prison, Uriel, Lord of Myth, Chrono Leech, Kronairos and Avalon's Law of the Closed Prison inflict it. Merlin, Tornado, Solomon, Sunshine Grace, Camael, Hamiel and angels are immune.

## tensura:insanity
Madness. Every 2 seconds, from level II up, it deals **2 × level** spiritual damage. If you're somewhere dark (light level below 3 × level − 2), it also deals **level − 1** normal damage. Players hear eerie cave sounds and can't skip the night by sleeping. Toggled Abnormal Condition Resistance counts it as 2 levels lower.

A creature that's insane (or in a Rampage) can't be named. Overfilling your aura drives you mad too: holding more than **{{pct:config/tensura/energy_config.toml|auraMultiplierForInsanity}}** over your max aura gives Insanity, at a higher level the further over you are.

Mental Crush, Snake Eye, Oppression, Envy (on its user), Cultist and Lunatic inflict it. Spiritual Attack Nullification, Merlin and Escanor make you immune.

## tensura:inspiration
A commander's rallying buff. Per level: **+{{cfg:config/tensura/ability/skill/unique_config.toml|Commander.inspireMultiplier}}×** base attack damage, attack speed, attack knockback, knockback resistance, max health, movement speed, jump strength and swim speed, and **+{{cfg:config/tensura/ability/skill/unique_config.toml|Commander.inspireCritChance}}%** critical hit chance. Inspired mobs also stay calm instead of going berserk from Rampage or Arrogance.

Commander gives it to allies within {{cfg:config/tensura/ability/skill/unique_config.toml|Commander.inspireRadius}} blocks, and Captivator, Hidden Ruler, Ruler, Subjugator, naming evolutions and several addon skills give it too.

## tensura:instant_regeneration
Rapid regeneration fueled by magicule. Every half second it heals **all** your missing health, paying **{{cfg:config/tensura/ability/skill/extra_config.toml|InfiniteRegeneration.magiculeCost}}** magicule per health point ({{cfg:config/tensura/ability/skill/extra_config.toml|InfiniteRegeneration.magiculeCostMastered}} if the skill giving it is mastered; Survivor's level I costs only 20). If you can't pay in full, it heals what you can afford and switches the skill off.

**Level II or higher** also:

- restores spiritual health ({{cfg:config/tensura/ability/skill/extra_config.toml|InfiniteRegeneration.shpMagiculeCost}} magicule per point, {{cfg:config/tensura/ability/skill/extra_config.toml|InfiniteRegeneration.shpMagiculeCostMastered}} mastered),
- lets you heal through Curse, Frost and Black Burn.

Ultraspeed Regeneration and Survivor give level I; Infinite Regeneration gives level II. Tensura: Mysticism's Brimstone Flames slow it down to one weaker heal every 5 seconds.

## tensura:lust_drain
Lust's draining touch. Each melee hit you land drains **{{cfg:config/tensura/ability/skill/unique_config.toml|Lust.drainEP}}** EP from the target into you, and this can take you past your normal maximum. Lust gives it for {{secs:config/tensura/ability/skill/unique_config.toml|Lust.drainDuration}} s (level II when mastered).

## tensura:lust_embracement
Held in an embrace. Your movement, flight, jumping and reach drop to **zero**, you get full knockback resistance, and your view is locked. You can't be teleported or leave the dimension. Every second, whoever is embracing you drains **{{cfg:config/tensura/ability/skill/unique_config.toml|Lust.embraceEP}}** EP from you (level II also drains a percentage of your EP), and pain nullification stops protecting you. It ends early if the embracer dies. Lust's and Asmodeus's Embrace and Luminous Valentine inflict it.

## tensura:mad_ogre
Berserk's Mad Ogre form, a transformation. Per level: **+45** attack damage, **+20** armor and **+0.4** knockback resistance. It also doubles your size and gives +0.04 speed, +2 reach and +1 step height, and fire can't keep you burning. While it lasts you're kept in {{link:tensura:rampage}} III. Mad orbs circle you.

Berserk gives level {{cfg:config/tensura/ability/skill/unique_config.toml|Berserk.madOgreLevel}} (level {{cfg:config/tensura/ability/skill/unique_config.toml|Berserk.madOgreLevelMastered}} mastered) for {{secs:config/tensura/ability/skill/unique_config.toml|Berserk.madOgreDuration}} s. When it ends you get the transformation hangover: {{link:minecraft:weakness}} II, {{link:tensura:fragility}} II and {{link:tensura:paralysis}} I for 10 minutes.

## tensura:magic_aura
Your weapon wrapped in magic. It gives **+1** physical resistance degradation. Each melee hit also deals a second hit of **{{cfg:config/tensura/ability/skill/extra_config.toml|MagicAura.auraMultiplier}}×** your attack damage as magic of the element you picked (holy, earth, fire, space, water, wind or plain magic). Weapons with slotted magic don't get the extra hit. It also lets your physical hits hurt magic elementals and similar beings at half damage. Magic Aura gives it for {{secs:config/tensura/ability/skill/extra_config.toml|MagicAura.auraDuration}} s.

## tensura:magic_barrier
A barrier against magic. It removes {{link:tensura:chill}} every second and gives +1 magic barrier. Against Tensura magic damage it works like this (percentages of your health when the barrier went up, mastered values in brackets):

- Hits smaller than **{{pct:config/tensura/ability/magic/aspectual_config.toml|MagicBarrier.barrierThreshold}}** ({{pct:config/tensura/ability/magic/aspectual_config.toml|MagicBarrier.barrierThresholdMastered}}) of that health are reduced by **{{pct:config/tensura/ability/magic/aspectual_config.toml|MagicBarrier.belowReduction}}** ({{pct:config/tensura/ability/magic/aspectual_config.toml|MagicBarrier.belowReductionMastered}}) of that health.
- Bigger hits are reduced by **{{pct:config/tensura/ability/magic/aspectual_config.toml|MagicBarrier.aboveReduction}}** ({{pct:config/tensura/ability/magic/aspectual_config.toml|MagicBarrier.aboveReductionMastered}}) of that health.

An attacker strong enough to shatter barriers breaks it instantly. Magic Barrier magic gives it for {{secs:config/tensura/ability/magic/aspectual_config.toml|MagicBarrier.barrierDuration}} s ({{secs:config/tensura/ability/magic/aspectual_config.toml|MagicBarrier.barrierDurationMastered}} s mastered); Reinforced Barrier and greater and arch daemons also use it.

## tensura:magic_elemental_transformation
Magic Elemental Transformation: you become a being of one element. Your damage of that element is multiplied by **{{cfg:config/tensura/ability/skill/extra_config.toml|MagicElementalTransform.transformBoost}}**, and your hits add an element effect:

| Element | On hit |
|---|---|
| Darkness | Darkness |
| Earth | {{link:tensura:burden}} |
| Flame | sets the target on fire |
| Light | Nausea |
| Water | {{link:tensura:fatal_poison}} |
| Wind | {{link:tensura:paralysis}} |
| Space | your physical hits count as severance damage |

Plain physical attacks barely touch you: in the current code a physical hit is reduced to just **0.01** damage, or **0.5** if the attacker has Haki Coat I, Magic Aura or Cook. Attackers with Haki Coat II or higher, Divine Ki or Anti-Skill hit you normally.

It lasts {{secs:config/tensura/ability/skill/extra_config.toml|MagicElementalTransform.transformationDuration}} s ({{secs:config/tensura/ability/skill/extra_config.toml|MagicElementalTransform.transformationDurationMastered}} s mastered). When it ends you get the transformation hangover: {{link:minecraft:weakness}} II, {{link:tensura:fragility}} II and {{link:tensura:paralysis}} I for 10 minutes.

## tensura:magic_interference
Disrupted magic. While you have it, you can't fly with Flight magic, Air Flight, Gravity Flight, Gravity Manipulation or Gravity Domination, and players who fly by other means are dropped (unless their race or form can still fly). At **level II or higher**, transformations can't be started and an active one is cancelled.

Magic Jamming inflicts level II on touch and level I in its arena. Holy Fields, Charybdis, Gilgamesh's Enkidu and prison skills (Yog-Sothoth, Uriel) also apply it. Law Manipulation, Law Domination and similar skills can cleanse it.

## tensura:magicule_poison
Magicule overload. Every second it deals **2** damage per level and gives Nausea. You get it when your magicule goes more than **{{pct:config/tensura/energy_config.toml|magiculeMultiplierForPoison}}** over your maximum (a higher level the further over you are), for example after absorbing too much. Some foods and Chrono Leech also cause it. Many angelic and high-tier skills make you immune.

## tensura:magicule_regeneration
**+50%** magicule regeneration per level. Some foods give it.

## tensura:mind_control
You're under someone else's control. While it lasts, whoever applied it becomes your temporary owner: a mob fights for them like a subordinate. It ends early if the controller loses the skill that gave it (checked every 3 seconds). When it ends, the mob goes back to its real owner, if it had one.

Dominate magic, Villain, Chosen One, Charm and temptation skills, Aphrodite, Mammon's Control Heart, Yog-Sothoth's Takeover and Hinata Sakaguchi inflict it. Summons from Daemon Army are bound with it. An alpha direwolf under mind control can't be named.

## tensura:movement_interference
Binding. Per level: **-10%** movement, swim, lava and glide speed, jump strength and attack speed, and **+0.1** knockback resistance. You also can't use your race's abilities while it lasts.

Mud Hand, Earth Jail, Shadow Bind, Demon Marionette, Greed, Dark Cube and death blessing fields inflict it. Disintegration and several holy judgement skills use level X or higher to pin their target in place.

## tensura:ogre_berserker
An ogre's berserk transformation. Per level: **+30** attack damage, **+10** armor and **+0.03** movement speed. Ogre Berserker gives level I.

Divine Berserker gives **level II or higher**, which is stronger but costly:

- you lose **10 health per level above I** every second,
- all non-physical damage you take counts as physical (so physical resistances protect you), and spiritual damage hits your body instead of your soul,
- Divine Berserker multiplies your battlewill damage by {{cfg:config/tensura/ability/skill/unique_config.toml|DivineBerserker.battlewillMultiplier}} ({{cfg:config/tensura/ability/skill/unique_config.toml|DivineBerserker.battlewillMultiplierMastered}} mastered).

When it ends you get the transformation hangover: {{link:minecraft:weakness}} II, {{link:tensura:fragility}} II and {{link:tensura:paralysis}} I for 10 minutes.

## tensura:ogre_guillotine
Ogre Sword Guillotine (battlewill). At level I: attack damage **×{{cfg:config/tensura/ability/battlewill_config.toml|OgreSwordGuillotine.attackMultiplier}}**, attack reach **×{{cfg:config/tensura/ability/battlewill_config.toml|OgreSwordGuillotine.reachMultiplier}}** and attack speed **×{{cfg:config/tensura/ability/battlewill_config.toml|OgreSwordGuillotine.attackSpeedMultiplier}}**. Level II doubles each of those changes. Your physical hits count as battlewill damage while it lasts, which ki and chi releases need. The art gives level I for {{secs:config/tensura/ability/battlewill_config.toml|OgreSwordGuillotine.effectTime}} s, or level II for {{secs:config/tensura/ability/battlewill_config.toml|OgreSwordGuillotine.effectTimeMastered}} s once mastered. Press it again to end it.

## tensura:oppression
Crushing pressure. It slows your movement and jumping by **95%** per level (so level II and up pins you completely). Every 10 seconds it also raises your {{link:tensura:insanity}} by one level. The Oppressor skill can then crush an oppressed target for {{cfg:config/tensura/ability/skill/unique_config.toml|Oppressor.oppressDamage}} gravity damage ({{cfg:config/tensura/ability/skill/unique_config.toml|Oppressor.oppressDamageMastered}} mastered). Michael, Feldway, Arthur's Holy Order and Avalon's Law of Crushing Heaven also inflict it.

## tensura:paralysis
Numbness. Per level: **-20%** movement and swim speed, **-33%** jump strength, **-10%** attack speed and **-30%** mining speed. From level II you can't sprint.

It's the third part of the transformation hangover (Paralysis I for 10 minutes). The Paralysis skill, Sleep Mist, Curse Bind, Snake Eye, the Centipede Dagger, electric and black lightning attacks, evil centipedes, feathered serpents, Sylphide and hell moths inflict it. Potions of Paralysis give Paralysis II or III.

Paralysis Resistance, Paralysis Nullification, Abnormal Condition Nullification, Survivor and Mammon make you immune. With Abnormal Condition Resistance toggled on, Paralysis II wears off within a second and higher levels count as 2 lower. Reverser turns it into Speed.

## tensura:petrification
Turning to stone. Per level: **-25%** movement, swim, lava and glide speed and jump strength. At **level IV or higher** you're fully petrified: within a quarter second you take damage equal to your **max health** (can't be dodged), and the effect ends. With Abnormal Condition Resistance toggled on it counts as 2 levels lower, and if that drops it below IV the effect simply ends.

Each basilisk spit adds a level. Snake Eye and Truth also petrify. Abnormal Condition Nullification, Survivor and Mammon make you immune, and basilisks can't be petrified.

## tensura:physical_barrier
A barrier against physical attacks. It removes {{link:tensura:chill}} every second and gives +1 physical barrier. Against physical hits it works like this (percentages of your health when the barrier went up, mastered values in brackets):

- Hits smaller than **{{pct:config/tensura/ability/magic/aspectual_config.toml|Barrier.barrierThreshold}}** ({{pct:config/tensura/ability/magic/aspectual_config.toml|Barrier.barrierThresholdMastered}}) of that health are reduced by **{{pct:config/tensura/ability/magic/aspectual_config.toml|Barrier.belowReduction}}** ({{pct:config/tensura/ability/magic/aspectual_config.toml|Barrier.belowReductionMastered}}) of that health.
- Bigger hits are reduced by **{{pct:config/tensura/ability/magic/aspectual_config.toml|Barrier.aboveReduction}}** ({{pct:config/tensura/ability/magic/aspectual_config.toml|Barrier.aboveReductionMastered}}) of that health.

An attacker strong enough to shatter barriers breaks it instantly. Barrier magic gives it for {{secs:config/tensura/ability/magic/aspectual_config.toml|Barrier.barrierDuration}} s ({{secs:config/tensura/ability/magic/aspectual_config.toml|Barrier.barrierDurationMastered}} s mastered); Reinforced Barrier and arch daemons also use it.

## tensura:presence_concealment
Hiding your presence. With it you're **invisible** (your armor and even flames on you are hidden), you get +1 step height, and creatures using presence sense can't highlight you. Every quarter second, mobs within 40 blocks that are targeting you lose track of you unless their presence sense is higher than your concealment level.

Invisible magic, Haze, Formhide, Murderer, Shadow Striker, Snatch, Hidden Ruler and many addon skills give it. Truth and Wind Reading can counter it.

## tensura:presence_sense
Sensing presences. Per level: **+1** presence sense. Creatures within your presence sense radius (30 blocks by default) glow through walls for you, with more detail at higher levels. At 4 or more, everything in range is highlighted. It also lets you keep track of concealed targets whose concealment is lower than your sense. Tyrant, Decipherer, Lost From Light, Truth and Lord of Myth give it.

## tensura:protection
**+{{cfg:config/tensura/ability/magic/aspectual_config.toml|Protection.protectionArmor}}** armor per level. Protection magic gives level {{cfg:config/tensura/ability/magic/aspectual_config.toml|Protection.protectionLevel}} to you, or to a targeted creature if you sneak, for {{secs:config/tensura/ability/magic/aspectual_config.toml|Protection.protectionDuration}} s ({{secs:config/tensura/ability/magic/aspectual_config.toml|Protection.protectionDurationMastered}} s mastered).

## tensura:rampage
Uncontrollable rage.

- **Self-inflicted** (Berserk, Wrath, Mad Ogre): per level, **+{{cfg:config/tensura/ability/skill/unique_config.toml|Wrath.rampageAttack}}** attack damage, **+{{cfg:config/tensura/ability/skill/unique_config.toml|Wrath.rampageArmor}}** armor, **+{{cfg:config/tensura/ability/skill/unique_config.toml|Wrath.rampageAttackSpeed}}** attack speed, **+{{cfg:config/tensura/ability/skill/unique_config.toml|Wrath.rampageSpeed}}** movement, swim and lava speed, and **+{{cfg:config/tensura/ability/skill/unique_config.toml|Wrath.rampageKnockbackResistance}}** knockback resistance.
- **Inflicted by someone else:** only the speed bonuses and a much smaller attack bonus (1/20 of the above), with no armor.

A rampaging **mob** attacks whatever is nearby (within {{cfg:config/tensura/entity/effect_config.toml|Rampage.mobAggroRadius}} blocks): at level I only players, from level II anything that isn't its ally, and from level III even its allies. Inspired mobs don't rampage.

A rampaging **player** takes {{pct:config/tensura/entity/effect_config.toml|Rampage.playerDamageHP}} of their max health and {{pct:config/tensura/entity/effect_config.toml|Rampage.playerDamageSHP}} of their max spiritual health every second during the last {{secs:config/tensura/entity/effect_config.toml|Rampage.playerDamageDuration}} s (never below 1).

Fighting keeps it going: each hit you land adds {{secs:config/tensura/entity/effect_config.toml|Rampage.replenishEach}} s (up to {{secs:config/tensura/entity/effect_config.toml|Rampage.replenishDamage}} s), and taking a hit refills it to at least {{secs:config/tensura/entity/effect_config.toml|Rampage.replenishHurt}} s. Rampaging creatures can't be named, charmed or mind-controlled, and feared mobs still fight while rampaging. Waking up after sleeping in the Overworld ends it. Summoned daemons, some boss minions and Charybdis's megalodons rampage.

## tensura:reinforcement
Strengthened equipment. Your gear loses **25% less durability** per level, so at level IV or higher it takes no durability damage at all. Reinforcement magic gives level {{cfg:config/tensura/ability/magic/aspectual_config.toml|Reinforcement.reinforcementLevel}} to you, or to a targeted creature if you sneak, for {{secs:config/tensura/ability/magic/aspectual_config.toml|Reinforcement.reinforcementDuration}} s ({{secs:config/tensura/ability/magic/aspectual_config.toml|Reinforcement.reinforcementDurationMastered}} s mastered).

## tensura:rest
Sloth's complete rest. Your movement, attack damage, attack speed, jumping, reach, swimming, gliding and dodge chances all drop to **zero**, but aura regeneration is multiplied by **{{cfg:config/tensura/ability/skill/unique_config.toml|Sloth.restAP}}** and magicule regeneration by **{{cfg:config/tensura/ability/skill/unique_config.toml|Sloth.restMP}}**. You can't fly, jump, use skills or race abilities, or learn new skills while resting. Sloth gives it while you hold its rest mode, and Sloth's manas gives it while you sleep.

## tensura:self_regeneration
Natural regeneration. Every second it heals **{{cfg:config/tensura/ability/skill/common_config.toml|SelfRegeneration.regenHP}}** health per level. At level II or higher it also restores **{{cfg:config/tensura/ability/skill/common_config.toml|SelfRegeneration.regenSHP}}** spiritual health per level. It does nothing while something is blocking your healing. The Self Regeneration skill keeps level {{cfg:config/tensura/ability/skill/common_config.toml|SelfRegeneration.regenLevel}} (level {{cfg:config/tensura/ability/skill/common_config.toml|SelfRegeneration.regenLevelMastered}} mastered) on you while toggled, and Aquatic Regeneration gives it in water.

## tensura:severance_blade
A cutting edge that severs space. Per level: **+10** attack damage. Your physical hits count as **severance damage**, which also cuts the target's maximum health for a while. From **level V** it also gives physical resistance degradation, so your hits ignore physical resistances.

Severer gives level {{cfg:config/tensura/ability/skill/unique_config.toml|Severer.severanceLevel}} (level {{cfg:config/tensura/ability/skill/unique_config.toml|Severer.severanceLevelMastered}} mastered) for {{secs:config/tensura/ability/skill/unique_config.toml|Severer.severanceDuration}} s. Absolute Severance's coating gives level {{cfg:config/tensura/ability/skill/unique_config.toml|AbsoluteSeverance.coatingLevel}} (level {{cfg:config/tensura/ability/skill/unique_config.toml|AbsoluteSeverance.coatingLevelMastered}} mastered). Camael, Judicator, Elyon and Yog-Sothoth also give it.

## tensura:shadow_step
Moving through shadows. You get **+0.1** movement speed, +1 step height, +0.1 dark vision and **+5** presence concealment (so you're invisible and mobs lose track of you). While in the shadows you **can't be hurt** (projectiles pass through you) and your own attacks deal nothing. You also can't jump, fly, interact, use race abilities, change dimension, or use skills beyond your race limit, and you can't take a breath (air doesn't run down, but it doesn't refill either).

Shadow Motion keeps it on you while held (only in light level 10 or darker until mastered), and Lost From Light gives it too.

## tensura:silence
You can't speak. Magic can't be cast (except spells that cast instantly) and Voice Cannon doesn't work. It also slows chanting by **10%** per level. If you're also {{link:tensura:webbed}}, catching fire burns the web away and ends the silence. Airflow Shut, web bullets, black spiders and hell caterpillars inflict it.

## tensura:sleep
Forced sleep. Your movement, flight, jumping, reach, attack damage and speed, and dodge chances all drop to **zero**, your view goes dark, and you can't jump or interact. Sleeping mobs lose track of targets. Each time you're hurt the sleep gets one level lighter, and a hit at level I wakes you up.

Hypnos magic puts targets to sleep at level {{cfg:config/tensura/ability/magic/aspectual_config.toml|Hypnos.sleepLevel}} for {{secs:config/tensura/ability/magic/aspectual_config.toml|Hypnos.sleepDuration}} s (level {{cfg:config/tensura/ability/magic/aspectual_config.toml|Hypnos.sleepLevelMastered}} for {{secs:config/tensura/ability/magic/aspectual_config.toml|Hypnos.sleepDurationMastered}} s mastered, and half as long if resisted). Merlin, Escanor, Solomon, Camael and angels are immune.

## tensura:soul_drain
Your soul is being eaten. Every half second it deals **10** spiritual damage per level. Merciless's hits give level {{cfg:config/tensura/ability/skill/unique_config.toml|Merciless.drainLevel}} for {{secs:config/tensura/ability/skill/unique_config.toml|Merciless.drainDuration}} s; Soul Manipulation, Soul Domination, Beelzebuth and Feldway's angels also inflict it. Angelic skills (Solomon, Camael, Sunshine Grace, Vehement) make you immune.

## tensura:spatial_blockade
Space around you is locked. You can't teleport or be teleported by skills, and you can't travel to another dimension. TR: Nightmares' teleport abilities can't move you either. At level X or higher even command teleports are blocked; boss fights put level X on players so they can't escape the arena.

Suppressor gives it for {{secs:config/tensura/ability/skill/unique_config.toml|Suppressor.blockadeDuration}} s. Holy Fields, Abaddon's Limitless World, Breaker's Limitless Space, Imaginator, Dragon Factor Haki, Michael and Feldway also apply it. Merlin, Solomon, Camael, Ultimate Eye and Ultimate Shield make you immune.

## tensura:spearhead
The Spearhead skill's rally. Per level: **+{{cfg:config/tensura/ability/skill/unique_config.toml|Spearhead.allyAttack}}** attack damage, **+{{cfg:config/tensura/ability/skill/unique_config.toml|Spearhead.allyArmor}}** armor, **+{{cfg:config/tensura/ability/skill/unique_config.toml|Spearhead.allySpeed}}** movement speed and **+{{cfg:config/tensura/ability/skill/unique_config.toml|Spearhead.allySwim}}** swim speed. Spearhead gives it to allies within {{cfg:config/tensura/ability/skill/unique_config.toml|Spearhead.allyRadius}} blocks (level II when mastered). Subordinates you've set as meat shields also move to the spot you're looking at.

## tensura:strengthen
**+6** attack damage per level. Strength and Steel Strength give level {{cfg:config/tensura/ability/skill/common_config.toml|Strength.strengthenLevel}} (level {{cfg:config/tensura/ability/skill/common_config.toml|Strength.strengthenLevelMastered}} mastered) for {{secs:config/tensura/ability/skill/common_config.toml|Strength.strengthenDuration}} s ({{secs:config/tensura/ability/skill/common_config.toml|Strength.strengthenDurationMastered}} s mastered), and those skills skip their cooldown while it lasts. Orc lords strengthen their subordinates when they kill, and many other skills (Berserk, Camael, Escanor, Judicator, Snatch, Truth) give it too.

## tensura:true_blindness
Complete blindness: dark fog closes in around you so you can only see a very short distance. Slimes are blind like this until they gain presence sense (for example from Magic Sense). Praying on a praying path, butchering, Melancholy, Michael and Kronairos also cause it. Races with a manas skill, Solomon, Camael and Tornado are immune.

## tensura:warping
You're about to warp. While a spatial skill's warp charges, you shimmer with portal particles and your screen wobbles like standing in a nether portal. When the charge finishes you're teleported to the warp point you picked (and the skill gains mastery). If the effect is removed early, the warp fails.

## tensura:webbed
Stuck in webbing. Your movement and swim speed drop by **99%**, jumping, reach and follow range are cut (by 50%, 50% and 80%), you can't jump, and your view is locked in place. **Catching fire burns the web away** instantly (and any {{link:tensura:silence}} with it). Web bullets, thrown cobwebs, black spiders and hell caterpillars inflict it.

## tensura:wind_protection
A wrapping of wind. Per level: **+{{pct:config/tensura/ability/magic/aspectual_config.toml|WindProtection.effectSpeed}}** movement speed and **+{{cfg:config/tensura/ability/magic/aspectual_config.toml|WindProtection.effectDodge}}%** projectile dodge chance, so projectiles almost never hit you. From level II, each level above I also gives **{{pct:config/tensura/ability/magic/aspectual_config.toml|WindProtection.effectBurn}}** shorter burning, **+{{cfg:config/tensura/ability/magic/aspectual_config.toml|WindProtection.effectKnockback}}** knockback resistance and **+{{cfg:config/tensura/ability/magic/aspectual_config.toml|WindProtection.effectFlameBoost}}** flame boost. Wind Protection magic gives level {{cfg:config/tensura/ability/magic/aspectual_config.toml|WindProtection.effectLevel}} for {{secs:config/tensura/ability/magic/aspectual_config.toml|WindProtection.effectDuration}} s, or level {{cfg:config/tensura/ability/magic/aspectual_config.toml|WindProtection.effectLevelMastered}} for {{secs:config/tensura/ability/magic/aspectual_config.toml|WindProtection.effectDurationMastered}} s once mastered.

<!-- kind: -->

## tensura:hell
The Underworld, a spiritual world of barren stone and red sand under a permanent noon, with thick fog everywhere. Its ambient magicule is **100,000** higher than normal and refills twice as fast, so weak players can get {{link:effect/tensura:magicule_poison}} here.

**Getting there:**

- **Hell Gate** structures hold a Hell Portal. They generate in flat lands, badlands, savannas, the {{link:tensura:barren_land}} and the {{link:tensura:desert_of_death}}, and in Hell itself. Stepping into a portal in the Overworld takes you to Hell, and the one in Hell takes you back to the Overworld.
- Ascension's Hell Passage skill (learned by mastering Gate and having Demon Lord Haki) opens a temporary portal.
- Phantoms and Lesser Daemons respawn in Hell.

Daemons live here: Summon Daemon magic pulls them out of Hell, and it can't be cast while you're in Hell. As a spiritual world, spirit-form creatures don't lose magicule here.

## tensura:labyrinth
Ramiris's Labyrinth, a spiritual world. Its ambient magicule is **29,500** higher than normal and refills twice as fast.

**Getting in:** step into the Labyrinth Portal inside a Labyrinth Tree, a structure that generates in the {{link:tensura:ancient_forest}}. Leaving takes you back to the Overworld.

**Rules inside:**

- Survival players are switched to **Adventure mode** (and back when they leave), and skills can't break blocks.
- You **can't die** here unless the `labyrinthDeath` gamerule is on: a lethal hit leaves you at almost no health and sends you back to the Overworld. PvP follows the `labyrinthPvp` gamerule.
- Warping and portal skills don't work inside.
- The **Elemental Colossus** guards the way. Losing to it (or beating it) marks you as having *passed* and moves you to the inner entrance, where the Labyrinth's spirits are.

## tensura:boss_area
The arena for the **Gazel Dwargo** boss fight. You get there through the warp pad in the royal tower of a Dwarf Village, which starts the fight. Players in the arena get {{link:tensura:spatial_blockade}} X, so they can't teleport out, and warp and portal skills don't work here. By default bosses here can't be named, mind-controlled or have their skills plundered (see the Boss settings in Tensura's behaviour config).

## tensura:ancient_forest
An old, magic-rich forest in the Overworld (ambient magicule **+19,500**, refilling faster than normal). It's the only place **Labyrinth Trees** generate, which hold the entrance to the {{link:tensura:labyrinth}}.

{{auto}}

## tensura:barren_land
Dusty wasteland in the Overworld with the strongest ambient magicule of Tensura's surface biomes (**+45,500**). It's foggy, and in rain or thunder a **sandstorm** closes visibility right down. Hell Gates can generate here.

{{auto}}

## tensura:desert_of_death
A deadly desert in the Overworld (ambient magicule **+29,500**). In rain or thunder a **sandstorm** closes visibility right down. Hell Gates can generate here.

{{auto}}

## tensura:miasmic_plains
Plains shrouded in miasma (ambient magicule **+19,500**), always foggy. The miasma changes the rules:

- Monsters can spawn here even in daylight, and undead don't burn in the sun (vampire races aren't hurt by it either).
- When the ambient magicule is too strong for you, you get {{link:effect/tensura:curse}} here instead of {{link:effect/tensura:magicule_poison}} (undead get magicule poison as usual).

{{auto}}

## tensura:underworld_barrens
Hell's rocky barrens (ambient magicule +3,500), always foggy.

{{auto}}

## tensura:underworld_spikes
Hell's field of stone spikes (ambient magicule +2,500), always foggy.

{{auto}}

## tensura:underworld_red_sands
Hell's red sand dunes (ambient magicule +1,500). Sand ruins can generate here.

{{auto}}

## tensura:underworld_sands
Hell's pale sand dunes (ambient magicule +500). Sand ruins can generate here.

{{auto}}
