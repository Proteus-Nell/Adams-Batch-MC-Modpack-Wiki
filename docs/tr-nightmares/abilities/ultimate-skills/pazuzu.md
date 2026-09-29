# ｢ Pazuzu, Lord of Mischief ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:pazuzu` |
| **Modes** | 6 |
| **Acquisition cost (MP)** | 1,000,000 |
| **Activation** | Toggle, Press |

</div>

> The ultimate evolution of Deal Maker — forge contracts that bind even ultimates, crystallize skills, and enter the minds of those bound to you.

## Modes

| # | Mode |
|---|---|
| 1 | Deal |
| 2 | Contract Book |
| 3 | End Deal |
| 4 | Storage |
| 5 | Skill Crystallize |
| 6 | Enter Mind |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Skill Crystallize | 5,000 |  |
| Enter Mind | 10,000 |  |
| other modes | 1,000 |  |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key

## Obtaining

- Acquisition checks: [｢ Pazuzu, Lord of Mischief ｣](pazuzu.md), [Deal Maker](../unique-skills/deal-maker.md)
- In-game message: *Evolution complete: Pazuzu has awakened.*

## Related

- **Related skills:** [Deal Maker](../unique-skills/deal-maker.md)
- **Items:** [Soul](../../items/miscellaneous/soul.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Pazuzu.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Pazuzu.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Pazuzu.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Pazuzu.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Pazuzu.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Pazuzu.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Pazuzu.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Pazuzu.mpAcquirement` | 1,000,000 | Magicule cost to acquire Pazuzu (evolution from Deal Maker). |
| `Pazuzu.enableUltimateEvolution` | true | Whether Pazuzu evolution is allowed. |
| `Pazuzu.magiculeCost` | 1,000 | Magicule cost to activate (general). |
| `Pazuzu.magiculeCostCrystallize` | 5,000 | Magicule cost for Skill Crystallize mode. |
| `Pazuzu.magiculeCostEnterMind` | 10,000 | Magicule cost for Enter Mind mode. |
| `Pazuzu.cooldownEnterMind` | 120 | Cooldown in seconds for Enter Mind mode. |
| `Pazuzu.maxActiveDeals` | 200 | Maximum number of active deals a player can have. |
| `Pazuzu.allowKingClassUltimates` | false | Whether Pazuzu can work on king-class ultimates (false = blocked). |

## In-game messages

<details markdown><summary>Show 9 messages</summary>

- &lt;neon p=12 r=3 a=0.08&gt;&lt;glitch f=2.5 j=0.03 b=0.01 s=0.12&gt;&lt;shadow c=000000 a=1&gt;&lt;pulse base=0.4 a=0.8 f=1.5&gt;&lt;grad from=#1A0000 to=#8B0000 sp=10&gt;&lt;rainb f=0.1 w=0.05&gt;Pazuzu, Lord of Mischief&lt;/rainb&gt;&lt;/grad&gt;&lt;/pulse&gt;&lt;/shadow&gt;&lt;/glitch&gt;&lt;/neon&gt;
- &lt;shake&gt;&lt;neon p=6 r=2 a=0.14&gt;&lt;grad from=#DA70D6 to=#800080 hue f=0.5 sp=12&gt;The ultimate evolution of Deal Maker — forge contracts that bind even ultimates, crystallize skills, and enter the minds of those bound to you.&lt;/grad&gt;&lt;/neon&gt;&lt;/shake&gt;
- You have no skills that can be crystallized.
- You have no active deals to enter the mind of.
- No deal parties are currently online.
- %s does not have an inner world dimension.
- Generating inner world for %s...
- Entering the mind of %s...
- Pazuzu Enter Mind Exit

</details>
