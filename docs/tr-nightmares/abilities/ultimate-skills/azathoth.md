# ｢ Azathoth, God of The Void ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![｢ Azathoth, God of The Void ｣](../../../assets/icons/trnightmare/skill/azathoth.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:azathoth` |
| **Modes** | 7 |
| **Acquisition cost (MP)** | 20,000,000 |
| **Max mastery** | 50,000 |
| **Cooldowns (s)** | 3 |
| **Activation** | Toggle, Press, Hold |

</div>

> God-class void sovereign. Commands imaginary space, void predation, multidimensional barriers, True Dragon nucleation, and nihility.

## Modes

| # | Mode |
|---|---|
| 1 | Imaginary Space |
| 2 | Imaginary Space: Isolation |
| 3 | Soul Gluttony |
| 4 | Darkest Void |
| 5 | Multidimensional Barrier |
| 6 | Nihility Generation |
| 7 | Imaginary Blade |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Adjusted by scrolling while active
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers when you take damage
- Does something when first learned

## Obtaining

- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.
- Listed in the `ultimateEnchantmentBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Ultimate skills blacklisted from Ultimate Enchantment.
- Listed in the `skillEngraveBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skills that cannot be engraved through Amatsumara skill engrave.
- Listed in the `compatibleUltimateSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Ultimate (or skill) resource ids that enable learning Spacetime Domination when possessed. Empty = unobtainable. Designer fill-in, e.g....
- Listed in the `requiredUltimateSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Ultimate skill ids that satisfy the learn gate (§3 may mirror into SpacetimeManipulationCompat).
- Listed in the `allowedUserIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can use Raphael-style alteration by default.

## Related

- **Related skills:** [｢ Raphael, Lord of Wisdom ｣](raphael-wisdom.md), [｢ Beelzebuth, Lord of Gluttony ｣](beelzebuth.md), [Void Resistance](../resistance-skills/void-resistance.md), [Spacetime Domination](../extra-skills/spacetime-domination.md)
- **Referenced by:** [Universal Shapeshift](../extra-skills/universal-shapeshift.md), [｢ Raphael, Lord of Knowledge ｣](raphael-knowledge.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Azathoth.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Azathoth.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Azathoth.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Azathoth.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Azathoth.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Azathoth.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Azathoth.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Azathoth.enableEvolution` | true | Enable Azathoth evolution. |
| `Azathoth.mpAcquirement` | 20,000,000 | Base max magicule required to acquire Azathoth (reduced per owned True Dragon ultimate). |
| `Azathoth.mpDiscountPerTrueDragon` | 5,000,000 | Max magicule discount per owned True Dragon ultimate (Veldora, Velgrynd, Velzard, Velgaia). |
| `Azathoth.epRequirement` | 40,000,000 | Minimum total EP (non-consumed) when player owns at least one True Dragon ultimate. |
| `Azathoth.epRequirementNoTrueDragon` | 60,000,000 | Minimum total EP (non-consumed) when player owns no True Dragon ultimates. |
| `Azathoth.namedSubordinates` | 100 | Named subordinates required. |
| `Azathoth.masteredSkills` | 100 | Mastered skills required. |
| `Azathoth.nucleationSacrificeMp` | 250,000 | MP cost to sacrifice a True Dragon into Azathoth after evolution (max magicule gate + drain amount). |
| `Azathoth.soulGluttonyRange` | 12 | Soul Gluttony predation range. |
| `Azathoth.soulGluttonyDamage` | 50 | Soul Gluttony base damage for mist. |
| `Azathoth.soulGluttonyMpPerTick` | 500 | Soul Gluttony MP per tick while held. |
| `Azathoth.nihilityGenPerSecond` | 500 | Nihility generated per second while holding Nihility Generation. |
| `Azathoth.nihilityGenNamedRaphaelPerSecond` | 5,000 | Nihility per second while holding Nihility Generation with a named Raphael. |
| `Azathoth.nihilityPassivePerSecond` | 500 | Passive Nihility per second from named Raphael when mastered. |
| `Azathoth.imaginaryBladeNihility` | 1,500 | Imaginary Blade nihility cost. |
| `Azathoth.imaginaryBladeNihilityMastered` | 1,000 | Imaginary Blade nihility cost when mastered. |
| `Azathoth.imaginaryBladeVoidDamage` | 250 | Imaginary Blade void damage per hit. |
| `Azathoth.soulNucleationNihility` | 50,000 | Soul Nucleation nihility cost. |
| `Azathoth.nihilityGenReleaseCooldown` | 3 | Cooldown (Manas skill ticks, ~one per second) after releasing Nihility Generation. |
| `Azathoth.darkestVoidReleaseCooldown` | 3 | Cooldown (Manas skill ticks, ~one per second) after releasing Darkest Void. |
| `Azathoth.imaginarySpaceIsolationCooldownSeconds` | 1 | Cooldown for Imaginary Space Isolation after removing Cook from the target. |
| `Azathoth.imaginaryBladePierceChance` | 0.25 | Chance for Imaginary Blade to pierce all Tensura defenses. |
| `Azathoth.nullResistanceDegradation` | 1 | Resistance degradation while Null toggle is active. |
| `Azathoth.nullPhysicalResistDegradation` | 1 | Physical resistance degradation while Null toggle is active. |
| `Azathoth.nullDodgeNegateChance` | 0.5 | Dodge negate chance while Null toggle is active. |
| `Azathoth.enableUltimateEvolution` | true | Whether azathoth can be obtained naturally |
| `ultMasteryConfig.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `ultMasteryConfig.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `ultMasteryConfig.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `ultMasteryConfig.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `ultMasteryConfig.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `ultMasteryConfig.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `ultMasteryConfig.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `ultMasteryConfig.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |

## In-game messages

<details markdown><summary>Show 1 messages</summary>

- &lt;pulse base=0.6 a=0.5 f=1.4&gt;&lt;shadow x=0.6 y=0.6 c=000000 a=0.9&gt;&lt;grad from=#FFFFFF to=#000000 hue sp=20&gt;&lt;wave a=0.9 f=0.8 w=0.25&gt;｢ Azathoth, God of The Void ｣&lt;/wave&gt;&lt;/grad&gt;&lt;/shadow&gt;&lt;/pulse&gt;

</details>

## Tags

`tensura:skills/ultimate_skills`
