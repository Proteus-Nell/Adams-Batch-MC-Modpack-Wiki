# `serverconfig/tombstone-server.toml`

<small>[Corail Tombstone](../index.md) &rsaquo; [Configs](index.md)</small>

## `[allowedMagicItems]`

Allows to disable some magic items

| Option | Default | Range | Description |
|---|---|---|---|
| `allow_voodoo_poppet` | true |  | Voodoo Poppet [false/true\|default:true] |
| `allow_receptacle_of_familiar` | true |  | Receptacle of Familiar [false/true\|default:true] |
| `allow_book_of_disenchantment` | true |  | Book of Disenchantment [false/true\|default:true] |
| `allow_scroll_of_preservation` | true |  | Scroll of Preservation [false/true\|default:true] |
| `allow_grave_key` | true |  | Grave's Key [false/true\|default:true] |
| `allow_scroll_of_knowledge` | true |  | Scroll of Knowledge [false/true\|default:true] |
| `allow_tablet_of_recall` | true |  | Tablet of Recall [false/true\|default:true] |
| `allow_tablet_of_home` | true |  | Tablet of Home [false/true\|default:true] |
| `allow_tablet_of_assistance` | true |  | Tablet of Assistance [false/true\|default:true] |
| `allow_tablet_of_cupidity` | true |  | Tablet of Cupidity [false/true\|default:true] |
| `allow_tablet_of_guard` | true |  | Tablet of Guard [false/true\|default:true] |
| `allow_scroll_of_unstable_intangibility` | true |  | Scroll of Unstable Intangibility [false/true\|default:true] |
| `allow_scroll_of_feather_fall` | true |  | Scroll of Feather Fall [false/true\|default:true] |
| `allow_scroll_of_purification` | true |  | Scroll of Purification [false/true\|default:true] |
| `allow_scroll_of_true_sight` | true |  | Scroll of True Sight [false/true\|default:true] |
| `allow_lost_tablet` | true |  | Lost Tablet [false/true\|default:true] |
| `allow_scroll_of_reach` | true |  | Scroll of Reach [false/true\|default:true] |
| `allow_scroll_of_lightning_resistance` | true |  | Scroll of Lightning Resistance [false/true\|default:true] |
| `allow_scroll_of_frost_resistance` | true |  | Scroll of Frost Resistance [false/true\|default:true] |
| `allow_scroll_of_aquatic_life` | true |  | Scroll of Aquatic Life [false/true\|default:true] |
| `allow_scroll_of_mercy` | true |  | Scroll of Mercy [false/true\|default:true] |
| `allow_scroll_of_projectile_reflection` | true |  | Scroll of Projectile Reflection [false/true\|default:true] |
| `allow_dust_of_vanishing` | true |  | Dust of Vanishing [false/true\|default:true] |
| `allow_dust_of_frost` | true |  | Dust of Frost [false/true\|default:true] |
| `allow_book_of_recycling` | true |  | Book of Recycling [false/true\|default:true] |
| `allow_book_of_repairing` | true |  | Book of Repairing [false/true\|default:true] |
| `allow_book_of_magic_impregnation` | true |  | Book of Magic Impregnation [false/true\|default:true] |
| `allow_book_of_scribe` | true |  | Book of Scribe [false/true\|default:true] |
| `allow_book_of_soulbound` | true |  | Book of Soulbound [false/true\|default:true] |
| `allow_book_of_oblivion` | true |  | Book of Oblivion [false/true\|default:true] |
| `allow_smoke_ball` | true |  | Smoke Ball [false/true\|default:true] |
| `allow_seeker_rod` | true |  | Seeker Rod [false/true\|default:true] |
| `allow_christmas_hat` | true |  | Christmas Hat [false/true\|default:true] |
| `allow_bag_of_seeds` | true |  | Bag of Seeds [false/true\|default:true] |
| `allow_magic_scroll` | true |  | Magic Scroll [false/true\|default:true] |
| `allow_gemstone_of_familiar` | true |  | Gemstone of Familiar [false/true\|default:true] |
| `allow_gemstone_of_merchant` | true |  | Gemstone of Merchant [false/true\|default:true] |
| `allow_gemstone_of_prayer` | true |  | Gemstone of Prayer [false/true\|default:true] |
| `allow_gemstone_of_guardian` | true |  | Gemstone of Guardian [false/true\|default:true] |

## `[decorative_grave]`

