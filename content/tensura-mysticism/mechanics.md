# Mechanics

Tensura: Mysticism is mostly about [races](@/tensura-mysticism/races/index.md): wyrms, direwolves, insects, elementals, angels, phantoms, daemon dolls, sculk beings and more, each with its own evolution tree.

## Soul Energy

Mysticism adds a third resource, **Soul Energy (SE)**, alongside aura and magicules.

- With the `uniqueSECost` game rule on (default: {{gamerule:uniqueSECost}}), acquiring a Unique skill also costs Soul Energy: the skill's magicule cost multiplied by **{{cfg:config/mysticism/general.toml|General.seCostMultiplier}}**.
- You gain Soul Energy from key moments: awakening, reincarnating completely, and receiving a name (more if the namer is special).

Check or change Soul Energy with `/mysticism edit stat <selector> soulEnergy ...` (see [Commands](@/tensura-mysticism/commands/index.md)).

## Special evolution requirements

Besides EP and boss kills, Mysticism races can require things like:

- being in certain biomes
- a particular light level
- possessing a Bone Golem (daemon dolls)
- satisfying any one of several conditions

Some evolutions are forced by what you do. Angels can **fall from grace** and become Fallen Angels or Phantoms, and a being that loses all connection to the light attribute becomes *Fallen*.

Each race page lists the exact requirements and their weights.

## Flight

Winged Mysticism races fly at a base speed of **{{cfg:config/mysticism/general.toml|General.flightSpeed}}**.

## Dimensions and structures

Mysticism adds the **Elemental Realm** and the **Kamui Dimension**, plus new biomes and structures. See [Dimensions](@/tensura-mysticism/dimensions/index.md), [Biomes](@/tensura-mysticism/biomes/index.md) and [Structures](@/tensura-mysticism/structures/index.md).
