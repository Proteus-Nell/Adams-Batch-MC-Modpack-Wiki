# Forbidden Knowledge

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `trnightmare:forbidden_knowledge` |
| **Activation** | Toggle |

</div>

> You have gazed into the void and the void gazes back. You learn skills much faster

## How it works

- Can be toggled on and off

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| learning | 8 | add |
| mastery | 8 | add |

## Related

- **Summons / entities:** Tensura

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_extra.toml`](../../configs/config-nightmare-ability-skill-nightmare-extra.md).

| Option | Default | Description |
|---|---|---|
| `ForbiddenKnowledge.mpAcquirement` | 10,000 | Magicule Acquirement Cost. |
| `ForbiddenKnowledge.epRequirement` | 1,000,000 | Number of Existence Points the player must have to meet the natural requirements. |
| `ForbiddenKnowledge.learningPoint` | 8 | Number of Learning Points gained from Forbidden Knowledge. |
| `ForbiddenKnowledge.masteryPoint` | 8 | Number of Mastery Points gained from Forbidden Knowledge. |