For settings related to decorative tombs and magic items

| Option | Default | Range | Description |
|---|---|---|---|
| `prayer_cooldown` | 60 | 1 to 60 | The cooldown in minutes to pray with the Ankh [1..60\|default:60] |

## `[enchantments]`

Allows to customize or disable the enchantments

| Option | Default | Range | Description |
|---|---|---|---|
| `soulbound_enchanting_table` | true |  | Allows Soulbound at enchanting table [false/true\|default:false] |
| `spectral_bite_enchanting_table` | true |  | Allows Spectral Bite at enchanting table [false/true\|default:false] |
| `magic_siphon_enchanting_table` | true |  | Allows Magic Siphon at enchanting table [false/true\|default:false] |
| `plague_bringer_enchanting_table` | true |  | Allows Plague Bringer at enchanting table [false/true\|default:false] |
| `curse_of_bones_enchanting_table` | true |  | Allows Curse of Bones at enchanting table [false/true\|default:false] |
| `blessing_enchanting_table` | true |  | Allows Blessing at enchanting table [false/true\|default:false] |
| `frostbite_enchanting_table` | true |  | Allows Frostbite at enchanting table [false/true\|default:false] |
| `spectral_conjurer_enchanting_table` | true |  | Allows Spectral Conjurer at enchanting table [false/true\|default:false] |
| `incurable_wounds_enchanting_table` | true |  | Allows Incurable Wounds at enchanting table [false/true\|default:false] |
| `decrepitude_enchanting_table` | true |  | Allows Decrepitude at enchanting table [false/true\|default:false] |
| `sanctified_enchanting_table` | true |  | Allows Sanctified at enchanting table [false/true\|default:false] |
| `ruthless_strike_enchanting_table` | true |  | Allows Ruthless Strike at enchanting table [false/true\|default:false] |

## `[magic_item]`

For settings related to magic items

| Option | Default | Range | Description |
|---|---|---|---|
| `chance_enchanted_grave_key` | 0 | -1 to 100 | Chance for players to obtain an enchanted Grave's Key on death (-1 disables the Perk Jailer) [-1..100\|default:0] |
| `disable_enchanted_grave_key_recipe` | false |  | Prevents to craft Enchanted Grave Key [false/true\|default:false] |
| `scroll_duration` | 12,000 | 1,200 to 120,000 | Scroll duration [1200..120000\|default:12000] |
| `scroll_of_knowledge_loss` | 0 | 0 to 90 | Defines experience lost when storing experience in a Scroll of Knowledge |
| `tablet_cooldown` | 300 | 60 to 1,200 | Cooldown in second after using a tablet [60..1200\|default:300] |
| `level_max_magic_scrolls` | 4 | 0 to 255 | Maximum level for Magic Scrolls [0..255\|default:4] |
| `cooldown_reset_perk` | 120 | 20 to 1,440 | The cooldown in minutes to reset the perks with the Book of Oblivion [20..1440\|default:120] |

## `[player_death]`

Options related to player's death

| Option | Default | Range | Description |
|---|---|---|---|
| `decay_time` | -1 | -1 to no limit | The time in minutes before a grave is unlocked to anyone [-1..MAX\|default:-1\|disabled:-1] |
| `xp_loss_on_death` | 95 | 0 to 100 | Experience lost on death [0..100\|default:95] |
| `ghostly_shape_duration` | 120 | 0 to no limit | The duration of the Ghostly Shape effect in seconds [0..MAX\|default:120] |

## `[potions]`

Allows to customize or disable the potions

| Option | Default | Range | Description |
|---|---|---|---|
| `allow_earthly_garden` | true |  | Allows Earthly Garden [false/true\|default:true] |
| `allow_bait` | true |  | Allows Bait [false/true\|default:true] |
| `allow_frostbite` | true |  | Allows Frostbite [false/true\|default:true] |
| `allow_darkness` | true |  | Allows Darkness [false/true\|default:true] |
| `allow_discretion` | true |  | Allows Discretion [false/true\|default:true] |
| `allow_restoration` | true |  | Allows Restoration [false/true\|default:true] |
| `allow_weaver_walk` | true |  | Allows Weaver Walk [false/true\|default:true] |
| `allow_giant_strength` | true |  | Allows Giant Strength [false/true\|default:true] |
| `allow_little_world` | true |  | Allows Little World [false/true\|default:true] |
