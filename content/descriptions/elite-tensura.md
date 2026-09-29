# Elite Tensura: what things do

Written from the mod's code (Elite Tensura 1.0.2.2). Each `## id` section becomes the "What it does" part of that entry's page.
"Per level" means the value grows with the effect level.

<!-- kind: effects -->

## elitetensura:bound
Bound in Hephaestus's chains. Per level: **-30%** attack damage, **-30%** armor and **-80%** movement speed. Hephaestus's Chains inflict level {{cfg:config/tensura/EliteTensura/UltimateSkillConfig.toml|HephaestusSkill.chainsAmplifier}} + 1 for {{secs:config/tensura/EliteTensura/UltimateSkillConfig.toml|HephaestusSkill.chainsDurationTicks}} s.

## elitetensura:celestial_mark
A mark left by the {{link:elitetensura:astral_edge}}. It does nothing by itself, but the Astral Edge's step ability teleports you behind the nearest marked enemy within {{cfg:config/tensura/EliteTensura/WeaponConfig.toml|AstralEdgeWeapon.stepRange}} blocks and strikes harder against it. Lasts {{secs:config/tensura/EliteTensura/WeaponConfig.toml|AstralEdgeWeapon.markDuration}} s.

## elitetensura:cycle_armed
Ouroboros's rebirth is ready. While you have it, dying doesn't end things: when you respawn you're sent back to where you died with **{{pct:config/tensura/EliteTensura/UltimateSkillConfig.toml|OuroborosSkill.rebirthHealthFraction}}** of your health, a few seconds of invulnerability, and {{link:elitetensura:cycle_debt}}. It doesn't work against severance or soul-destroying damage. Arming it costs half your max magicule and lasts {{secs:config/tensura/EliteTensura/UltimateSkillConfig.toml|OuroborosSkill.cycleArmedDurationTicks}} s.

## elitetensura:cycle_debt
The price of an Ouroboros rebirth. Per level: **-15%** max health and max magicule. Each rebirth while you still carry it raises its level by one. Lasts {{secs:config/tensura/EliteTensura/UltimateSkillConfig.toml|OuroborosSkill.cycleDebtDurationTicks}} s.

## elitetensura:dimensional_mark
A mark left by the {{link:elitetensura:void_edge}}. It does nothing by itself, but the Void Edge's teleport ability jumps you behind the nearest marked enemy within {{cfg:config/tensura/EliteTensura/WeaponConfig.toml|VoidEdgeWeapon.teleportRange}} blocks and strikes harder against it. The Astral Edge's big attack consumes the mark for **×{{cfg:config/tensura/EliteTensura/WeaponConfig.toml|AstralEdgeWeapon.purgeBonus}}** damage. Lasts {{secs:config/tensura/EliteTensura/WeaponConfig.toml|VoidEdgeWeapon.markDuration}} s.

## elitetensura:eternal_renewal
Shows that Ouroboros is toggled on. It has no effect of its own.

## elitetensura:fenrir_sword_effect
Frostbite from the {{link:elitetensura:fenrir_sword}}. Per level: **-20%** movement and swim speed, **-33%** jump strength, **-10%** attack speed and **-30%** mining speed. From level II you can't sprint. Abnormal Condition Nullification, while toggled on, counts it as one level lower. The Fenrir Sword applies level V on hit.

## elitetensura:fractured_reality
Reality cracking around you, from the {{link:elitetensura:void_edge}}'s fracture ability. You're slowed by **{{pct:config/tensura/EliteTensura/WeaponConfig.toml|VoidEdgeWeapon.fractureSlow}}** per level, take **{{cfg:config/tensura/EliteTensura/WeaponConfig.toml|VoidEdgeWeapon.fractureTickDamage}}** damage per level every second, and every hit you take is multiplied by **{{cfg:config/tensura/EliteTensura/WeaponConfig.toml|VoidEdgeWeapon.fractureDamageTakenMultiplier}}**. The Astral Edge's big attack consumes it for bonus damage.

