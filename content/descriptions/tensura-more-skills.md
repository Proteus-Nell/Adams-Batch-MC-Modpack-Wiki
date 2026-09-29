# TensuraMoreSkills: what things do

Written from the mod's code (TensuraMoreSkills 0.0.4.9.2). Each `## id` section becomes the "What it does" part of that entry's page.
"Per level" means the value grows with the effect level. Most time effects come from the Istaroth skill, which applies them at high levels (often IV to VIII), so their slows usually stop you completely. While an Istaroth user is nearby, its Time Tax also hurts enemies that are moving or carrying any of these time effects.

<!-- kind: effects -->

## tensuramoreskills:albis_diamond_dust
Glittering frost from Albis Vina. It slows you by **8%** per level, and while it lasts, the Albis Vina user's water and ice attacks deal **×{{cfg:config/tensuramoreskills-grand.toml|albis_vina.diamond_dust.diamondDustWaterIceDamageMultiplier}}** damage to you (×{{cfg:config/tensuramoreskills-grand.toml|albis_vina.diamond_dust.diamondDustWaterIceDamageMultiplierMastered}} once mastered). Albis Vina applies it for {{secs:config/tensuramoreskills-grand.toml|albis_vina.diamond_dust.diamondDustDurationTicks}} s.

## tensuramoreskills:borrowed_seconds
Time borrowed from you. Per level: **-65%** magicule, aura and spiritual health regeneration. Istaroth's Borrowed Seconds inflicts it.

## tensuramoreskills:causality_loop
Stuck repeating the same moment. Per level: **-95%** movement and flying speed and **-75%** attack speed. Istaroth's Twenty-Second Loop inflicts it at level V.

## tensuramoreskills:condemned_repeat
Condemned to repeat. Per level: **-65%** movement and flying speed. Istaroth's Condemned Repeat inflicts it at level V.

## tensuramoreskills:delayed_verdict
A sentence waiting to land. Per level: **-35%** magicule and aura regeneration. Istaroth's Delayed Verdict inflicts it at level V.

## tensuramoreskills:eternal_moment
Istaroth's own time blessing. Per level: **+12%** movement speed, **+18%** attack speed and **+0.25** chant speed. While Istaroth's Eternal Moment runs, your other buffs keep getting extended.

## tensuramoreskills:event_silence
Events around you are silenced. Per level: **-55%** movement speed, **-95%** attack and chant speed and **-65%** magicule and aura regeneration. Istaroth's ultimate techniques inflict it.

## tensuramoreskills:future_exile
Exiled from the present. Your movement, flying speed and attack speed drop to **zero**. Istaroth's banishment inflicts it until you return.

## tensuramoreskills:future_rejection
Your future is denied. Per level: **-80%** melee and projectile dodge chance and less dodge invulnerability, so you can hardly dodge anything. Istaroth applies it to enemies who threaten its user and through many of its techniques.

## tensuramoreskills:life_seizure
Naberius's life siphon. Per level: **-45%** max health, **-55%** armor, **-75%** knockback resistance, **-95%** magicule regeneration, **-85%** aura and spiritual health regeneration, **no** presence concealment and **no** chanting, and spells cost more. (The code also describes draining you each second and pulling you toward Naberius's summons, but that part never runs in this version because of how the effect is set up.) Naberius inflicts it.

## tensuramoreskills:naberius_vision
Naberius's sight. It gives **+1** presence sense, **+10** presence sense radius, **+4** heat sense radius, **+100** analysis level and **+2** analysis distance, **+1** chant speed, **+0.25** resistance degradation, **+20%** dodge negation, and spells cost **20% less**. Naberius keeps it on its user. (Its code also grants Future Vision and energy over time, but that part never runs in this version.)

## tensuramoreskills:naberius_will
Naberius's will to live. It gives **+75%** max health, **+45%** attack damage, **+40** armor, **+0.5** knockback resistance, **+150%** magicule and aura regeneration, **+75** spiritual health regeneration and better dodging. Naberius keeps it on its user. (Its code also describes emergency heals at low health, but that part never runs in this version.)

## tensuramoreskills:object_permanence
Frozen as an object in time. Your movement, flying speed and attack speed drop to **zero**, you get full knockback resistance and your spiritual health doesn't regenerate. Istaroth's Object Permanence inflicts it at level IV (VI mastered).

## tensuramoreskills:organ_decay
Rotting organs. Per level: **-75%** max health, **-95%** attack damage, **-50%** armor, **-25%** movement speed, **-35%** attack speed, **-65%** knockback resistance and magicule and aura regeneration, **-75%** spiritual health regeneration and dodge chances, and spells cost **75%** more. (The code also describes damage over time, but that part never runs in this version.) Naberius's Organ Failure and its domain inflict it.

## tensuramoreskills:past_burial
The past buried with you. Per level: **-85%** attack speed and **-75%** chant speed. Nothing in the current version of the mod applies it.

## tensuramoreskills:stillness_of_the_king
Istaroth's kingly stillness. Per level: **+40** armor and full knockback resistance, but your spiritual health doesn't regenerate. Istaroth gives it at level III (V mastered).

## tensuramoreskills:temporal_screen
A visual marker used by Istaroth's time stops: it shows the time-stop screen effect. It has no gameplay effect of its own, and Istaroth's duration stealing skips it.

## tensuramoreskills:temporal_stutter
Time skipping around you. Per level: **-70%** movement and flying speed, **-65%** attack speed and **-55%** chant speed. Istaroth applies it through most of its techniques.

