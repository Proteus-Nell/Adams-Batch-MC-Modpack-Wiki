# Divine General Mahoraga

<small>[TensuraMoreSkills](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![Divine General Mahoraga](../../../assets/icons/tensuramoreskills/skill/divine_general_mahoraga.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `tensuramoreskills:divine_general_mahoraga` |
| **Modes** | 2 |
| **Cooldowns (s)** | 20, 200 |
| **Activation** | Toggle, Press |

</div>

> A King-Class Ultimate that adapts to everything it survives.

## Modes

| # | Mode |
|---|---|
| 1 | Summon Sword |
| 2 | Adapted |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when an effect is applied to you
- Triggers when you respawn
- Does something when first learned
- Does something when mastered

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| degrade | 1 | add |

## Related

- **Related skills:** [Cold Resistance](../../../tensura-reincarnated/abilities/resistance-skills/cold-resistance.md), [Cold Nullification](../../../tensura-reincarnated/abilities/resistance-skills/cold-nullification.md), [Corrosion Resistance](../../../tensura-reincarnated/abilities/resistance-skills/corrosion-resistance.md), [Corrosion Nullification](../../../tensura-reincarnated/abilities/resistance-skills/corrosion-nullification.md), [Darkness Attack Resistance](../../../tensura-reincarnated/abilities/resistance-skills/darkness-attack-resistance.md), [Darkness Attack Nullification](../../../tensura-reincarnated/abilities/resistance-skills/darkness-attack-nullification.md), [Earth Attack Resistance](../../../tensura-reincarnated/abilities/resistance-skills/earth-attack-resistance.md), [Earth Attack Nullification](../../../tensura-reincarnated/abilities/resistance-skills/earth-attack-nullification.md), [Electricity Resistance](../../../tensura-reincarnated/abilities/resistance-skills/electricity-resistance.md), [Electricity Nullification](../../../tensura-reincarnated/abilities/resistance-skills/electricity-nullification.md), [Flame Attack Resistance](../../../tensura-reincarnated/abilities/resistance-skills/flame-attack-resistance.md), [Flame Attack Nullification](../../../tensura-reincarnated/abilities/resistance-skills/flame-attack-nullification.md), [Gravity Attack Resistance](../../../tensura-reincarnated/abilities/resistance-skills/gravity-attack-resistance.md), [Gravity Attack Nullification](../../../tensura-reincarnated/abilities/resistance-skills/gravity-attack-nullification.md), [Holy Attack Resistance](../../../tensura-reincarnated/abilities/resistance-skills/holy-attack-resistance.md), [Holy Attack Nullification](../../../tensura-reincarnated/abilities/resistance-skills/holy-attack-nullification.md), [Light Attack Resistance](../../../tensura-reincarnated/abilities/resistance-skills/light-attack-resistance.md), [Light Attack Nullification](../../../tensura-reincarnated/abilities/resistance-skills/light-attack-nullification.md), [Magic Resistance](../../../tensura-reincarnated/abilities/resistance-skills/magic-resistance.md), [Magic Nullification](../../../tensura-reincarnated/abilities/resistance-skills/magic-nullification.md) and 5 more
- **Effects:** [Instant Regeneration](../../../tensura-reincarnated/effects/instant-regeneration.md), [Self-Regeneration](../../../tensura-reincarnated/effects/self-regeneration.md)
- **Items:** [Extermination Blade](../../items/weapons/extermination-blade.md), [Dead End Rainbow](../../../tensura-reincarnated/items/weapons/dead-end-rainbow.md)
- **Summons / entities:** [Severance](../../../tensura-reincarnated/enchantments/severance.md), [Energy Steal](../../../tensura-reincarnated/enchantments/energy-steal.md)

## Stats (config defaults)

Set in [`config/tensuramoreskills-grand.toml`](../../configs/config-tensuramoreskills-grand.md).

| Option | Default | Description |
|---|---|---|
| `mastery_bonus.masteredResistanceDegradationBonus` | 1 (0 to 1,000) | Flat Resistance Degradation bonus while Mahoraga is mastered. |
| `timing.learningBonusIntervalTicks` | 20 (1 to no limit) | How often the global mastery bonus applies while toggled. |
| `timing.learningBonusAmount` | 50 (0 to no limit) | Mastery points granted to learned skills each interval. |
| `timing.bladeAlreadyOwnedCooldownTicks` | 20 (0 to no limit) | Cooldown if the player already has the Extermination Blade. |
| `timing.bladeCooldownTicks` | 200 (0 to no limit) | Cooldown after summoning the Extermination Blade. |
| `adaptation_reduction.gainNullAfterHits` | 2 (1 to no limit) | Hits taken from a damage bucket before Mahoraga learns the matching nullification skill. |
| `outgoing_stage_damage.masteredOutgoingDamageBonus` | 0.1 (0 to 100) | Extra outgoing damage multiplier added when mastered. 0.10 = +10 percent. |
| `regeneration.playerRegenRefreshBelowTicks` | 200 (0 to no limit) | Refresh player regeneration when remaining duration falls below this. |
| `regeneration.playerRegenAmplifier` | 1 (0 to 255) | Instant Regeneration amplifier for players. 0 means level 1. |
| `regeneration.playerRegenDurationTicks` | 240 (1 to no limit) | Instant Regeneration duration applied to players while toggled. |
| `regeneration.mobRegenRefreshBelowTicks` | 200 (0 to no limit) | Refresh mob regeneration when remaining duration falls below this. |
| `regeneration.mobRegenAmplifier` | 30 (0 to 255) | Self Regeneration amplifier for non-players. |
| `regeneration.mobRegenDurationTicks` | 240 (1 to no limit) | Self Regeneration duration applied to non-players. |
| `stage_thresholds.stage5BuiltHits` | 5 (1 to no limit) | Hits needed for learned stage 5. |
| `stage_thresholds.stage4BuiltHits` | 4 (1 to no limit) | Hits needed for learned stage 4. |
| `stage_thresholds.stage3BuiltHits` | 3 (1 to no limit) | Hits needed for learned stage 3. |
| `stage_thresholds.stage2BuiltHits` | 2 (1 to no limit) | Hits needed for learned stage 2. |
| `adaptation_reduction.maxDamageReductionMasteredPercent` | 50 (0 to 99) | Maximum percent damage reduction when mastered. |
| `adaptation_reduction.maxDamageReductionUnmasteredPercent` | 25 (0 to 99) | Maximum percent damage reduction before mastery. |
| `adaptation_reduction.baseDamageReductionPercent` | 1 (0 to 99) | Base percent damage reduction when a damage adaptation is enabled. |
| `adaptation_reduction.hitsPerExtraReductionPercent` | 3 (1 to no limit) | Extra hits needed for each additional 1 percent damage reduction. |
| `outgoing_stage_damage.stage2DamageMultiplier` | 1.15 (0 to 100) | Outgoing damage multiplier at learned stage 2. |
| `outgoing_stage_damage.stage3DamageMultiplier` | 1.3 (0 to 100) | Outgoing damage multiplier at learned stage 3. |
| `outgoing_stage_damage.stage4DamageMultiplier` | 1.45 (0 to 100) | Outgoing damage multiplier at learned stage 4. |
| `outgoing_stage_damage.stage5TensuraDamageMultiplier` | 1.9 (0 to 100) | Outgoing damage multiplier at learned stage 5 for Tensura resistance buckets. |
| `outgoing_stage_damage.stage5DamageMultiplier` | 1.7 (0 to 100) | Outgoing damage multiplier at learned stage 5 for non-Tensura-typed buckets. |

## In-game messages

<details markdown><summary>Show 15 messages</summary>

- No adaptations recorded yet.
- Press a row to select it. Use Toggle to enable or disable the selected adaptation.
- ✦ Sword of Extermination resummoned.
- ✦ Adapted Effects (Shift = Toggle Selected)
- ✦ Enabled: %s
- ✦ Disabled: %s
- ✦ Adapted: %s
- ✦ You adapted: Severance Immunity.
- ✦ Mahoraga adapts: Your attacks now carry Severance.
- ✦ You adapted: Cook Immunity.
- ✦ Mahoraga adapts: Your attacks now carry Cook.
- ✦ Adaptation (%s): Nullification acquired.
- ✦ Adaptation (%s): Resistance bypassed.
- ✦ Adaptation (%s): Nullification degraded.
- ✦ Adaptation (%s): Nullification bypassed.

</details>
