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
