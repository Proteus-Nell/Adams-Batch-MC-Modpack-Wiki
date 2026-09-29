# Divine Ki Release

<small>[Tensura: Reincarnated](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Intrinsic Skills](index.md)</small>

<div class="infobox" markdown>

![Divine Ki Release](../../../assets/icons/tensura/skill/divine_ki_release.png)

| | |
|---|---|
| **Type** | Intrinsic Skill |
| **ID** | `tensura:divine_ki_release` |
| **Activation** | Toggle |

</div>

> Use your Divine Ki to amplify your battlewill to deal more damage and destroy weaker equipment.

## How it works

- Can be toggled on and off
- Triggers when you damage a target
- Triggers on melee contact

### Attribute changes

| Attribute | Amount | Operation |
|---|---|---|
| degrade | 1 | add |

## Obtaining

- Intrinsic skill of: [Divine Beast](../../races/divine-beast.md), [Divine Bird](../../races/divine-bird.md), [Divine Oni](../../races/divine-oni.md), [Divine Fighter](../../races/divine-fighter.md), [Divine Giant](../../races/divine-giant.md), [Divine Boar](../../races/divine-boar.md), [Divine Dragon](../../races/divine-dragon.md), [Divine Fish](../../races/divine-fish.md), [Divine Elf](../../races/divine-elf.md), [Divine Human](../../races/divine-human.md), [Divine Dwarf](../../races/divine-dwarf.md), [God Slime](../../races/god-slime.md), [Divine Vampire](../../races/divine-vampire.md), [Divine Skeleton](../../races/divine-skeleton.md), [Devil Lord](../../races/devil-lord.md), [Divine Chimera](../../../tr-nightmares/races/divine-chimera.md), [Divine Dragon Lord](../../../tr-nightmares/races/divine-dragon-lord.md), [Divine Gehenna Dragon](../../../tr-nightmares/races/divine-gehenna-dragon.md), [Divine Fox](../../../tr-nightmares/races/divine-fox.md), [Knight of Black](../../../tr-nightmares/races/knight-black.md), [pTrue qFairy pKing](../../../tr-nightmares/races/true-fairy-king.md), [Guardian Of qThe Tree](../../../tr-nightmares/races/guardian-of-the-tree.md), [Divine Saiyan](../../../elite-tensura/races/divine-saiyan.md), [Divine Majin Elemental](../../../tensura-mysticism/races/divine-majin-elemental.md), [Divine Elemental](../../../tensura-mysticism/races/divine-elemental.md), [Chaos Metalloid](../../../tensura-mysticism/races/chaos-metalloid.md), [Devil Doll](../../../tensura-mysticism/races/devil-doll.md), [Archangel](../../../ascension/races/archangel.md), [Seraphim](../../../ascension/races/seraphim.md), [Divine Angel](../../../ascension/races/divine-angel.md), [Fallen Angel](../../../ascension/races/fallen-angel.md), [Cosmic Deity](../../../ascension/races/cosmic-deity.md), [Chaotic Deity](../../../ascension/races/chaotic-deity.md), [6 Tailed Fox](../../../ascension/races/six-tail-fox.md), [9 Tailed Fox](../../../ascension/races/nine-tail-fox.md), [Divine Kitsune](../../../ascension/races/divine-kitsune.md), [Royal Djinn](../../../ascension/races/royal-djinn.md), [Wishbound Djinn](../../../ascension/races/wishbound-djinn.md), [Primordial Djinn](../../../ascension/races/primordial-djinn.md), [Ascended Djinn](../../../ascension/races/ascended-djinn.md), [Sovereign Djinn](../../../ascension/races/sovereign-djinn.md), [Infinite Djinn](../../../ascension/races/infinite-djinn.md), [Omniversal Djinn](../../../ascension/races/omniversal-djinn.md), [Chaos Dragon](../../../ascension/races/chaos-dragon.md), [Beholder](../../../ascension/races/beholder.md), [Death Tyrant](../../../ascension/races/death-tyrant.md), [Divine King](../../../ascension/races/divine-king.md), [Sun Wukong](../../../ascension/races/sun-wukong.md)
- Listed in the `intrinsicSkills` config option (config/nightmare/race/scholar_config.toml): List of skills obtained by this race.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/restricted_human_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/dragonoid_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/phantom_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/sculk_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/forgotten_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/wyrm_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/angel_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/direwolf/direwolf_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/beetle_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/centipede_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/ant_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/scorpion_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/mantis_config.toml): The list of intrinsic skills that the race gets.
- Listed in the `intrinsicSkills` config option (config/mysticism/race/insect/wasp_config.toml): The list of intrinsic skills that the race gets.

## Related

- **Referenced by:** [｢ Alternative, Proxy Rights ｣](../../../tr-nightmares/abilities/ultimate-skills/alternative.md)

## Stats (config defaults)

Set in [`config/tensura/ability/skill/intrinsic_config.toml`](../../configs/config-tensura-ability-skill-intrinsic-config.md).

| Option | Default | Description |
|---|---|---|
| `DivineKiRelease.battlewillDamage` | 50 | The bonus battlewill damage when toggled. |
| `DivineKiRelease.battlewillDamageMastered` | 100 | The bonus battlewill damage when toggled with mastery. |
| `DivineKiRelease.durabilityBreak` | 3 | The multiplier of the durability break of the target's equipments when damaged by user's physical/battlewill attack. |
| `DivineKiRelease.durabilityBreakMastered` | 5 | The multiplier of the durability break of the target's equipments when damaged by user's physical/battlewill attack when mastered. |

## Tags

`tensura:skills/intrinsic_skills`, `tensura:skills/restricted_learnable`
