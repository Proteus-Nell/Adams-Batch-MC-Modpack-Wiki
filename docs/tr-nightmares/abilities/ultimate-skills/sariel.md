# ｢ Sariel, Lord of Hope ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![｢ Sariel, Lord of Hope ｣](../../../assets/icons/trnightmare/skill/sariel.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:sariel` |
| **Modes** | 4 |
| **Acquisition cost (MP)** | 500,000 |
| **Max mastery** | 5,000 |
| **Cooldowns (s)** | 5, 7, 10 |
| **Activation** | Press, Hold |

</div>

> Ultimate of Unyielding — hope, backup, fortitude, and life domination.

## Modes

| # | Mode |
|---|---|
| 1 | Backup |
| 2 | Life Domination: Empower |
| 3 | Fortitude |
| 4 | Life Domination: Reconstruction |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | *set by config (base cost (ego ultimate cost))* |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers when you are attacked
- Triggers when you die
- Triggers when one of your subordinates dies

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| degrade | 5 | add |

## Obtaining

- Listed in the `virtueDominionSkills` config option (config/nightmare/ability/skill/nightmare_ult.toml): Virtue skills that Ultimate Dominion can copy from targets.
- Listed in the `skillEngraveBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skills that cannot be engraved through Amatsumara skill engrave.
- Listed in the `globalSkillsBlacklist` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): List of Skill registry names that cannot be copied. Format: modid:skill_name

## Related

- **Related skills:** [Cook](../../../tensura-reincarnated/abilities/unique-skills/cook.md), [｢ Susanoo, Lord of Tyranny ｣](susanoo.md)
- **Effects:** [Strengthen](../../../tensura-reincarnated/effects/strengthen.md), [Haki Coat](../../../tensura-reincarnated/effects/haki-coat.md), [Hopes Gift](../../effects/hopes-gift.md)
- **Referenced by:** [｢ Yog-Sothoth, Lord of Space-Time ｣](yog-sothoth.md), [Hopeful Manas](hopeful-manas.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Sariel.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Sariel.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Sariel.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Sariel.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Sariel.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Sariel.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Sariel.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Sariel.mpAcquirement` | 500,000 | Magicule obtainment cost. |
| `Sariel.reconstructionCooldownSeconds` | 5 | Reconstruction cooldown after release (Tensura seconds). |
| `Sariel.reconstructionMagiculeDrainPerSecond` | 10,000 | Reconstruction magicule drain per second while channeling. |
| `Sariel.reconstructionHealPerSecond` | 50 | Reconstruction HP/SHP healed per second to owner and subordinates. |
| `Sariel.fortitudeCooldownSeconds` | 7 | Fortitude cooldown after a successful drain (Tensura seconds). |
| `Sariel.fortitudeNoUltimateEpRatio` | 0.5 | Fortitude EP ratio threshold for no-ultimate drain tier. |
| `Sariel.fortitudeNoUltimateDrain` | 0.99 | Fortitude drain ratio when target has no ultimate and is below threshold. |
| `Sariel.fortitudeTier1EpRatio` | 0.3 | Fortitude EP ratio threshold for tier 1 drain. |
| `Sariel.fortitudeTier1Drain` | 0.8 | Fortitude tier 1 drain ratio. |
| `Sariel.fortitudeTier2EpRatio` | 0.5 | Fortitude EP ratio threshold for tier 2 drain. |
| `Sariel.fortitudeTier2Drain` | 0.6 | Fortitude tier 2 drain ratio. |
| `Sariel.fortitudeTier3EpRatio` | 0.7 | Fortitude EP ratio threshold for tier 3 drain. |
| `Sariel.fortitudeTier3Drain` | 0.4 | Fortitude tier 3 drain ratio. |
| `Sariel.magicCancelEpThreshold` | 0.5 | Magic attack cancel EP threshold multiplier while unmastered. |
| `Sariel.magicCancelEpThresholdMastered` | 0.75 | Magic attack cancel EP threshold multiplier while mastered. |
| `Sariel.empowerDurationTicks` | 1,200 | Empower buff duration (ticks). |
| `Sariel.empowerResistanceAmplifier` | 1 | Empower DAMAGE_RESISTANCE amplifier. |
| `Sariel.empowerStrengthenAmplifier` | 4 | Empower STRENGTHEN amplifier. |
| `Sariel.empowerHakiCoatAmplifier` | 0 | Empower HAKI_COAT amplifier. |
| `Sariel.empowerDegradeBonus` | 5 | Empower RESISTANCE_DEGRADATION bonus value. |
| `Sariel.empowerCooldownSeconds` | 10 | Empower cooldown (Tensura seconds). |
| `Sariel.fortitudeParticleIntervalTicks` | 3 | Fortitude particle interval (ticks). |
| `Sariel.fortitudeParticleCount` | 12 | Fortitude particle count per burst. |
| `Sariel.fortitudeParticleOffsetX` | 0.5 | Fortitude particle X offset spread. |
| `Sariel.fortitudeParticleOffsetY` | 0.6 | Fortitude particle Y offset spread. |
| `Sariel.fortitudeParticleOffsetZ` | 0.5 | Fortitude particle Z offset spread. |
| `Sariel.fortitudeParticleSpeed` | 0.02 | Fortitude particle speed. |
| `Sariel.naturalDomainAuraRegenMultiplier` | 4 | Natural Domain aura regeneration multiplier bonus. |
| `Sariel.naturalDomainSpiritualRegenMultiplier` | 4 | Natural Domain spiritual health regeneration multiplier bonus. |
| `Sariel.hopeGiftDurationTicks` | 100 | Hope Gift effect duration (ticks). |
| `Sariel.subordinateEffectRadius` | 64 | Radius used for subordinate effect/heal propagation (blocks). |
| `Sariel.evolutionRaidWins` | 10 | Raid wins required to evolve Unyielding into Sariel. |
| `Sariel.evolutionNamedSubordinates` | 25 | Named subordinates required to evolve Unyielding into Sariel. |
| `Sariel.evolutionMobKills` | 100 | Mob kills required to evolve Unyielding into Sariel. |
| `Sariel.enableUltimateEvolution` | true | Whether Sariel evolution is allowed. |

## In-game messages

<details markdown><summary>Show 1 messages</summary>

- Current bond points with %s: %s

</details>

## Tags

`tensura:skills/hopeful`, `tensura:skills/ultimate_skills`
