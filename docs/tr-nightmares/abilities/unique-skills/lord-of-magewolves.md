# Lord of Magewolves

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:lord_of_magewolves` |
| **Modes** | 4 |
| **Acquisition cost (MP)** | 55,000 |
| **Cooldowns (s)** | 5 |
| **Activation** | Toggle, Press, Hold |

</div>

> Command a growing magewolf pack and enhance your abilities with their own.

## Modes

| # | Mode |
|---|---|
| 1 | Tribe Summon |
| 2 | Tribe Regeneration |
| 3 | Assimilation |
| 4 | Will Manipulation |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Adjusted by scrolling while active
- Triggers when you die
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| melee | 10 | add |
| projectile | 10 | add |

## Related

- **Effects:** [Instant Regeneration](../../../tensura-reincarnated/effects/instant-regeneration.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `UltraInstinct.meleeDodge` | 10 | Melee Dodge Chance when activated. |
| `UltraInstinct.projectileDodge` | 10 | Projectile Dodge Chance when activated. |

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `lordOfMagewolves.mpAcquirement` | 55,000 | Magicule obtainment cost. |
| `lordOfMagewolves.mpAcquirement` | 55,000 | Magicule obtainment cost. |
| `lordOfMagewolves.maxMastery` | 1,000 | Max mastery. |

## In-game messages

<details markdown><summary>Show 26 messages</summary>

- Summoned %s direwolf allies.
- Your pack cannot exceed twelve direwolves from this skill.
- Only one Star Tempest wolf may exist from this skill.
- Your pack is now known as %s.
- Master Lord of Magewolves to name your pack.
- Pack name cannot be empty.
- No valid pack member or subordinate to assimilate.
- Assimilated %s.
- Released %s from assimilation.
- Neutral
- Passive
- Aggressive
- Protect
- Will command: %s
- Pack set to neutral.
- Pack set to passive.
- Pack set to aggressive.
- Pack set to protect.
- Follow
- Pack will set to Follow.
- Stay
- Pack will set to Stay.
- Guard
- Pack will set to Guard.
- Hunt
- Pack will set to Hunt.

</details>
