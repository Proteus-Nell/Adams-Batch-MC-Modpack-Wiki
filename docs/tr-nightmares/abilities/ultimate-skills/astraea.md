# ｢ Astraea, Lord of Gifts ｣

<small>[TR: Nightmares](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![｢ Astraea, Lord of Gifts ｣](../../../assets/icons/trnightmare/skill/gift.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `trnightmare:astraea` |
| **Modes** | 2 |
| **Acquisition cost (MP)** | 750,000 |
| **Max mastery** | 1,000 |
| **Cooldowns (s)** | 10 |
| **Activation** | Press, Hold |

</div>

> The full unfettered potential of the Sword Saint's bloodline, descendant from the first Von Astraea

## Modes

| # | Mode |
|---|---|
| 1 | Sword Saint |
| 2 | Blessing Bestowal |

## Costs

| When | Magicule (MP) | Aura (AP) |
|---|---|---|
| Always | *set by config (base cost)* |  |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released
- Adjusted by scrolling while active
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers on melee contact
- Triggers when you are attacked
- Triggers when you take damage
- Triggers when an effect is applied to you
- Triggers when a projectile hits you
- Triggers when you die
- Triggers when you respawn
- Does something when first learned

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| inst1 | 50 | add |
| inst2 | 100 | add |

## Obtaining

- Acquisition checks: [Glorious](../unique-skills/glorious.md), [｢ Astraea, Lord of Gifts ｣](astraea.md), [Gift](../unique-skills/gift.md)
- In-game message: *The Odd Laguna recognizes your strength and grants you further gifts to use for both yourself and others. This cannot be rejected.*

## Related

- **Related skills:** [Phoenix](phoenix.md), [Sword Saint](sword-saint.md), [Death God](death-god.md), [Phoenix Next](phoenix-next.md), [Hero Banner Blessing](../extra-skills/hero-banner-blessing.md), [Glorious](../unique-skills/glorious.md), [Gift](../unique-skills/gift.md)
- **Referenced by:** [Blessing of Faith](../extra-skills/faith-blessing.md), [｢ Zehirete, God of Faith ｣](zehirete.md)

## Stats (config defaults)

Set in [`config/nightmare/ability/skill/nightmare_ult.toml`](../../configs/config-nightmare-ability-skill-nightmare-ult.md).

| Option | Default | Description |
|---|---|---|
| `Astraea.masterySinUlt` | 15,000 | The max amount of mastery points for Sin Ultimate Skills. |
| `Astraea.masteryVirtueUlt` | 25,000 | The max amount of mastery points for Virtue Ultimate Skills. |
| `Astraea.masteryAngelicUlt` | 5,000 | The max amount of mastery points for Angelic Ultimate Skills. |
| `Astraea.masteryDemonicUlt` | 5,000 | The max amount of mastery points for Demonic Ultimate Skills. |
| `Astraea.masteryGodUlt` | 50,000 | The max amount of mastery points for God Ultimate Skills. |
| `Astraea.masteryKingUlt` | 35,000 | The max amount of mastery points for King Ultimate Skills. |
| `Astraea.masteryGenericUlt` | 5,000 | The max amount of mastery points for Generic Ultimate Skills. |
| `Astraea.mpAcquirement` | 750,000 | Magicule cost required to acquire Astraea. |
| `Astraea.blessingCreationCooldown` | 10 | Cooldown for Blessing Creation (mode 0). |
| `Astraea.blessingBestowalCooldown` | 100 | Cooldown for Blessing Bestowal (mode 1). |
| `Astraea.swordSaintEngraveCooldown` | 10 | Cooldown for Sword Saint Holy Weapon engraving (mode 3). |
| `Astraea.swordSaintMaxHolyWeapon` | 3 | Maximum Holy Weapon level Astraea can engrave (Sword Saint). |
| `Astraea.enableUltimateEvolution` | true | Enable evolution from Gift to Astraea. |
| `Astraea.astraMobs` | 500 | Mobs slain for Astraea |
| `Astraea.astraSkills` | 50 | Skills mastered slain for Astraea |
| `Astraea.astraHeroCount` | 50 | Raid Victories for Astraea |
| `Astraea.astraSubs` | 50 | Subordinate Count for Astraea |
| `Astraea.allowedBlessings` | "trnightmare:dark_blessing", "trnightmare:earth_blessing", "trnightmare:fire_blessing", "trnightmare:gathering_spirits_blessing", "trnightmare:judgement_blessing", "trnightmare:lakes_blessing", "trnightmare:light_blessing", "trnightmare:sandplay_blessing", "trnightmare:shedding_blood_blessing", "trnightmare:time_blessing", "trnightmare:water_blessing", "trnightmare:wind_blessing", "trnightmare:unarmed_combat_blessing", "trnightmare:critical_blessing", "trnightmare:fortitude_blessing", "trnightmare:faith_blessing", "trnightmare:wind_reading", "trnightmare:wind_evasion", "trnightmare:sky_enjoyer", "trnightmare:insensitivity" ... (22 total) | Permitted Divine Protection skills for Astraea menus and sub-skill creation. |

## In-game messages

<details markdown><summary>Show 5 messages</summary>

- How can I be a sword saint... Without a sword to saint?
- You have no blessings to bestow.
- You've failed to create a Blessing.
- Blessing Creation
- Would you like to create this blessing?

</details>
