# Endorse

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:endorse` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 90,000 |
| **Max mastery** | 1,000 |
| **Activation** | Press |

</div>

> A unique skill that amplifies your cause. Encore bolsters barriers and battle poise; Stockpile charges your next strike with flame and lightning.

## Modes

| # | Mode |
|---|---|
| 1 | Encore |
| 2 | Stockpile |

## How it works

- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you damage a target

## Obtaining

- Listed in the `egoWhitelist` config option (config/nightmare/ability/skill/ego/general_config.toml): Skills allowed to develop ego if in whitelist mode
- Listed in the `virtueDominionSkills` config option (config/nightmare/ability/skill/nightmare_ult.toml): Virtue skills that Ultimate Dominion can copy from targets.

## Related

- **Referenced by:** [｢ Raguel, Lord of Charity ｣](../ultimate-skills/raguel.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `endorse.mpAcquirement` | 90,000 | Magicule obtainment cost. |
| `endorse.mpAcquirement` | 90,000 | Magicule obtainment cost. |
| `endorse.maxMastery` | 1,000 | Max mastery. |
| `endorse.stockpileCooldownSeconds` | 5 | Stockpile mode cooldown (Tensura seconds). |

## In-game messages

<details markdown><summary>Show 3 messages</summary>

- Encore applied to %s.
- Stockpile: %s%% charged.
- Stockpile is fully charged.

</details>

## Tags

`tensura:skills/joyful`
