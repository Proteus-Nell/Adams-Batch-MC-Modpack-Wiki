# Deal Maker

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Deal Maker](../../../assets/icons/trnightmare/skill/deal_maker.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `trnightmare:deal_maker` |
| **Modes** | 4 |
| **Acquisition cost (MP)** | 50,000 |
| **Activation** | Toggle, Press, Hold |

</div>

> Forge binding contracts with other entities to exchange attributes, skills, items, and more.

## Modes

| # | Mode |
|---|---|
| 1 | Deal |
| 2 | Contract Book |
| 3 | End Deal |
| 4 | Storage |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | 500 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Triggers when you are attacked
- Triggers when you die
- Triggers when you respawn

## Obtaining

- Listed in the `skillTheftBlacklist` config option (config/nightmare/ability/skill/nightmare_ult.toml): Skill IDs that Mammon cannot copy or steal.

## Related

- **Items:** [Soul](../../items/miscellaneous/soul.md)
- **Referenced by:** [｢ Pazuzu, Lord of Mischief ｣](../ultimate-skills/pazuzu.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_unique.toml`](../../configs/config-nightmare-ability-skill-nightmare-unique.md).

| Option | Default | Description |
|---|---|---|
| `dealMaker.mpAcquirement` | 50,000 | Magicule cost to acquire Deal Maker. |
| `dealMaker.magiculeCost` | 500 | Magicule cost to activate. |
| `dealMaker.cooldown` | 30 | Cooldown in seconds after activation. |
| `dealMaker.maxActiveDeals` | 50 | Maximum number of active deals a player can have. |
| `dealMaker.maxDealDistance` | 100 | Maximum distance in blocks for deal creation. |

## In-game messages

<details markdown><summary>Show 12 messages</summary>

- &lt;shadow c=550000 a=0.9&gt;&lt;fade a=0.4 f=0.8&gt;&lt;wave a=0.4 f=0.6 w=0.3&gt;&lt;grad from=#6B0000 to=#AA0000&gt;Deal Maker&lt;/grad&gt;&lt;/wave&gt;&lt;/fade&gt;&lt;/shadow&gt;
- &lt;shake&gt;&lt;neon p=4 r=1 a=0.1&gt;&lt;grad from=#FF6347 to=#DC143C hue f=0.4 sp=10&gt;Forge binding contracts with other entities to exchange attributes, skills, items, and more.&lt;/grad&gt;&lt;/neon&gt;&lt;/shake&gt;
- You have reached the maximum number of active deals.
- Deal successfully created!
- Failed to create deal.
- You need a signed contract in your main hand, or use empty hand to get a writable contract.
- You received a Writable Contract. Write deal data into it, then use Deal mode again to forge the deal.
- Opening contract book...
- You have no active deals.
- You have no stored deals.
- No souls with ultimate skills found in storage.
- [Soul Bond] You collected the soul of %s.

</details>
