# `config/tombstone-client.toml`

<small>[Corail Tombstone](../index.md) &rsaquo; [Configs](index.md)</small>

## `[alignment]`

Options related to player's alignment

| Option | Default | Range | Description |
|---|---|---|---|
| `points_free_soul_receptacle` | 50 | 0 to 500 | Points for freeing a soul in a receptacle [0..500\|default:50] |
| `points_plunder_player_grave` | -10 | -500 to 0 | Points for plundering a player's grave [-500..0\|default:-10] |
| `points_exorcism_zombie_villager` | 20 | 0 to 500 | Points for zombie villager exorcism [0..500\|default:20] |
| `points_zombify_villager` | -20 | -500 to 0 | Points for zombifying a villager [-500..0\|default:-20] |
| `points_kill_decreasing_alignment` | -10 | -500 to 0 | Points for killing some entities decreasing alignment [-500..0\|default:-10] |
| `points_kill_increasing_alignment` | 10 | 0 to 500 | Points for killing some entities increasing alignment [0..500\|default:10] |
| `points_tablet_of_cupidity` | -10 | -500 to 0 | Points for tablet of cupidity [-500..0\|default:-10] |
| `points_pray_of_protection` | 20 | 0 to 500 | Points for Pray of Protection [0..500\|default:20] |
| `points_earthly_garden` | 10 | 0 to 500 | Points for using a Potion of Earthly Garden [0..500\|default:10] |
| `points_kill_tamed_creature` | -10 | -500 to 0 | Points for killing one of your tamed creatures [-500..0\|default:-10] |

## `[client]`

Personal Options that can be edited even on server

| Option | Default | Range | Description |
|---|---|---|---|
| `show_magic_circle` | true |  | Shows the magic circles when using some items [false/true\|default:true] |
| `show_enhanced_tooltips` | true |  | Shows all the infos in the tooltip of items [false/true\|default:true] |
| `highlight` | true |  | Highlights the tomb from far when holding the key [false/true\|default:true] |
| `skip_respawn_screen` | false |  | Skips the Respawn Screen [false/true\|default:false] |
| `show_shield_particle` | true |  | Shows shield particles on villager [false/true\|default:true] |
| `enable_halloween_ghost` | true |  | Allows the ghost to appear around you during Halloween [false/true\|default:true] |
| `date_in_mc_time` | false |  | Shows only the elapsed minecraft days since the death on graves [false/true\|default:false] |
| `display_knowledge_message` | true |  | Display or not the messages of gain of points in knowledge of death [false/true\|default:true] |
| `display_alignment_message` | true |  | Display or not the messages of earned of points in Alignment [false/true\|default:true] |
| `equip_elytra_in_priority` | false |  | Equips elytra in priority when recovering your lost items [false/true\|default:false] |
| `equip_shield_in_priority` | false |  | Equips shield in priority when recovering your lost items [false/true\|default:false] |
| `reverse_inventory_sorting` | false |  | Sorts the inventory by filling the last slots first [false/true\|default:false] |
| `show_info_on_enchantment` | true |  | Shows the use of the Tombstone's enchantments in tooltip [false/true\|default:true] |
| `priorize_tool_on_hotbar` | false |  | Favor the tools on the hotbar when recovering a grave [false/true\|default:false] |
| `activate_grave_by_sneaking` | true |  | Allows to activate a grave by sneaking [false/true\|default:true] |
| `allow_grave_in_water` | true |  | Allows your grave to appear in water [false/true\|default:true] |
| `particle_casting_color` | 14,937,088 | 0 to 16,777,215 | Decimal value for the color of the particles when using magic items [0..16777215\|default:125656] |
| `text_color_death_date` | 2,962,496 | 0 to 16,777,215 | Decimal value for the color of the grave text &lt;Death Date&gt; [0..16777215\|default:2962496] |
| `text_color_rip` | 2,962,496 | 0 to 16,777,215 | Decimal value for the color of the grave text &lt;R.I.P.&gt; [0..16777215\|default:2962496] |
| `text_color_owner` | 5,991,302 | 0 to 16,777,215 | Decimal value for the color of the grave text &lt;Owner Name&gt; [0..16777215\|default:5991302] |
| `fog_color` | 16,777,215 | 0 to 16,777,215 | Decimal value of the fog color [0..16777215\|default:125656] |
| `fog_density` | "NORMAL" |  | Fog density around the graves [NONE/LOW/NORMAL/HIGH\|default:NORMAL] |
| `favorite_grave` | "GRAVE_SIMPLE" | one of: GRAVE_SIMPLE, GRAVE_NORMAL, GRAVE_CROSS, TOMBSTONE, SUBARAKI_GRAVE, GRAVE_ORIGINAL | Favorite grave |
| `favorite_grave_marble` | "DARK" |  | Favorite grave marble |
| `grave_skin_rule` | "DEFAULT" |  | Defines the rule to use for grave's skin [DEFAULT/FORCE_NORMAL/FORCE_HALLOWEEN\|default:DEFAULT] |
| `auto_equip_rule` | `defaultVal` |  | Defines when to automatically equip your items [NEVER/GRAVE_RECOVERY/DEATH_RESPAWN/ALWAYS\|default:ALWAYS] |
| `marker_type` | `defaultVal` |  | Defines the type of marker when holding in hand some items like the Grave's Key [WING/SPARK/NOTE/BOX\|default:WING] |
| `font_rule` | `defaultVal` |  | Defines the font to use in Tombstone's screens (only for english, french and spanish languages) [FANTASY/VANILLA\|default:FANTASY] |
| `show_tooltip_combine` | true |  | Display the combinations in item tooltip [false/true\|default:true] |
| `no_blinking_nightvision` | true |  | Prevent night vision from flashing when less than 5 seconds left [false/true\|default:true] |
| `scale_guiscreens` | true |  | Scales Tombstone guiscreens to be larger as possible [false/true\|default:true] |

