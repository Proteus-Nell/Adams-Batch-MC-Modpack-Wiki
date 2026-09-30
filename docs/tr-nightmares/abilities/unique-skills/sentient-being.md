# Sentient Being

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Sentient Being](../../../assets/icons/trnightmare/skill/sentient_being.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:sentient_being` |
| **Modes** | 2 |
| **Activation** | Press, Hold |

</div>

> Born from the magicules of your peers, your growth depends on them and theirs depends on you. You are naturally more attuned to the absorption of energy from the environment.

## Modes

| # | Mode |
|---|---|
| 1 | Snack For Later! |
| 2 | Family Bonds! |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Magicule Regeneration Multiplier | 4 | multiply total |

## Related

- **Summons / entities:** Tensura
- **Referenced by:** [Ruler](ruler.md), [Carnation](carnation.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `SentientBeing.snackmultiplier` | 5 | Multiplier for Magicule Regeneration via Snack For Later (doubled on mastery). |
| `SentientBeing.mpAcquirement` | 95,000 | Magicule Acquirement Cost. |
| `SentientBeing.abundanceMultiplier` | 2 | Multiplier for Magicule Regeneration via Abundance. |
| `SentientBeing.snackmultiplier` | 5 | Multiplier for Magicule Regeneration via Snack For Later (doubled on mastery). |
| `SentientBeing.bondsCooldown` | 120 | Cooldown for activating Family Bonds!. |