## elitetensura:kaioken
Kaioken, a transformation with four tiers (the tier you can reach depends on your EP: {{cfg:config/tensura/EliteTensura/IntrinsicSkillConfig.toml|Kaioken.mode1EP}}, {{cfg:config/tensura/EliteTensura/IntrinsicSkillConfig.toml|Kaioken.mode2EP}} and {{cfg:config/tensura/EliteTensura/IntrinsicSkillConfig.toml|Kaioken.mode3EP}} for tiers II to IV).

- Max magicule and aura grow by **+{{cfg:config/tensura/EliteTensura/IntrinsicSkillConfig.toml|Kaioken.mode0EnergyMultiplier}}×** at tier I, +{{cfg:config/tensura/EliteTensura/IntrinsicSkillConfig.toml|Kaioken.mode1EnergyMultiplier}}× at II, +{{cfg:config/tensura/EliteTensura/IntrinsicSkillConfig.toml|Kaioken.mode2EnergyMultiplier}}× at III and +{{cfg:config/tensura/EliteTensura/IntrinsicSkillConfig.toml|Kaioken.mode3EnergyMultiplier}}× at IV (×2, ×3, ×10 and ×20 by default), and both are refilled when it starts.
- Per tier: **+{{cfg:config/tensura/EliteTensura/IntrinsicSkillConfig.toml|Kaioken.attackBonusPerTier}}** attack damage, **+{{cfg:config/tensura/EliteTensura/IntrinsicSkillConfig.toml|Kaioken.armorBonusPerTier}}** armor and **+{{cfg:config/tensura/EliteTensura/IntrinsicSkillConfig.toml|Kaioken.speedBonusPerTier}}** movement speed.
- Every second it burns **{{cfg:config/tensura/EliteTensura/IntrinsicSkillConfig.toml|Kaioken.healthDrainPerTick}}** health per tier (never below {{pct:config/tensura/EliteTensura/IntrinsicSkillConfig.toml|Kaioken.minHealthFraction}} of your max) and **{{cfg:config/tensura/EliteTensura/IntrinsicSkillConfig.toml|Kaioken.energyDrainPerTick}}** magicule and aura per tier.

When it ends, your magicule and aura are divided back down, and you're exhausted: {{link:minecraft:weakness}} II, {{link:tensura:fragility}} II and {{link:tensura:paralysis}} I for {{secs:config/tensura/EliteTensura/IntrinsicSkillConfig.toml|Kaioken.exhaustionDurationTicks}} s. You can't use Kaioken again while you have Fragility.

## elitetensura:rend
Torn armor. **-2** armor per level. Weapons with the {{link:elitetensura:rending}} enchantment inflict it for 3 seconds (level I to III, matching the enchantment level).

## elitetensura:starlight_judgment
Judged by starlight, from the {{link:elitetensura:astral_edge}}'s dawn ability. Your attack damage drops by **{{pct:config/tensura/EliteTensura/WeaponConfig.toml|AstralEdgeWeapon.judgmentAttackDown}}** per level, you take **{{cfg:config/tensura/EliteTensura/WeaponConfig.toml|AstralEdgeWeapon.judgmentTickDamage}}** damage per level every second, and every hit you take is multiplied by **{{cfg:config/tensura/EliteTensura/WeaponConfig.toml|AstralEdgeWeapon.judgmentDamageTakenMultiplier}}**.

<!-- kind: -->

## elitetensura:walpurgis_hall
The Council Hall where Demon Lords hold a **Walpurgis** banquet. Only players who count as Demon Lords can enter, and only while a banquet is running. The whole system can be switched off with the {{gamerule:ETWalpurgisEnabled}} gamerule.

**Calling a Walpurgis:** a Demon Lord uses a {{link:elitetensura:walpurgis_orb}}. A gate to the hall opens where they stand, and the other Demon Lords have **{{cfg:config/tensura/EliteTensura/WalpurgisConfig.toml|WalpurgisCore.CONVENE_WINDOW_MINS}} minutes** to answer by using their own orb. If at least **{{cfg:config/tensura/EliteTensura/WalpurgisConfig.toml|WalpurgisCore.MIN_CONVENERS}}** answer, the banquet convenes; otherwise it's cancelled. Demon Lords get in by stepping into a gate or with `/etwalpurgis teleport`, and their nation gains reputation for attending.

