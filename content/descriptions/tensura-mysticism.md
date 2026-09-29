# Tensura: Mysticism: what things do

Written from the mod's code (Mysticism 2.2.1). Each `## id` section becomes the "What it does" part of that entry's page.
"Per level" means the value grows with the effect level.

<!-- kind: effects -->

## mysticism:aura_healing
Tenacity's regeneration, paid with aura instead of magicule. Every half second it heals **all** your missing health, costing **{{cfg:config/mysticism/ability/skill/intrinsic_config.toml|Tenacity.auraCost}}** aura per health point ({{cfg:config/mysticism/ability/skill/intrinsic_config.toml|Tenacity.auraCostMastered}} once Tenacity is mastered). If you can't pay in full, it heals what you can afford and switches Tenacity off.

At **level II** (mastered Tenacity) it also restores spiritual health ({{cfg:config/mysticism/ability/skill/intrinsic_config.toml|Tenacity.shpAuraCost}} aura per point, {{cfg:config/mysticism/ability/skill/intrinsic_config.toml|Tenacity.shpAuraCostMastered}} mastered) and heals through Curse, Frost, Black Burn and {{link:mysticism:brimstone_flames}}. At level I those block it.

## mysticism:awakened_foresight
Relapse's ascended mode. While it lasts, your skills **cost no aura**. When it ends you drop out of flight unless Gravity Domination is toggled on.

## mysticism:brimstone_flames
Hellish fire. Every second it deals **{{cfg:config/mysticism/effect/effects.toml|BrimstoneFlames.brimstoneFlamesDamage}}** flame damage per level, mostly elemental, which can't be dodged and ignores resistances. It also cripples healing: Aura Healing stops working, and Instant Regeneration only heals every 5 seconds, at 20% strength. Weapons with the {{link:mysticism:holy_flames}} enchantment inflict it for 5 seconds.

## mysticism:collective
Relapse's Divine Inferius mode. It raises almost everything by **50%**: max health, attack damage, attack speed, movement speed, mining speed, reach, step height, water movement, max magicule and aura, their regeneration, and max spiritual health and its regeneration.

## mysticism:constant_destruction
Constant's destruction mode. While it lasts, **every hit you land deals a fixed amount of damage**: the highest single hit Constant has recorded for you (it tracks your biggest hit while its Physical mode is on), up to {{cfg:config/mysticism/ability/skill/unique_config.toml|Constant.constantDestructionMaxDamage}}. Hold the skill to keep it up, for up to {{secs:config/mysticism/ability/skill/unique_config.toml|Constant.constantDestructionHeldTicks}} s.

## mysticism:constant_energy
Constant's energy mode, which lasts {{cfg:config/mysticism/ability/skill/unique_config.toml|Constant.constantEnergyDuration}} s. While it's active, **your skills cost nothing up front** and your magicule and aura don't regenerate. When it ends, everything you spent is taken at once. If you can't afford the bill, your magicule or aura is left at 25% of the maximum and you get {{link:mysticism:constant_energy_debuff}}.

## mysticism:constant_energy_debuff
The price for overspending with {{link:mysticism:constant_energy}}: your magicule and aura **don't regenerate** at all for {{cfg:config/mysticism/ability/skill/unique_config.toml|Constant.constantEnergyDebuffDuration}} s.

## mysticism:constant_health
Constant's health mode. While you hold the skill (up to {{secs:config/mysticism/ability/skill/unique_config.toml|Constant.constantHealthHeldTicks}} s), every time you're hurt your health and spiritual health are reset to what they were when you started, so damage doesn't stick. It costs energy every second.

## mysticism:countering
Restricted's counter stance. You can't move or attack while waiting. The **next physical hit** against you is completely blocked: the stance ends and the attacker becomes {{link:mysticism:imbalanced}} for {{secs:config/mysticism/ability/skill/unique_config.toml|Restricted.counterImbalanceDuration}} s. Press Restricted again to drop the stance without the cooldown.

## mysticism:cultivating
A Cultivator breakthrough in progress. You gain **3×** as much magicule while it lasts. If it runs its full course, your cultivation level goes up by one and Cultivator gains mastery. If you **die** while cultivating, your cultivation level and Cultivator's mastery are reset to zero. You can only start a breakthrough after {{cfg:config/mysticism/ability/skill/unique_config.toml|Cultivator.mobKillsNeeded}} kills.

## mysticism:dazzled
Captivated by a star. You're forced to stare at whoever dazzled you and can't move. Dazzled mobs stop attacking. Captivator's Star Power inflicts it for 10 seconds.

