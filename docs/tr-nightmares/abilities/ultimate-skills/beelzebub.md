# ｢ Beelzebub, Lord of Gourmet ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:beelzebub` |
| **Modes** | 7 |
| **Acquisition cost (MP)** | 120,000 |
| **Max mastery** | 5,000 |
| **Cooldowns (s)** | 60, 5 |
| **Activation** | Toggle, Press, Hold |

</div>

> Devour all in your path — corrosion, spatial storage, food chain, chaos control, and gourmet mist.

## Modes

| # | Mode |
|---|---|
| 1 | Corrosion |
| 2 | Stomach |
| 3 | Food Chain |
| 4 | Chaos Control |
| 5 | Gourmet Mist |
| 6 | Guardian Grant |
| 7 | Guardian Wall |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Corrosion | 200 |  |
| Stomach | 1,000 |  |
| Food Chain | 5,000 |  |
| Chaos Control | 2,000 |  |
| Gourmet Mist | 10,000 |  |
| Guardian Grant | 1,000 |  |
| Guardian Wall | 0 |  |
| other modes | 0 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Adjusted by scrolling while active
- Has a continuous (per-tick) effect
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| Movement Speed | -0.5 | multiply total |
| armor | armor amount | add |
| knockBack | knock amount | add |

## Obtaining

