# ｢ Alternative, Proxy Rights ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![｢ Alternative, Proxy Rights ｣](../../../assets/icons/trnightmare/skill/dominator.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:alternative` |
| **Modes** | 7 |
| **Acquisition cost (MP)** | 900,000 |
| **Max mastery** | 5,000 |
| **Cooldowns (s)** | 5 |
| **Activation** | Press, Hold |

</div>

> Proxy rights granted under Michael. Seven modes of absolute superiority.

## Modes

| # | Mode |
|---|---|
| 1 | Absolute Superiority |
| 2 | Complete Concealment |
| 3 | Dominion Bullet |
| 4 | Enemy Identification |
| 5 | Parallel Existence |
| 6 | Soul Protect |
| 7 | Subjugation Conquest |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect

## Obtaining

- Listed in the `globalSkillsBlacklist` config option (serverconfig/nightmare/mechanic/nightmare_mechanics.toml): List of Skill registry names that cannot be copied. Format: modid:skill_name

## Related

- **Related skills:** [Wrath](../../../tensura-reincarnated/abilities/unique-skills/wrath.md), [Divine Ki Release](../../../tensura-reincarnated/abilities/intrinsic-skills/divine-ki-release.md)
- **Effects:** [Presence Concealment](../../../tensura-reincarnated/effects/presence-concealment.md), [Soul Protect](../../effects/soul-protect.md), [Mind Control](../../../tensura-reincarnated/effects/mind-control.md), [Insanity](../../../tensura-reincarnated/effects/insanity.md), [Fear](../../../tensura-reincarnated/effects/fear.md), [Rampage](../../../tensura-reincarnated/effects/rampage.md), [Holy Damage](../../../tensura-reincarnated/effects/holy-damage.md)
- **Summons / entities:** Tensura, Sacred Haki
- **Referenced by:** [Divine Wisdom Core](../intrinsic-skills/divine-wisdom-core.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Alternative.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Alternative.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Alternative.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Alternative.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Alternative.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Alternative.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Alternative.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Alternative.mpAcquirement` | 900,000 | Magicule obtainment cost. |
| `Alternative.absoluteSuperiorityMagicCostModifier` | -0.5 | Absolute Superiority magic cost modifier (ADD_MULTIPLIED_TOTAL). |
| `Alternative.concealCritBonus` | 25 | Complete Concealment critical attack chance bonus. |
| `Alternative.concealMeleeDodgeBonus` | 25 | Complete Concealment melee auto-dodge chance bonus. |
| `Alternative.concealProjectileDodgeBonus` | 25 | Complete Concealment projectile auto-dodge chance bonus. |
| `Alternative.soulProtectActiveTicks` | 600 | Soul Protect active window (ticks). |
| `Alternative.soulProtectCooldownTicks` | 200 | Soul Protect cooldown window (ticks). |
| `Alternative.dominionBulletTargetRange` | 32 | Dominion Bullet targeting range (blocks). |
| `Alternative.dominionBulletLowEpThresholdRatio` | 0.5 | Dominion Bullet low-EP threshold ratio vs user EP. |
| `Alternative.dominionBulletLowEpBonus` | 2,500 | Dominion Bullet bonus damage if target EP is below threshold. |
| `Alternative.dominionBulletNonAwakenedBonus` | 1,000 | Dominion Bullet bonus damage if target is not awakened. |
| `Alternative.dominionBulletNonMajinBonus` | 2,000 | Dominion Bullet bonus damage if target is not Majin. |
| `Alternative.dominionBulletNonDivineBonus` | 1,500 | Dominion Bullet bonus damage if target is not divine. |
| `Alternative.dominionBulletMaxDamage` | 7,000 | Dominion Bullet max capped damage. |
| `Alternative.dominionBulletPreambleDamage` | 10 | Dominion Bullet pre-hit spiritual damage. |
| `Alternative.dominionBulletPostambleDamage` | 10 | Dominion Bullet post-hit spiritual damage. |
| `Alternative.dominionBulletCooldownSeconds` | 30 | Dominion Bullet cooldown (Tensura seconds). |
| `Alternative.enemyIdentificationRange` | 24 | Enemy Identification targeting range (blocks). |
| `Alternative.enemyIdentificationMaxEpMultiplier` | 2 | Enemy Identification max target EP multiplier vs user. |
| `Alternative.parallelMaxClones` | 3 | Parallel Existence max active clone count. |
| `Alternative.parallelCooldownSeconds` | 5 | Parallel Existence cooldown (Tensura seconds). |
| `Alternative.subjugationReleaseCooldownSeconds` | 5 | Subjugation Conquest cooldown set on release (Tensura seconds). |
| `Alternative.subjugationHolyDamage` | 50 | Subjugation Conquest holy damage per pulse when not mastered. |
| `Alternative.subjugationHolyDamageMastered` | 100 | Subjugation Conquest holy damage per pulse when mastered. |
| `Alternative.enableUltimateEvolution` | true | Whether Alternative evolution is allowed. |

Set in [`config/tensura/ability/skill/extra_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `SacredHaki.epAcquirement` | 200,000 | EP Requirement for Learning. |
| `SacredHaki.magiculeCost` | 50 | Magicule Cost to activate Magicule Release. |
| `SacredHaki.magiculeCostCoat` | 100 | Magicule Cost to activate Haki Coat. |
| `SacredHaki.coatDuration` | 2,400 | The duration in tick of the Haki Coat when activated. |
| `SacredHaki.epDifferenceMultiplier` | 0.5 | The EP difference multiplier for each Fear Level. |
| `SacredHaki.healHP` | 60 | The amount of HP to heal allies every 5 seconds. |
| `Haki.hakiRadius` | 15 | The attack radius of the haki in blocks. |
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

<details markdown><summary>Show 4 messages</summary>

- Parallel Existence clone cap reached (%s).
- Target is too strong to identify.
- Uniques: %s \| Ultimates: %s
- Parallel existence manifested.

</details>

## Tags

`tensura:skills/ultimate_skills`
