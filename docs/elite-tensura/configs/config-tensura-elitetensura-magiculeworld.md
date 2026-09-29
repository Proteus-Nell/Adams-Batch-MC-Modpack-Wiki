# `config/tensura/EliteTensura/MagiculeWorld.toml`

<small>[Elite Tensura](../index.md) &rsaquo; [Configs](index.md)</small>

## `[ORE_CONVERSION]`

| Option | Default | Range | Description |
|---|---|---|---|
| `minMagiculeForConversion` | 50 |  | Chunk magicule at/below which conversion uses the minimum chance. DEFAULT: 50 |
| `maxConversionMagicule` | 500 |  | Chunk magicule at/above which conversion uses the maximum chance. DEFAULT: 500 |
| `minConversionChance` | 0.001 |  | Conversion chance per sampled ore block at minimum magicule. DEFAULT: 0.001 |
| `maxConversionChance` | 0.05 |  | Conversion chance per sampled ore block at maximum magicule. DEFAULT: 0.05 |
| `conversionMagiculeCost` | 600 |  | Chunk magicule subtracted per successful conversion. DEFAULT: 600 |
| `chunkScanInterval` | 100 |  | Server ticks between conversion scan cycles. DEFAULT: 100 |
| `samplesPerChunk` | 16 |  | Random block positions sampled per scanned chunk (never an exhaustive scan). DEFAULT: 16 |
| `chunksPerCycle` | 32 |  | Loaded chunks processed per scan cycle, per level (round-robin). DEFAULT: 32 |

## `[CRYSTAL_GROWTH]`

| Option | Default | Range | Description |
|---|---|---|---|
| `motherRockGrowthChance` | 0.05 |  | Per-random-tick chance a Mother Rock attempts to sprout a new bud. DEFAULT: 0.05 |
| `growthCostSmallBud` | 300 |  | Chunk magicule required (and consumed) to sprout a Small Bud. DEFAULT: 300 |
| `growthCostMediumBud` | 575 |  | Chunk magicule required (and consumed) to advance Small -&gt; Medium Bud. DEFAULT: 575 |
| `growthCostLargeBud` | 850 |  | Chunk magicule required (and consumed) to advance Medium -&gt; Large Bud. DEFAULT: 850 |
| `growthCostCluster` | 1,000 |  | Chunk magicule required (and consumed) to advance Large Bud -&gt; Cluster. DEFAULT: 1000 |

## `[ENTITY_INFLUENCE]`

| Option | Default | Range | Description |
|---|---|---|---|
| `entityMagiculeInfluenceInterval` | 40 |  | Server ticks between entity-influence cycles. DEFAULT: 40 |
| `entityMagiculeInfluenceMinMagicule` | 50,000 |  | Minimum entity magicule to contribute to its chunk. DEFAULT: 50000 |
| `entityMagiculeInfluenceFactor` | 2 |  | Entity magicule is multiplied by this to get its contribution. DEFAULT: 2.0 |
| `entityMagiculeInfluenceEntityCap` | 1,000 |  | Maximum contribution from a single entity. DEFAULT: 1000 |
| `entityMagiculeInfluenceChunkCap` | 5,000 |  | Maximum target bonus / max-magicule a chunk can reach from influence. DEFAULT: 5000 |
| `entityMagiculeInfluenceApproachRate` | 0.2 |  | Fraction of the gap to the contribution closed each cycle. DEFAULT: 0.2 |
| `entityMagiculeInfluenceRegenRatio` | 0.02 |  | Share of contribution added to the chunk's regen rate. DEFAULT: 0.02 |
| `entityMagiculeInfluenceDiffusionRate` | 0.04 |  | Fraction of a chunk's current bonus diffused to each adjacent loaded chunk per cycle. DEFAULT: 0.04 |
| `entityMagiculeInfluenceScanRadiusChunks` | 2 |  | Chunk radius around each player scanned for contributing entities. DEFAULT: 2 |
| `entityMagiculeInfluenceDisableInSpawn` | true |  | Freeze area magicule inside the LocationManager SpawnProtection region (overworld only): entities there raise no chunk magicule, no bonus diffuses in, and any existing influence bonus is reset to the Tensura base. DEFAULT: true |

## `[MOB_REPLACEMENT]`

| Option | Default | Range | Description |
|---|---|---|---|
| `mobReplacementEnabled` | true |  | Enable high-magicule natural-spawn replacement. DEFAULT: true |
| `mobReplacementMinMagicule` | 1,000 |  | Minimum chunk magicule for replacement to be considered. DEFAULT: 1000 |
| `mobReplacementChance` | 0.15 |  | Chance a qualifying natural spawn is replaced by its whitelisted upgrade. DEFAULT: 0.15 |
