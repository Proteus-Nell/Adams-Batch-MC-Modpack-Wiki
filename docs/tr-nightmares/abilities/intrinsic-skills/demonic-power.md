# Demonic Power

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Demonic Power](../../../assets/icons/trnightmare/skill/demonic_power.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `trnightmare:demonic_power` |
| **Activation** | Toggle, Press |

</div>

> Darken my soul, for it is power I crave.

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect
- Does something when mastered

## Related

- **Effects:** [Strengthen](../../../tensura-reincarnated/effects/strengthen.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_intrinsic.toml`](../../configs/config-nightmare-ability-skill-nightmare-intrinsic.md).

| Option | Default | Description |
|---|---|---|
| `DemonicPower.epAcquirement` | 30 | Learning / obtainment cost. |
| `DemonicPower.meetEpThreshold` | 20,000 | Minimum EP to meet requirement. |
| `DemonicPower.magiculeCost` | 30 | Magicule cost per tick / toggle use. |
| `DemonicPower.strengthenTickDuration` | 240 | Strengthen duration (ticks) while toggled drain path. |
| `DemonicPower.strengthenTickAmplifier` | 2 | Strengthen amplifier while toggled. |
| `DemonicPower.pressDurationNormal` | 1,200 | Strengthen duration (ticks) on press when not mastered. |
| `DemonicPower.pressDurationMastered` | 2,400 | Strengthen duration (ticks) on press when mastered. |
| `DemonicPower.pressAmplifierNormal` | 2 | Strengthen amplifier on press when not mastered. |
| `DemonicPower.pressAmplifierMastered` | 4 | Strengthen amplifier on press when mastered. |
| `DemonicPower.toggleOffStripMaxAmplifier` | 2 | Strip strengthen on toggle off if amplifier at most this. |
