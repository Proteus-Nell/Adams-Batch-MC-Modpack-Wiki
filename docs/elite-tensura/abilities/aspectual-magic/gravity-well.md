# Gravity Well

<small>[Elite Tensura](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Gravity Well](../../../assets/icons/elitetensura/skill/gravity_well.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `elitetensura:gravity_well` |
| **Max mastery** | 300 |
| **Cooldowns (s)** | 18 mastered, 25 otherwise |
| **Activation** | Hold |

</div>

> Gravity magic. Hold to warp space at the point you are aiming at, then release to collapse it into a crushing sphere that drags everything inside toward its centre, deals a fraction of each victim's max health every second, and smothers flight and dash escapes. When mastered, hold past the cast time to charge a wider, longer, harder-crushing well. Requires Burden mastered to learn.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 500 |  |

## How it works

- Triggers when the held key is released

## Related

- **Related skills:** [Burden](../../../tensura-reincarnated/abilities/aspectual-magic/burden.md)
- **Summons / entities:** [Gravity Well](gravity-well.md)

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/MagicConfig.toml`](../../configs/config-tensura-elitetensura-magicconfig.md).

| Option | Default | Description |
|---|---|---|
| `GravityWell.castTime` | 60 | Cast (charge) time in ticks (20 = 1s). |
| `GravityWell.castTimeMastered` | 40 | Cast (charge) time in ticks when mastered. |
| `GravityWell.magiculeCost` | 500 | Magicule cost per normal cast. |
| `GravityWell.magiculeCostCharged` | 900 | Magicule cost for the charged (mastered, held-longer) cast. |
| `GravityWell.cooldown` | 25 | Cooldown in seconds. |
| `GravityWell.cooldownMastered` | 18 | Cooldown in seconds when mastered. |
| `GravityWell.radius` | 6 | Sphere radius in blocks. |
| `GravityWell.radiusCharged` | 9 | Sphere radius for the charged cast. |
| `GravityWell.durationTicks` | 160 | How long the well lasts, in ticks (20 = 1s). |
| `GravityWell.durationTicksCharged` | 200 | Well duration in ticks for the charged cast. |
| `GravityWell.crushPercent` | 0.03 | Crush damage per second as a fraction of the victim's max health (0.03 = 3%). |
| `GravityWell.crushPercentCharged` | 0.05 | Crush fraction per second for the charged cast. |
| `GravityWell.crushDamageCap` | 100 | Hard cap on a single crush hit, in half-hearts of damage. Keeps percent-max-HP crush from melting huge-HP bosses. 0 = uncapped. |
| `GravityWell.pullStrength` | 0.15 | Inward pull strength per tick at the sphere's rim (pull weakens toward the centre). |
| `GravityWell.castRange` | 24 | Max distance (blocks) at which the well can be anchored along the caster's aim. |
| `GravityWell.friendlyFire` | false | If true the well also pulls and crushes players in the caster's own nation or hunt party. |

Set in [`config/tensura/ability/magic_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

## Tags

`tensura:skills/aspectual_magic`, `tensura:skills/gravity_skills`
