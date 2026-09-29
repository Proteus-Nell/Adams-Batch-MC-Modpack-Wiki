# The Slayer of Dragons

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![The Slayer of Dragons](../../../assets/icons/ascension/skill/slayer_of_dragons.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `ascension:slayer_of_dragons` |
| **Modes** | 3 |
| **Max mastery** | 100 |
| **Cooldowns (s)** | 10, 300, 30 |
| **Activation** | Press, Hold |

</div>

> Ultimate awakening of Dragon Slayer. Toggle on for: peace with all dragons; ice/fire/thunder breath bypass resistances; +30 Max HP per dragon essence or Ice&amp;Fire flesh eaten (no cap, removed on death); each dragon kill permanently grants +50,000 Max EP and +1 armor. Modes: Dragon Infusion (consume held Dragon Heart for +40k/+50k EP), Draconic Rage (5 min of Strength XX + Strengthen V + Resistance III), Dragon King Roar (held — fires Ice + Flame + Thunder breaths simultaneously).

## Modes

| # | Mode |
|---|---|
| 1 | Dragon Infusion |
| 2 | Draconic Rage |
| 3 | Dragon King Roar |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| armor | next | add |

## Related

- **Effects:** [Strengthen](../../../tensura-reincarnated/effects/strengthen.md)
- **Summons / entities:** [Flame Breath](../../../tensura-reincarnated/abilities/intrinsic-skills/flame-breath.md), [Ice Breath](../../../tensura-reincarnated/abilities/intrinsic-skills/ice-breath.md), [Thunder Breath](../../../tensura-reincarnated/abilities/intrinsic-skills/thunder-breath.md), Tensura

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `slayer_of_dragons.enabled` | true | Enable The Slayer of Dragons. |
| `slayer_of_dragons.infusionEpGainMastered` | 50,000 (0 to 1,000,000,000) | EP granted per Dragon Heart consumed via Dragon Infusion, mastered. |
| `slayer_of_dragons.infusionEpGain` | 40,000 (0 to 1,000,000,000) | EP granted per Dragon Heart consumed via Dragon Infusion, unmastered. |
| `slayer_of_dragons.infusionCooldownSeconds` | 10 (0 to 3,600) | Dragon Infusion cooldown (seconds). |
| `slayer_of_dragons.rageDurationSeconds` | 300 (1 to 3,600) | Draconic Rage duration (seconds). |
| `slayer_of_dragons.rageStrengthAmp` | 19 (0 to 127) | Strength amplifier applied by Draconic Rage (19 = Strength XX). |
| `slayer_of_dragons.rageStrengthenAmp` | 4 (0 to 127) | Tensura Strengthen amplifier applied by Draconic Rage (4 = Strengthen V; +6 attack damage per level). |
| `slayer_of_dragons.rageResistanceAmp` | 2 (0 to 127) | Resistance amplifier applied by Draconic Rage (2 = Resistance III). |
| `slayer_of_dragons.rageCooldownSeconds` | 300 (0 to 3,600) | Draconic Rage cooldown (seconds). |
| `slayer_of_dragons.roarSizeMultiplier` | 0.6 (0.1 to 5) | Cone-width multiplier applied to roar-spawned breath entities (0.6 = 40% narrower). Lower = tighter, more focused beam. Set 1.0 for vanilla width. |
| `slayer_of_dragons.roarLengthMultiplier` | 2 (1 to 10) | Range multiplier applied to roar-spawned breath entities (2.0 = 2x reach). |
| `slayer_of_dragons.roarDamageMastered` | 50 (0 to 1,000,000) | Per-hit damage for each breath stream while Dragon King Roar is held, mastered. |
| `slayer_of_dragons.roarDamage` | 25 (0 to 1,000,000) | Per-hit damage for each breath stream while Dragon King Roar is held, unmastered. Overrides Tensura's base breath damage. Tensura's elemental Domination toggle (FLAME/WATER/LIGHTNING_BOOST) scales this multiplicatively via the DamagingHandler attribute lookup; with no toggle on the corresponding element this is the raw landed damage. |
| `slayer_of_dragons.roarCooldownSeconds` | 30 (0 to 3,600) | Dragon King Roar cooldown applied on key release (seconds). |
| `slayer_of_dragons.killEpBonus` | 50,000 (0 to 1,000,000,000) | Permanent Max EP granted per dragon kill while toggled on. Split 50/50 across MAX_AURA + MAX_MAGICULE. |
| `slayer_of_dragons.killArmorBonus` | 1 (0 to 100) | Permanent ARMOR granted per dragon kill while toggled on (stacks via a single growing modifier). |

## In-game messages

<details markdown><summary>Show 1 messages</summary>

- A dragon falls. +%s Max EP, +1 armor.

</details>
