# ｢ Yog-Sotohort, God of Space-Time ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:yog-sotohort` |
| **Modes** | 5 |
| **Acquisition cost (MP)** | 2,501,000 |
| **Max mastery** | 5,000 |
| **Cooldowns (s)** | 300, 180, 3 mastered, 5 otherwise, 5, 12, 6 |
| **Activation** | Toggle, Press, Hold |

</div>

> The ultimate master of space and time — usurp, sever, imprison, stop time, and empower allies.

## Modes

| # | Mode |
|---|---|
| 1 | Usurping |
| 2 | Absolute |
| 3 | Courage |
| 4 | Justice |
| 5 | Hope |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Usurping | 50,000 |  |
| Absolute | 25,000 |  |
| other modes | 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers on melee contact
- Triggers when you are attacked
- Triggers when you die
- Does something when first learned
- Triggers when one of your subordinates dies

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| atk | bonus | add |

## Obtaining

- Listed in the `skillEngraveBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skills that cannot be engraved through Amatsumara skill engrave.
- Listed in the `compatibleUltimateSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Ultimate (or skill) resource ids that enable learning Spacetime Domination when possessed. Empty = unobtainable. Designer fill-in, e.g....
- Listed in the `requiredUltimateSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Ultimate skill ids that satisfy the learn gate (§3 may mirror into SpacetimeManipulationCompat).
- Listed in the `blacklistedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that are banned from being transferred through Food Chain.
- Acquisition checks: [｢ Yog-Sotohort, God of Space-Time ｣](yog-sotohort.md)
- In-game message: *Yog-Sotohort, God of Space-Time — spacetime manipulation granted!*

## Related

- **Related skills:** [Spacetime Manipulation](../extra-skills/spacetime-manipulation.md)
- **Effects:** [Anti-Skill](../../../tensura-reincarnated/effects/anti-skill.md), [Mind Control](../../../tensura-reincarnated/effects/mind-control.md), [Infinite Imprisonment](../../../tensura-reincarnated/effects/infinite-imprisonment.md), [Magic Interference](../../../tensura-reincarnated/effects/magic-interference.md), [Fate Change](../../../tensura-reincarnated/effects/fate-change.md), [Haki Coat](../../../tensura-reincarnated/effects/haki-coat.md), [Strengthen](../../../tensura-reincarnated/effects/strengthen.md), [Severance Blade](../../../tensura-reincarnated/effects/severance-blade.md), [Hopes Gift](../../effects/hopes-gift.md)
- **Summons / entities:** Severance Cutter, Tensura
- **Referenced by:** [Witch's Greed](../unique-skills/witches-greed.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `YogSotohort.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `YogSotohort.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `YogSotohort.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `YogSotohort.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `YogSotohort.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `YogSotohort.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `YogSotohort.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `YogSotohort.mpAcquirement` | 2,501,000 | Magicule cost to acquire Yog-Sotohort (evolution from Yog-Sothoth). |
| `YogSotohort.epRequirement` | 10,000,000 | EP requirement for Yog-Sotohort evolution. |
| `YogSotohort.enableUltimateEvolution` | true | Whether Yog-Sotohort evolution is allowed. |
| `YogSotohort.absoluteCoatingMpDrain` | 1,000 | Absolute Coating MP drain per tick. |
| `YogSotohort.usurpingRobberyMpCost` | 50,000 | Usurping Robbery MP cost. |
| `YogSotohort.usurpingTakeoverMpCost` | 100,000 | Usurping Takeover MP cost. |
| `YogSotohort.absoluteProjectileMpCost` | 25,000 | Absolute Projectile MP cost. |
| `YogSotohort.absoluteImprisonMpCost` | 75,000 | Absolute Imprison MP cost. |
| `YogSotohort.absoluteImprisonDuration` | 600 | Absolute Imprison duration in ticks. |
| `YogSotohort.courageCooldown` | 5 | Courage mode cooldown in seconds. |
| `YogSotohort.justiceCooldown` | 5 | Justice mode cooldown in seconds. |
| `YogSotohort.hopeCooldown` | 5 | Hope mode cooldown in seconds. |
| `ultMasteryConfig.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |

Set in [`config/tensura/ability/skill/extra_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `Haki.cooldownMastered` | 3 | The cooldown in second of the haki when mastered. |
| `Haki.epAcquirement` | 100,000 | EP Requirement for Learning. |
| `Haki.magiculeCost` | 25 | Magicule Cost to activate. |
| `Haki.speedMultiplier` | 0.05 | Activation Speed Multiplier when activated. |
| `Haki.speedMultiplierMastered` | 0.1 | Activation Speed Multiplier when activated with mastery. |
| `Haki.hakiRadius` | 15 | The attack radius of the haki in blocks. |
| `Haki.epDifferenceMultiplier` | 0.25 | The EP difference multiplier for each Fear Level. |
| `Haki.fearDuration` | 200 | The duration in tick of the Fear effect when applied. |
| `Haki.cooldown` | 5 | The cooldown in second of the haki. |
| `Haki.cooldownMastered` | 3 | The cooldown in second of the haki when mastered. |

## In-game messages

<details markdown><summary>Show 34 messages</summary>

- Usurping
- Absolute
- Courage
- Justice
- Hope
- Switched to: %s — %s
- Yog-Sotohort, God of Space-Time — spacetime manipulation granted!
- Rob
- Copy
- Takeover
- Severance Cutter
- Infinity Prison
- Time Stop
- Hero Haki
- Hero Charisma
- Lucky Field
- Hold to activate Hero Haki!
- Castle Guard
- Armageddon
- Regalia Dominion
- Ultimate Dominion
- Hold to summon Angel Knights!
- Hold to dominate a target!
- Life Domination: Empower
- Fortitude
- Life Domination: Reconstruction
- Fortitude is a passive in-slot ability.
- Hold to regenerate!
- No sub-abilities learnt for this mode!
- Takeover successful! %s is now yours.
- Time Leap savepoint created!
- Time Leap activated — returned to savepoint!
- Spacetime Manipulation is passively granted while this skill is learned.
- &lt;turb a=1.4 f=1.2&gt;&lt;wave a=1.2 f=1.0 w=0.45&gt;&lt;grad from=#4B0082 to=#00BFFF hue f=0.4 sp=18&gt;&lt;pulse base=0.7 a=0.5 f=1.3&gt;｢ Yog-Sotohort, God of Space-Time ｣&lt;/pulse&gt;&lt;/grad&gt;&lt;/wave&gt;&lt;/turb&gt;

</details>

## Tags

`tensura:skills/no_plundering`
