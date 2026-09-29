# Caedros, God of Conquest

<small>[TensuraMoreSkills](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![Caedros, God of Conquest](../../../assets/icons/tensuramoreskills/skill/caedros_god_of_conquest.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `tensuramoreskills:caedros_god_of_conquest` |
| **Modes** | 6 |
| **Max mastery** | 6,000 |
| **Cooldowns (s)** | 4, 8, 16, 10, 20, 28 |
| **Activation** | Toggle, Press |

</div>

> The god of conquest, guilt and ruin. Wields an ashen halberd and twists the world into a blood-red realm.

## Modes

| # | Mode |
|---|---|
| 1 | Conquest |
| 2 | Plague and Pestilence |
| 3 | Bang |
| 4 | Cloud the Skies |
| 5 | Fang and Serpent (Guilt) |
| 6 | Construct |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Conquest | 0 |  |
| Plague and Pestilence | 0 |  |
| Bang | 0 |  |
| Cloud the Skies | 0 |  |
| Fang and Serpent (Guilt) | 0 |  |
| Construct | 0 |  |
| other modes | 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Does something when first learned

## Related

- **Related skills:** [Burden](../../../tensura-reincarnated/abilities/aspectual-magic/burden.md), [Weather Manipulation](../../../tensura-reincarnated/abilities/extra-skills/weather-manipulation.md), [Curse](../../../tensura-reincarnated/abilities/spiritual-magic/curse.md)
- **Effects:** [Insanity](../../../tensura-reincarnated/effects/insanity.md), [Magic Interference](../../../tensura-reincarnated/effects/magic-interference.md), [Fear](../../../tensura-reincarnated/effects/fear.md), [Infection](../../../tensura-reincarnated/effects/infection.md), [Guarded](../../../tensura-reincarnated/effects/guarded.md), [Inspiration](../../../tensura-reincarnated/effects/inspiration.md), [Haki Coat](../../../tensura-reincarnated/effects/haki-coat.md), [Strengthen](../../../tensura-reincarnated/effects/strengthen.md), [Magic Aura](../../../tensura-reincarnated/effects/magic-aura.md), [Self-Regeneration](../../../tensura-reincarnated/effects/self-regeneration.md), [Fragility](../../../tensura-reincarnated/effects/fragility.md), [Corrosion](../../../tensura-reincarnated/effects/corrosion.md), [Chill](../../../tensura-reincarnated/effects/chill.md), [Paralysis](../../../tensura-reincarnated/effects/paralysis.md), [Webbed](../../../tensura-reincarnated/effects/webbed.md), [Black Burn](../../../tensura-reincarnated/effects/black-burn.md), [Drowsiness](../../../tensura-reincarnated/effects/drowsiness.md), [Movement Interference](../../../tensura-reincarnated/effects/movement-interference.md), [Oppression](../../../tensura-reincarnated/effects/oppression.md), [Soul Drain](../../../tensura-reincarnated/effects/soul-drain.md), [Spatial Blockade](../../../tensura-reincarnated/effects/spatial-blockade.md)
- **Items:** [Caedros Ashen Halberd](../../items/weapons/caedros-ashen-halberd.md)
- **Summons / entities:** Disintegration, Tensura

## Stats (config defaults)

Set in [`config/tensuramoreskills-grand.toml`](../../configs/config-tensuramoreskills-grand.md).

| Option | Default | Description |
|---|---|---|
| `obtainment.acquirementMastery` | 0 (-1 to no limit) | Starting mastery when Caedros is obtained. |
| `obtainment.maxMastery` | 6,000 (1 to no limit) | Maximum mastery for Caedros. |
| `costs.conquestCost` | 0 (0 to no limit) |  |
| `costs.plagueCost` | 0 (0 to no limit) |  |
| `costs.bangCost` | 0 (0 to no limit) |  |
| `costs.cloudCost` | 0 (0 to no limit) |  |
| `costs.fangCost` | 0 (0 to no limit) |  |
| `costs.constructCost` | 0 (0 to no limit) |  |
| `reconstruct.reconstructBaseGuiltCost` | 10,000 (0 to no limit) |  |
| `reconstruct.reconstructGuiltDivisorMastered` | 20 (1 to no limit) |  |
| `reconstruct.reconstructGuiltDivisor` | 10 (1 to no limit) |  |
| `reconstruct.reconstructEpCost` | 10,000 (0 to no limit) |  |
| `cloud.cloudStripsCaedrosIfOwnerDies` | true |  |
| `cloud.cloudRespawnsVictimsInsidePaths` | true |  |
| `conquest.conquestSweepRadius` | 10 (0 to 256) |  |
| `conquest.conquestSweepDamage` | 3,200 (0 to 340282349999999991754788743781432688640) |  |
| `guilt.maxGuiltTier` | 10 (0 to 1,000) |  |
| `guilt.guiltTierDivisor` | 10,000 (1 to no limit) | Guilt required per tier. 10000 = one tier every 10k guilt. |
| `bang.bangRange` | 150 (1 to 1,024) |  |
| `construct.constructAttackIntervalTicks` | 10 (1 to no limit) |  |
| `construct.constructMasterRange` | 20 (1 to 512) |  |
| `construct.constructBaseRange` | 10 (1 to 512) |  |
| `construct.constructSpiritMasteredDamage` | 1,500 (0 to 340282349999999991754788743781432688640) |  |
| `construct.constructSpiritBaseDamage` | 1,200 (0 to 340282349999999991754788743781432688640) |  |
| `construct.constructSwordBreakGuilt` | 250 (0 to no limit) |  |
| `fang.fangRadius` | 25 (0 to 512) |  |
| `fang.fangFearDurationTicks` | 140 (1 to no limit) |  |
| `fang.fangInsanityDurationTicks` | 140 (1 to no limit) |  |
| `fang.fangBurdenDurationTicks` | 120 (1 to no limit) |  |
| `fang.fangMagicInterferenceDurationTicks` | 120 (1 to no limit) |  |
| `fang.fangSkillDisableAmountMastered` | 2 (0 to 64) |  |
| `fang.fangSkillDisableAmount` | 1 (0 to 64) |  |
| `fang.fangCanDisableUniqueSkills` | true |  |
| `fang.fangCanDisableUltimateSkills` | true |  |
| `skill_deletion_safety.fangCanPermanentlyDeleteSkills` | false | If true, Fang and Serpent can permanently delete random Unique/Ultimate skills. If false, it only disables them. |
| `fang.fangCooldownTicks` | 4 (0 to no limit) |  |
| `conquest.conquestSummonCooldownTicks` | 8 (0 to no limit) |  |
| `conquest.conquestMiniBangCooldownTicks` | 16 (0 to no limit) |  |
| `conquest.conquestChargeTicks` | 100 (1 to no limit) |  |
| `conquest.conquestSweepCooldownTicks` | 10 (0 to no limit) |  |
| `conquest.conquestReleaseCooldownTicks` | 20 (0 to no limit) |  |
| `conquest.conquestMiniBangRange` | 28 (1 to 512) |  |
| `conquest.conquestMiniBangRadius` | 3 (0 to 128) |  |
| `conquest.conquestMiniBangDamage` | 5,000 (0 to 340282349999999991754788743781432688640) |  |
| `conquest.conquestChargedDamage` | 38,000 (0 to 340282349999999991754788743781432688640) |  |
| `conquest.conquestChargedRange` | 50 (1 to 512) |  |
| `plague.plagueSlashesMastered` | 8 (1 to 128) |  |
| `plague.plagueSlashes` | 6 (1 to 128) |  |
| `plague.plagueReachMastered` | 24 (1 to 512) |  |
| `plague.plagueReach` | 18 (1 to 512) |  |
| `plague.plagueWidthMastered` | 5.5 (0 to 128) |  |
| `plague.plagueWidth` | 4.25 (0 to 128) |  |
| `plague.plagueMasteredDamage` | 9,000 (0 to 340282349999999991754788743781432688640) |  |
| `plague.plagueBaseDamage` | 3,500 (0 to 340282349999999991754788743781432688640) |  |
| `plague.plagueDebuffPicksMastered` | 4 (0 to 64) |  |
| `plague.plagueDebuffPicks` | 3 (0 to 64) |  |
| `plague.plagueCooldownTicks` | 28 (0 to no limit) |  |
| `bang.bangRepeatFireLockoutTicks` | 4 (0 to no limit) |  |
| `bang.bangGuiltCost` | 1,000 (0 to no limit) |  |
| `bang.bangWindupTicks` | 60 (1 to no limit) |  |
| `bang.bangCooldownTicks` | 300 (0 to no limit) |  |
| `total_war_bang.totalWarBangRange` | 300 (1 to 2,048) |  |
| `total_war_bang.totalWarBangRadius` | 30 (0 to 512) |  |
| `bang.bangRadius` | 12 (0 to 256) |  |
| `total_war_bang.totalWarBangDamage` | 340282349999999991754788743781432688640 (0 to 340282349999999991754788743781432688640) |  |
| `bang.bangDamage` | 70,000 (0 to 340282349999999991754788743781432688640) |  |
| `bang.bangCanDestroyBlocks` | true |  |
| `total_war_bang.totalWarBangCanDestroyBedrock` | true |  |
| `bang.bangCanDestroyBedrock` | false |  |
| `cloud.cloudWindupTicks` | 100 (1 to no limit) |  |
| `cloud.cloudDurationTicks` | 2,400 (1 to no limit) |  |
| `cloud.cloudCooldownTicks` | 120 (0 to no limit) |  |
| `cloud.edenLeashRange` | 100 (1 to 1,024) |  |
| `cloud.cloudOwnerAttackMultiplier` | 2 (0 to 100) |  |
| `cloud.cloudOwnerHealthMultiplier` | 1.5 (0 to 100) |  |
| `cloud.edenWorldBorderSize` | 200 (1 to 60,000,000) |  |
| `cloud.cloudTeleportsAllPlayers` | true |  |
| `construct.constructDamage` | 10,000 (0 to 340282349999999991754788743781432688640) |  |
| `construct.constructCooldownTicks` | 30 (0 to no limit) |  |
| `fear_aura.fearInsanityIntervalTicks` | 70 (1 to no limit) |  |
| `fear_aura.fearInsanityRadius` | 25 (0 to 512) |  |
| `fear_aura.fearInsanityMaxAmplifier` | 9 (0 to 255) |  |
| `fear_aura.fearInsanityDurationTicks` | 140 (1 to no limit) |  |
| `ouroboros.ouroborosCheckIntervalTicks` | 1,200 (1 to no limit) |  |
| `ouroboros.ouroborosGuiltUpkeep` | 1 (0 to no limit) |  |
| `ouroboros.enableOuroborosSkillEating` | true | If false, Caedros will never eat the user's skills from guilt starvation. |
| `ouroboros.allowOuroborosToKillUser` | true | If true, the user dies when Ouroboros cannot eat another skill. |
| `guilt.guiltOfflineGainPerSecond` | 30 (0 to no limit) |  |
| `guilt.guiltSubordinateRadius` | 50 (0 to 512) | Radius used to count subordinate-based guilt gain/drain. |
| `guilt.guiltSubordinateBonus` | 15 (0 to no limit) |  |
| `guilt.guiltSkillBonus` | 12 (0 to no limit) |  |
| `guilt.guiltToggleDrainPerSecond` | 25 (0 to no limit) |  |
| `guilt.guiltSubordinateDrain` | 8 (0 to no limit) |  |
| `guilt.guiltSkillDrain` | 4 (0 to no limit) |  |
| `toggle_buffs.toggleAttackBase` | 0.45 (-1 to 100) |  |
| `toggle_buffs.toggleAttackPerTier` | 0.24 (0 to 100) |  |
| `toggle_buffs.toggleAttackSpeedBase` | 0.12 (-1 to 100) |  |
| `toggle_buffs.toggleAttackSpeedPerTier` | 0.05 (0 to 100) |  |
| `toggle_buffs.toggleKnockbackCap` | 1 (0 to 100) |  |
| `toggle_buffs.toggleKnockbackBase` | 0.15 (0 to 100) |  |
| `toggle_buffs.toggleKnockbackPerTier` | 0.08 (0 to 100) |  |
| `toggle_buffs.toggleDodgeCap` | 90 (0 to 1,000) |  |
| `toggle_buffs.toggleDodgeBase` | 10 (0 to 1,000) |  |
| `toggle_buffs.toggleDodgePerTier` | 7.5 (0 to 1,000) |  |
| `toggle_buffs.toggleEnergyGainBase` | 0.2 (0 to 100) |  |
| `toggle_buffs.toggleEnergyGainPerTier` | 0.1 (0 to 100) |  |
| `toggle_buffs.toggleBuffDurationTicks` | 120 (1 to no limit) |  |
| `toggle_buffs.toggleGuardedMaxAmplifier` | 5 (0 to 255) |  |
| `toggle_buffs.toggleHakiMaxAmplifier` | 4 (0 to 255) |  |
| `toggle_buffs.toggleStrengthenMaxAmplifier` | 6 (0 to 255) |  |
| `toggle_buffs.toggleInspirationMaxAmplifier` | 6 (0 to 255) |  |
| `toggle_buffs.toggleMagicAuraMaxAmplifier` | 4 (0 to 255) |  |
| `toggle_buffs.toggleSelfRegenMaxAmplifier` | 3 (0 to 255) |  |
| `ouroboros.allowEatingUniqueSkills` | true |  |
| `ouroboros.allowEatingUltimateSkills` | true |  |
| `ouroboros.allowEatingIntrinsicSkills` | true |  |
| `ouroboros.allowEatingResistanceSkills` | true |  |
| `ouroboros.allowEatingCommonSkills` | true |  |
| `ouroboros.allowEatingExtraSkills` | true |  |
| `control.controlEnabled` | true |  |
| `control.controlEpThresholdRatio` | 0.005 (0 to 1) |  |
| `control.controlForcesSpectator` | true |  |
| `skill_deletion_safety.controlCanPermanentlyDeleteLockedSkill` | false | If true, CONTROL can permanently delete the selected locked skill. If false, it only disables/unslots it. |
| `control.controlCanDisableLockedSkill` | true |  |
| `control.controlCanUnslotLockedSkill` | true |  |
| `famine.famineEnabled` | true |  |
| `famine.famineStarvesPlayers` | true |  |
| `famine.famineRadius` | 512 (1 to 4,096) |  |
| `famine.famineDebuffsPerStack` | 10 (1 to no limit) |  |
| `famine.famineDurationTicks` | 600 (1 to no limit) |  |
| `famine.famineDisableSkillsOnHit` | 1 (0 to 64) |  |
| `famine.famineCanDisableUniqueSkills` | true |  |
| `famine.famineCanDisableUltimateSkills` | true |  |
| `skill_deletion_safety.famineCanPermanentlyDeleteSkillsOnHit` | false | If true, FAMINE can permanently delete random Unique/Ultimate skills on hit. If false, it only disables them. |
| `famine.famineMaxAmplifier` | 5 (0 to 255) |  |
| `famine.famineMaxSecondaryAmplifier` | 2 (0 to 255) |  |
| `famine.famineBurstDurationTicks` | 120 (1 to no limit) |  |
| `war.warEnabled` | true |  |
| `war.warConquerThresholdRatio` | 0.1 (0 to 1) |  |
| `war.warTempEpGainRatio` | 0.5 (0 to 100) |  |
| `death.deathEnabled` | true |  |
| `death.deathReplicaFollowRadius` | 64 (1 to 4,096) |  |
| `death.deathReplicaTeleportDistanceSqr` | 16 (1 to no limit) |  |
| `war.warDamageEpGainCapMultiplier` | 6 (1 to 1,000) |  |
| `war.warMagiculeDamageRatio` | 0.1 (0 to 100) |  |
| `war.warMagiculeDamageDivisor` | 500 (1 to no limit) |  |
| `death.deathSoulDamageDivisor` | 100,000 (1 to no limit) |  |
| `final_damage.finalDamageGuiltPerTier` | 0.22 (0 to 100) |  |
| `fear_aura.fearDamagePerStackMastered` | 0.2 (0 to 100) |  |
| `fear_aura.fearDamagePerStack` | 0.05 (0 to 100) |  |
| `final_damage.trueDamageMinimum` | 1 (0 to 340282349999999991754788743781432688640) |  |
| `death_revive.enableDeathRevive` | true |  |
| `death_revive.deathReviveSoulPointCost` | 10,000 (0 to no limit) |  |
| `construct.constructMaxSwords` | 6 (0 to 128) |  |
| `construct.constructSwordUses` | 20 (1 to no limit) |  |
| `plague.plagueDebuffAmplifierMastered` | 2 (0 to 255) |  |
| `plague.plagueDebuffAmplifier` | 1 (0 to 255) |  |
| `plague.plagueDebuffDurationMasteredTicks` | 180 (1 to no limit) |  |
| `plague.plagueDebuffDurationTicks` | 140 (1 to no limit) |  |

## In-game messages

<details markdown><summary>Show 6 messages</summary>

- You summon the Ashen Halberd of Conquest.
- Conquest begins to charge...
- Not enough Guilt. You need 10000.
- Cloud the Skies is already active in this world.
- The skies cloud and a white desert swallows the world...
- The red clouds disperse and Caedros releases the realm.

</details>
