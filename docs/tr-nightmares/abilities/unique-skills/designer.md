# Designer

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Designer](../../../assets/icons/trnightmare/skill/designer.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:designer` |
| **Modes** | 5 |
| **Acquisition cost (MP)** | 95,000 |
| **Activation** | Press, Hold |

</div>

> The greatest gift to ever be formed.

## Modes

| # | Mode |
|---|---|
| 1 | Copy |
| 2 | Skill Designer |
| 3 | Recycle |
| 4 | Skill Evolution |
| 5 | Magicule Furnace |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| learning | 6 | add |
| atk | atk bonus | add |
| armor | armor bonus | add |

## Obtaining

- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.
- Listed in the `virtueDominionSkills` config option (config/nightmare/ability/skill/nightmare_ult.toml): Virtue skills that Ultimate Dominion can copy from targets.

## Related

- **Related skills:** [Darkness Cannon](../../../tensura-reincarnated/abilities/spiritual-magic/darkness-cannon.md)
- **Summons / entities:** Tensura, Holy Cannon Projectile
- **Referenced by:** [｢ Astarte, Lord of Heaven ｣](../ultimate-skills/astarte.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `Designer.mpAcquirement` | 95,000 |  |
| `Designer.byDesignLearningBonus` | 6 |  |
| `Designer.furnaceMaxMpPercent` | 2.25 | Magicule Furnace: max MP the furnace can charge to, as a multiple of the user's max MP (2.25 = 225%). |
| `Designer.furnaceRestorePercentMastered` | 0.05 |  |
| `Designer.furnaceRestorePercent` | 0.03 | Magicule Furnace: fraction of max MP restored per second (normal / mastered). |
| `Designer.divineDarknessMpCostPercent` | 0.035 | Divine Darkness: fraction of max MP drained per second. |
| `Designer.divineDarknessDamageMastered` | 100 |  |
| `Designer.divineDarknessDamage` | 50 | Divine Darkness: Holy + Darkness damage per second (normal / mastered). |
| `Designer.apocryphaAtkBonusMastered` | 30 |  |
| `Designer.apocryphaAtkBonus` | 10 | Apocrypha: flat attack damage bonus (normal / mastered). |
| `Designer.apocryphaArmorBonusMastered` | 30 |  |
| `Designer.apocryphaArmorBonus` | 15 | Apocrypha: flat armor bonus (normal / mastered). |
| `Designer.apocryphaDrainPercentMastered` | 0.06 |  |
| `Designer.apocryphaDrainPercent` | 0.08 | Apocrypha: fraction of max MP drained every 2 seconds (normal / mastered). |

## In-game messages

<details markdown><summary>Show 19 messages</summary>

- Skills stored in Skill Designer.
- Copy skills first with Copy.
- No eligible skills to recycle.
- No skill evolutions are available.
- Magicules at maximum capacity.
- Apocrypha activated.
- Apocrypha deactivated.
- Apocrypha deactivated — not enough magicules.
- Not enough magicules.
- Destroy
- Create Permanently
- Skill Designer
- That skill cannot be created (already owned or not stored).
- Skill creation failed — MP and mastery refunded.
- Forged temporary skill: %s
- Permanently acquired: %s
- Unique and Ultimate skills can only be forged temporarily.
- Analyzed %1$s: %2$s/%3$s copies (%4$s remaining to create).
- You have been granted the Designer skill by standing still on a bed!

</details>
