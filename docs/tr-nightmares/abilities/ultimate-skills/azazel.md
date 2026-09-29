# ｢ Azazel, Lord of Temptation ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:azazel` |
| **Modes** | 8 |
| **Acquisition cost (MP)** | 940,000 |
| **Max mastery** | 15,000 |
| **Cooldowns (s)** | 1,200, 5, 25, 500, 320, 600 |
| **Activation** | Toggle, Press |

</div>

> Ultimate temptation — Tempt Control, All of Creation, Solicitation, Charm Domination, Severed Realm, and collapse arts.

## Modes

| # | Mode |
|---|---|
| 1 | Charm Domination |
| 2 | Temptation World |
| 3 | Solicitation |
| 4 | Severed Realm |
| 5 | End of World |
| 6 | End of World: Requiem |
| 7 | Punitive Domination |
| 8 | Multidimensional Barrier |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you are attacked
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| learn | magic mult | add |
| master | magic mult | add |
| chant | 2 | add |

## Obtaining

- Listed in the `astralMasteredCreationUltimates` config option (config/nightmare/ability/skill/nightmare_ult.toml): Ultimate skill IDs only offered from Astral Light Skill Creation when Astral Light is mastered.
- Listed in the `skillEngraveBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skills that cannot be engraved through Amatsumara skill engrave.
- Listed in the `compatibleUltimateSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Ultimate (or skill) resource ids that enable learning Spacetime Domination when possessed. Empty = unobtainable. Designer fill-in, e.g....
- Listed in the `allowedSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can be affected by Raphael-style alteration by default.
- Acquisition checks: [｢ Azazel, Lord of Temptation ｣](azazel.md), [Tempter](../unique-skills/tempter.md), [Seeker](../../../tensura-reincarnated/abilities/unique-skills/seeker.md)
- In-game message: *Tempter and Seeker unite. Azazel awakens.*

## Related

- **Related skills:** [Tempter](../unique-skills/tempter.md), [Seeker](../../../tensura-reincarnated/abilities/unique-skills/seeker.md), [Spacetime Manipulation](../extra-skills/spacetime-manipulation.md)
- **Effects:** [Mind Control](../../../tensura-reincarnated/effects/mind-control.md)
- **Referenced by:** [Alteration](../extra-skills/alteration.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Azazel.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Azazel.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Azazel.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Azazel.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Azazel.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Azazel.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Azazel.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Azazel.enableUltimateEvolution` | true |  |
| `Azazel.mpAcquirement` | 940,000 |  |
| `Azazel.namedSubordinates` | 25 |  |
| `Azazel.masteredMagics` | 50 |  |
| `Azazel.raidWins` | 10 |  |
| `Azazel.thoughtAccelerationMagicMultiplier` | 4 |  |
| `Azazel.requiemLearnPoints` | 500 |  |
| `Azazel.requiemUsesRequired` | 100 |  |
| `Azazel.requiemCooldown` | 760 |  |
| `Azazel.punitiveCooldown` | 320 |  |
| `Azazel.copyChanceMastered` | 100 |  |
| `ultMasteryConfig.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `ultMasteryConfig.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `ultMasteryConfig.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `ultMasteryConfig.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `ultMasteryConfig.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `ultMasteryConfig.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `ultMasteryConfig.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `ultMasteryConfig.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |

Set in [`config/tensura/ability/skill/extra_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `ThoughtAcceleration.chantSpeed` | 2 | The chant speed multiplier when activated. |
| `ThoughtAcceleration.epAcquirement` | 8,000 | EP Requirement for Learning. |
| `ThoughtAcceleration.chantSpeed` | 2 | The chant speed multiplier when activated. |
| `ThoughtAcceleration.movementSpeed` | 0.01 | The bonus movement speed when activated. |
| `ThoughtAcceleration.movementSpeedMastered` | 0.02 | The bonus movement speed when activated with mastery. |
| `ThoughtAcceleration.attackSpeed` | 0.2 | The bonus movement speed when activated. |
| `ThoughtAcceleration.attackSpeedMastered` | 0.4 | The bonus movement speed when activated with mastery. |
| `ThoughtAcceleration.dodgeInvulnerability` | 1 | The bonus dodge invulnerability when toggled. |

## Tags

`tensura:skills/ultimate_skills`
