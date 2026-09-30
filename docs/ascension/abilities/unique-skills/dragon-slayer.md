# Dragon Slayer

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Dragon Slayer](../../../assets/icons/ascension/skill/dragon_slayer.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `ascension:dragon_slayer` |
| **Modes** | 2 |
| **Activation** | Press |

</div>

> Toggle: dragons treat you as neutral; your Ice/Fire/Thunder Breath bypass resistances. Grants Ice/Fire/Thunder Breath and Dragon Skin/Ear/Eye automatically. Eating a Dragon Essence permanently adds +20 max HP (uncapped, reset on death). Modes: Dragon Infusion (consume a Dragon Heart in hand for +20,000 EP), Dragon Rage (Strength X for 30s, 60s cooldown).

## Modes

| # | Mode |
|---|---|
| 1 | Dragon Infusion |
| 2 | Dragon Rage |

## How it works

- Activated by pressing the skill key

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| attr | target | add |

## Obtaining

- Listed in the `additionalUniqueSkills` config option (config/tensura/ascension-common.toml): Unique skills added to the reincarnation pool. Remove an entry to exclude that skill from random reincarnation rolls.

## Related

- **Related skills:** [Dragon Skin](../../../tensura-reincarnated/abilities/intrinsic-skills/dragon-skin.md), [Dragon Ear](../../../tensura-reincarnated/abilities/intrinsic-skills/dragon-ear.md), [Dragon Eye](../../../tensura-reincarnated/abilities/intrinsic-skills/dragon-eye.md)
- **Summons / entities:** [Ice Breath](../../../tensura-reincarnated/abilities/intrinsic-skills/ice-breath.md), [Flame Breath](../../../tensura-reincarnated/abilities/intrinsic-skills/flame-breath.md), [Thunder Breath](../../../tensura-reincarnated/abilities/intrinsic-skills/thunder-breath.md), Tensura

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `dragon_slayer.enabled` | true | Enable Dragon Slayer. |
| `dragon_slayer.infusionEpGainMastered` | 40,000 (0 to 1,000,000,000) | EP granted per Dragon Heart consumed via Dragon Infusion, mastered. |
| `dragon_slayer.infusionEpGain` | 20,000 (0 to 1,000,000,000) | EP granted per Dragon Heart consumed via Dragon Infusion, unmastered. |
| `dragon_slayer.infusionCooldownSecondsMastered` | 2 (0 to 3,600) | Dragon Infusion cooldown (seconds), mastered. |
| `dragon_slayer.infusionCooldownSeconds` | 5 (0 to 3,600) | Dragon Infusion cooldown (seconds), unmastered. |
| `dragon_slayer.rageDurationSecondsMastered` | 60 (1 to 3,600) | Dragon Rage strength duration (seconds), mastered. |
| `dragon_slayer.rageDurationSeconds` | 30 (1 to 3,600) | Dragon Rage strength duration (seconds), unmastered. |
| `dragon_slayer.rageAmplifierMastered` | 14 (0 to 127) | Strength amplifier applied by Dragon Rage, mastered (14 = Strength XV). |
| `dragon_slayer.rageAmplifier` | 9 (0 to 127) | Strength amplifier applied by Dragon Rage, unmastered (9 = Strength X). |
| `dragon_slayer.rageCooldownSecondsMastered` | 30 (0 to 3,600) | Dragon Rage cooldown (seconds), mastered. |
| `dragon_slayer.rageCooldownSeconds` | 60 (0 to 3,600) | Dragon Rage cooldown (seconds), unmastered. |
| `slayer_of_dragons.enabled` | true | Enable The Slayer of Dragons. |
| `slayer_of_dragons.essenceMaxHpPer` | 30 (0 to 1,000) | Permanent max-HP bonus per Dragon Essence / dragon flesh eaten while toggled on (no cap, reset on death). |
| `dragon_slayer.essenceMaxHpPer` | 20 (0 to 1,000) | Permanent max-HP bonus added per Dragon Essence eaten (no cap, reset on death). |

## In-game messages

<details markdown><summary>Show 2 messages</summary>

- No Dragon Heart in hand.
- Dragon Heart consumed. +%s EP.

</details>

## Tags

`tensura:skills/unique_skills`
