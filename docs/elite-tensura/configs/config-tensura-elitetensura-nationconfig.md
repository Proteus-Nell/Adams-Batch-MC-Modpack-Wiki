# `config/tensura/EliteTensura/NationConfig.toml`

<small>[Elite Tensura](../index.md) &rsaquo; [Configs](index.md)</small>

## `[Nations]`

| Option | Default | Range | Description |
|---|---|---|---|
| `foundingMinMembers` | 2 |  | A party team may be founded as a Nation when it has at least this many members AND... |
| `foundingMinClaimedChunks` | 1 |  | ...has claimed at least this many FTB chunks. Both conditions are required to found. |
| `maxLevel` | 20 |  | Maximum Nation level. |
| `levelBaseScore` | 100 |  | Score required to reach level 2 (the first threshold above the founding level 1). |
| `levelGrowth` | 1.25 |  | Geometric growth factor between consecutive level thresholds. |
| `weightPopulation` | 10 |  | Score weight: per nation member (population). |
| `weightTerritory` | 4 |  | Score weight: per claimed chunk (territory). |
| `weightEp` | 20 |  | Score weight: multiplied by log10(1 + total member EP). |
| `weightAwakened` | 20 |  | Score weight: per awakened member. |
| `weightHero` | 40 |  | Score weight: per True Hero member. |
| `weightDemonLord` | 40 |  | Score weight: per True Demon Lord member. |
| `weightRecord` | 10 |  | Score weight: per player record obtained by members. |
| `weightWorldEvent` | 8 |  | Score weight: per world event participated in. |
| `weightAchievement` | 15 |  | Score weight: per nation achievement earned. |
| `weightMissions` | 2 |  | Score weight: per mission the nation has completed (lifetime). |
| `claimBudgetPerLevel` | 4 |  | Extra FTB claim-chunk budget granted to the team per Nation level. |
| `walpurgisBridgeEnabled` | true |  | Enable Walpurgis council motions to ripple into the Nation system (enemy-&gt;war, treaty-&gt;alliance, claim-&gt;budget). Independent kill switch layered on top of the ETNationSystem gamerule. |
| `councilClaimBudgetBonus` | 2 |  | Bonus FTB claim chunks granted to a nation each time the Walpurgis council approves one of its territorial claims. Accumulates and is durable across level-ups. |
| `bonusesEnabled` | true |  | Apply Nation bonuses (attribute/effect modifiers) to members. |
| `voiceAnnouncementsEnabled` | true |  | Show member-scoped Voice of the World messages (achievement, level-up). |
| `globalAnnouncementsEnabled` | true |  | Broadcast global Voice announcements (nation founded/destroyed, world-records). |
| `recomputeIntervalTicks` | 600 |  | Ticks between periodic aggregate recomputation per nation (20 = 1 second). |
| `debug` | false |  | Log Nation evaluation to the server log. |
| `playerSpawnerSearchRadius` | 16 |  | Search radius (blocks) used to match a spawned mob back to a player-placed nation spawner. |
| `spawnerDebug` | false |  | Log nation-spawner gate decisions (placement, blocked spawns) to the server log. |

## `[Reputation]`

