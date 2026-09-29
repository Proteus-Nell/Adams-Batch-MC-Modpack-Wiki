# Shadow Striker

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Shadow Striker](../../../assets/icons/tensura/skill/shadow_striker.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:shadow_striker` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 60,000 |
| **Cooldowns (s)** | 5 mastered, 10 otherwise |
| **Activation** | Toggle, Press, Hold |

</div>

> Become one with the shadows and deal massive spiritual damage and become immune to lesser presence detection.

## Modes

| # | Mode |
|---|---|
| 1 | Ultra Acceleration |
| 2 | Insta-kill |
| 3 | Espionage |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 3,000 or 0 | 100 or 0 |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect
- Triggers when you damage a target

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| dodge | 0.25 | add |
| invulnerability | 2 | add |

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.

## Related

- **Effects:** [Presence Concealment](../../effects/presence-concealment.md)
- **Referenced by:** [Alteration](../../../tr-nightmares/abilities/extra-skills/alteration.md), [｢ Tsukiyomi, Lord of Moonshadow ｣](../../../tr-nightmares/abilities/ultimate-skills/tsukiyomi.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `ShadowStriker.mpAcquirement` | 60,000 | Magicule Acquirement Cost. |
| `ShadowStriker.magiculeCostKill` | 3,000 | Magicule Cost to activate Insta-kill. |
| `ShadowStriker.auraCost` | 100 | Aura Cost to activate Ultra Acceleration. |
| `ShadowStriker.chantSpeed` | 2 | The chant speed multiplier when toggled. |
| `ShadowStriker.dodgeStrength` | 0.25 | The bonus dodge strength when toggled. |
| `ShadowStriker.dodgeInvulnerability` | 2 | The bonus dodge invulnerability when toggled. |
| `ShadowStriker.ultraDistance` | 15 | The Ultra Acceleration distance when activated. |
| `ShadowStriker.ultraDistanceMastered` | 20 | The Ultra Acceleration distance when activated with mastery. |
| `ShadowStriker.ultraDamage` | 0 | The bonus attack when using Ultra Acceleration on a target. |
| `ShadowStriker.ultraDamageMastered` | 70 | The bonus attack when using Ultra Acceleration on a target when mastered. |
| `ShadowStriker.killDamage` | 500 | The amount of spiritual damage on target when using Insta-Kill. |
| `ShadowStriker.killDamageMastered` | 1,000 | The amount of spiritual damage on target when using Insta-Kill with mastery. |
| `ShadowStriker.killCooldown` | 10 | The cooldown in second of the Insta-Kill. |
| `ShadowStriker.killCooldownMastered` | 5 | The cooldown in second of the Insta-Kill when mastered. |
| `ShadowStriker.concealmentLevel` | 1 | The level of Presence Concealment when using Espionage. |
| `ShadowStriker.concealmentLevelMastered` | 2 | The level of Presence Concealment when using Espionage with mastery. |

Set in [`config/tensura/ability/ability_config.toml`](../../configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/unique_skills`