**How a banquet runs:**

1. **Agenda** ({{cfg:config/tensura/EliteTensura/WalpurgisConfig.toml|WalpurgisCore.AGENDA_PHASE_MINS}} minutes): Demon Lords submit motions: Territorial Claim, Declare Enemy, Declare Neutral, New Demon Lord Recognition, Expel Member, Treaty or Free Topic. If nobody submits one, the banquet dissolves.
2. **Vote** ({{cfg:config/tensura/EliteTensura/WalpurgisConfig.toml|WalpurgisCore.VOTE_PHASE_MINS}} minutes per motion, extended by {{cfg:config/tensura/EliteTensura/WalpurgisConfig.toml|WalpurgisCore.VOTE_EXTENSION_MINS}} minutes while votes are missing, up to {{cfg:config/tensura/EliteTensura/WalpurgisConfig.toml|WalpurgisCore.VOTE_HARD_CAP_MINS}} minutes): vote with `/etwalpurgis vote aye|nay|abstain`. A {{link:elitetensura:walpurgis_seal}} holder's vote counts {{cfg:config/tensura/EliteTensura/WalpurgisConfig.toml|Seal.voteWeight}} times.
3. **Combat Clause:** after a tied vote the council waits {{cfg:config/tensura/EliteTensura/WalpurgisConfig.toml|WalpurgisCore.DUEL_INVITE_SECONDS}} s for a challenge (`/etwalpurgis challenge <name>`). The defender has {{cfg:config/tensura/EliteTensura/WalpurgisConfig.toml|WalpurgisCore.ACCEPT_WINDOW_SECONDS}} s to accept, and the duel (first to fall to half a heart loses, at most {{cfg:config/tensura/EliteTensura/WalpurgisConfig.toml|WalpurgisCore.MAX_DUEL_MINS}} minutes) settles the motion. No challenge, a timeout or a disconnect means the motion fails.

Passed motions take effect right away: territorial claims, public enemies and treaties are recorded (`/etwalpurgis territories`, `enemies` and `treaties` list them). When the banquet ends, everyone in the hall is sent back and the gates close. The council then rests for **{{cfg:config/tensura/EliteTensura/WalpurgisConfig.toml|WalpurgisCore.COOLDOWN_MINS}} minutes** before another Walpurgis can be called.

## elitetensura:walpurgis_void
{{auto}} It's the only biome of the {{link:dimension/elitetensura:walpurgis_hall}}.

<!-- kind: items -->

## class:com.johnadmin.elitetensura.items.armor.AetherforgedArmorItem
A piece of **Aetherforged Plate**. Wearing all four pieces reduces the damage you take by up to **{{cfg:config/tensura/EliteTensura/MiscConfigs.toml|AETHERFORGED_PLATE.maxReductionPercent}}%**, scaling with your EP: you get the full reduction at 10,000,000 max EP (half of it at 5,000,000, and so on).

{{auto}}

## elitetensura:fenrir_sword
A frost sword. Every hit gives the target {{link:effect/elitetensura:fenrir_sword_effect}} V for 3 seconds. When you swing at a creature, every non-ally within 5 blocks gets Fenrir's frost V for 5 seconds and water within 2 blocks of the target freezes into ice. Repair it with Stellar Gold Coins.

{{auto}}

## elitetensura:chronicle
Opens your **Chronicle** in the Elite Tensura codex: your daily objectives and season progress. Each completed daily gives {{cfg:config/tensura/EliteTensura/SeasonConfig.toml|Chronicle.dailyCrateCount}} {{cfg:config/tensura/EliteTensura/SeasonConfig.toml|Chronicle.dailyCrateId}} crate key, and you get {{cfg:config/tensura/EliteTensura/SeasonConfig.toml|Chronicle.dailiesPerDay}} dailies per real day.