## `[compatibility]`

Allows to enable some features related to others mods

| Option | Default | Range | Description |
|---|---|---|---|
| `curio_auto_equip` | true |  | Allows to auto-equip the slots from Curio mod [false/true\|default:true] |
| `keep_cosmetic_armor` | true |  | Keeps the cosmetic armor when you die [false/true\|default:true] |
| `preserve_effects_on_return_end_conquered` | true |  | Ensure the potion effects to stay on the player after returning from end conquered [false/true\|default:true] |

## `[decorative_grave]`

For settings related to decorative tombs and magic items

| Option | Default | Range | Description |
|---|---|---|---|
| `can_replace_grave_plate` | true |  | Allows to replace a grave plate already set on a grave [false/true\|default:true] |
| `allow_grave_gardian` | true |  | Allows the merchant grave gardian [false/true\|default:true] |
| `distance_between_grave_guardian` | 100 | 10 to 200 | Minimum distance between Grave Gardians to spawn [10..200\|default:100] |
| `restock_time_grave_guardian` | 60 | 1 to 1,000 | Time in minutes for a Grave Guardian to restock its offers [1..1000\|default:60] |
| `soul_time` | 10 | 1 to 10,000 | Time in minutes to check if a soul appears on a grave [1..10000\|default:10] |
| `soul_chance` | 25 | 0 to 100 | Chance on 1000 that a soul appears on a grave [0..100\|default:25] |

## `[general]`

Miscellaneous options

| Option | Default | Range | Description |
|---|---|---|---|
| `teleport_dim` | true |  | Allows teleportation to other dimensions [false/true\|default:true] |
| `knowledge_reduce_phantom_spawn` | true |  | Increases the minimum time without sleeping for phantom spawn around player based on their level in Knowledge of Death [false/true\|default:true] |
| `time_for_phantom_spawn` | 72,000 | 1,200 to no limit | Minimum time without sleeping for phantom to spawn around players [1200..MAX\|default:72000] |
| `cooldown_request_teleport` | -1 | -1 to 1,440 | Cooldown in minutes to use the command tbrequestteleport [-1..1440\|default:-1] |
| `cooldown_teleport_death` | -1 | -1 to 1,440 | Cooldown in minutes to use the command tbteleportdeath [-1..1440\|default:-1] |
| `unhandled_beneficial_effects` | "minecraft:hero_of_the_village" |  | Beneficial effects that can't used by certain features such as ankh of prayer, lollipop, scroll of preservation, alchemy perk and magic siphon enchantment |
| `unhandled_harmful_effects` | "minecraft:nausea" |  | Harmful effects that can't used by certain features such as tablet of cupidity and the enchantment plague bringer |
| `decrepitude_max_damage` | no limit | 1 to no limit | Allows to limit the damages done by Decrepitude |

## `[loot]`

Options related to looted items

| Option | Default | Range | Description |
|---|---|---|---|
| `max_xp_lost_page` | 2,000 | 100 to 200,000 | Maximum xp rewarded with a Lost Page of Erdös [100..200000\|default:2000] |
| `denied_modid_for_equipment` | "tombstone" |  | Denied mods for equipment drops |
| `only_vanilla_for_equipment` | false |  | Only vanilla drops for equipment [false/true\|default:false] |

## `[magic_item]`

For settings related to magic items

| Option | Default | Range | Description |
|---|---|---|---|
| `can_recycle_damaged_item` | true |  | Damaged items can be recycled with the Book of Recycling |
| `denied_item_to_recycle` | `defaultVal` |  | The items that can't be recycled by the Book of Recycling |
| `can_disenchant_enchanted_book` | false |  | Allows to disenchant enchanted books with the Book of Disenchantment |
| `lost_tablet_search_outside_world` | true |  | Allows lost tablets to find locations outside the current world [false/true\|default:true] |
| `lost_tablet_modded_structure` | true |  | Allows lost tablets to find modded structures [false/true\|default:true] |
| `lost_tablet_denied_structures` | `defaultVal` |  | The structures that can't be discovered by lost tablets |
| `lost_tablet_denied_worlds` | `defaultVal` |  | The worlds that can't be discovered by lost tablets |

