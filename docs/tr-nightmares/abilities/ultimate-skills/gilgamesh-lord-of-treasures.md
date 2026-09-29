# Gilgamesh Lord Of Treasures

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:gilgamesh_lord_of_treasures` |
| **Acquisition cost (MP)** | 800,000 |
| **Max mastery** | 5,000 |
| **Activation** | Press, Hold |

</div>

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Adjusted by scrolling while active
- Has a continuous (per-tick) effect

## Obtaining

- Acquisition checks: [Babylon](../unique-skills/babylon.md), [Gilgamesh Lord Of Treasures](gilgamesh-lord-of-treasures.md)
- In-game message: *Babylon has evolved into Gilgamesh, Lord of Treasures.*

## Related

- **Related skills:** [Babylon](../unique-skills/babylon.md)
- **Referenced by:** [Gilgamesh King Of Uruk](gilgamesh-king-of-uruk.md), [｢ Gilgamesh, God of Myth ｣](gilgamesh-god-of-myth.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `GilgameshLord.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `GilgameshLord.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `GilgameshLord.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `GilgameshLord.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `GilgameshLord.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `GilgameshLord.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `GilgameshLord.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `GilgameshLord.mpAcquirement` | 800,000 | Magicule cost to acquire Gilgamesh, Lord of Treasures. |
| `GilgameshLord.enableUltimateEvolution` | true | Enable evolution from Babylon. |