{{auto}}

## elitetensura:common_key, elitetensura:rare_key, elitetensura:elite_key
A key for the matching Elite Tensura **crate** ({{link:elitetensura:common_crate}}, {{link:elitetensura:rare_crate}} or {{link:elitetensura:elite_crate}}): use it on the crate to open it for a random reward. Chronicle dailies give Common keys.

{{auto}}

## elitetensura:potential_catalyst
Unlocks the hidden potential of a forged item. Hold a forged item (from the Forge Station) in your **off hand** and use the catalyst: if the item's potential is at least 30%, it gains a permanent bonus to its main stat (attack damage for weapons, armor for armor, max health otherwise) equal to its potential × {{cfg:config/tensura/EliteTensura/CraftingConfigs.toml|POTENTIAL_CATALYST.weakScale}} (weak, under 50%), × {{cfg:config/tensura/EliteTensura/CraftingConfigs.toml|POTENTIAL_CATALYST.moderateScale}} (moderate, 50 to 75%) or × {{cfg:config/tensura/EliteTensura/CraftingConfigs.toml|POTENTIAL_CATALYST.strongScale}} (strong, 75% and up). Moderate and strong unlocks also add **+{{cfg:config/tensura/EliteTensura/CraftingConfigs.toml|POTENTIAL_CATALYST.bonusHealth}}** max health, and a strong unlock gives you Luck for {{cfg:config/tensura/EliteTensura/CraftingConfigs.toml|POTENTIAL_CATALYST.strongLuckSeconds}} s. Calamity raids can drop them.

{{auto}}

## elitetensura:walpurgis_orb
Used to call a **Walpurgis** banquet (only Demon Lords can use it): see the {{link:dimension/elitetensura:walpurgis_hall}}.

{{auto}}

## elitetensura:walpurgis_seal
The mark of a Demon Lord recognised by the council. When a **New Demon Lord Recognition** motion passes at a Walpurgis, the recognised player gets a seal (on their next login if they're offline). It's soul-bound to its owner. While you carry your own seal, your magicule and aura regenerate **{{pct:config/tensura/EliteTensura/WalpurgisConfig.toml|Seal.magiculeRegenBonus}}** faster, and your Walpurgis votes count {{cfg:config/tensura/EliteTensura/WalpurgisConfig.toml|Seal.voteWeight}} times.

{{auto}}

<!-- kind: mobs -->

## elitetensura:lich_boss
The **Lich**, one of Elite Tensura's calamity bosses. Stats: {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|LichBoss.maxHealth}} health, {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|LichBoss.armor}} armor, {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|LichBoss.attackDamage}} attack damage. How it fights:

- It summons waves of {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|LichBoss.waveSizeMin}} to {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|LichBoss.waveSizeMax}} tethered minions (a new wave {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|LichBoss.waveCooldownSeconds}} s after the last one dies, from phase 2). While any minion is alive it takes only **{{pct:config/tensura/EliteTensura/CalamityConfig.toml|LichBoss.minionWallDamageMultiplier}}** of the damage.
- It heals for {{pct:config/tensura/EliteTensura/CalamityConfig.toml|LichBoss.siphonPercent}} of the damage it deals, and regenerates by draining the area's magicule.
- No single hit can take more than {{pct:config/tensura/EliteTensura/CalamityConfig.toml|LichBoss.hitCapPercent}} of its max health.
- Holy and fire damage hurt it **×{{cfg:config/tensura/EliteTensura/CalamityConfig.toml|LichBoss.holyFireVulnerability}}**.
- Once per fight, **Last Rites** lets it defy death.
- It only starts fights with players who have at least {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|LichBoss.targetEpGate}} max EP.