## `[player_death]`

Options related to player's death

| Option | Default | Range | Description |
|---|---|---|---|
| `pvp_unlock_grave` | true |  | Whether to unlock access to a grave if the player has been killed by another player [false/true\|default:true] |
| `restore_effects_on_death` | false |  | Whether to restore beneficial effects after a player dies [false/true\|default:true] |
| `loss_on_death_only_for_abandoned_grave` | true |  | Only abandoned graves can have losses of items (based on the decay_time) [false/true\|default:true] |
| `loss_on_death_only_for_stackable_items` | true |  | Only stackable items can be lost on death [false/true\|default:true] |
| `prevent_death_outside_world_border` | true |  | Prevents death outside the borders of the world [false/true\|default:true] |
| `prevent_death_outside_build_height` | false |  | Prevents death outside the build height [false/true\|default:false] |
| `allow_to_fill_existing_grave` | true |  | Allows to fill an existing grave instead of creating a new one [false/true\|default:true] |
| `nerf_ghostly_shape_teleport_with_key` | true |  | Caps the duration of Ghostly Shape effect to 10 seconds when teleporting with a Grave's Key [false/true\|default:true] |
| `sniffer_range` | 5 | 1 to 10 | The radius in which items should be collected when a grave is spawned [1..10\|default:5] |
| `chance_mob_on_grave_recovery` | 0 | 0 to 100 | The chance that creatures appear after the contents of a grave are retrieved [0..100\|default:0] |
| `pvp_stolen_xp` | 30 | 0 to 100 | Percent of stolen experience by killing a player when PvP mode is enabled [0..100\|default:30] |
| `chance_loss_on_death` | 0 | 0 to 100 | The chance that some items are lost on death [0..100\|default:0] |
| `percent_loss_on_death` | 0 | 0 to 100 | The percentage of items that are lost on death [0..100\|default:0] |
| `no_grave_dimension` | `defaultVal` |  | Graveless Dimensions |

## `[recovery]`

Options related to the command recovery and auto-save of players

| Option | Default | Range | Description |
|---|---|---|---|
| `recovery_player_enable` | true |  | Enables to backup automatically players [false/true\|default:true] |
| `backup_on_death` | true |  | Backup players on death [false/true\|default:false] |
| `recovery_player_timer` | 19 | 5 to 1,000 | Time in minutes between players' backups [10..1000\|default:40] |
| `recovery_player_max_saves` | 15 | 5 to 100 | Maximum number of backups per player [5..100\|default:15] |
| `log_auto_backup` | false |  | Log when players are automatically back up [false/true\|default:false] |

## `[special_events]`

Allows to enable special events

| Option | Default | Range | Description |
|---|---|---|---|
| `allow_halloween` | true |  | Allows Halloween [false/true\|default:true] |
| `allow_christmas` | true |  | Allows Christmas [false/true\|default:true] |
| `allow_spring_bloom` | true |  | Allows Spring Bloom [false/true\|default:true] |
| `force_special_event` | "NONE" |  | Allows you to set a Special Event as permanent [NONE/HALLOWEEN/CHRISTMAS/SPRING_BLOOM\|default:NONE] |

## `[village_siege]`

Allows to define the conditions for a village siege to begin

| Option | Default | Range | Description |
|---|---|---|---|
| `handle_village_siege` | true |  | Allows to handle village sieges [false/true\|default:true] |
| `log_siege_state` | false |  | Logs the different states of a village siege while searching for an adequate place [false/true\|default:false] |
| `glowing_creature_test` | false |  | The creatures of the siege have a glowing effect (only uses this for test purposes) [false/true\|default:false] |
| `allow_creative_players_for_siege` | true |  | Allows to use the positions of creative players to define the siege location [false/true\|default:true] |
| `undead_wear_helm_in_siege` | false |  | Undeads always wear a helm when sieging [false/true\|default:false] |
| `persistent_mob_in_siege` | false |  | Mobs in siege are persistent [false/true\|default:false] |
| `shuffle_players_for_siege` | true |  | Shuffles the list of players before testing the siege location [false/true\|default:true] |
| `siege_chance` | 10 | 0 to 100 | Chance for a siege to occur [0..100\|default:10] |
| `siege_max_creature` | 20 | 0 to 100 | Maximum of creatures appearing in a siege [0..100\|default:20] |
| `delay_siege_test` | 200 | 0 to 1,200 | Delay in seconds for a second test of siege when the first failed [0..1200\|default:200] |
