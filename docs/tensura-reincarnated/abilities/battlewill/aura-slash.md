# Aura Slash

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Battlewill](index.md)</small>

<div class="infobox" markdown>

![Aura Slash](../../../assets/icons/tensura/skill/aura_slash.png)

| | |
|---|---|
| **Type** | Battlewill |
| **ID** | `tensura:aura_slash` |
| **Kind** | Melee |
| **Cooldowns (s)** | 1 mastered, 2 otherwise |
| **Activation** | Press |

</div>

> Condense your aura along your blade and release ranged slash.

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always |  | 50 |

## How it works

- Activated by pressing the skill key
- Does something when mastered

## Obtaining

- Sold by dwarf traders (medium manual)
- Listed in the `battlewillManualList` config option (config/tensura/ability/ability_config.toml): List of Battlewills that can be randomly obtained from using the Battlewill Manual.

## Related

- **Related skills:** [Heavy Slash](heavy-slash.md)
- **Referenced by:** [Heavy Slash](heavy-slash.md), [Arthur, The Once and Future King](../../../tensura-more-skills/abilities/ultimate-skills/arthur-once-and-future-king.md)

## Stats (config defaults)

Set in [`config/tensura/ability/battlewill_config.toml`](../../configs/config-tensura-ability-battlewill-config.md).

| Option | Default | Description |
|---|---|---|
| `AuraSlash.auraCost` | 50 | Aura Cost to activate. |
| `AuraSlash.attackMultiplier` | 1 | The damage multiplier of the projectiles compare to the user's weapon base attack damage when activated. |
| `AuraSlash.attackMultiplierMastered` | 2 | The damage multiplier of the projectiles compare to the user's weapon base attack damage when activated when Mastered. |

## Tags

`tensura:skills/battlewill`, `tensura:skills/medium_manual_dwarf_trade`