**Calamities:** every {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|CalamityCore.minIntervalHours}} to {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|CalamityCore.maxIntervalHours}} hours (when at least {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|CalamityCore.minQualifiedPlayers}} players with {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|CalamityCore.qualifyingPlayerEP}}+ max EP are online), Elite Tensura spawns a calamity boss with ×{{cfg:config/tensura/EliteTensura/CalamityConfig.toml|CalamityCore.hpMultiplier}} health and ×{{cfg:config/tensura/EliteTensura/CalamityConfig.toml|CalamityCore.damageMultiplier}} damage, usually on a Walpurgis territory claim. It's protected by a **resonance shield** that several different players must all hit within {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|CalamityCore.shieldBreakWindowSeconds}} s to shatter, which leaves it vulnerable for {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|CalamityCore.vulnerabilitySeconds}} s. No hit can deal more than {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|CalamityCore.maxDamagePerHit}} damage, its healing is cut to {{pct:config/tensura/EliteTensura/CalamityConfig.toml|CalamityCore.bossHealMultiplier}}, and it leaves after {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|CalamityCore.maxDurationMinutes}} minutes if nobody beats it. Everyone who dealt at least {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|CalamityCore.rewardContributionPercent}}% of its health gets a Rare crate key and the Calamity Slayer title, the top damage dealer an Elite key, and everyone who hurt it a Potential Catalyst.

{{auto}}

## elitetensura:gravebound_colossus
The **Gravebound Colossus**, a calamity boss that never moves: it fights everything within {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|GraveboundColossus.engageRange}} blocks. Stats: {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|GraveboundColossus.maxHealth}} health, {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|GraveboundColossus.armor}} armor, {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|GraveboundColossus.attackDamage}} attack damage.

- Three **Sigils** ({{cfg:config/tensura/EliteTensura/CalamityConfig.toml|GraveboundColossus.sigilHealth}} health each) protect it: while any stands, the Colossus takes only {{pct:config/tensura/EliteTensura/CalamityConfig.toml|GraveboundColossus.sigilBossDamageFraction}} of the damage and the rest hits a Sigil. Breaking all three leaves it **Exposed** for {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|GraveboundColossus.exposedSeconds}} s, taking ×{{cfg:config/tensura/EliteTensura/CalamityConfig.toml|GraveboundColossus.exposedDamageMultiplier}} damage.
- **Slam Shockwave** every {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|GraveboundColossus.slamCooldownSeconds}} s (a ring up to {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|GraveboundColossus.slamRadius}} blocks), and **Grave Spire** columns every {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|GraveboundColossus.spireCooldownSeconds}} s against ranged attackers.
- From phase 2: **Gravity Well** pulls everyone within {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|GraveboundColossus.wellRadius}} blocks, and **Sunder Zones** hurt anyone standing in them.
- Its attacks partly pierce resistances and barriers.
- If nobody fights it for {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|GraveboundColossus.enrageAfterSeconds}} s, it regenerates {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|GraveboundColossus.enrageRegenPercent}}% of its health per second.

**Calamities:** every {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|CalamityCore.minIntervalHours}} to {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|CalamityCore.maxIntervalHours}} hours (when at least {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|CalamityCore.minQualifiedPlayers}} players with {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|CalamityCore.qualifyingPlayerEP}}+ max EP are online), Elite Tensura spawns a calamity boss with ×{{cfg:config/tensura/EliteTensura/CalamityConfig.toml|CalamityCore.hpMultiplier}} health and ×{{cfg:config/tensura/EliteTensura/CalamityConfig.toml|CalamityCore.damageMultiplier}} damage, usually on a Walpurgis territory claim. It's protected by a **resonance shield** that several different players must all hit within {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|CalamityCore.shieldBreakWindowSeconds}} s to shatter, which leaves it vulnerable for {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|CalamityCore.vulnerabilitySeconds}} s. No hit can deal more than {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|CalamityCore.maxDamagePerHit}} damage, its healing is cut to {{pct:config/tensura/EliteTensura/CalamityConfig.toml|CalamityCore.bossHealMultiplier}}, and it leaves after {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|CalamityCore.maxDurationMinutes}} minutes if nobody beats it. Everyone who dealt at least {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|CalamityCore.rewardContributionPercent}}% of its health gets a Rare crate key and the Calamity Slayer title, the top damage dealer an Elite key, and everyone who hurt it a Potential Catalyst.

