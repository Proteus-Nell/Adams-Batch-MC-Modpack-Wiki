# The Unbound Jester

<small>[Ascension](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Ultimate Skills](index.md)</small>

<div class="infobox" markdown>

![The Unbound Jester](../../../assets/icons/ascension/skill/unbound_jester.png)

| | |
|---|---|
| **Type** | Ultimate Skill |
| **ID** | `ascension:unbound_jester` |
| **Modes** | 3 |
| **Max mastery** | 100 |
| **Cooldowns (s)** | 60, 10 mastered, 60 otherwise |
| **Activation** | Press, Hold |

</div>

> Ultimate awakening of Imprisoned Jester. In-slot: +50%% physical/magic damage, +30%% crit chance for +100%% crit. Toggle: 25%% reflect on all incoming damage; The Bit Goes On — fatal hits become 5s of invulnerable invisibility instead of death (5min CD, drains pools to 5%%). Modes: Chaos Theater (360° AOE, hits HP+SHP, 16-block radius), Curtain Call (current-HP AOE, 16-block radius, hits HP+SHP), Final Punishment (mark target with Sentence — 5%% max HP/sec for 10s, on death absorbs 25%% EP).

## Modes

| # | Mode |
|---|---|
| 1 | Chaos Theater |
| 2 | Curtain Call |
| 3 | Final Punishment |

## How it works

- Activated by pressing the skill key
- Charged or channelled by holding the skill key
- Triggers when the held key is released

## Stats (config defaults)

Set in [`config/tensura/ascension-skills.toml`](../../configs/config-tensura-ascension-skills.md).

| Option | Default | Description |
|---|---|---|
| `unbound_jester.enabled` | true | Enable The Unbound Jester. |
| `unbound_jester.theaterCooldownSecondsMastered` | 10 (0 to 600) | Chaos Theater cooldown (seconds, mastered). |
| `unbound_jester.theaterCooldownSeconds` | 30 (0 to 600) | Chaos Theater cooldown (seconds, unmastered). |
| `unbound_jester.theaterEpCap` | 10,000,000 (0 to 1,000,000,000,000) | Caster EP cap used for Chaos Theater damage scaling. |
| `unbound_jester.theaterEpFactor` | 0.0001 (0 to 1) | EP-to-damage factor for Chaos Theater (1.5× Chaos Spades' default; was 2.0× before the -25% nerf). |
| `unbound_jester.theaterAuraFraction` | 0.05 (0 to 1) | Fraction of caster's max aura consumed per Chaos Theater cast (0.05 = 5%). |
| `unbound_jester.theaterRadius` | 8 (1 to 64) | Chaos Theater AOE radius (blocks). |
| `unbound_jester.curtainRadius` | 16 (1 to 64) | Curtain Call AOE radius (blocks). |
| `unbound_jester.curtainCooldownSeconds` | 60 (0 to 3,600) | Curtain Call cooldown (seconds). |
| `unbound_jester.punishRange` | 16 (1 to 128) | Final Punishment targeting range (blocks). |
| `unbound_jester.punishEpRatio` | 1.5 (1 to 100) | Caster-EP / target-EP ratio required to apply Sentence. |
| `unbound_jester.punishDurationSeconds` | 10 (1 to 600) | Sentence effect duration (seconds). |
| `unbound_jester.punishCooldownSecondsMastered` | 10 (0 to 3,600) | Final Punishment cooldown, mastered (seconds). |
| `unbound_jester.punishCooldownSeconds` | 60 (0 to 3,600) | Final Punishment cooldown, unmastered (seconds). |
| `unbound_jester.punishHpFraction` | 0.05 (0 to 1) | Fraction of target's max HP dealt per second by Sentence (0.05 = 5%). |
| `unbound_jester.punishEpAbsorb` | 0.25 (0 to 1) | Fraction of target's EP absorbed by caster on death during Sentence (0.25 = 25%). |
| `unbound_jester.physicalBonus` | 0.5 (0 to 10) | In-slot outgoing physical damage bonus (0.50 = +50%). |
| `unbound_jester.magicBonus` | 0.5 (0 to 10) | In-slot outgoing magic damage bonus (0.50 = +50%). |
| `unbound_jester.critChance` | 0.3 (0 to 1) | In-slot crit chance per hit (0.30 = 30%). |
| `unbound_jester.critDamage` | 1 (0 to 100) | Crit damage bonus (1.00 = +100% on crit). |
| `unbound_jester.reflectFraction` | 0.25 (0 to 1) | Fraction of all incoming damage reflected to the attacker while toggled (0.25 = 25%). |

## In-game messages

<details markdown><summary>Show 7 messages</summary>

- Not enough aura.
- Target is too strong to sentence.
- %1$s has sentenced you.
- Absorbed %2$s EP from %1$s's sentence.
- The bit goes on...
- ✦ Soul Resonance Achieved ✦
- The Unbound Jester awaits your awakening.

</details>
