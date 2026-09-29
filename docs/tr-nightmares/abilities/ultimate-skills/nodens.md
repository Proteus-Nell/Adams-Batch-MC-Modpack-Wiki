# ｢ Nodens, God of Abyss ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:nodens` |
| **Modes** | 3 |
| **Acquisition cost (MP)** | 3,400,000 |
| **Max mastery** | 50,000 |
| **Activation** | Press, Hold |

</div>

> Born from the collapse of Pride, forged in the void between soul and thought, Nodens is the incarnation of pure abyssal thought. This God-Class Ultimate Skill cannot be learned, only survived.

## Modes

| # | Mode |
|---|---|
| 1 | Soul Gluttony |
| 2 | Imaginary Space |
| 3 | Catastrophic Eclipse |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | *set by config (base cost (ego ultimate cost))* |  |
| Always | var14 (ego ultimate cost) |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Adjusted by scrolling while active
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers on melee contact
- Triggers when you are attacked
- Triggers when you take damage
- Triggers when an effect is applied to you
- Triggers when a projectile hits you
- Triggers when you die
- Triggers when you respawn
- Does something when first learned

## Obtaining

- {0} has been replaced with {1}!
- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.
- Listed in the `ultimateEnchantmentBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Ultimate skills blacklisted from Ultimate Enchantment.
- Listed in the `skillEngraveBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skills that cannot be engraved through Amatsumara skill engrave.
- Listed in the `compatibleUltimateSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Ultimate (or skill) resource ids that enable learning Spacetime Domination when possessed. Empty = unobtainable. Designer fill-in, e.g....
- Listed in the `excludedSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that Skill Storage will NOT store when obtained (blacklist).
- Listed in the `allowedSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can be affected by Raphael-style alteration by default.
- Acquisition checks: [｢ Nodens, God of Abyss ｣](nodens.md), [｢ Lucifer, Lord of Pride ｣](lucifer.md), [Ultimate Arroganz](ultimate-arroganz.md), [Skill Storage](../extra-skills/skill-storage.md)
- In-game message: *Lucifer, Lord of Pride has begun to collapse under the infinite cascade of information. It was not, in truth, an endless wellit had a bottom. To preserve yourself, you initiate the forbidden protocol: Ego Upload. Your innermost essenceyour ego , jigais cast into the abyss. The heart core , kokoro shatters, releasing a storm of infons. As your astral body is torn open and overwritten, something far greater begins to take shape... Nodens, God of Abyss has been born. Your body has been reformed. A God-Class Ultimate Skill has awakened.*

## Related

- **Related skills:** [｢ Lucifer, Lord of Pride ｣](lucifer.md), [Ultimate Arroganz](ultimate-arroganz.md), [Skill Storage](../extra-skills/skill-storage.md), [Spacetime Manipulation](../extra-skills/spacetime-manipulation.md), [Multidimensional Barrier](../extra-skills/multidimensional-barrier.md)
- **Effects:** [Godspeed Regeneration](../../effects/godspeed-regeneration.md)
- **Referenced by:** [Alteration](../extra-skills/alteration.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Nodens.baseMpAcquirement` | 3,400,000 | Base MP cost for standard Lucifer → Nodens evolution. |
| `Nodens.maxNihility` | 100,000 | Max nihility from Nodens nihility bar. |
| `Nodens.catastrophicEclipseLearnPoints` | 500 | Learning points required for Catastrophic Eclipse mode. |
| `Nodens.enableUltimateEvolution` | true | Whether Nodens can be obtained naturally |
| `ultMasteryConfig.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `ultMasteryConfig.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `ultMasteryConfig.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `ultMasteryConfig.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `ultMasteryConfig.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `ultMasteryConfig.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `ultMasteryConfig.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `ultMasteryConfig.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Lucifer.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Lucifer.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Lucifer.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Lucifer.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Lucifer.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Lucifer.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Lucifer.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Lucifer.mpAcquirement` | 1,700,000 | The Cost for the Ultimate Skill: Lucifer. |
| `Lucifer.copyChance` | 20 | The skill copy chance when attacked (Arroganz). Matches Tensura Pride defaults. |
| `Lucifer.copyChanceMastered` | 100 | The skill copy chance when attacked with mastery. |
| `Lucifer.copyMastery` | 0.0004 | Mastery gained per magicule cost of a successfully copied ability. |
| `Lucifer.copyMasteryFail` | 0 | Multiplier of mastery gained per magicule cost of a failed copy attempt. |
| `Lucifer.copyCooldown` | 45 | Cooldown in seconds per mastery gained from a successful copy. |
| `Lucifer.copyCooldownFail` | 4.5 | Cooldown in seconds per mastery gained from a failed copy. |
| `Lucifer.ocularAnalysisCooldown` | 0 | Cooldown ticks applied to Ocular Analysis (mode 1) after attempts. Arroganz uses copyCooldown \* mastery on slot 0. |
| `Lucifer.LuciferMastered` | 100 | Number of mastered skills required for Lucifer evolution. |
| `Lucifer.LuciferHPPercentage` | 0.4 | HP percentage threshold for Lucifer evolution. |
| `Lucifer.enableUltimateEvolution` | true | Whether Lucifer evolution is allowed. If false, Pride cannot evolve into Lucifer. |
| `Lucifer.copyRanged` | 25 | This is the range of the projectile copying of Lucifer. |
| `Lucifer.copyRange` | 5 | This is the range of the normal copying of Lucifer. |

## In-game messages

<details markdown><summary>Show 13 messages</summary>

- Lucifer, Lord of Pride has begun to collapse under the infinite cascade of information. It was not, in truth, an endless wellit had a bottom. To preserve yourself, you initiate the forbidden protocol: Ego Upload. Your innermost essenceyour ego , jigais cast into the abyss. The heart core , kokoro shatters, releasing a storm of infons. As your astral body is torn open and overwritten, something far greater begins to take shape... Nodens, God of Abyss has been born. Your body has been reformed. A God-Class Ultimate Skill has awakened.
- Compiled %s into skill storage.
- No skill has all submodes copied yet.
- Need %s MP to compile this skill.
- Nodens needs at least %s mastery for Skill Creation.
- Nodens needs at least %s mastery for Skill Duplication.
- Permanently acquired %s.
- Nothing available for this Arroganz mode.
- Weapon altered by the abyss.
- Hold The World or a Hihii-irokane Scythe in either hand.
- Material Creation intrinsic required for Abyss Weapon Alteration.
- Analyze Azathoth Imaginary Blade, own Azathoth, or slot Imaginary Blade.
- &lt;glitch f=3 j=0.03 b=0.01 s=0.12&gt;&lt;grad from=#FF0000 to=#000000 hue sp=16&gt;&lt;wave a=0.8 f=1.2 w=0.3&gt;｢ Nodens, God of Abyss ｣&lt;/wave&gt;&lt;/grad&gt;&lt;/glitch&gt;

</details>

## Tags

`tensura:skills/ultimate_skills`
