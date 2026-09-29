# Infinity

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Infinity](../../../assets/icons/trnightmare/skill/infinity.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:infinity` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 150,000 |
| **Activation** | Press, Hold |

</div>

> Infinity is a unique and incredibly powerful Enchantment-Type Unique Skill. Its effects are so outside the norm of most magic, that it's been called unfair and cheating.

## Modes

| # | Mode |
|---|---|
| 1 | Spellbook |
| 2 | Cancel |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when you damage a target
- Triggers when you are attacked
- Triggers when an effect is applied to you

## Obtaining

- Listed in the `astralExtraUniqueSkills` config option (config/nightmare/ability/skill/nightmare_ult.toml): Extra unique skill IDs merged into Astral Light Skill Creation (after Tensura Creator).

## Related

- **Effects:** [Magic Interference](../../../tensura-reincarnated/effects/magic-interference.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `infinitySettings.epAcquirement` | 150,000 | EP obtainment cost to acquire Infinity. |
| `infinitySettings.magicDamageBoostPercent` | 10 | Magic Damage boost % while Infinity is in-slot (reserved / attribute hooks). |
| `infinitySettings.magicDamageBoostId` | "d1a3e2b1-8f2a-4c9b-9f1a-123456789abc" | UUID for Magic Damage boost attribute modifier (TOML has no UUID type; use string). |
| `infinitySettings.cancelRange` | 20 | Range for Absolute Cancel targeting. |
| `infinitySettings.cancelRadius` | 12 | Radius for AoE Absolute Cancel when shift-used. |
| `infinitySettings.learnChance` | 0.15 | Chance to learn magic when exposed to it. |
| `infinitySettings.learnChanceMastered` | 0.35 | Chance to learn magic when Infinity is mastered. |
| `infinitySettings.copyRangeMagic` | 20 | Range for learning magic from projectiles. |
| `infinitySettings.copyCooldownSuccess` | 40 | Cooldown after successfully learning magic from a projectile. |
| `infinitySettings.copyCooldownFail` | 20 | Cooldown after failing to learn magic from a projectile. |
| `infinitySettings.tensuraMagicFlatBonus` | 20 | Flat bonus damage when using Tensura magic while toggled. |
| `infinitySettings.absoluteCancelMagiculeCost` | 0 | Magicule cost for Absolute Cancel (mode 1); 0 = no cost. |
| `infinitySettings.absoluteCancelCooldownTicks` | 0 | Cooldown in ticks for Absolute Cancel after use. |