{{auto}}

## elitetensura:choir_heart, elitetensura:choir_voice
The **Hollow Choir**: a Heart ({{cfg:config/tensura/EliteTensura/CalamityConfig.toml|HollowChoir.heartMaxHealth}} health) surrounded by orbiting **Voices**. The Heart re-splits into new Voices at 66% and 33% health ({{cfg:config/tensura/EliteTensura/CalamityConfig.toml|HollowChoir.voicesPhase1}}, then {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|HollowChoir.voicesPhase2}}, then {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|HollowChoir.voicesPhase3}} Voices).

- While at least {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|HollowChoir.wardMinVoices}} Voices live, the **Choir Ward** deflects most direct damage from the Heart (only {{pct:config/tensura/EliteTensura/CalamityConfig.toml|HollowChoir.wardPassthroughFraction}} gets through). Damage you deal to a Voice also carries {{pct:config/tensura/EliteTensura/CalamityConfig.toml|HollowChoir.voiceTransferPercent}} over to the Heart.
- The Voices sing an aura within {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|HollowChoir.songRadius}} blocks that grows stronger the longer you stay in their line of sight.
- The Heart releases a **Dirge** pulse around itself every {{cfg:config/tensura/EliteTensura/CalamityConfig.toml|HollowChoir.dirgeCooldownSeconds}} s.

It's one of the calamity bosses Elite Tensura can pick, but this pack's calamity list doesn't include it, so it only appears if spawned by hand.

{{auto}}

## elitetensura:leviathan
The **Leviathan**, a sea-serpent raid boss made of a head and many body segments. A nation summons it with a Leviathan raid (paid from the nation treasury, once per season); it emerges after a countdown, and the raid is lost if it isn't killed in time. Break its plates to expose the head. It dives under at 75%, 50% and 25% health, healing part of its health each time.

{{auto}}

<!-- kind: enchantments -->

## elitetensura:vampiric
An Elite Tensura **engraving** for weapons (see below). Each hit heals you for **8% per level** of the damage dealt.

Engravings are applied to forged gear rather than found on the enchanting table: use an {{link:elitetensura:engraving_scroll}} while holding the forged item in your off hand, engrave it with {{link:skill/elitetensura:hephaestus}}, or let a legendary weapon earn them by slaying bosses.

{{auto}}

## elitetensura:voidpiercer
A weapon **engraving**: each hit deals **+1.5 damage per level**, plus **6% of the target's armor** per level, so it hits armored targets harder.

{{auto}}

## elitetensura:critical_strike
A weapon **engraving**: each hit has a **10% per level** chance to deal **×1.5** damage (+0.25 per level above I).

{{auto}}

## elitetensura:executioner
A weapon **engraving**: **+10% damage per level** against targets below 30% health.

{{auto}}

## elitetensura:soul_render
A weapon **engraving**: **+8% damage per level** against spiritual creatures.

{{auto}}

## elitetensura:stormbrand
A weapon **engraving**: each hit has a **10% per level** chance to arc lightning to the nearest other enemy within 4 blocks, dealing 30% of the hit's damage.

{{auto}}

## elitetensura:cleave
A weapon **engraving**: each hit also deals **25% per level** of its damage to every other enemy within 2 blocks of the target.

{{auto}}

## elitetensura:frostbrand
A weapon **engraving**: each hit gives the target Slowness (level I at Frostbrand I, up to IV), lasting 3 seconds +1 per level.

{{auto}}

## elitetensura:rending
A weapon **engraving**: each hit gives the target {{link:effect/elitetensura:rend}} (level = engraving level) for 3 seconds, stripping its armor.

{{auto}}

## elitetensura:keen_edge
A weapon **engraving**: **+0.75 attack damage per level**.

{{auto}}

## elitetensura:featherweight
A weapon **engraving**: **+0.15 attack speed per level**.

{{auto}}

