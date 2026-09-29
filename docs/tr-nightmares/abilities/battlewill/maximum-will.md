# Maximum Will

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `trnightmare:maximum_will` |
| **Cooldowns (s)** | 10 |
| **Activation** | Hold |

</div>

> Hold to enter a counter stance. Incoming attacks can be dodged, then punished on release with heavy retaliatory damage.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 15,000 or 12,000 |

## How it works

- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Acquisition checks: [Violent Break](../../../tensura-reincarnated/abilities/battlewill/violent-break.md), [Battlewill](../../../tensura-reincarnated/abilities/battlewill/battlewill.md)

## Related

- **Related skills:** [Violent Break](../../../tensura-reincarnated/abilities/battlewill/violent-break.md), [Battlewill](../../../tensura-reincarnated/abilities/battlewill/battlewill.md)
- **Effects:** [Anti-Skill](../../../tensura-reincarnated/effects/anti-skill.md)
- **Referenced by:** [Alteration](../extra-skills/alteration.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/battlewill/nightmare_battlewill.toml`](../../configs/config-nightmare-ability-battlewill-nightmare-battlewill.md).

| Option | Default | Description |
|---|---|---|
| `MaximumWill.learningAuraCost` | 15,000 | Aura point cost used while learning Maximum Will. |
| `MaximumWill.auraCostPerSecond` | 12,000 | Aura cost per second while holding. |
| `MaximumWill.damageMultiplier` | 5 | Damage multiplier on counter-attack release. |
| `MaximumWill.masteredDamageMultiplier` | 10 | Mastered damage multiplier on counter-attack release. |
| `MaximumWill.masteredMpCostPerSecond` | 5,000 | MP cost per second while holding and mastered. |
| `MaximumWill.cooldownSeconds` | 10 | Cooldown in seconds after releasing Maximum Will. |

## In-game messages

<details markdown><summary>Show 2 messages</summary>

- Maximum Will - Counter Stance \| Dodges: %1$s
- Dodged! (%1$s total)

</details>
