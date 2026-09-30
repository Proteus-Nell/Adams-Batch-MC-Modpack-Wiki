# Races

<small>[TensuraMoreSkills](../index.md)</small>

TensuraMoreSkills adds **6** races: **2** starting, **3** in-between and **2** final. 1 race has no evolutions at all, so it counts as both starting and final.

- **Starting:** the first race of its evolution line. Nothing evolves into it, so you get it by reincarnating into it or through a special item, skill or event.
- **In-between:** reached by evolving, and can evolve further.
- **Final:** the last step of its line. It does not evolve any further.

Races that link to other mods' races (for example an addon race that evolves from a Tensura race) are placed using the whole pack's evolution trees.

<div class="filter-table" data-filter="Stage" data-order="Starting,In-between,Final" markdown>

| Race | Stage | Difficulty | Alignment | Evolves from | Evolves into |
|---|---|---|---|---|---|
| [Blood Monarch](blood-monarch.md) | <span class="stage stage-in-between">In-between</span> | Hard | Majin | [Blood Noble](blood-noble.md) | [Crimson Progenitor](crimson-progenitor.md) |
| [Blood Noble](blood-noble.md) | <span class="stage stage-in-between">In-between</span> | Hard | Majin | [Elder Bloodfiend](elder-bloodfiend.md) | [Blood Monarch](blood-monarch.md) |
| [Bloodfiend](bloodfiend.md) | <span class="stage stage-starting">Starting</span> | Intermediate | Majin |  | [Elder Bloodfiend](elder-bloodfiend.md) |
| [Crimson Progenitor](crimson-progenitor.md) | <span class="stage stage-final">Final</span> | Hard | Majin | [Blood Monarch](blood-monarch.md) |  |
| [Elder Bloodfiend](elder-bloodfiend.md) | <span class="stage stage-in-between">In-between</span> | Intermediate | Majin | [Bloodfiend](bloodfiend.md) | [Blood Noble](blood-noble.md) |
| [Parasite](parasite.md) | <span class="stage stage-starting">Starting</span> / <span class="stage stage-final">Final</span> | Easy | Majin |  |  |

</div>

## Evolution trees

### Bloodfiend line

```mermaid
flowchart LR
  r0["Blood Monarch"]
  r1["Blood Noble"]
  r2["Bloodfiend"]
  r3["Crimson Progenitor"]
  r4["Elder Bloodfiend"]
  r0 --> r3
  r1 --> r0
  r2 --> r4
  r4 --> r1
```