## elitetensura:predators_mark
A weapon **engraving**: when you kill something with it, you gain an extra **5% per level** of the EP the kill gives.

{{auto}}

## elitetensura:prospector
A weapon **engraving**: when you kill a mob, there's a **10% per level** chance its drops (except tools and armor) are doubled.

{{auto}}

## elitetensura:regeneration
An **engraving** for anything with durability: while you hold or wear it, it repairs **1 durability per level** every second.

{{auto}}

## elitetensura:soulbound
An **engraving** for anything with durability: the item stays with you when you die and comes back when you respawn.

{{auto}}

## elitetensura:vitality
An armor **engraving**: **+2 max health per level**.

{{auto}}

## elitetensura:reinforced
An armor **engraving**: **+0.5 armor per level**.

{{auto}}

## elitetensura:toughened
An armor **engraving**: **+0.5 armor toughness per level**.

{{auto}}

## elitetensura:swiftness
An armor **engraving**: **+0.01 movement speed per level** (about +10% per level for a player).

{{auto}}

## elitetensura:magicule_conduit
An armor **engraving**: **+25% magicule regeneration per level**.

{{auto}}

## elitetensura:aura_conduit
An armor **engraving**: **+25% aura regeneration per level**.

{{auto}}

## elitetensura:featherfall
A boots **engraving**: **25% less fall damage per level** (it stacks with other protection up to the usual cap).

{{auto}}

<!-- kind: blocks -->

## elitetensura:forge_station_basic, elitetensura:forge_station_magisteel, elitetensura:forge_station_mythril, elitetensura:forge_station_dragonforge
Elite Tensura's **Forge**: right-click the station to pick a recipe and forge one-of-a-kind gear through a minigame (Hammer Timing, Rune Alignment, Magicule Flow, and Dragonfire Forging for the toughest recipes). The better you play, the better the **quality** of the result, which multiplies its stats:

| Quality | Stats | Durability |
|---|---|---|
| Poor | ×0.85 | ×0.9 |
| Common | ×1 | ×1 |
| Fine | ×1.1 | ×1.15 |
| Superior | ×1.25 | ×1.35 |
| Masterwork | ×1.45 | ×1.6 |
| Legendary | ×1.7 | ×2 |
| Mythical | ×2 | ×2.5 |

Legendary and Mythical are only reached through lucky **critical upgrades** ({{pct:config/tensura/EliteTensura/CraftingConfigs.toml|QUALITY.critUpgradeBaseChance}} base chance, more for a high minigame score). Forged gear can also carry **engravings**, and the station's Salvage button breaks forged items back down into part of their materials.

Make a Basic station from 8 iron ingots around an anvil. A station **upgrades itself** as you use it: Basic becomes Magisteel after {{cfg:config/tensura/EliteTensura/CraftingConfigs.toml|STATION_UPGRADE.basicToMagisteel}} crafts, Magisteel becomes Mithril after {{cfg:config/tensura/EliteTensura/CraftingConfigs.toml|STATION_UPGRADE.magisteelToMythril}} and Mithril becomes Dragonforge after {{cfg:config/tensura/EliteTensura/CraftingConfigs.toml|STATION_UPGRADE.mythrilToDragonforge}}. Higher tiers can forge everything the lower ones can. The Forge chapter of the Elite Tensura Codex has the full rules.

{{auto}}

## class:com.johnadmin.elitetensura.items.ability.CrateBlock
A loot crate. Right-click it while holding its key to open it: the key is used up and you win one random reward. **Hit it or right-click it with an empty hand** to preview every reward with its exact chance, for free.

| Crate | Opens with | Chance of a Rare or better reward |
|---|---|---|
| {{link:elitetensura:common_crate}} | {{link:elitetensura:common_key}} | about 5% |
| {{link:elitetensura:rare_crate}} | {{link:elitetensura:rare_key}} | about 29% |
| {{link:elitetensura:elite_crate}} | {{link:elitetensura:elite_key}} | about 62% |

