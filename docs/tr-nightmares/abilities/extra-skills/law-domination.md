# Law Domination

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `trnightmare:law_domination` |
| **Modes** | 2 |
| **Activation** | Toggle, Press |

</div>

> An improved law authority that passively cleanses law-affected debuffs and grants configurable effect immunity while toggled.

## Modes

| # | Mode |
|---|---|
| 1 | Abnormality Cleanse |
| 2 | Takeover |

## How it works

- Can be toggled on and off
- Activated by pressing the skill key
- Has a continuous (per-tick) effect

## Obtaining

- Listed in the `allowedSkillIds` config option (config/nightmare/ability/skill/nightmare_extra.toml): Skill ids that can be affected by Raphael-style alteration by default.

## Related

- **Effects:** [Magic Interference](../../../tensura-reincarnated/effects/magic-interference.md)
- **Referenced by:** [Alteration](alteration.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_extra.toml`](../../configs/config-nightmare-ability-skill-nightmare-extra.md).

| Option | Default | Description |
|---|---|---|
| `LawDomination.immuneEffectIds` | "tensura:infinite_inprisonment", "tensura:spatial_blockade" | Effects this skill grants immunity to while toggled. Use &lt;namespace:path&gt; IDs. |

Set in [`config/tensura/ability/skill/extra_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `LawManipulation.epAcquirement` | 800,000 | EP Requirement for Learning. |
| `LawManipulation.magicMastered` | 30 | The number of Magic needed to be mastered to learn. |
| `LawManipulation.resistBypassEP` | 1,000,000 | The amount of EP that the user needs to have minimum to be able to bypass Resist Skills with Magic/Battlewill when toggled. |
| `LawManipulation.cleanseRange` | 20 | The range in block of Abnormality Cleanse. |
| `LawManipulation.takeoverRange` | 30 | The range in block of Takeover. |
| `LawManipulation.brokenMagicCooldown` | 2 | The cooldown in second of the magic circle destroyed by Takeover for the targeted caster. |
| `LawManipulation.brokenMagicCooldownMastered` | 4 | The cooldown in second of the magic circle destroyed by Takeover for the targeted caster when mastered. |
| `LawManipulation.takeoverMultiplier` | 0.75 | The multiplier of the user's EP that a target with Law Manipulation needs to have above to be unaffected by Takeover. |
