# Guardian

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Guardian](../../../assets/icons/tensura/skill/guardian.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `tensura:guardian` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 50,000 |
| **Activation** | Press |

</div>

> Stand as a bastion against the force of your enemies. Absorb the damage from your allies and fortify their defenses.

## Modes

| # | Mode |
|---|---|
| 1 | Grant Protection |
| 2 | Iron Wall |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 100 |  |

## How it works

- Activated by pressing the skill key

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| knockBack | knock amount | add |

## Obtaining

- Listed in the `startingSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation.
- Listed in the `secondSkills` config option (config/tensura/reincarnation_config.toml): List of Unique skills that can be randomly obtained through reincarnation as a second Unique - Only applies when the Skill Number on...
- Listed in the `uniqueSkills` config option (config/tensura/ability/skill/unique_config.toml): List of Unique skills that can be created by Creator.
- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.

## Related

- **Effects:** [Guarded](../../effects/guarded.md)
- **Referenced by:** [｢ Beelzebub, Lord of Gourmet ｣](../../../tr-nightmares/abilities/ultimate-skills/beelzebub.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/unique_config.toml`](../../configs/config-tensura-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Guardian.mpAcquirement` | 50,000 | Magicule Acquirement Cost. |
| `Guardian.magiculeCost` | 100 | Base Magicule Cost to activate. |
| `Guardian.protectionRadius` | 25 | The radius of the Grant Protection Mode. |
| `Guardian.protectionDuration` | 3,600 | The duration in tick of the Protection effect to apply on Allies. |
| `Guardian.protectionArmor` | 10 | The amount of armor point gained when applied with Protection. |
| `Guardian.protectionBarrier` | 30 | The amount of barrier point gained when applied with Protection. |
| `Guardian.wallArmor` | 15 | The amount of armor point gained when activated Iron Wall. |
| `Guardian.wallArmorMastered` | 40 | The amount of armor point gained when activated Iron Wall with mastery. |
| `Guardian.wallKnockResist` | 0.4 | The amount of knockback resistance gained when activated Iron Wall. |
| `Guardian.wallKnockResistMastered` | 1 | The amount of knockback resistance gained when activated Iron Wall with mastery. |

## In-game messages

<details markdown><summary>Show 1 messages</summary>

- %s damage taken on behalf of %s

</details>

## Tags

`tensura:skills/unique_skills`
