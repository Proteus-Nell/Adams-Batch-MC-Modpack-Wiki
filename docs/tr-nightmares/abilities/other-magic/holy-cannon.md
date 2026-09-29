# Holy Cannon

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Other Magic](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Other Magic |
| **ID** | `trnightmare:holy_cannon` |
| **Max mastery** | 300 |
| **Activation** | Hold |

</div>

> Take your magicules and infuse them with a steady stream of holy energy into a beam, steadily dispersing enemy magicules into the air.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 5,000 |  |

## How it works

- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Obtaining

- Can appear in common tomes in buried wizard towers
- Can appear in common tomes in burnt wizard towers
- Can appear in common tomes in frozen wizard towers
- Can appear in common tomes in rotted wizard towers
- Can appear in common tomes in ruined wizard towers
- Can be found in skill tomes
- Sold by dwarf traders (low basic tome)
- Sold by dwarf traders (low upgraded tome)
- Sold by dwarf traders (medium basic tome)
- Sold by dwarf traders (medium upgraded tome)
- Can appear in uncommon tomes in buried wizard towers
- Can appear in uncommon tomes in burnt wizard towers
- Can appear in uncommon tomes in frozen wizard towers
- Can appear in uncommon tomes in rotted wizard towers
- Can appear in uncommon tomes in ruined wizard towers

## Related

- **Summons / entities:** Holy Cannon Projectile

## Stats (config defaults)

Set in [`config/nightmare/ability/magic/holy.toml`](../../configs/config-nightmare-ability-magic-holy.md).

| Option | Default | Description |
|---|---|---|
| `HolyCannon.castTime` | 3 | Cast time in seconds. |
| `HolyCannon.magiculeCost` | 5,000 | Magicule Cost to cast. |
| `HolyCannon.spiritronCost` | 10 | Spiritron Cost to cast. |
| `HolyCannon.holyDamage` | 40 | The holy damage of the beam. |
| `HolyCannon.range` | 8 | The block range of the beam. |

Set in [`config/tensura/ability/magic_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-magic-config.md).

| Option | Default | Description |
|---|---|---|
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masterySummoning` | 200 | The max amount of mastery point for Summoning Magic. |
| `AspectualMagic.masteryLow` | 100 | The max amount of mastery point for Low Aspectual Magic. |
| `AspectualMagic.masteryMedium` | 300 | The max amount of mastery point for Medium Aspectual Magic. |
| `AspectualMagic.masteryHigh` | 700 | The max amount of mastery point for High Aspectual Magic. |
| `AspectualMagic.masteryGreat` | 1,500 | The max amount of mastery point for Great Aspectual Magic. |

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

`tensura:skills/common_tome_buried_wizard_tower`, `tensura:skills/common_tome_burnt_wizard_tower`, `tensura:skills/common_tome_frozen_wizard_tower`, `tensura:skills/common_tome_rotted_wizard_tower`, `tensura:skills/common_tome_ruined_wizard_tower`, `tensura:skills/found_in_tome`, `tensura:skills/low_basic_tome_dwarf_trade`, `tensura:skills/low_upgraded_tome_dwarf_trade`, `tensura:skills/magic`, `tensura:skills/medium_basic_tome_dwarf_trade`, `tensura:skills/medium_upgraded_tome_dwarf_trade`, `tensura:skills/uncommon_tome_buried_wizard_tower`, `tensura:skills/uncommon_tome_burnt_wizard_tower`, `tensura:skills/uncommon_tome_frozen_wizard_tower`, `tensura:skills/uncommon_tome_rotted_wizard_tower`, `tensura:skills/uncommon_tome_ruined_wizard_tower`