## tensuramoreskills:timeline_verdict
Judged by the timeline. Per level: **-85%** movement, flying, attack and chant speed and **-85%** magicule, aura and spiritual health regeneration. Istaroth's verdict techniques inflict it.

## tensuramoreskills:world_of_still_seconds
The world stands still. Per level: **-98%** movement, flying and attack speed and **-90%** chant speed. Istaroth's World of Still Seconds and its Doom Tornado inflict it.

<!-- kind: -->

## tensuramoreskills:asmoday_prison_realm
The dark, flat void that {{link:skill/tensuramoreskills:asmoday}}'s **Five-Hundred-Year Closed Space** seals players into. Only players can be sealed.

**How someone ends up here:** the Asmoday user looks at a player within {{cfg:config/tensuramoreskills-grand.toml|asmoday.prison_realm_activation.prisonRealmRange}} blocks ({{cfg:config/tensuramoreskills-grand.toml|asmoday.prison_realm_activation.prisonRealmRangeMastered}} mastered) and holds the ability for **{{cfg:config/tensuramoreskills-grand.toml|asmoday.prison_realm_activation.prisonRealmHoldSeconds}} seconds**. The target is slowed while it charges, and switching targets sets the charge back. When it finishes, the target is locked in a bedrock box of their own in this dimension, and the user gets a **Prison Cube**, the only key. A user can hold one prisoner at a time.

**While sealed:**

- The prisoner can't die or be hurt: they're healed to full every tick, kept topped up with {{cfg:config/tensuramoreskills-grand.toml|asmoday.prison_realm_effects.prisonProtectionAbsorption}} absorption, and can't get more than {{cfg:config/tensuramoreskills-grand.toml|asmoday.prison_realm_box.prisonMaxDistanceFromCenter}} blocks from the center.
- They're kept under {{link:effect/tensura:spatial_blockade}}, {{link:effect/tensura:magic_interference}}, {{link:effect/tensura:movement_interference}} and {{link:effect/tensura:energy_blockade}} at high levels.
- Logging out doesn't help: they're put back in the box when they log in.
- Every {{secs:config/tensuramoreskills-grand.toml|asmoday.prison_realm_upkeep.prisonPayIntervalTicks}} s the user pays **{{cfg:config/tensuramoreskills-grand.toml|asmoday.prison_realm_upkeep.prisonMagiculeDrain}}** magicule (×{{cfg:config/tensuramoreskills-grand.toml|asmoday.prison_realm_upkeep.prisonMasteredDrainMultiplier}} once mastered), or {{cfg:config/tensuramoreskills-grand.toml|asmoday.prison_realm_upkeep.prisonAuraDrain}} aura if they're short. Each missed payment costs the prison {{cfg:config/tensuramoreskills-grand.toml|asmoday.prison_realm_upkeep.prisonDestabilizeOnFail}}% stability, and at 0% it collapses.

**Release:** using the Prison Cube sends the prisoner back to where they were sealed. They're also thrown out, with brief {{link:effect/tensura:movement_interference}}, if the user dies or forgets Asmoday, if the dropped cube burns, falls into lava or into the void, or if the prison collapses.

The prison is only tracked while the server is running, so after a restart the prisoner is no longer held, healed or released by the cube, and has to get out of the box another way.

## tensuramoreskills:avalon
The **Kingdom of Avalon**, a sunlit dueling ground made by {{link:skill/tensuramoreskills:avalon_god_of_eternal_kingdom}}.

**How you get here:** use the Kingdom of Avalon mode while looking at a living enemy within {{cfg:config/tensuramoreskills-grand.toml|avalon_god_of_eternal_kingdom.kingdom_target_range}} blocks. It costs {{cfg:config/tensuramoreskills-grand.toml|avalon_god_of_eternal_kingdom.kingdom_cost}} magicule and has a {{secs:config/tensuramoreskills-grand.toml|avalon_god_of_eternal_kingdom.kingdom_cooldown_ticks}} s cooldown. You and the target are pulled into an arena of your own, facing each other 22 blocks apart.

**Inside:**

- Neither of you can leave the arena (about 62 blocks across from the center); stepping out puts you back in.
- Every half second, everyone within 70 blocks who isn't the user or their ally gets {{link:effect/tensura:silence}}, mobs also get {{link:effect/tensura:anti_skill}}, and toggled skills are switched off every second.
- Avalon's Royal Laws can only be declared here.

It ends after {{secs:config/tensuramoreskills-grand.toml|avalon_god_of_eternal_kingdom.kingdom_duration_ticks}} s, when either fighter dies or leaves, or when the user uses the mode again while sneaking. Both are then sent back to where they were.

## tensuramoreskills:paths
The **Paths**, a world of eternal midnight guarded by {{link:entity/tensuramoreskills:feldway}}.

**Getting there:** find a {{link:structure/tensuramoreskills:paths_gate}} (it generates in plains and sunflower plains) and stand in its portal for **5 seconds**. You need at least **5,000,000 max EP**, or the portal refuses you. Arriving builds a return portal at least at Y 110 above the spot you came from. Standing in it for 5 seconds takes you back to the gate you entered by.

**Summoning Feldway:** build a 3 × 3 floor of {{link:tensura:pure_magisteel_block}}, put a {{link:tensura:mithril_block}} on the center with two blocks of air above it, and right-click the Mithril Block. It's used up and Feldway appears (only one at a time within 96 blocks). This only works in the Paths.

## tensuramoreskills:avalon_plains
{{auto}} It's the only biome of the {{link:dimension/tensuramoreskills:avalon}}.

## tensuramoreskills:paths_plains
{{auto}} It's the only biome of the {{link:dimension/tensuramoreskills:paths}}.
