# Races

<small>[Elite Tensura](../index.md)</small>

Elite Tensura adds **4** races: **1** starting, **2** in-between and **1** final.

- **Starting:** the first race of its evolution line. Nothing evolves into it, so you get it by reincarnating into it or through a special item, skill or event.
- **In-between:** reached by evolving, and can evolve further.
- **Final:** the last step of its line. It does not evolve any further.

Races that link to other mods' races (for example an addon race that evolves from a Tensura race) are placed using the whole pack's evolution trees.

<div class="filter-table" data-filter="Stage" data-order="Starting,In-between,Final" markdown>

| Race | Stage | Difficulty | Alignment | Evolves from | Evolves into |
|---|---|---|---|---|---|
| [Divine Saiyan](divine-saiyan.md) | <span class="stage stage-final">Final</span> | Extreme | Default | [High Class Saiyan](high-saiyan.md) |  |
| [High Class Saiyan](high-saiyan.md) | <span class="stage stage-in-between">In-between</span> | Extreme | Default | [Lesser Saiyan](lesser-saiyan.md), [Medium Class Saiyan](medium-saiyan.md) | [Divine Saiyan](divine-saiyan.md) |
| [Lesser Saiyan](lesser-saiyan.md) | <span class="stage stage-starting">Starting</span> | Extreme | Default |  | [Medium Class Saiyan](medium-saiyan.md), [High Class Saiyan](high-saiyan.md) |
| [Medium Class Saiyan](medium-saiyan.md) | <span class="stage stage-in-between">In-between</span> | Extreme | Default | [Lesser Saiyan](lesser-saiyan.md) | [High Class Saiyan](high-saiyan.md) |

</div>

## Evolution trees

### Lesser Saiyan line

```mermaid
flowchart LR
  r0["Divine Saiyan"]
  r1["High Class Saiyan"]
  r2["Lesser Saiyan"]
  r3["Medium Class Saiyan"]
  r1 --> r0
  r2 --> r1
  r2 --> r3
  r3 --> r1
```
