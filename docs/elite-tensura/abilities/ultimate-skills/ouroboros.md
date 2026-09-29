# Ouroboros, Lord of Eternity

<small>[Elite Tensura](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![Ouroboros, Lord of Eternity](../../../assets/icons/elitetensura/skill/ouroboros.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `elitetensura:ouroboros` |
| **Modes** | 5 |
| **Acquisition cost (MP)** | 0 |
| **Max mastery** | 10,000 |
| **Cooldowns (s)** | 8, 15 mastered, 30 otherwise, 60, 12, 600 |
| **Activation** | Toggle, Press |

</div>

> The serpent that devours its own tail. Feed on the fight, strike across seconds, shed what wounds you, rewind your missteps, complete death rather than avoid it, and devour what stands before you.

## Modes

| # | Mode |
|---|---|
| 1 | Timeless Fangs |
| 2 | Molt |
| 3 | Coil Back |
| 4 | Cycle's End |
| 5 | Serpent's Maw |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Timeless Fangs | 3,000 |  |
| Molt | 2,000 |  |
| Coil Back | 20,000 |  |
| other modes | 0 |  |
| Serpent's Maw | 10,000 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Triggers when you damage a target
- Triggers when you die
- Triggers when you respawn

## Obtaining

- Acquisition checks: [Survivor](../../../tensura-reincarnated/abilities/unique-skills/survivor.md), [Gourmet](../../../tensura-reincarnated/abilities/unique-skills/gourmet.md)

## Related

- **Related skills:** [Survivor](../../../tensura-reincarnated/abilities/unique-skills/survivor.md), [Gourmet](../../../tensura-reincarnated/abilities/unique-skills/gourmet.md)
- **Effects:** [Eternal Renewal](../../effects/eternal-renewal.md), [Cycle's End](../../effects/cycle-armed.md), [Cycle Debt](../../effects/cycle-debt.md)
- **Summons / entities:** [Severance](../../../tensura-reincarnated/enchantments/severance.md)

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/UltimateSkillConfig.toml`](../../configs/config-tensura-elitetensura-ultimateskillconfig.md).

| Option | Default | Description |
|---|---|---|
| `OuroborosSkill.IsEnabled` | true | Is this Skill Enabled? |
| `OuroborosSkill.renewalHealFraction` | 0.15 | Fraction of dealt damage returned as healing while toggled. |
| `OuroborosSkill.renewalShpHealFraction` | 0.15 | Fraction of dealt damage returned as spiritual health while toggled (0 disables). |
| `OuroborosSkill.renewalMagiculeFraction` | 0.1 | Fraction of dealt damage returned as magicule while toggled. |
| `OuroborosSkill.renewalDamagePenalty` | 0.2 | Outgoing damage penalty while toggled. Keeps returned value below sacrificed value (the loop leaks). |
| `OuroborosSkill.fangsCost` | 3,000 | Magicule cost to prime the fangs. |
| `OuroborosSkill.fangsPrimeTicks` | 100 | Ticks the prime lasts waiting for a hit. |
| `OuroborosSkill.fangsEchoBonusPerStep` | 0.25 | Bonus per successive echo (echo 1 = 1x+bonus, echo 2 = 1x+2xbonus). |
| `OuroborosSkill.fangsEchoDelayTicks` | 20 | Ticks between the strikes (hit, +delay, +2xdelay). |
| `OuroborosSkill.fangsCooldown` | 8 | Cooldown in seconds of Timeless Fangs. |
| `OuroborosSkill.moltCostPerDebuff` | 2,000 | Magicule cost per harmful effect shed. |
| `OuroborosSkill.moltBaseAbsorption` | 4 | Base absorption granted on any successful molt (2.0 = 1 heart). |
| `OuroborosSkill.moltAbsorptionPerDebuff` | 2 | Absorption granted per debuff shed. |
| `OuroborosSkill.moltCooldown` | 30 | Cooldown in seconds of Molt. |
| `OuroborosSkill.moltCooldownMastered` | 15 | Cooldown in seconds of Molt when mastered. |
| `OuroborosSkill.coilBackCost` | 20,000 | Magicule cost of the rewind. |
| `OuroborosSkill.coilBackRewindTicks` | 100 | How far back the rewind reaches, in ticks. |
| `OuroborosSkill.coilBackHealFraction` | 0.5 | Fraction of HP lost over the window that the rewind restores. |
| `OuroborosSkill.coilBackCooldown` | 60 | Cooldown in seconds of Coil Back. |
| `OuroborosSkill.coilBackShockwaveRadius` | 4 | Radius in blocks of the arrival shockwave (set base and fraction to 0 to disable). |
| `OuroborosSkill.coilBackShockwaveBase` | 50 | Flat base damage of the arrival shockwave. |
| `OuroborosSkill.coilBackShockwaveFraction` | 5 | Extra shockwave damage per point of HP restored by the rewind. |
| `OuroborosSkill.cycleArmCostFraction` | 0.5 | Fraction of MAX magicule paid to arm the cycle. |
| `OuroborosSkill.cycleArmedDurationTicks` | 6,000 | Duration in ticks of the armed state (the visible effect icon). |
| `OuroborosSkill.rebirthHealthFraction` | 0.3 | Fraction of max HP restored on rebirth. |
| `OuroborosSkill.cycleDebtDurationTicks` | 12,000 | Duration in ticks of one Cycle Debt application. |
| `OuroborosSkill.cycleCooldown` | 600 | Cooldown in seconds of arming Cycle's End. |
| `OuroborosSkill.mawCost` | 10,000 | Magicule cost of the bite. |
| `OuroborosSkill.mawRange` | 6 | Cone reach in blocks. |
| `OuroborosSkill.mawAngle` | 90 | Full cone angle in degrees. |
| `OuroborosSkill.mawBaseDamage` | 100 | Flat damage per target. |
| `OuroborosSkill.mawMaxHpFraction` | 0.1 | Fraction of target max HP added as damage. |
| `OuroborosSkill.mawHealFraction` | 0.25 | Fraction of total damage dealt returned as healing. |
| `OuroborosSkill.mawCooldown` | 12 | Cooldown in seconds of Serpent's Maw. |
| `OuroborosSkill.friendlyFire` | false | If true, Coil Back's shockwave and Serpent's Maw also hit players in the user's own nation or hunt party. |

Set in [`config/tensura/ability/skill_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-skill-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryUltimate` | 10,000 | The max amount of mastery point for Ultimate Skills. |
| `Mastery.masteryIntrinsic` | 100 | The max amount of mastery point for Intrinsic Skills. |
| `Mastery.masteryExtra` | 500 | The max amount of mastery point for Extra Skills. |
| `Mastery.masteryUnique` | 1,000 | The max amount of mastery point for Unique Skills. |
| `Mastery.masteryUniqueSin` | 1,500 | The max amount of mastery point for Unique Skills of Sins. |
| `Mastery.masteryUltimate` | 10,000 | The max amount of mastery point for Ultimate Skills. |

## Tags

`tensura:skills/no_plundering`, `tensura:skills/ultimate_skills`
