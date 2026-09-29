<small>[Ascension](../index.md)</small>

# Mechanics

Ascension (Tensura: Ascension) adds new race lines and an **Ultimate awakening** ritual on top of [Tensura: Reincarnated](../../tensura-reincarnated/mechanics/index.md).

## Ultimate awakening

A mastered Unique skill can be awakened into an Ultimate at an **awakening altar**. The ritual needs:

- a complete altar pattern and a **Catalyst** placed on it
- **True Demon Lord** or **True Hero** status
- at least **5,000,000** Max EP
- a mastered Unique skill that has an Ultimate awakening

Some Ultimates have extra tributes:

| Ultimate | Extra requirement |
|---|---|
| Timeless Mage | Mastery of every Aspectual magic |
| The Slayer of Dragons | 30 Dragon Essences |
| The Unbound Jester | 1,000,000 spirit damage dealt while shackled |
| The Evil Majin | 50 Majin Candies eaten in your lifetime |
| Sealer's awakening | A Suppression Stone holding 400,000 Max EP |

After a successful ritual your soul needs **120** real-time minutes to recover before you can do it again. Players who witness an awakening gain Max EP. The `doAscensionUltimate` game rule (default: true) turns the whole system on or off.

## Races

Ascension's race lines (angels, frogs, djinn, bloodfiends, corrupted dragons, dragonewts, gazers, kitsune, undead, wights and Wukong) each have their own stats, starting-EP range and evolution EP requirement, set in [`ascension-races.toml`](../configs/config-tensura-ascension-races.md). Evolving into a race grants bonus EP (by default half of that race's evolution requirement). A holy soul cannot take the demon lord path.

## Hyperbolic Chamber

EP gained from kills inside the Hyperbolic Chamber dimension is multiplied by **3**.

## Reincarnation pool

The mod adds its Unique skills to Tensura's reincarnation pool (the `additionalUniqueSkills` list in [`ascension-common.toml`](../configs/config-tensura-ascension-common.md)).
