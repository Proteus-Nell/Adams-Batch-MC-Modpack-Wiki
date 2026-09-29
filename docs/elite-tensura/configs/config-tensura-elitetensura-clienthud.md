# `config/tensura/EliteTensura/ClientHud.toml`

<small>[Elite Tensura](../index.md) &rsaquo; [Configs](index.md)</small>

## `[MAGICULE_HUD]`

| Option | Default | Range | Description |
|---|---|---|---|
| `corner` | - |  | Anchor point: TOP_LEFT, TOP_CENTER, TOP_RIGHT, MIDDLE_LEFT, MIDDLE_CENTER, MIDDLE_RIGHT, BOTTOM_LEFT, BOTTOM_CENTER or BOTTOM_RIGHT. |
| `offsetX` | - |  | Horizontal offset in pixels from the anchor (signed shift from center for \*_CENTER). |
| `offsetY` | - |  | Vertical offset in pixels from the anchored screen edge (signed shift from center for MIDDLE_\*). |

## `[GEAR_COOLDOWN_HUD]`

| Option | Default | Range | Description |
|---|---|---|---|
| `corner` | - |  | Anchor point: TOP_LEFT, TOP_CENTER, TOP_RIGHT, MIDDLE_LEFT, MIDDLE_CENTER, MIDDLE_RIGHT, BOTTOM_LEFT, BOTTOM_CENTER or BOTTOM_RIGHT. |
| `offsetX` | - |  | Horizontal offset in pixels from the anchor (signed shift from center for \*_CENTER). |
| `offsetY` | - |  | Vertical offset in pixels from the anchored screen edge (signed shift from center for MIDDLE_\*). |

## `[BOSS_CONTRIBUTION_HUD]`

| Option | Default | Range | Description |
|---|---|---|---|
| `corner` | - |  | Anchor point: TOP_LEFT, TOP_CENTER, TOP_RIGHT, MIDDLE_LEFT, MIDDLE_CENTER, MIDDLE_RIGHT, BOTTOM_LEFT, BOTTOM_CENTER or BOTTOM_RIGHT. |
| `offsetX` | - |  | Horizontal offset in pixels from the anchor (signed shift from center for \*_CENTER). |
| `offsetY` | - |  | Vertical offset in pixels from the anchored screen edge (signed shift from center for MIDDLE_\*). |

## `[PARTY_HUD]`

| Option | Default | Range | Description |
|---|---|---|---|
| `corner` | - |  | Anchor point: TOP_LEFT, TOP_CENTER, TOP_RIGHT, MIDDLE_LEFT, MIDDLE_CENTER, MIDDLE_RIGHT, BOTTOM_LEFT, BOTTOM_CENTER or BOTTOM_RIGHT. |
| `offsetX` | - |  | Horizontal offset in pixels from the anchor (signed shift from center for \*_CENTER). |
| `offsetY` | - |  | Vertical offset in pixels from the anchored screen edge (signed shift from center for MIDDLE_\*). |

## Top level

| Option | Default | Range | Description |
|---|---|---|---|
| `hideMinimapWhilePhoneOpen` | true |  | Hide the FTB Chunks minimap while the Ultimate Banking System smartphone overlay is open (no effect without UBS). DEFAULT: true |
| `showPlayerTitles` | true |  | Draw other players' showcase titles above their nameplates. Local only — the server can still disable the feature. DEFAULT: true |
| `showGearCooldowns` | true |  | Show the gear cooldown panel (Aetherforged weapons, Void Edge, Astral Edge). DEFAULT: true |
| `showPartyFrames` | true |  | Show the hunt-party member frames (HP + direction/distance). DEFAULT: true |
| `showWarOverlay` | true |  | Tint enemy-nation claims and pin Nation Cores on the FTB Chunks map and minimap. Local only — the server can still disable the feature. DEFAULT: true |
| `showStarfallMarkers` | true |  | Show the Starfall foreshadow wedge and impact pin on the FTB Chunks map and minimap. Local only — the server can still disable the feature. DEFAULT: true |
