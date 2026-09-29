# Artifacts: what things do

Written from the mod's code (Artifacts 13.2.5). Each `## id` section becomes the "What it does" part of that entry's page.

## artifacts:aqua_dashers
Feet artifact. While you're **sprinting** you can run across the surface of water (and other non-lava fluids) instead of sinking.

## artifacts:strider_shoes
Feet artifact. While you're **sneaking** you can walk across the surface of lava. They also make you immune to "hot floor" damage from standing on magma blocks and similar blocks.

## artifacts:cloud_in_a_bottle
Belt artifact. Lets you **double jump**: press jump again in mid-air to jump a second time. Sprinting while you double jump gives extra forward and upward speed. It also raises your safe fall distance by {{cfg:config/artifacts/items.toml|cloud_in_a_bottle.safeFallDistanceBonus}} blocks, and fall damage after a double jump is multiplied by {{cfg:config/artifacts/items.toml|cloud_in_a_bottle.fallDamageMultiplier}}.

## artifacts:everlasting_beef, artifacts:eternal_steak
Food that is **never used up**: eating it feeds you but keeps the item, then puts it on a short cooldown ({{cfg:config/artifacts/items.toml|everlasting_beef.cooldown}} s for Everlasting Beef, {{cfg:config/artifacts/items.toml|eternal_steak.cooldown}} s for Eternal Steak). Everlasting Beef restores 3 hunger and has a chance to drop when a player kills a cow or mooshroom. Cook it into Eternal Steak, which restores 8 hunger.

<!-- kind: effects -->

## artifacts:magnetism
Pulls nearby dropped items toward you. The pull range is 1 block per level (up to 10), and up to about 50 items are pulled at once. Items you threw yourself aren't pulled back. The Universal Attractor gives it while worn.
