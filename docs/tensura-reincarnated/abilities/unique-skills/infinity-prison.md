# Infinity Prison

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Infinity Prison](../../../assets/icons/tensura/skill/infinity_prison.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:infinity_prison` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 90,000 |
| **Cooldowns (s)** | 10 mastered, 20 otherwise |
| **Activation** | Press |

</div>

> Trap enemies in an unbreakable dimensional cage or shield yourself from any threat with your dimensional barrier. Gain access to spatial storage.

## Modes

| # | Mode |
|---|---|
| 1 | Imprison |
| 2 | Imaginary Space |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 50,000 |  |

## How it works

- Activated by pressing the skill key
- Triggers when you are attacked
- Triggers when you take damage
- Does something when first learned

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `egoWhitelist` config option (config/nightmare/ability/skill/ego/general_config.toml): Skills allowed to develop ego if in whitelist mode
- Listed in the `virtueDominionSkills` config option (config/nightmare/ability/skill/nightmare_ult.toml): Virtue skills that Ultimate Dominion can copy from targets.
- Listed in the `AngelicSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): List of Angelic skills registry names that can be created via Holy Essence consumption. Format: modid:skill_name
- Listed in the `VirtueSkillsList` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): Virtue unique skill ids for Michael Ultimate Dominion.

## Related

- **Effects:** [Infinite Imprisonment](../../effects/infinite-imprisonment.md)
- **Referenced by:** [Time Traveler](../../../tr-nightmares/abilities/unique-skills/time-traveler.md), [｢ Lucifer, Lord of Pride ｣](../../../tr-nightmares/abilities/ultimate-skills/lucifer.md), [｢ Uriel, Lord of Vows ｣](../../../tr-nightmares/abilities/ultimate-skills/uriel-lord-of-vow.md), [｢ Yog-Sothoth, Lord of Space-Time ｣](../../../tr-nightmares/abilities/ultimate-skills/yog-sothoth.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `InfinityPrison.mpAcquirement` | 90,000 | Magicule Acquirement Cost. |
| `InfinityPrison.magiculeCostGuard` | 25 | The base magicule cost to block per damage point with Absolute Guard. |
| `InfinityPrison.magiculeCostImprison` | 50,000 | The Minimal Magicule Cost to activate Imprison. |
| `InfinityPrison.magiculeCostImprisonTarget` | 0.5 | The multiplier of the target's EP to be added as Magicule Cost for the user to imprison the target. |
| `InfinityPrison.guardEP` | 0.75 | The multiplier of the user's EP that an attacker needs to have above to bypass Absolute Guard. |
| `InfinityPrison.imprisonRange` | 30 | The max range in block to Imprison an target. |
| `InfinityPrison.imprisonDuration` | 6,000 | The duration in tick of the Imprison effect. |
| `InfinityPrison.imprisonDurationMastered` | 12,000 | The duration in tick of the Imprison effect when mastered. |
| `InfinityPrison.cooldownImprison` | 20 | The cooldown in second when activated Imprison. |
| `InfinityPrison.cooldownImprisonMastered` | 10 | The cooldown in second when activated Imprison with mastery. |
| `InfinityPrison.waterCapacity` | 9,000 | The bonus water capacity when the skill is acquired. |
| `InfinityPrison.lavaCapacity` | 9,000 | The bonus lava capacity when the skill is acquired. |

## Tags

`tensura:skills/paladin`, `tensura:skills/unique_skills`, `tensura:skills/virtue_skills`