## mysticism:dragon_burn
Dragon embers. Every second it deals damage equal to **5%** of your max health. Nothing in the current version of the mod applies it.

## mysticism:enkidu
The chains of Enkidu. Your movement, flight, jumping, reach, attack damage and speed, dodge chances and magicule and aura regeneration all drop to **zero**, you're pulled out of flight, and you **can't use skills**. Gatekeeper's Enkidu binds a target and can release it again.

## mysticism:eternal_permafrost
Creeping frost. You're slowed by **30%**, plus 15% for each level above I (up to 95%). While frozen, battlewill and magic skills have a **50% chance to fail** when you use them (and go on a 5 second cooldown). It thaws over time, losing a level every 2 seconds. Weapons with the {{link:mysticism:boreal_frost}} enchantment inflict it at level VI.

## mysticism:fixation
Fixed in place by Coalescence. You can't move, jump, swim, attack, mine, use items, right-click blocks or use skills, your view is locked, and you get full knockback resistance. Flight stops. Coalescence's Fixation and Eternal Domain inflict it. Anyone who has Anti-Skill can't be fixated.

## mysticism:gravity_fluctuation
Unstable gravity. You bob up and down in a steady wave (stronger and faster at higher levels) and take no fall damage while it lasts. Gravity Flux inflicts it.

## mysticism:imbalanced
Thrown off balance by a counter. Your attack speed drops to **zero** and your attacks deal **no damage** at all while it lasts. Restricted's counter stance ({{link:mysticism:countering}}) inflicts it.

