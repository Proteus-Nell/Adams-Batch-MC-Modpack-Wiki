# Ascension: what things do

Written from the mod's code (Ascension 2.1.2). Each `## id` section becomes the "What it does" part of that entry's page.

## ascension:hyperbolic_chamber
A training dimension: an endless flat floor of {{link:ascension:hyperbolic_fabric}} (as unbreakable as bedrock) under a white sky, with thick fog past 64 blocks. It is always noon, beds explode, and nothing spawns on its own.

**Getting in:** the only way in is the {{link:ascension:hyperbolic_passage}} extra skill. You learn it automatically once you've **mastered both Gate and Sacred Haki**. Pressing it costs **{{pct:config/tensura/ascension-skills.toml|Skills.hyperbolic_passage.magiculeFraction}}** of your *current* magicule and opens a white portal 2 blocks in front of you. The portal lasts **{{cfg:config/tensura/ascension-skills.toml|Skills.hyperbolic_passage.portalLifetimeSeconds}} s**. Walk into it to go through. The skill's cooldown is {{cfg:config/tensura/ascension-skills.toml|Skills.hyperbolic_passage.cooldownSeconds}} s ({{cfg:config/tensura/ascension-skills.toml|Skills.hyperbolic_passage.cooldownSecondsMastered}} s mastered). You arrive on the floor near the same X/Z you left from.

**Getting out:** cast the skill again inside the chamber. The portal it opens there leads back to the **Overworld**, near the same X/Z.

**Why go there:**

- **EP from kills is multiplied by {{cfg:config/tensura/ascension-common.toml|Races.Dimensions.HyperbolicChamber.epMultiplier}}** when you, or one of your subordinates, kill something inside. The bonus is added after Tensura's normal EP gain, so EP-gain gear and gamerule caps still apply.
- The ambient (chunk) magicule is **1,000,000** higher than normal and refills **3×** as fast.

## ascension:hyperbolic_fabric
The floor of the {{link:ascension:hyperbolic_chamber}}. It copies bedrock's properties, so it can't be broken in survival and resists explosions.

## ascension:chaos_fire
White fire left behind where The Imprisoned Jester's Chaos Spades hit. It can only be placed on solid ground (not on water). Anything standing in it that isn't fire-immune takes **{{cfg:config/tensura/ascension-skills.toml|Skills.imprisoned_jester.chaosFireDamage}}** spiritual (soul) damage every {{cfg:config/tensura/ascension-skills.toml|Skills.imprisoned_jester.chaosFireTickInterval}} ticks. It doesn't spread or burn blocks, and goes out on its own after {{cfg:config/tensura/ascension-skills.toml|Skills.imprisoned_jester.chaosFireBurnoutTicks}} ticks.

<!-- kind: effects -->

## ascension:angel_wings
Lets you glide like an elytra without wearing one. **Double-tap jump** in mid-air (not in water) to start gliding. While you have it, gliding doesn't stop on its own, even without an elytra. Fireworks boost it as usual.

The {{link:ascension:angel_wings}} skill gives it for {{cfg:config/tensura/ascension-skills.toml|Skills.angel_wings.durationSeconds}} s on a press, or for as long as the skill is toggled on.

## ascension:bleeding
Blood loss. Every second it deals **0.5** blood-drain damage per level, and ignores the usual invulnerability frames after a hit. Prickly Hands and Deus Sanguis inflict it on melee hits, and the {{link:ascension:serrated}} enchantment does too.

## ascension:regen_suppression
Shuts down regeneration skills. Every tick it switches off **Self Regeneration**, **Ultraspeed Regeneration** and **Infinite Regeneration** if they're toggled on, so they can't be used until it ends. Only Blockade inflicts it: {{cfg:config/tensura/ascension-skills.toml|Skills.blockade.durationSeconds}} s, or {{cfg:config/tensura/ascension-skills.toml|Skills.blockade.durationSecondsMastered}} s mastered.

<!-- kind: enchantments -->

## ascension:serrated
Each hit also gives the target {{link:ascension:bleeding}} for **5 seconds**: Bleeding I at Serrated I, up to Bleeding III at Serrated III. It can't be combined with Fire Aspect.

## ascension:ep_attunement
Gives an item its own EP pool, which repairs it. It can go on anything that can take Curse of Vanishing.

- An attuned item starts with **10,000 EP** and regains **20 EP per second** while worn or held.
- While it has EP, that EP is spent to repair the item's durability, 1 EP per point.
- Each kill (while the item is equipped) raises the item's max EP and current EP by **2%** of the victim's EP. A victim without EP gives **25 × its max health** instead.
