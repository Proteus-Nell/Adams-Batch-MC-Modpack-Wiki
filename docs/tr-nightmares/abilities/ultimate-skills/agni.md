# ｢ Agni, Lord of Blaze ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:agni` |
| **Modes** | 4 |
| **Acquisition cost (MP)** | 5,000,000 |
| **Max mastery** | 3,000 |
| **Activation** | Toggle, Hold |

</div>

> Ultimate blaze charity — Flame Authority, Blast Blow, Blazeball, Maximum Blazeball, and Blaze Wave.

## Modes

| # | Mode |
|---|---|
| 1 | Blast Blow |
| 2 | Blazeball |
| 3 | Maximum Blazeball |
| 4 | Blaze Wave |

## How it works

- Can be toggled on and off
- Charged or channelled by holding the skill key
- Triggers when you damage a target

## Obtaining

- Listed in the `astralMasteredCreationUltimates` config option (config/nightmare/ability/skill/nightmare_ult.toml): Ultimate skill IDs only offered from Astral Light Skill Creation when Astral Light is mastered.
- Acquisition checks: [｢ Agni, Lord of Blaze ｣](agni.md), [｢ Raguel, Lord of Charity ｣](raguel.md)
- In-game message: *The nether's flames crown you. Agni awakens.*

## Related

- **Related skills:** [｢ Raguel, Lord of Charity ｣](raguel.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Agni.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Agni.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Agni.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Agni.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Agni.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Agni.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Agni.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Agni.mpAcquirement` | 5,000,000 | Magicule cost to acquire Agni. |
| `Agni.evolutionBlazePowderEaten` | 10 | Blaze powder uses required to evolve Raguel into Agni. |
| `Agni.blastBlowKillEpRatioUltimate` | 0.5 | Target max EP must be below this fraction of owner max EP to instakill (has ultimate). 0.5 = 50%. |
| `Agni.blastBlowKillEpRatioNoUltimate` | 0.6 | Target max EP must be below this fraction of owner max EP to instakill (no ultimate). 0.6 = 60%. |
| `Agni.blastBlowFlameDamage` | 50 | Flame damage on non-instakill Blast Blow hit (unmastered). |
| `Agni.blastBlowFlameDamageMastered` | 100 | Flame damage on non-instakill Blast Blow hit (mastered). |
| `Agni.enableUltimateEvolution` | true | Whether Agni can be obtained naturally |

## Tags

`tensura:skills/joyful`, `tensura:skills/ultimate_skills`
