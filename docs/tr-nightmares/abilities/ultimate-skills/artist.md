# ｢ Artist, Authentic Writer ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:artist` |
| **Modes** | 3 |
| **Activation** | Press |

</div>

> The ultimate evolution of Imitator. Act any target including ultimates, battlewills, and magics. Imprint disguise onto stage crew. Open the Gallery to acquire any learned skill.

## Modes

| # | Mode |
|---|---|
| 1 | Actor |
| 2 | Stage Crew |
| 3 | Gallery Fake |

## How it works

- Activated by pressing the skill key

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Artist.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Artist.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Artist.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Artist.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Artist.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Artist.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Artist.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Artist.mpAcquirement` | 750,000 | Magicule cost to acquire Artist (evolution from Imitator). |
| `Artist.evolutionCatalogRequired` | 30 | Catalog entries required to evolve Imitator into Artist. |
| `Artist.enableUltimateEvolution` | true | Whether Artist evolution is allowed. |
| `Artist.learnRequired` | 100 | Number of learning pulses required to fully learn a target (same as Imitator). |
| `Artist.epGateRatio` | 0.5 | EP ratio gate for acting as a player (same as Imitator). |
| `Artist.magiculeCostGalleryFake` | 500,000 | Magicule cost for Gallery Fake skill acquisition. |
| `Artist.cooldownGalleryFake` | 200 | Cooldown for Gallery Fake skill acquisition in ticks (20 ticks = 1 second). |
