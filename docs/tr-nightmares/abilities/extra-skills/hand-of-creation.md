# Hand of Creation

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `trnightmare:hand_of_creation` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 50,000 |
| **Activation** | Press, Hold |

</div>

> An extra skill that allows evolution and recycling of skills, with an energy engine mode for magicule and spiritron regeneration.

## Modes

| # | Mode |
|---|---|
| 1 | Skill Evolution |
| 2 | Recycle |
| 3 | Energy Engine |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key

## Related

- **Referenced by:** [｢ Astaroth, King of Fallen ｣](../ultimate-skills/astaroth.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_extra.toml`](../../configs/config-nightmare-ability-skill-nightmare-extra.md).

| Option | Default | Description |
|---|---|---|
| `HandOfCreation.mpAcquirement` | 50,000 | Magicule Acquirement Cost. |
| `HandOfCreation.furnaceRestorePercent` | 0.05 | Percentage of max Magicules restored per second by Energy Engine (unmastered). |
| `HandOfCreation.furnaceRestorePercentMastered` | 0.07 | Percentage of max Magicules restored per second by Energy Engine (mastered). |
| `HandOfCreation.furnaceMaxMpPercent` | 2.5 | Maximum Magicules Energy Engine can generate, as a multiplier of max Magicules. |
| `HandOfCreation.spiritronRegen` | 50 | Spiritrons generated per second by Energy Engine (unmastered). |
| `HandOfCreation.spiritronRegenMastered` | 100 | Spiritrons generated per second by Energy Engine (mastered). |

## In-game messages

<details markdown><summary>Show 2 messages</summary>

- Energy Engine is full!
- You have gained the Hand of Creation!

</details>
