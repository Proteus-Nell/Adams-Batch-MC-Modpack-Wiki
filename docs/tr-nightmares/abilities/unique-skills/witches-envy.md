# Witch's Envy

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Witch's Envy](../../../assets/icons/trnightmare/skill/witches_envy.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:witches_envy` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 120,000 |
| **Max mastery** | 1,000 |
| **Activation** | Toggle, Press, Hold |

</div>

> Sin Factor of envy — return by death, witch's curse, and envious plunder.

## Modes

| # | Mode |
|---|---|
| 1 | Witch's Wrath |
| 2 | Envious Life |
| 3 | Deadly Ramble |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when you are attacked
- Triggers when you die

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| learning | stacks | add |
| mastery | stacks | add |

## Obtaining

- Listed in the `blacklistedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that are banned from being transferred through Food Chain.

## Related

- **Related skills:** [Witch's Greed](witches-greed.md)
- **Effects:** [Witch's Curse](../../effects/witches-curse.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `witchesEnvy.epAcquirement` | 120,000 | EP / magicule obtainment cost. |
| `witchesEnvy.learningCost` | 1,500 | Learning / mastery point cost. |
| `witchesEnvy.maxMastery` | 1,000 | Max mastery. |
| `witchesEnvy.learningByDeathMaxStacks` | 20 | Learning By Death: max bonus stacks (+1 learning &amp; mastery gain each). |
| `witchesEnvy.learningByDeathCooldownTicks` | 1,200 | Learning By Death: cooldown between stack gains (ticks). |
| `witchesEnvy.curseMaxStacks` | 5 | Witch's Curse: max stacks without mastery. |
| `witchesEnvy.curseMaxStacksMastered` | 10 | Witch's Curse: max stacks when mastered. |
| `witchesEnvy.curseStacksPerKill` | 1 | Witch's Curse: stacks added when the user is killed. |
| `witchesEnvy.curseDurationTicks` | 6,000 | Witch's Curse: effect duration (ticks). |
| `witchesEnvy.curseOnHitChance` | 0.1 | Witch's Curse: chance on hit when mastered. |
| `witchesEnvy.wrathRange` | 12 | Witch's Wrath: targeting range. |
| `witchesEnvy.wrathDamage` | 10 | Witch's Wrath: corrosion + spiritual damage per stack. |
| `witchesEnvy.wrathDamageMastered` | 25 | Witch's Wrath: damage per stack when mastered. |
| `witchesEnvy.rambleRadius` | 30 | Deadly Ramble: radius in blocks. |
| `witchesEnvy.rambleOthersShpFraction` | 0.2 | Deadly Ramble: fraction of max SHP drained from others per second. |
| `witchesEnvy.rambleSelfShpFraction` | 0.15 | Deadly Ramble: fraction of max SHP drained from self per second. |

## In-game messages

<details markdown><summary>Show 2 messages</summary>

- Return By Death
- Envious Life copied %s

</details>

## Tags

`tensura:skills/no_plundering`