The Common Crate has **pity**: after 15 opens in a row without a Rare-or-better reward, the next one is guaranteed to be Rare or better (keys don't count as a hit). Rare and Elite crates have no pity in this pack (`pityThresholds` in Elite Tensura's MiscConfigs.toml). Rewards include ores and ingots, spawn eggs, potions, Tensura gear, more keys and plushies (Common plushies in Common crates, Uncommon and Rare ones in Rare crates, Epic and Legendary ones in Elite crates). Epic and Legendary pulls set off fireworks.

{{auto}}

## class:com.johnadmin.elitetensura.items.plushie.PlushieCommon, class:com.johnadmin.elitetensura.items.plushie.PlushieUncommon, class:com.johnadmin.elitetensura.items.plushie.PlushieRare, class:com.johnadmin.elitetensura.items.plushie.PlushieEpic, class:com.johnadmin.elitetensura.items.plushie.PlushieLegendary
A collectible plushie. Place it as decoration (it has no collision) or wear it on your head. Plushies can't be crafted: they come from **crates** and from winning **chat trivia**. Each trivia win after your second gives a random plushie from your highest unlocked tier: Uncommon from 8 lifetime wins, Rare from 16, Epic from 25 and Legendary from 30.

{{auto}}

## elitetensura:nation_core
Your nation's heart. A Sovereign or Officer places it inside the nation's claims (one per nation). Members standing near it in their own land get bonus **magicule/aura regeneration and armor**; the aura reaches {{cfg:config/tensura/EliteTensura/NationConfig.toml|Core.auraRadiusChunks}} chunks at Tier 1 and goes quiet while the treasury is in debt. Upgrade it from the treasury up to Tier 4 for more health, reach and bonuses.

During an active war the enemy can **besiege** it: if it falls, they gain war score and part of your treasury, and the core is shattered and drops a tier until repaired. Sneak and right-click it with an empty hand for its status card. Forged at a Dragonforge station.

{{auto}}

## elitetensura:ley_nexus
A war objective. While a war between two nations is active, 1 to 3 Ley Nexus crystals rise on unclaimed land between them. Stand within 16 blocks to push its capture meter for your side (the side with more people there wins; about a minute of unopposed control captures it). Each minute one of your members stands in a nexus you hold earns your side 2 war points. They vanish when the war ends, and you can't place one yourself.

{{auto}}

## elitetensura:arena_anchor
The arena for Elite Tensura **tournaments** (1v1, 2v2 or nation-squad PvP brackets). Admins place and bind it; right-click it to join an announced tournament (or use `/ettournament join`). Nobody dies in a tournament match: a lethal blow benches you instead.

{{auto}}

## elitetensura:magic_ore_mother_rock
A crystal-growing rock. In magic-rich chunks, Magic Ore slowly turns into Mother Rock, and Mother Rock sprouts **Magic Ore crystal buds** on its open sides that grow Small → Medium → Large → Cluster. Each step uses up some of the chunk's magicule ({{cfg:config/tensura/EliteTensura/MagiculeWorld.toml|CRYSTAL_GROWTH.growthCostSmallBud}}, {{cfg:config/tensura/EliteTensura/MagiculeWorld.toml|CRYSTAL_GROWTH.growthCostMediumBud}}, {{cfg:config/tensura/EliteTensura/MagiculeWorld.toml|CRYSTAL_GROWTH.growthCostLargeBud}} and {{cfg:config/tensura/EliteTensura/MagiculeWorld.toml|CRYSTAL_GROWTH.growthCostCluster}}). All of this only happens when the `ETMagiculeWorldSystem` gamerule is on (it's off by default).

{{auto}}

## elitetensura:magic_ore_small_bud, elitetensura:magic_ore_medium_bud, elitetensura:magic_ore_large_bud, elitetensura:magic_ore_cluster
A Magic Ore crystal growing on {{link:elitetensura:magic_ore_mother_rock}}, like amethyst. It keeps growing while the chunk has enough magicule; mine the full **Cluster** for Magic Ore Shards.

{{auto}}