| Option | Default | Range | Description |
|---|---|---|---|
| `warWinRep` | 60 |  | Reputation gained by the winner of a war. |
| `defenderWinRep` | 20 |  | Extra reputation when the war winner was the defender (added on top of warWinRep). |
| `warLossRep` | -40 |  | Reputation lost by the loser of a war (surrender or force-end). |
| `bullyRep` | -30 |  | Reputation lost by an attacker who declares on a far-weaker nation (bullying). |
| `bullyRatio` | 0.4 |  | Attacker is 'bullying' when the defender's score is below this fraction of the attacker's score. |
| `allianceFormRep` | 15 |  | Reputation gained by both nations when an alliance forms. |
| `allianceBreakRep` | -50 |  | Reputation lost by the nation that breaks an alliance (betrayal). |
| `allyHonorRep` | 2 |  | Passive reputation gained per active ally, each reputation tick. |
| `calamityDefenseRep` | 40 |  | Reputation gained by each nation that helped defeat a World Calamity. |
| `walpurgisAttendRep` | 10 |  | Reputation gained by a nation when one of its members enters a Walpurgis council. |
| `councilEnemyRep` | -25 |  | Reputation lost by the TARGET nation when a Walpurgis council declares it an enemy. |
| `councilTreatyRep` | 5 |  | Reputation gained by the proposing nation when a Walpurgis council treaty is filed. |
| `councilClaimRep` | 10 |  | Reputation gained by a nation when a Walpurgis council approves its territorial claim. |
| `councilNeutralRep` | 5 |  | Reputation gained when a Walpurgis council declares neutrality / rescinds hostilities. |
| `achievementRep` | 25 |  | Reputation gained when a nation earns a nation achievement. |
| `repDecayIntervalTicks` | 24,000 |  | Ticks between reputation ticks (passive ally-honor + decay). 24000 = 20 minutes. |
| `decayStep` | 5 |  | Reputation moves this many points toward 0 each reputation tick. |
| `rogueThreshold` | -250 |  | At or below this reputation a nation is 'rogue' (no alliances, loses war-cooldown protection, can't declare). |
| `warDeclareFloor` | -250 |  | Minimum reputation required to DECLARE war (rogue nations cannot declare). |
| `slotCapReviled` | 0 |  | Max alliances at Reviled tier (rogue). |
| `slotCapInfamous` | 0 |  | Max alliances at Infamous tier (rogue). |
| `slotCapDistrusted` | 1 |  | Max alliances at Distrusted tier. |
| `slotCapNeutral` | 2 |  | Max alliances at Neutral tier. |
| `slotCapRespected` | 3 |  | Max alliances at Respected tier. |
| `slotCapHonored` | 4 |  | Max alliances at Honored tier. |
| `slotCapExalted` | 5 |  | Max alliances at Exalted tier. |

## `[Economy]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | false |  | Master switch for the nation treasury economy. Also requires Ultimate Banking System to be installed. |
| `taxPercent` | 5 |  | Percent of picked-up mob cash value charged from a nation member's primary bank account into the nation treasury (0 = none). Charged together with centralBankTaxPercent as one withdrawal. |
| `centralBankTaxPercent` | 10 |  | Additional percent of picked-up mob cash value charged from the member and deposited into the UBS central bank's reserve (0 = none). Money sink — leaves player circulation. |
| `incomePerChunkCents` | 12 |  | Passive treasury income in cents per claimed chunk per recompute interval. NOTE: this accrues per recompute tick (server running time) while upkeep bills on wall-clock hours, so the real break-even is a server-uptime figure, not a flat number. |
| `incomeLevelMultiplier` | 0.05 |  | Territory income is multiplied by (1 + this \* nationLevel). |
| `levelBaseCostCents` | 500,000 |  | Treasury cost in cents to buy level 2. Cost for level L = levelBaseCostCents \* levelCostGrowth^(L-2). |
| `levelCostGrowth` | 1.6 |  | Geometric growth of the level-up cost per level. |
| `spendMinRole` | 1 |  | Minimum role allowed to spend treasury (levelup/perks/withdraw): 0 = SOVEREIGN only, 1 = SOVEREIGN+OFFICER. |
| `warDeclareCostCents` | 250,000 |  | Treasury cost in cents to declare a war (0 = free). |
| `warSpoilsPercent` | 25 |  | Percent of the loser's treasury looted by the war winner. |
| `disbandRefundToFounder` | true |  | On disband, refund the treasury balance to the founder's primary bank account. |
| `ledgerCap` | 50 |  | Max ledger entries kept per nation. |
| `blockWithdrawDuringWar` | true |  | Block treasury withdrawals while the nation has a war in WARMUP or ACTIVE phase, so a war chest cannot be emptied mid-campaign. Deposits are always allowed. |
| `upkeepEnabled` | true |  | Charge every nation a recurring upkeep bill. Requires 'enabled' and Ultimate Banking System. |
| `upkeepPeriodHours` | 24 |  | Hours between upkeep bills. All nations bill on the same global boundary. Changing this re-derives the whole schedule from the stored anchor, not just future boundaries: nations re-anchor to the new index on their next pass, so raising it can skip a bill and lowering it can trigger one immediately. |
| `upkeepPerChunkCents` | 3,000 |  | Upkeep cost in cents per claimed chunk per billing period. Sized against incomePerChunkCents: at both defaults a nation breaks even at roughly 3 hours of server uptime per day. |
| `upkeepPerLevelCents` | 10,000 |  | Upkeep cost in cents per nation level per billing period. |
| `upkeepLevelCapRatio` | 1 |  | Cap the per-level upkeep term at this multiple of the per-chunk term. Income scales with claimed chunks alone, so without a cap a high-level, chunk-poor nation is structurally insolvent and its debt only deepens. At 1.0 the level bill can never exceed the territory bill. 0 disables the cap. |
| `upkeepCatchUpDays` | 1 |  | Max billing periods charged at once after server downtime. 1 means a week offline still costs one day. |
| `inactiveUpkeepPercent` | 25 |  | Percent of the normal upkeep charged for a period in which no member was online (0-100). |
| `upkeepMaxDebtPeriods` | 7 |  | Stop billing upkeep once the treasury is this many periods' worth of bills in debt. Keeps a returning nation able to dig out, and bounds what disbanding forgives. 0 means bill forever. |
| `treasuryInterestEnabled` | true |  | Pay the nation treasury interest on a positive balance. Requires 'enabled' and Ultimate Banking System — the payout is injected into UBS's own savings-interest tick, so nation treasuries and member savings accrue together. |
| `treasuryInterestApyPercent` | 1.8 |  | Interest rate on the nation treasury, as a percent per 365 payouts. One payout happens per UBS savings-interest tick (its SavingsInterestIntervalTicks, default 24000 = one Minecraft day), so at defaults this is 1.8% per 365 Minecraft days, NOT per real year — lowering SavingsInterestIntervalTicks multiplies the real yield. Paid only to nations with a member active within the current or previous upkeepPeriodHours window (same activity signal as upkeep, not an instant online check); a treasury at or below zero earns nothing and debt never compounds. Sub-cent yield is dropped, so a balance below about 10139 cents earns nothing. |

## `[Missions]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master switch for nation missions. |
| `cyclePeriodHours` | 168 |  | Length of one mission cycle in real hours. All nations roll at the same moment. |
| `missionsPerCycle` | 3 |  | How many missions are drawn per nation per cycle. Draws fewer if the level-filtered pool is smaller. |
| `graceForNewNations` | true |  | Nations founded mid-cycle sit out until the next roll instead of getting a partial cycle. |
| `cycleClearPerkId` | "" |  | Nation perk id whose bonuses are granted while a nation has cleared all of its missions this cycle. Empty = no clear buff. Changing this while nations hold the buff strands the old modifiers. |
| `announceCompletions` | true |  | Announce mission completions and cycle clears through Voice of the World. |
| `crateRewardsEnabled` | true |  | Grant crate keys to online nation members for mission completions and cycle clears. |
| `missionCrateId` | "common" |  | Crate id whose key each online member receives per completed mission. Empty = none. |
| `cycleClearCrateId` | "rare" |  | Crate id whose key each online member receives when the nation clears its whole cycle. Empty = none. |

## `[Contracts]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master switch for the nation contract board. |
| `maxOpenPerNation` | 5 |  | Maximum simultaneously open contracts per nation. |
| `durationHours` | 72 |  | Hours a contract stays open before it expires and refunds its escrow. |
| `minCashRewardCents` | 1,000 |  | Minimum cash reward in cents for a cash contract. |
| `blockPostingDuringWar` | true |  | Nations currently at war cannot post new contracts. Closes a spoils-denial exploit: escrowed cash has already left the treasury, so a losing nation could dump its balance into contracts and cancel after the war. |
| `allowHostileFulfilment` | false |  | Allow members of a nation at war with the poster to fulfil its contracts. |
| `bountiesEnabled` | true |  | Enable PvP bounty contracts: a nation-funded bounty on a named player, paid to whoever kills them first. Requires 'enabled'. |
| `minBountyCents` | 5,000 |  | Minimum cash reward in cents for a PvP bounty. Separate from minCashRewardCents — a bounty is a bigger ask than a delivery. |
| `bountyVisibility` | "BROADCAST" |  | Bounty announcements: BROADCAST (server-wide), SILENT (board only), BROADCAST_AND_DM (server-wide plus a direct warning to the target). Unknown values fall back to BROADCAST. Note: switching the economy off with cash bounties open evaporates their escrow, same as cash contracts. |
| `personalEnabled` | true |  | Allow any player (in a nation or not) to post contracts and bounties funded from their OWN bank and inventory. Nation-funded rows are unaffected. Requires 'enabled'. |
| `maxOpenPerPlayer` | 3 |  | Maximum simultaneously open personal contracts per player. |
| `forgedCommissionsEnabled` | true |  | Allow FORGED (quality-gated) commission contracts. Off = posting denied; already-open commissions stay fulfillable. |

## `[Perks]`

| Option | Default | Range | Description |
|---|---|---|---|
| `spawnerLevelBonus` | 1 |  | spawner_overclock: extra effective nation levels for the spawner unlock gate and mob cap. |
| `interestMultiplier` | 1.5 |  | golden_ledger: multiplier on the nation's daily treasury savings interest. |
| `missionSlotBonus` | 1 |  | charter_of_industry: extra missions drawn per cycle. |
| `epShareMultiplier` | 2 |  | bond_of_souls: multiplier on the subordinate EP share percent (only matters while the ETSubordinateEpShare gamerule is on). |
| `contractSlotBonus` | 2 |  | deep_pockets: extra simultaneously open contracts on the nation contract board. |
| `defenderKillPointBonus` | 0.5 |  | defenders_resolve: bonus fraction on war kill points while the member's side is the defender (0.5 = +50%). |
| `attunementRestoreFraction` | 0.01 |  | magicule_attunement: fraction of max magicule and aura restored per pulse while inside the nation's own claim (0.01 = 1%). |
| `attunementIntervalTicks` | 400 |  | magicule_attunement: ticks between restore pulses (400 = 20s). |

## `[Core]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master switch for the Nation Core block (placement, aura, siege). |
| `maxHp` | 5,000 |  | Core hit points. |
| `auraRadiusChunks` | 8 |  | Aura radius in chunks (Chebyshev) around the core; the member must also stand in own-nation claims. |
| `auraRegenBonus` | 0.1 |  | Aura: additive bonus to tensura magicule/aura regeneration multiplier (0.10 = +10%). |
| `auraArmorBonus` | 4 |  | Aura: flat bonus to generic.armor while inside the aura. |
| `damageScale` | 1 |  | Siege: attacker ATTACK_DAMAGE attribute is multiplied by this per hit. |
| `hitCooldownTicks` | 10 |  | Siege: per-player ticks between counted hits. |
| `maxDamagePerTickPct` | 0.02 |  | Siege: cap on total core damage per tick as a fraction of maxHp (multi-hit weapons). |
| `fallWarPoints` | 200 |  | War score awarded to the attacking side when the core falls. |
| `fallSeasonPoints` | 25 |  | Nation season-ladder points awarded to the attacking nation when the core falls. |
| `spoilsPercent` | 10 |  | At war resolution, extra percentage of the loser's treasury moved to the winner if the loser's core fell (0-100). |
| `repairCentsPerHp` | 100 |  | Repair cost in cents per missing HP (economy active). |
| `repairFreeWithoutEconomy` | true |  | When the nation economy is inactive, repair is free. |
| `bossBarRadius` | 32 |  | Boss bar radius in blocks around a core under siege. |
| `tierCostDollars` | "0,500000,1500000,3000000" |  | Upgrade cost per tier in whole dollars; entry 1 is the placed tier (ignored). Entry count = tier count. Blank = one tier, no upgrades. DEFAULT: 0,500000,1500000,3000000 |
| `tierMaxHp` | "5000,8000,12000,16000" |  | Core HP per tier; fallback maxHp. DEFAULT: 5000,8000,12000,16000 |
| `tierAuraRadiusChunks` | "8,10,12,14" |  | Aura radius in chunks per tier; fallback auraRadiusChunks. DEFAULT: 8,10,12,14 |
| `tierAuraRegenBonus` | "0.10,0.15,0.20,0.25" |  | Aura regen bonus per tier; fallback auraRegenBonus. DEFAULT: 0.10,0.15,0.20,0.25 |
| `tierAuraArmorBonus` | "4,6,8,10" |  | Aura armor bonus per tier; fallback auraArmorBonus. DEFAULT: 4,6,8,10 |
| `tierFallWarPoints` | "200,300,400,500" |  | War score for toppling the core, per tier; fallback fallWarPoints. DEFAULT: 200,300,400,500 |
| `fallDropsTier` | true |  | A core that falls in war drops one tier (never below 1). DEFAULT: true |

## `[Wonders]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master switch for Nation Wonders. |
| `cancelRefundPercent` | 0.5 |  | Fraction (0-1) of the CURRENT stage's paid cash refunded on cancel. Deposited items are never refunded. |
| `seasonPoints` | 50 |  | Nation season-ladder points awarded when a wonder completes. |
| `jointEnabled` | true |  | Joint Wonders: allied nations may be invited into a build as partners. false PAUSES invites/joins and partner payments/deposits; existing partners are kept and still receive the wonder. |
| `maxPartners` | 2 |  | Joint Wonders: maximum partner nations per build (the lead is not counted). |
| `forgeCritBonus` | 0.05 |  | grand_forge: extra crit-upgrade chance on forge quality rolls for members. |
| `spireAuraMultiplier` | 2 |  | aether_spire: multiplier on the Nation Core aura radius (chunks) and aura regen bonus. |
| `warPointBonus` | 0.15 |  | war_academy: multiplier bonus on war kill points (0.15 = +15%). |
| `synergySlotBonus` | 1 |  | hall_of_records: extra active synergy slots for members. |
| `epGainBonus` | 0.05 |  | hall_of_records: ADD_MULTIPLIED_BASE bonus to tensura magicule_gain and aura_gain. |
| `sanctumRegen` | 0.05 |  | sanctum_of_the_world (unique): ADD_VALUE bonus to magicule/aura regeneration multiplier for EVERY online player. |
| `beaconDamageReduction` | 0.1 |  | eternal_beacon (unique): fraction of damage from calamity bosses (BOSS_TAG) removed for everyone. |

## `[Personal]`

| Option | Default | Range | Description |
|---|---|---|---|
| `perksEnabled` | true |  | Enable personal perks for players not in a founded nation (bought from their own bank). |
| `missionsEnabled` | true |  | Enable personal missions for players not in a founded nation. |
| `missionsPerCycle` | 2 |  | Personal missions rolled per cycle (shares the nation mission cycle period). |
| `missionCrateId` | "common" |  | Crate id given per completed personal mission (blank = none). |
| `cycleClearCrateId` | "rare" |  | Crate id given when every personal mission of the cycle is complete (blank = none). |
| `announceCompletions` | true |  | Announce personal mission completions to the player (Voice of the World notice). |

## `[Doctrines]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enabled` | true |  | Master switch. Off: no doctrine effects, command and Codex block hidden. DEFAULT: true |
| `unlockLevel` | 3 |  | Nation level required to choose a doctrine. DEFAULT: 3 |
| `switchCostDollars` | 1,000,000 |  | Treasury fee in whole dollars to switch doctrine (first pick is free; free when the economy is off). DEFAULT: 1000000 |
| `switchLockDays` | 14 |  | Days a nation is locked to its doctrine after choosing it. DEFAULT: 14 |
| `militaristKillPointBonus` | 0.25 |  | Militarist: war kill-point bonus (0.25 = +25%). DEFAULT: 0.25 |
| `militaristUpkeepPenalty` | 0.25 |  | Militarist: upkeep penalty (0.25 = +25%). DEFAULT: 0.25 |
| `mercantileInterestBonus` | 0.5 |  | Mercantile: treasury interest bonus (0.5 = +50%). DEFAULT: 0.5 |
| `mercantileIncomeBonus` | 0.15 |  | Mercantile: territory income bonus (0.15 = +15%). DEFAULT: 0.15 |
| `mercantileKillPointPenalty` | 0.25 |  | Mercantile: war kill-point penalty (0.25 = -25%). DEFAULT: 0.25 |
| `arcaneAuraMultiplier` | 1.5 |  | Arcane: multiplier on the Core aura's regen and armor bonuses. DEFAULT: 1.5 |
| `arcaneSpawnerCapPenalty` | 0.25 |  | Arcane: nation spawner mob-cap penalty (0.25 = -25%). DEFAULT: 0.25 |
| `builderWonderDiscount` | 0.2 |  | Builder: discount on wonder stage cash (0.2 = -20%). DEFAULT: 0.2 |
| `builderIncomePenalty` | 0.2 |  | Builder: territory income penalty (0.2 = -20%). DEFAULT: 0.2 |
| `missionWeightMultiplier` | 2 |  | Draw-weight multiplier for missions matching the doctrine's metrics. DEFAULT: 2 |
