# Stick Steel Thread

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Extra Skills](index.md)</small>

<div class="infobox" markdown>

![Stick Steel Thread](../../../assets/icons/tensura/skill/sticky_steel_thread.png)

| | |
|---|---|
| **Type** | Extra Skill |
| **ID** | `tensura:sticky_steel_thread` |
| **Modes** | 4 |
| **Cooldowns (s)** | 1 mastered, 3 otherwise, 3 mastered, 5 otherwise |
| **Activation** | Press |

</div>

> Manipulate threads in various form.

## Modes

| # | Mode |
|---|---|
| 1 | Sticky |
| 2 | Steel |
| 3 | Slinger |
| 4 | Arcane Thread Fetters |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Steel | 100 |  |
| Slinger | 200 |  |
| Arcane Thread Fetters | 200 |  |
| other modes | 50 |  |

## How it works

- Activated by pressing the skill key

## Obtaining

- Innate to mobs: [Black Spider](../../mobs/black-spider.md)
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Golden Chimera can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Chimera Lord can randomly receive.
- Listed in the `intrinsicPool` config option (config/nightmare/race/chimera_config.toml): List of intrinsic skills Divine Chimera can randomly receive.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/direwolf/special_direwolf_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Effects:** [Webbed](../../effects/webbed.md), [Silence](../../effects/silence.md)
- **Items:** [Sticky Web Cartridge](../../items/miscellaneous/sticky-web-cartridge.md), [Sticky Steel Web Cartridge](../../items/miscellaneous/sticky-steel-web-cartridge.md), [Web Cartridge](../../items/miscellaneous/web-cartridge.md), [Steel Thread](../../items/miscellaneous/steel-thread.md)
- **Summons / entities:** Web Bullet

## Stats (config defaults)

Set in [`config/tensura/ability/skill/extra_config.toml`](../../configs/config-tensura-ability-skill-extra-config.md).

| Option | Default | Description |
|---|---|---|
| `StickySteelThread.magiculeCostSticky` | 50 | Magicule Cost to activate Sticky Thread mode. |
| `StickySteelThread.magiculeCostSteel` | 100 | Magicule Cost to activate Steel Thread mode. |
| `StickySteelThread.magiculeCostSlinger` | 200 | Magicule Cost to activate Slinger mode. |
| `StickySteelThread.magiculeCostArcane` | 200 | Magicule Cost to activate Arcane Thread mode. |
| `StickySteelThread.threadCooldown` | 3 | The cooldown in second of Sticky/Steel Thread mode. |
| `StickySteelThread.threadCooldownMastered` | 1 | The cooldown in second of Sticky/Steel Thread mode when mastered. |
| `StickySteelThread.arcaneRange` | 10 | The maximum range in block of Arcane Thread mode. |
| `StickySteelThread.arcaneRangeMastered` | 20 | The maximum range in block of Arcane Thread mode when mastered. |
| `StickySteelThread.arcaneDuration` | 500 | The duration in tick of the Webbed effect of Arcane Thread mode. |
| `StickySteelThread.arcaneReactivate` | 100 | The maximum duration since activated for Arcane Thread to reactivate to deal damage. |
| `StickySteelThread.arcaneReactivateMastered` | 200 | The maximum duration since activated for Arcane Thread to reactivate to deal damage when mastered. |
| `StickySteelThread.arcaneReactivateDamage` | 30 | The damage of Arcane Thread when reactivate. |
| `StickySteelThread.arcaneReactivateDamageMastered` | 60 | The damage of Arcane Thread when reactivate with mastery. |
| `StickySteelThread.arcaneCooldown` | 5 | The cooldown in second of Arcane Thread mode. |
| `StickySteelThread.arcaneCooldownMastered` | 3 | The cooldown in second of Arcane Thread mode when mastered. |

## Tags

`tensura:skills/extra_skills`
