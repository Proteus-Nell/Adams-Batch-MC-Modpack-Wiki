# Raziel, Lord of Secrets

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![Raziel, Lord of Secrets](../../../assets/icons/trnightmare/skill/azrael.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:raziel` |
| **Modes** | 4 |
| **Acquisition cost (MP)** | 1,050,000 |
| **Max mastery** | 5,000 |
| **Cooldowns (s)** | 120, 180 |
| **Activation** | Toggle, Press |

</div>

> A hidden authority that erases names, seals secrets, and turns forbidden knowledge into veiled dominion.

## Modes

| # | Mode |
|---|---|
| 1 | Ink Manipulation |
| 2 | Confined Secrets |
| 3 | Secretive Intentions |
| 4 | Erase |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers when you are attacked
- Triggers when an effect is applied to you
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| negate | 100 | add |

## Obtaining

- You have awakened Raziel, Lord of Secrets.

## Related

- **Effects:** [Mind Control](../../../tensura-reincarnated/effects/mind-control.md), [Lust Drain](../../../tensura-reincarnated/effects/lust-drain.md), [Lust Embracement](../../../tensura-reincarnated/effects/lust-embracement.md), [Asmodeus](../../effects/asmodeus.md), [Asmodeusd](../../effects/asmodeusd.md), [Inked](../../effects/inked.md), [Anti-Skill](../../../tensura-reincarnated/effects/anti-skill.md)
- **Referenced by:** [Secretive Manas](secretive-manas.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Raziel.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Raziel.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Raziel.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Raziel.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Raziel.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Raziel.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Raziel.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Raziel.enableUltimateEvolution` | false | Whether Raziel can be granted when its direct obtainment requirements are met. |
| `Raziel.mpAcquirement` | 1,050,000 | Magicule acquirement cost. |
| `Raziel.enableLocateCommand` | true | Whether /trnightmare raziel locate is enabled. |
| `Raziel.enableRenameCommand` | true | Whether /trnightmare raziel rename is enabled. |
| `Raziel.deconstructScanIntervalTicks` | 40 | How often Raziel scans for forbidden ultimate skills. |
| `Raziel.secretMarkerAwakenCount` | 4 | Secret markers required to awaken the Secretive Ego. |
| `Raziel.inkDurationTicks` | 600 | Inked duration in ticks. |
| `Raziel.renameThreshold` | 5 | Inked stack threshold to rename the target. |
| `Raziel.antiSkillThreshold` | 12 | Inked stack threshold to apply Anti Skill. |
| `Raziel.inkCap` | 30 | Maximum Inked stacks. |
| `Raziel.antiSkillDurationTicks` | 400 | Anti Skill duration in ticks when Inked reaches the threshold. |
| `Raziel.confinedSecretsRange` | 64 | Targeting range for Confined Secrets. |
| `Raziel.confinedSecretsCooldownSeconds` | 120 | Cooldown for Confined Secrets in Tensura seconds. |
| `Raziel.confinedUltimateSealChance` | 0.5 | Chance to seal an Ultimate Skill with Confined Secrets. |
| `Raziel.confinedUltimateSealChanceMastered` | 0.75 | Chance to seal an Ultimate Skill with Confined Secrets when mastered. |
| `Raziel.eraseRange` | 64 | Targeting range for Erase. |
| `Raziel.eraseThreshold` | 30 | Minimum Inked stacks required before Erase can be used. |
| `Raziel.eraseCooldownSeconds` | 180 | Cooldown for Erase in Tensura seconds. |
| `Raziel.eraseUniqueCopyChance` | 0.15 | Chance for Erase to copy a Unique Skill. |
| `Raziel.strongEraseTargetEpRatio` | 0.5 | A target counts as strong if their EP is at least this fraction of the user's EP. |
| `Raziel.strongEraseTargetMinEp` | 100,000 | Absolute minimum EP for a target to count as strong for Secretive Ego progress. |
| `ultMasteryConfig.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |

## In-game messages

<details markdown><summary>Show 14 messages</summary>

- Raziel's Secretive Ego has awakened.
- Secret Identity rejects subordination.
- %1$s was deconstructed into a Secret Marker.
- Secret Markers: %1$s/%2$s
- Erased %1$s and recorded %2$s skill(s).
- You do not possess Raziel.
- That name is invalid.
- Secret Identity will appear as %1$s.
- Ink Manipulation will rename targets to %1$s.
- Raziel Rename is disabled in the config.
- Raziel Locate is disabled in the config.
- No loaded subordinates were found.
- Raziel Locate:
- %1$s -&gt; %2$s @ (%3$s, %4$s, %5$s)

</details>

## Tags

`tensura:skills/secretive`, `tensura:skills/ultimate_skills`
