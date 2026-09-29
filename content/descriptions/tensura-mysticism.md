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
