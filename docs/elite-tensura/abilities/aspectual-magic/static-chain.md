# Static Chain

<small>[Elite Tensura](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Aspectual Magic](index.md)</small>

<div class="infobox" markdown>

![Static Chain](../../../assets/icons/elitetensura/skill/static_chain.png)

| | |
|---|---|
| **Type** | Aspectual Magic |
| **ID** | `elitetensura:static_chain` |
| **Max mastery** | 300 |
| **Activation** | Hold |

</div>

> Lightning magic. Loose an arc at the target you are looking at; it leaps to nearby foes, dealing less damage with each jump and leaving them Glowing and slowed. When mastered, hold past the cast time to charge a longer, harder-hitting chain that arcs through more targets. Requires Thunder mastered to learn.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 120 |  |

## How it works

- Triggers when the held key is released

## Related

- **Related skills:** [Thunder Lance](../../../tensura-reincarnated/abilities/aspectual-magic/thunder-lance.md)

## Stats (config defaults)

Set in [`config/tensura/EliteTensura/MagicConfig.toml`](../../configs/config-tensura-elitetensura-magicconfig.md).

| Option | Default | Description |
|---|---|---|
| `StaticChain.castTime` | 30 | Cast time in ticks (20 = 1s). |
| `StaticChain.castTimeMastered` | 20 | Cast time in ticks when mastered. |
| `StaticChain.magiculeCost` | 120 | Magicule cost per normal cast. |
| `StaticChain.magiculeCostCharged` | 200 | Magicule cost for the charged (mastered, held-longer) cast. |
| `StaticChain.cooldown` | 0 | Cooldown in seconds. |
| `StaticChain.cooldownMastered` | 0 | Cooldown in seconds when mastered. |
| `StaticChain.baseDamage` | 20 | Magic damage dealt to the first target (decays each hop). |
| `StaticChain.baseDamageCharged` | 35 | Base damage for the charged cast. |
| `StaticChain.damageDecay` | 0.65 | Damage multiplier applied per chain hop (0.65 = each hop deals 65% of the previous). |
| `StaticChain.chargedDamageDecay` | 0.8 | Damage decay per hop for the charged cast (higher = holds damage longer). |
| `StaticChain.maxHops` | 4 | Maximum number of targets the arc chains through. |
| `StaticChain.chargedBonusHops` | 4 | Extra hops added by the charged cast. |
| `StaticChain.initialRange` | 14 | Range (blocks) to acquire the first target in the look direction. |
| `StaticChain.chainRange` | 6 | Max distance (blocks) the arc can jump between chain links. |
| `StaticChain.strikeRadius` | 1.5 | Radius (blocks) of each lightning strike's area damage at a link. |
| `StaticChain.glowingDuration` | 60 | Glowing effect duration (ticks) applied to each hit target. |
| `StaticChain.slowDuration` | 30 | Slowness effect duration (ticks) applied to each hit target. |
| `StaticChain.slowAmplifier` | 2 | Slowness amplifier (0-indexed; 2 = Slowness III). |
| `StaticChain.friendlyFire` | false | If true the arc also chains onto players in the caster's own nation or hunt party. The deliberately-aimed first target is never filtered. |

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

`tensura:skills/aspectual_magic`, `tensura:skills/lightning_skills`
