# Hand of Destruction

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `trnightmare:hand_of_destruction` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 50,000 |
| **Activation** | Press, Hold |

</div>

> An extra skill that channels destruction through divine darkness beams and customizable firing styles.

## Modes

| # | Mode |
|---|---|
| 1 | Divine Darkness |
| 2 | Divine Darkness Style |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key

## Related

- **Related skills:** [Darkness Cannon](../../../tensura-reincarnated/abilities/spiritual-magic/darkness-cannon.md)
- **Summons / entities:** Holy Cannon Projectile
- **Referenced by:** [｢ Astaroth, King of Fallen ｣](../ultimate-skills/astaroth.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_extra.toml`](../../configs/config-nightmare-ability-skill-nightmare-extra.md).

| Option | Default | Description |
|---|---|---|
| `HandOfDestruction.mpAcquirement` | 50,000 | Magicule Acquirement Cost. |
| `HandOfDestruction.divineDarknessDamage` | 100 | Divine Darkness damage per hit (unmastered). |
| `HandOfDestruction.divineDarknessDamageMastered` | 250 | Divine Darkness damage per hit (mastered). |
| `HandOfDestruction.divineDarknessMpCostPercent` | 0.035 | Fraction of max MP drained per Divine Darkness use. |

## In-game messages

<details markdown><summary>Show 2 messages</summary>

- Not enough Magicules!
- You have gained the Hand of Destruction!

</details>
