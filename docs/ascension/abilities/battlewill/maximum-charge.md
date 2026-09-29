# Maximum Charge

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

![Maximum Charge](../../../assets/icons/ascension/skill/maximum_charge.png)

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `ascension:maximum_charge` |
| **Activation** | Hold |

</div>

> Hold: regen 10% max magicule/s (15% mastered) at the cost of 2% max aura/s. Auto-learned at 100,000 EP once Energy Charge is mastered.

## How it works

- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Related

- **Summons / entities:** Maximum Charge Aura

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `maximum_charge.auraRestorePerSecMastered` | 0.15 (0 to 10) | Fraction of max aura restored per second, mastered. |
| `maximum_charge.auraRestorePerSec` | 0.1 (0 to 10) | Fraction of max aura restored per second, unmastered. |
| `maximum_charge.magiculeCostPerSec` | 0.06 (0 to 10) | Fraction of max magicule consumed per second. |
| `maximum_charge.enabled` | true | Enable Maximum Charge (and block its EP auto-unlock when false). |
| `maximum_charge.slownessAmplifier` | 3 (0 to 127) | Slowness amplifier applied while channeling. 0 = Slowness I, 1 = Slowness II, ... |
| `maximum_charge.maxHeldSeconds` | 5 (1 to 300) | Maximum seconds the skill can be channeled before it force-releases and goes on cooldown. |
| `maximum_charge.cooldownSeconds` | 5 (0 to 600) | Cooldown (seconds) applied on release — both force-release at the cap and early release. |
| `energy_charge.auraRestorePerSecMastered` | 0.07 (0 to 10) | Fraction of max aura restored per second, mastered. |
| `energy_charge.auraRestorePerSec` | 0.05 (0 to 10) | Fraction of max aura restored per second, unmastered. |
| `energy_charge.magiculeCostPerSec` | 0.03 (0 to 10) | Fraction of max magicule consumed per second. |
| `energy_charge.enabled` | true | Enable Energy Charge (and block its EP auto-unlock when false). |
| `energy_charge.slownessAmplifier` | 1 (0 to 127) | Slowness amplifier applied while channeling. 0 = Slowness I, 1 = Slowness II, ... |
| `energy_charge.maxHeldSeconds` | 5 (1 to 300) | Maximum seconds the skill can be channeled before it force-releases and goes on cooldown. |
| `energy_charge.cooldownSeconds` | 5 (0 to 600) | Cooldown (seconds) applied on release — both force-release at the cap and early release. |

## Tags

`tensura:skills/battlewill`
