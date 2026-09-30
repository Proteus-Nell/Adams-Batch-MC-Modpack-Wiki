# Asmoday Prison Realm

<small>[TensuraMoreSkills](../index.md) &rsaquo; [Dimensions](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `tensuramoreskills:asmoday_prison_realm` |
| **Dimension type** | `tensuramoreskills:asmoday_prison_realm` |
| **Generator** | `minecraft:flat` |
| **Has skylight** | False |
| **Has ceiling** | False |
| **Ultrawarm** | False |
| **Natural** | False |
| **Piglin safe** | False |
| **Bed works** | False |
| **Respawn anchor works** | False |
| **Has raids** | False |
| **Min y** | 0 |
| **Height** | 256 |
| **Ambient light** | 0.03 |
| **Coordinate scale** | 1.0 |

</div>

## What it does

The dark, flat void that [Asmoday](../abilities/ultimate-skills/asmoday.md)'s **Five-Hundred-Year Closed Space** seals players into. Only players can be sealed.

**How someone ends up here:** the Asmoday user looks at a player within 48 blocks (64 mastered) and holds the ability for **30 seconds**. The target is slowed while it charges, and switching targets sets the charge back. When it finishes, the target is locked in a bedrock box of their own in this dimension, and the user gets a **Prison Cube**, the only key. A user can hold one prisoner at a time.

**While sealed:**

- The prisoner can't die or be hurt: they're healed to full every tick, kept topped up with 20 absorption, and can't get more than 6.5 blocks from the center.
- They're kept under [Spatial Blockade](../../tensura-reincarnated/effects/spatial-blockade.md), [Magic Interference](../../tensura-reincarnated/effects/magic-interference.md), [Movement Interference](../../tensura-reincarnated/effects/movement-interference.md) and [Energy Blockade](../../tensura-reincarnated/effects/energy-blockade.md) at high levels.
- Logging out doesn't help: they're put back in the box when they log in.
- Every 5 s the user pays **500,000** magicule (×0.62 once mastered), or 450 aura if they're short. Each missed payment costs the prison 8% stability, and at 0% it collapses.

**Release:** using the Prison Cube sends the prisoner back to where they were sealed. They're also thrown out, with brief [Movement Interference](../../tensura-reincarnated/effects/movement-interference.md), if the user dies or forgets Asmoday, if the dropped cube burns, falls into lava or into the void, or if the prison collapses.

The prison is only tracked while the server is running, so after a restart the prisoner is no longer held, healed or released by the cube, and has to get out of the box another way.