## mysticism:intangible
Phaser's intangibility. Attacks and projectiles pass straight through you while it lasts ({{secs:config/mysticism/ability/skill/unique_config.toml|Phaser.intangibilityDuration}} s). Phaser triggers it by itself when you're hit (if it's off cooldown), or you can activate it. It then goes on a {{cfg:config/mysticism/ability/skill/unique_config.toml|Phaser.intangibilityActiveCooldown}} s cooldown. Void damage and creative players still get through.

## mysticism:lightning_mode
Lightning Mode, a transformation. It gives **+12** attack damage and **+0.2** movement speed. When it ends your current magicule and aura are **halved**, and you get the transformation hangover: {{link:minecraft:weakness}} II, {{link:tensura:fragility}} II and {{link:tensura:paralysis}} I for 10 minutes. Only one transformation can be active at a time.

## mysticism:marked_for_death
You take **double** damage per level (×2 at level I, ×4 at level II). Captivator's Unveil inflicts it for 10 seconds.

## mysticism:pay_it_forward
Provider's gift of speed. It gives movement speed and step height that grow with level: +0.1 speed and +0.5 step at level I, up to +0.5 speed and +3 step height at level V. It drains the Provider's energy every second and ends when that runs out. Provider and its halo give it.

## mysticism:pressure
Kyurem's pressure. Your skills cost **{{cfg:config/mysticism/ability/skill/unique_config.toml|Kyurem.pressureCostMultiplier}}×** as much magicule and aura. Anyone who hits a Kyurem user gets it for {{cfg:config/mysticism/ability/skill/unique_config.toml|Kyurem.pressureEffectDuration}} s.

## mysticism:provider_boost
Provider's generosity boost for creatures: **+{{cfg:config/mysticism/ability/skill/unique_config.toml|Provider.generosityEntitySpeedBoost}}×** movement speed, **+{{cfg:config/mysticism/ability/skill/unique_config.toml|Provider.generosityEntityStepHeightBoost}}** step height, and every hit it deals is multiplied by **{{cfg:config/mysticism/ability/skill/unique_config.toml|Provider.generosityEntityDamageBoost}}**.

## mysticism:reducer_holy_coat
Reducer's Emancipation: a holy coating. It gives +1 physical resistance degradation, and each melee hit adds a second **holy** hit worth **{{cfg:config/mysticism/ability/skill/unique_config.toml|Reducer.emancipationMultiplier}}×** your attack damage. It costs {{cfg:config/mysticism/ability/skill/unique_config.toml|Reducer.emancipationMaintainCost}} energy every second and ends when you can't pay. Press Reducer again to turn it off.

## mysticism:reducer_purity_edge
Reducer's Purity Edge, a one-shot holy strike. It gives +1 resistance degradation, and your **next melee hit** deals holy damage equal to **{{pct:config/mysticism/ability/skill/unique_config.toml|Reducer.purityEdgeDamagePercentage}}** of the target's max health ({{pct:config/mysticism/ability/skill/unique_config.toml|Reducer.purityEdgeDamagePercentageMastered}} mastered), which uses it up. If you don't land a hit within {{secs:config/mysticism/ability/skill/unique_config.toml|Reducer.purityEdgeRecoilTime}} s ({{secs:config/mysticism/ability/skill/unique_config.toml|Reducer.purityEdgeRecoilTimeMastered}} s mastered), it backfires and you take **{{pct:config/mysticism/ability/skill/unique_config.toml|Reducer.purityEdgeRecoil}}** of your own max health ({{pct:config/mysticism/ability/skill/unique_config.toml|Reducer.purityEdgeRecoilMastered}} mastered) as holy damage.

## mysticism:revenants_horror
Relapse's Revenant mode. While it lasts, your skills **cost no magicule**. When it ends you drop out of flight unless Gravity Domination is toggled on.

## mysticism:rupturing
Ruptured veins. Every second it deals damage equal to **5%** of your max health per level. Butcher's Rupture inflicts level II with no time limit. Butcher's hits also inflict it: it lasts forever on targets without regeneration, 2 minutes with Self Regeneration, 1 minute with Ultraspeed Regeneration and 15 seconds with Infinite Regeneration.

## mysticism:sanctifying_light
Relapse's Whole mode ({{cfg:config/mysticism/ability/skill/intrinsic_config.toml|Relapse.gimelDurationHoly}} s). Each of your hits also deals extra holy damage based on your race: **{{cfg:config/mysticism/ability/skill/intrinsic_config.toml|Relapse.gimelDamageWhole}}** as a Whole, **{{cfg:config/mysticism/ability/skill/intrinsic_config.toml|Relapse.gimelDamageAscended}}** as an Ascended and **{{cfg:config/mysticism/ability/skill/intrinsic_config.toml|Relapse.gimelDamageExcelsius}}** as a Divine Excelsius. It ends early once its hits are used up.

## mysticism:severed_arm
A severed arm, from Butcher's butchering. Your attack damage and attack speed drop by **50%** at level I and to **zero** from level II. Your skill cooldowns are also **doubled** while it lasts.

## mysticism:severed_leg
A severed leg, from Butcher's butchering. Your movement speed, step height and jump strength drop by **50%** at level I and to **zero** from level II.

## mysticism:stagnate
Stopped in time by Stagnator's aura. You can't move at all (players are held in place, mobs lose their AI), your attack damage and speed, jumping, reach, swimming and gliding drop to **zero**, and you can't use items or right-click blocks.

## mysticism:stillness
Your skills **cost no magicule or aura** while it lasts. Eternal Domain gives it.

## mysticism:tailed_beast_cloak
Jinchuriki's chakra cloak. Its bonuses grow with level:

| Level | Attack damage | Armor | Movement speed |
|---|---|---|---|
| I | +9 | +5 | +0.04 |
| II | +15 | +10 | +0.08 |
| III | +30 | +20 | +0.12 |
| IV | +36 | +35 | +0.15 |
| V+ | +45 | +60 | +0.18 |

It drains Jinchuriki's energy every second and ends when that runs out.

## mysticism:unstable_requiem
Relapse's Divine Excelsius mode. You **can't be hurt at all** while it lasts ({{cfg:config/mysticism/ability/skill/intrinsic_config.toml|Relapse.alephNullExcelsiusInvincibility}} s). When it ends you **explode**: a 15-block magic explosion that deals 250 damage (50 to the outer area). A mob with this effect is destroyed by its own explosion.

<!-- kind: -->

## mysticism:elemental_realm
The realm of spirits and elementals, made of seven biomes, one per element: Fire, Water, Earth, Wind, Space, Light and Darkness. It's always noon and beds don't work. It counts as a spiritual world: ambient magicule is **100,000** higher than normal and refills twice as fast, and spirit-form creatures don't lose magicule here.

**Getting there:**

- From Tensura's {{link:dimension/tensura:labyrinth}}: fly up to between **Y 158 and 210** and you're pulled into the Elemental Realm, with a few seconds of Slow Falling.
- {{link:race/mysticism:lesser_elemental}} and {{link:race/mysticism:lesser_angel}} players respawn here.

**Getting out:**

- Fall below **Y -60** and you drop into the Labyrinth (at 17, 109, 683).
- Elemental Realm Portals lead to the Overworld. They sit in portal structures in the Wind, Earth and Darkness biomes (each kind is spread about 3,200 blocks apart, so they are rare). A portal in the Overworld or the Labyrinth would lead back here, but portals only generate inside the realm.

The {{link:entity/mysticism:memoires}} can spawn anywhere in the realm. If it falls below Y -60 it's teleported back up to Y 150.

## mysticism:kamui_dimension
The pocket world of the {{link:skill/mysticism:phaser}} skill, a dark, empty land where it's always noon.

**Getting in and out:** use Phaser's Authority of the Gods mode while holding **Shift** and keep it held for {{secs:config/mysticism/ability/skill/unique_config.toml|Phaser.kamuiWarpTicks}} s (half that once mastered; bigger bodies take longer). It costs {{cfg:config/mysticism/ability/skill/unique_config.toml|Phaser.kamuiCost}} magicule and has a {{cfg:config/mysticism/ability/skill/unique_config.toml|Phaser.kamuiCooldown}} s cooldown. Do it again inside Kamui to go back to the dimension you came from. Falling below **Y -60** in Kamui drops you into the Overworld.

Distances in Kamui are **10×** shorter than in the Overworld (the Nether is 8×), so it works as a shortcut: walk 100 blocks inside and you come out 1,000 blocks away.

Once Phaser is mastered, charging it without Shift while looking at a creature moves that creature. Inside Kamui it throws the creature out to the Overworld. Outside, the code is meant to pull the creature in, but in this version it moves **you** into Kamui at the creature's position instead.

## mysticism:kamui_biome
{{auto}} It's the only biome of the {{link:dimension/mysticism:kamui_dimension}}.

## mysticism:fire_biome
{{auto}}

Ambient magicule **+3,500**, and magicule refills a little faster. Now and then 1 to 3 extra Blazes appear on the surface.

## mysticism:water_biome
{{auto}}

Ambient magicule **+1,500**, and magicule refills a little faster.

## mysticism:earth_biome
{{auto}}

Ambient magicule **+500**, and magicule refills a little faster. Earth portal structures (a way back to the Overworld) generate here.

## mysticism:wind_biome
{{auto}}

Ambient magicule **+2,500**, and magicule refills a little faster. Lightning strikes at random around players here, and each strike has a **10%** chance to drop {{link:mysticism:lightning_essence}}. Now and then 1 to 3 extra Breezes appear on the surface. Wind portal structures (a way back to the Overworld) generate here.

## mysticism:space_biome
{{auto}}

Ambient magicule **+3,500**, and magicule refills a little faster.

## mysticism:light_biome
{{auto}}

Ambient magicule **+1,500**, and magicule refills a little faster.

## mysticism:darkness_biome
{{auto}}

Ambient magicule **+500**, and magicule refills a little faster. Darkness portal structures (a way back to the Overworld) generate here.

<!-- kind: items -->

## mysticism:axiom, mysticism:waltz
**Axiom** and **Waltz** are a matched pair of Hihi'irokane long swords (30,000 durability) carried by {{link:entity/mysticism:memoires}}. Waltz's hits give the target {{link:effect/tensura:chill}} III for 10 seconds. The {{link:skill/mysticism:repeater}} skill has a storehouse that holds the pair: use it with Axiom in your main hand and Waltz in your off hand to put them away, and again to draw both at once.

{{auto}}

## mysticism:ritual_scythe
The scythe of the {{link:skill/mysticism:spiritualist}} skill, which summons it into your hand. It deals no normal damage: a fully charged swing hurts the target's **spiritual health** directly for 30 up to 1,500 (scaling with your soul points, maxing at 50,000,000), and a weaker swing does a tenth of that.

{{auto}}

<!-- kind: mobs -->

## mysticism:memoires
**Memoires**, a boss of the {{link:dimension/mysticism:elemental_realm}}. It spawns naturally (rarely) in the realm's biomes, wielding {{link:mysticism:axiom}} and {{link:mysticism:waltz}}. If it falls below Y -60 it's teleported back up. Slaying it is one of the requirements to evolve into {{link:race/mysticism:divine_inferius}}.

{{auto}}

<!-- kind: structures -->

## mysticism:elemental_realm/dark_portal_big, mysticism:elemental_realm/earth_portal, mysticism:elemental_realm/wind_portal
A portal shrine in the {{link:dimension/mysticism:elemental_realm}} (in its Darkness, Earth or Wind biome), holding an Elemental Realm Portal that leads back to the Overworld.

{{auto}}

<!-- kind: blocks -->

## mysticism:ice_ore
The source of {{link:mysticism:ice_essence}}. It generates inside the ice of vanilla **Ice Spikes** biomes (between Y 55 and 100) and in the frozen blobs of the Elemental Realm's {{link:biome/mysticism:water_biome}}. Fortune gives more Ice Essence, and Silk Touch keeps the ore.

{{auto}}
