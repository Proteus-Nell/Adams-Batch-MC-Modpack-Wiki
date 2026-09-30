# Walpurgis Hall

<small>[Elite Tensura](../index.md) &rsaquo; [Dimensions](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **ID** | `elitetensura:walpurgis_hall` |
| **Dimension type** | `elitetensura:walpurgis_dim_type` |
| **Generator** | `minecraft:flat` |
| **Has skylight** | False |
| **Has ceiling** | True |
| **Ultrawarm** | False |
| **Natural** | False |
| **Piglin safe** | True |
| **Bed works** | False |
| **Respawn anchor works** | False |
| **Has raids** | False |
| **Fixed time** | 18000 |
| **Min y** | 0 |
| **Height** | 384 |
| **Ambient light** | 0.1 |
| **Coordinate scale** | 1.0 |

</div>

## What it does

The Council Hall where Demon Lords hold a **Walpurgis** banquet. Only players who count as Demon Lords can enter, and only while a banquet is running. The whole system can be switched off with the false gamerule.

**Calling a Walpurgis:** a Demon Lord uses a [Walpurgis Orb](../items/miscellaneous/walpurgis-orb.md). A gate to the hall opens where they stand, and the other Demon Lords have **10 minutes** to answer by using their own orb. If at least **3** answer, the banquet convenes; otherwise it's cancelled. Demon Lords get in by stepping into a gate or with `/etwalpurgis teleport`, and their nation gains reputation for attending.

**How a banquet runs:**

1. **Agenda** (5 minutes): Demon Lords submit motions: Territorial Claim, Declare Enemy, Declare Neutral, New Demon Lord Recognition, Expel Member, Treaty or Free Topic. If nobody submits one, the banquet dissolves.
2. **Vote** (5 minutes per motion, extended by 2 minutes while votes are missing, up to 15 minutes): vote with `/etwalpurgis vote aye|nay|abstain`. A [Walpurgis Seal](../items/miscellaneous/walpurgis-seal.md) holder's vote counts 2 times.
3. **Combat Clause:** after a tied vote the council waits 60 s for a challenge (`/etwalpurgis challenge <name>`). The defender has 30 s to accept, and the duel (first to fall to half a heart loses, at most 5 minutes) settles the motion. No challenge, a timeout or a disconnect means the motion fails.

Passed motions take effect right away: territorial claims, public enemies and treaties are recorded (`/etwalpurgis territories`, `enemies` and `treaties` list them). When the banquet ends, everyone in the hall is sent back and the gates close. The council then rests for **150 minutes** before another Walpurgis can be called.
