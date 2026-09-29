# ｢ Livyatan, Lord of Floods ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![｢ Livyatan, Lord of Floods ｣](../../../assets/icons/trnightmare/skill/deluge.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:livyatan` |
| **Modes** | 6 |
| **Acquisition cost (MP)** | 1,800,000 |
| **Max mastery** | 15,000 |
| **Activation** | Toggle, Press, Hold |

</div>

> An ultimate flood authority that warps the battlefield with water, clones, weather, and oppressive suppression.

## Modes

| # | Mode |
|---|---|
| 1 | World Of Floods |
| 2 | Water Clone |
| 3 | Flood The Sky |
| 4 | Water Barrage |
| 5 | Rejection |
| 6 | Slip |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Does something when first learned

## Obtaining

- Acquisition checks: [Deluge](../unique-skills/deluge.md), [｢ Livyatan, Lord of Floods ｣](livyatan.md)
- In-game message: *Your Deluge has evolved into Livyatan, Lord of Floods.*

## Related

- **Related skills:** [Deluge](../unique-skills/deluge.md)
- **Summons / entities:** [Clone](../../../tensura-reincarnated/mobs/clone.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Livyatan.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Livyatan.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Livyatan.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Livyatan.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Livyatan.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Livyatan.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Livyatan.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Livyatan.mpAcquirement` | 1,800,000 | The Cost for the Ultimate Skill: Livyatan. |
| `Livyatan.worldOfFloodsCost` | 3,500 | Magicule cost for World of Floods. |
| `Livyatan.worldOfFloodsRadius` | 18 | Radius of World of Floods. |
| `Livyatan.cloneCost` | 2,500 | Magicule cost for Water Clone. |
| `Livyatan.floodTheSkyCost` | 4,000 | Magicule cost for Flood the Sky. |
| `Livyatan.waterBarrageCost` | 2,000 | Magicule cost for Water Barrage. |
| `Livyatan.waterBarrageShiftCost` | 6,000 | Magicule cost for shifted Water Barrage. |
| `Livyatan.waterBarrageDamage` | 100 | Damage dealt by Water Barrage. |
| `Livyatan.rejectionCost` | 250 | Magicule cost per second for Rejection's base mode. |
| `Livyatan.defenseRejectionCost` | 5,000 | Magicule cost per second for Rejection defense. |
| `Livyatan.offenseRejectionCost` | 250 | Magicule cost per second for Rejection offense. |
| `Livyatan.rejectionRadius` | 24 | Radius used by Rejection. |
| `Livyatan.enableUltimateEvolution` | true | Whether Livyatan evolution is allowed. If false, Deluge cannot evolve into Livyatan. |
