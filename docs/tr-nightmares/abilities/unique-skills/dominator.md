# Dominator

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Dominator](../../../assets/icons/trnightmare/skill/dominator.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:dominator` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 90,000 |
| **Cooldowns (s)** | 120 mastered, 240 otherwise |
| **Activation** | Press, Hold |

</div>

> Command Heaven itself. Take the throne, seize control, and claim their skills as your own.

## Modes

| # | Mode |
|---|---|
| 1 | Angelic Incarnation |
| 2 | Heavenly Barrier |
| 3 | Kings Command |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Triggers when you are attacked

## Obtaining

- Listed in the `egoWhitelist` config option (config/nightmare/ability/skill/ego/general_config.toml): Skills allowed to develop ego if in whitelist mode
- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.
- Listed in the `globalSkillsBlacklist` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): List of Skill registry names that cannot be copied. Format: modid:skill_name

## Related

- **Referenced by:** [｢ Michael, Lord of Justice ｣](../ultimate-skills/michael.md), [｢ Yog-Sothoth, Lord of Space-Time ｣](../ultimate-skills/yog-sothoth.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `dominator.mpAcquirement` | 90,000 | Magicule obtainment cost. |
| `dominator.mpAcquirement` | 90,000 | Magicule obtainment cost. |
| `dominator.maxMastery` | 1,000 | Max mastery. |

## In-game messages

<details markdown><summary>Show 10 messages</summary>

- You have dominated and copied %s!
- The king's command has been heard
- Summoning angel knight... %ss / %ss
- King's Authority... %ss / %ss
- Angel Knight
- Castle Guard needs at least %s subordinates.
- Castle Guard ended — out of magicule.
- Castle Guard duration ended.
- Dominator Kings Authority Low Ep
- Dominator Kings Authority No Mp

</details>

## Tags

`tensura:skills/justice`
