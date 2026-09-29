# Dark Melt Slash

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Other Magic](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Other Magic |
| **ID** | `trnightmare:dark_melt_slash` |
| **Activation** | Hold |

</div>

> A nuclear dark-element magic that carves through targets with melting destructive force.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 10,000 |  |

## How it works

- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when you damage a target

## Obtaining

- Can appear in epic tomes from wizard towers
- Can be found in skill tomes
- Sold by dwarf traders (great upgraded tome)

## Stats (config defaults)

Set in [`config/nightmare/ability/magic/nuclear.toml`](../../configs/config-nightmare-ability-magic-nuclear.md).

| Option | Default | Description |
|---|---|---|
| `MeltSlash.castTime` | 6 | Cast time in seconds. |
| `MeltSlash.castTime` | 6 | Cast time in seconds. |
| `MeltSlash.magiculeCost` | 10,000 | Magicule Cost to cast. |
| `MeltSlash.nuclearDamage` | 150 | The nuclear damage of the strike. |
| `MeltSlash.cookPerc` | 70 | Percentage of damage the cooks SHP. |

Set in [`config/tensura/ability/ability_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-ability-config.md).

| Option | Default | Description |
|---|---|---|
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryPoint` | 1 | The base value of how many mastery points the player gains when using an ability - Only applies for new players when changed cus this is an attribute. |
| `Mastery.masteryHitMultiplier` | 2 | The multiplier of mastery point the player gains when the ability hit a target. |
| `Mastery.masteryKillMultiplier` | 2 | The multiplier of mastery point the player gains when the ability kills a target. |
| `Mastery.masteryHoldTick` | 60 | How long in tick the user need to hold down an ability to gain a mastery point for holding abilities. |
| `Mastery.masteryActivateTime` | 10 | How many time the user need to activate some passive abilities (tick/on attack) to gain a mastery point for holding abilities. |

## Tags

`tensura:skills/epic_tome_wizard_tower`, `tensura:skills/found_in_tome`, `tensura:skills/great_upgraded_tome_dwarf_trade`, `tensura:skills/magic`
