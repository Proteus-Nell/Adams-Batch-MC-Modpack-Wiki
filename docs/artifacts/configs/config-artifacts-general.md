# `config/artifacts/general.toml`

<small>[Artifacts](../index.md) &rsaquo; [Configs](index.md)</small>

## Top level

| Option | Default | Range | Description |
|---|---|---|---|
| `artifactRarity` | 1 |  | Affects how common artifacts are in chests<br>Values above 1 will make artifacts rarer, values between 0 and 1 will make artifacts more common<br>Doubling this value will make artifacts approximately twice as hard to find, and vice versa<br>To prevent artifacts from appearing as chest loot, set this to 10000. |
| `entityEquipmentChance` | 0.0015 |  | The chance that a skeleton, zombie or piglin spawns with an artifact equipped |
| `archaeologyChance` | 0.0625 |  | The chance that an artifact generates in suspicious sand or gravel |

## `[campsite]`

| Option | Default | Range | Description |
|---|---|---|---|
| `campsiteCount` | 40 |  | How many times a campsite will attempt to generate per chunk<br>Set this to 0 to prevent campsites from generating |
| `minY` | -60 |  | The minimum height campsites can spawn at |
| `maxY` | 40 |  | The maximum height campsites can spawn at |
| `mimicChance` | 0.3 |  | The probability that a campsite has a mimic instead of a chest |
| `useModdedChests` | true |  | Whether to use wooden chests from other mods when generating campsites |
| `allowLightSources` | true |  | Whether campsites can contain blocks that emit light |
| `minimalistCampsites` | false |  | Replaces campsites with a single chest/mimic |

## `[slots]`

| Option | Default | Range | Description |
|---|---|---|---|
| `enableAccessoriesCompat` | true |  | Whether Artifacts should add slots to the Accessories menu,<br>and allow artifacts to be equipped in them |
| `enableCuriosCompat` | true |  | Whether Artifacts should add slots to the Curios menu,<br>and allow artifacts to be equipped in them |
| `enableTrinketsCompat` | true |  | Whether Artifacts should add slots to the Trinket menu,<br>and allow artifacts to be equipped in them |
| `addFaceSlot` | false |  | When enabled, adds a separate slot for the Snorkel and Night Vision Goggles<br>(Trinkets only, currently not compatible with Curios or Accessories) |
| `removeSlotRestrictions` | false |  | When enabled, allows any artifact to be equipped in any slot<br>(Requires Curios or Trinkets, currently not compatible with Accessories) |
