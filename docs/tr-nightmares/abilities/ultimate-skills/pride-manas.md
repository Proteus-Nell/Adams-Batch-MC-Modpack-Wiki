# Pride Manas

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:pride_manas` |
| **Acquisition cost (MP)** | 1,700,000 |
| **Max mastery** | 5,000 |
| **Activation** | Press, Hold |

</div>

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Has a continuous (per-tick) effect
- Does something when first learned

## Related

- **Related skills:** [｢ Lucifer, Lord of Pride ｣](lucifer.md), [Ego Management](../extra-skills/ego-management.md), [Auto Battle Mode](../extra-skills/auto-battle-mode.md), [Mathematician](../../../tensura-reincarnated/abilities/unique-skills/mathematician.md), [Usurper](../../../tensura-reincarnated/abilities/unique-skills/usurper.md), [Bewilder](../../../tensura-reincarnated/abilities/unique-skills/bewilder.md), [Severer](../../../tensura-reincarnated/abilities/unique-skills/severer.md), [Traveler](../../../tensura-reincarnated/abilities/unique-skills/traveler.md), [Thrower](../../../tensura-reincarnated/abilities/unique-skills/thrower.md), [Observer](../../../tensura-reincarnated/abilities/unique-skills/observer.md), [Healer](../../../tensura-reincarnated/abilities/unique-skills/healer.md), [Degenerate](../../../tensura-reincarnated/abilities/unique-skills/degenerate.md), [Berserker](../../../tensura-reincarnated/abilities/unique-skills/berserker.md), [Survivor](../../../tensura-reincarnated/abilities/unique-skills/survivor.md), [Wrath](../../../tensura-reincarnated/abilities/unique-skills/wrath.md), [｢ Raguel, Lord of Charity ｣](raguel.md), [｢ Gabriel, Lord of Patience ｣](gabriel.md)
- **Effects:** [Spearhead](../../../tensura-reincarnated/effects/spearhead.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Lucifer.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Lucifer.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Lucifer.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Lucifer.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Lucifer.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Lucifer.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Lucifer.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Lucifer.mpAcquirement` | 1,700,000 | The Cost for the Ultimate Skill: Lucifer. |
| `Lucifer.copyChance` | 20 | The skill copy chance when attacked (Arroganz). Matches Tensura Pride defaults. |
| `Lucifer.copyChanceMastered` | 100 | The skill copy chance when attacked with mastery. |
| `Lucifer.copyMastery` | 0.0004 | Mastery gained per magicule cost of a successfully copied ability. |
| `Lucifer.copyMasteryFail` | 0 | Multiplier of mastery gained per magicule cost of a failed copy attempt. |
| `Lucifer.copyCooldown` | 45 | Cooldown in seconds per mastery gained from a successful copy. |
| `Lucifer.copyCooldownFail` | 4.5 | Cooldown in seconds per mastery gained from a failed copy. |
| `Lucifer.ocularAnalysisCooldown` | 0 | Cooldown ticks applied to Ocular Analysis (mode 1) after attempts. Arroganz uses copyCooldown \* mastery on slot 0. |
| `Lucifer.LuciferMastered` | 100 | Number of mastered skills required for Lucifer evolution. |
| `Lucifer.LuciferHPPercentage` | 0.4 | HP percentage threshold for Lucifer evolution. |
| `Lucifer.enableUltimateEvolution` | true | Whether Lucifer evolution is allowed. If false, Pride cannot evolve into Lucifer. |
| `Lucifer.copyRanged` | 25 | This is the range of the projectile copying of Lucifer. |
| `Lucifer.copyRange` | 5 | This is the range of the normal copying of Lucifer. |
