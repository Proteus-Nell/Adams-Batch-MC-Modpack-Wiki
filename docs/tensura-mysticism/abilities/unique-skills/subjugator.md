# Subjugator

<small>[Tensura: Mysticism](../../index.md) &rsaquo; [Abilities](../index.md) &rsaquo; [Unique Skills](index.md)</small>

<div class="infobox" markdown>

![Subjugator](../../../assets/icons/mysticism/skill/subjugator.png)

| | |
|---|---|
| **Type** | Unique Skill |
| **ID** | `mysticism:subjugator` |
| **Modes** | 6 |
| **Activation** | Press, Hold |

</div>

> You've always been a powerful manipulator. Capable of bringing anyone and anything under your control. ...But, something is strange...

## Modes

| # | Mode |
|---|---|
| 1 | Takeover |
| 2 | Communication Movement |
| 3 | Communication Targeting |
| 4 | Unbreakable Defense |
| 5 | Return |
| 6 | The Voice |

## How it works

- Activated by pressing the skill key
- Triggers when the held key is released
- Adjusted by scrolling while active
- Has a continuous (per-tick) effect
- Triggers when you damage a target
- Triggers when you take damage
- Triggers when you die
- Triggers when one of your subordinates dies

## Related

- **Effects:** [Inspiration](../../../tensura-reincarnated/effects/inspiration.md)
- **Summons / entities:** Tensura

## Stats (config defaults)

Set in [`config/mysticism/ability/skill/unique_config.toml`](../../configs/config-mysticism-ability-skill-unique-config.md).

| Option | Default | Description |
|---|---|---|
| `Subjugator.mpAcquirement` | 95,000 | Magicule Acquirement Cost. |
| `Subjugator.unbreakableDefenseStep` | 2,000 | The step in loyalty points that is accounted for whenever the user is to gain more damage reduction from the passive. |
| `Subjugator.unbreakableDefenseGain` | 0.02 | The percentage of damage reduction you gain every time you gain a multiple of the above value. (Please do it in decimal notation and not percentage notation.) |
| `Subjugator.loyaltyRange` | 8 | The range of the Undying Loyalty passive in blocks. |
| `Subjugator.loyaltyPointGain` | 2 | The amount of loyalty points gained from nearby subordinates every five seconds. |
| `Subjugator.loyaltyRangeMastery` | 16 | The range of the Undying Loyalty passive in blocks when the skill is mastered. |
| `Subjugator.loyaltyPointGainMastery` | 4 | The amount of loyalty points gained from nearby subordinates every five seconds when the skill is mastered. |
| `Subjugator.loyaltyResistance` | 1 | The resistance level granted to subordinates in your vicinity. |
| `Subjugator.loyaltyResistanceMastered` | 2 | The resistance level granted to subordinates in your vicinity when the skill is mastered. |
| `Subjugator.inspirationLevel` | 1 | The level of inspiration granted to subordinates when changing their movement mode. |
| `Subjugator.inspirationDuration` | 30 | The duration of the inspiration effect bestowed onto subordinates when changing their movement mode, in seconds. |
| `Subjugator.inspirationLevelMastery` | 2 | The level of inspiration granted to subordinates when changing their movement mode when the skill is mastered. |
| `Subjugator.inspirationDurationMastery` | 60 | The duration of the inspiration effect bestowed onto subordinates when changing their movement mode when the skill is mastered, in seconds. |
| `Subjugator.maximumTotalLoyaltyPoints` | 50,000 | The maximum gainable loyalty points that will cap out the user's Damage Reduction. |
| `Subjugator.takeoverDistance` | 5 | The distance in blocks that Takeover can be used from. |
| `Subjugator.takeoverDistanceMastery` | 10 | The distance in blocks that Takeover can be used from when the skill is mastered. |
| `Subjugator.takeoverEPMultiplierRequirement` | 1 | The multiplier of EP the player needs to meet in order to convert the target. |
| `Subjugator.takeoverEPMultiplierRequirementMastered` | 2 | The multiplier of EP the player needs to meet in order to convert the target. |
| `Subjugator.takeoverCooldown` | 300 | The cooldown of the Takeover mode in seconds. |
| `Subjugator.takeoverCooldownMastered` | 120 | The cooldown of the Takeover mode in seconds when the skill is mastered. |
| `Subjugator.casualConversationChance` | 0.02 | The chance that a conversation is started every 5 seconds. |
| `Subjugator.allyRadius` | 20 | The radius in block to apply skill effect on Allies. |
| `Subjugator.baseMaxEPForMindControl` | 600,000 | The base max amount of EP that the target can have for Takeover can work |

Set in [`config/tensura/ability/skill/common_config.toml`](../../../tensura-reincarnated/configs/config-tensura-ability-skill-common-config.md).

| Option | Default | Description |
|---|---|---|
| `ThoughtCommunication.telepathyRadius` | 30 | The radius of the Telepathy activation. |

## In-game messages

<details markdown><summary>Show 22 messages</summary>

- &lt;???&gt; Hello...? Where... Where am I?
- &lt;???&gt; You... You can hear me, right? Please, answer me.
- [1]
- &lt;???&gt; ...Apologies. I cannot quite recall anything. What is my purpose?
- Someone has awakened something that was meant to lay dormant.
- [1] Who is this...?
- [2] Um??? Get out of my chat???
- [3] ...
- You are already in a conversation!
- &lt;%s&gt; Death... So that is what it feels like.
- &lt;%s&gt; Perhaps you should adopt a different strategy?
- &lt;%s&gt; Dang, almost had that one.
- &lt;%s&gt; Ouch... That's gotta hurt. Get back up and try again.
- &lt;%s&gt; Wish I could help you, but I'm just your skill.
- &lt;%s&gt; Good job.
- &lt;%s&gt; You are doing excellent.
- &lt;%s&gt; Dang, their guts flew everywhere.
- &lt;%s&gt; Nice!
- &lt;%s&gt; You're strong!
- &lt;%s&gt; Unbreakable Defense is active. You need to turn it off if you want to use your other abilities.
- Your Unbreakable Defense from [Subjugator] is active! Skills and Magic cannot be used except for Battlewills!
- Something here lays dormant.

</details>

## Tags

`tensura:skills/unique_skills`, `tensura:skills/virtue_skills`