- Listed in the `allowedSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can use Food Chain.
- Listed in the `resistanceAllowedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can transfer resistance skills through Food Chain.
- Listed in the `extraAllowedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can transfer extra skills through Food Chain.
- Listed in the `commonAllowdIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can transfer common skills through Food Chain.
- Listed in the `intrinsicAllowedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can transfer intrinsic skills through Food Chain.
- Listed in the `blacklistedIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that are banned from being transferred through Food Chain.
- Listed in the `allowedSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can be affected by Raphael-style alteration by default.
- Acquisition checks: [Gourmet](../../../tensura-reincarnated/abilities/unique-skills/gourmet.md), [Guardian](../../../tensura-reincarnated/abilities/unique-skills/guardian.md), [｢ Beelzebub, Lord of Gourmet ｣](beelzebub.md)
- In-game message: *Gluttony and Guardian merge — Beelzebub, Lord of Gourmet awakens!*

## Related

- **Related skills:** [Gourmet](../../../tensura-reincarnated/abilities/unique-skills/gourmet.md), [Guardian](../../../tensura-reincarnated/abilities/unique-skills/guardian.md)
- **Effects:** [Guarded](../../../tensura-reincarnated/effects/guarded.md), [Corrosion](../../../tensura-reincarnated/effects/corrosion.md)
- **Items:** [Meat Crusher](../../../tensura-reincarnated/items/weapons/meat-crusher.md)
- **Summons / entities:** Beelzebuth Mist
- **Referenced by:** [Alteration](../extra-skills/alteration.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Beelzebub.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Beelzebub.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Beelzebub.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Beelzebub.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Beelzebub.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Beelzebub.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Beelzebub.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Beelzebub.mpAcquirement` | 120,000 | Magicule cost to acquire Beelzebub (evolution from Gourmet + Guardian). |
| `Beelzebub.damageTakenRequired` | 100,000 | Total damage taken required for evolution. |
| `Beelzebub.subordinateCountRequired` | 25 | Subordinates required for evolution. |
| `Beelzebub.enableUltimateEvolution` | true | Whether Beelzebub evolution is allowed. |
| `Beelzebub.ultraspeedRegenHpPerTick` | 2 | Ultraspeed Regeneration HP per tick. |
| `Beelzebub.ultraspeedRegenMpDrain` | 500 | Ultraspeed Regeneration MP drain. |
| `Beelzebub.guardianRedirectFraction` | 0.5 | Guardian damage redirection fraction (0-1). |
| `Beelzebub.predationRadius` | 2 | Predation mist radius in blocks. |
| `Beelzebub.predationDuration` | 200 | Predation mist duration in ticks. |
| `Beelzebub.predationMpCost` | 10,000 | Predation MP cost. |
| `Beelzebub.corrosionRadius` | 10 | Corrosion AoE radius in blocks. |
| `Beelzebub.corrosionDamagePerTick` | 50 | Corrosion damage per tick. |
| `Beelzebub.corrosionMpDrain` | 200 | Corrosion MP drain per tick. |
| `Beelzebub.foodChainMpCost` | 5,000 | Military Power (Food Chain) MP cost. |
| `Beelzebub.stomachMpCost` | 1,000 | Stomach (Spatial Storage) MP cost. |
| `Beelzebub.chaosControlMpCost` | 2,000 | Chaos Control projectile MP cost. |
| `Beelzebub.chaosControlCooldown` | 5 | Chaos Control cooldown in seconds. |
| `Beelzebub.foodChainRange` | 5 | Food Chain Range. |
| `ultMasteryConfig.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

Set in [`config/tensura/energy_config.toml`](../../../tensura-reincarnated/configs/config-tensura-energy-config.md).

| Option | Default | Description |
|---|---|---|
| `maximumEPSteal` | 1,000,000 | The maximum amount of EP that an EP stealing ability can take. |
| `minAura` | 10 | The Minimum amount of Aura an entity can have. |
| `maxAura` | 1,000,000,000 | The Maximum amount of Aura an entity can have. |
| `baseAuraGain` | 1 | The Base percentage of Aura an entity can gain from slain enemies' EP. |
| `maxAuraGain` | 10 | The Max percentage of Aura an entity can gain from slain enemies' EP. |
| `minMagicule` | 10 | The Minimum amount of Magicule an entity can have. |
| `maxMagicule` | 1,000,000,000 | The Maximum amount of Magicule an entity can have. |
| `baseMagiculeGain` | 1 | The Base percentage of Magicule an entity can gain from slain enemies' EP. |
| `maxMagiculeGain` | 10 | The Max percentage of Magicule an entity can gain from slain enemies' EP. |
| `baseAuraRegen` | 5 | The base amount of Aura that entities regenerate each 10 ticks (half a second). |
| `areaMagiculeRegen` | 0.01 | The percentage of the current chunk's Magicule gets turned into players' MP within the chunk each 10 ticks (half a second). |
| `minimumMagiculePoison` | 1,000 | The minimum amount of Magicule the current chunk needs to have to apply Magicule Poison on players if applicable. |
| `sleepModeTick` | 180 | The number of seconds will the entity be in sleep mode when Magicule reaches 0. |
| `sleepModeAura` | 0.003 | The bonus multiplier of Max Aura that the entity regenerates each 10 ticks during Sleep Mode. |
| `sleepModeMagicule` | 0.003 | The bonus multiplier of Max Magicule that the entity regenerates each 10 ticks during Sleep Mode. |
| `wakeUpAura` | 0.16 | The multiplier of Max Aura that the entity regenerates after waking up naturally. |
| `wakeUpMagicule` | 0.16 | The multiplier of Max Magicule that the entity regenerates after waking up naturally. |
| `spiritualMagiculeLost` | 115 | Amount of Magicule that an entity in Spiritual Form loses each 10 ticks (half a second) while in unsuitable area. |
| `exceedMaxLost` | 5 | Amount of Aura/Magicule that an entity loses each 10 ticks when exceeding the max Aura/Magicule. |
| `auraMultiplierForInsanity` | 0.25 | Multiplier of max aura an entity needs to exceed for each level of Insanity.<br>Example: By default, Aura = 125% Max Aura -&gt; Insanity I, Aura = 150% Max Aura -&gt; Insanity II |
| `magiculeMultiplierForPoison` | 0.25 | Multiplier of max magicule an entity needs to exceed for each level of Magicule Poison.<br>Example: By default, Magicule = 125% Max Magicule -&gt; Poison I, Magicule = 150% Max Magicule -&gt; Poison II |
| `maximumEPSteal` | 1,000,000 | The maximum amount of EP that an EP stealing ability can take. |
| `maxEPReductionPercentage` | 90 | The maximum percentage of EP reduction when used in calculation for EP gain after killing mobs. |
| `penaltyLimitGain` | true | Whether the EP Gain from killing Players limit by the EP death Penalty gamerule. |
