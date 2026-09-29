# `config/tensura/client/hud_config.toml`

<small>[Tensura: Reincarnated](../index.md) &rsaquo; [Configs](index.md)</small>

## Top level

| Option | Default | Range | Description |
|---|---|---|---|
| `tensuraHud` | true |  | Controls if Tensura HUD elements should be rendered at all or not |
| `vanillaHud` | false |  | Controls if Vanilla HUD elements should be rendered at all or not |

## `[status]`

| Option | Default | Range | Description |
|---|---|---|---|
| `positionX` | 0 |  | Ignored if defaultRendering is true |
| `positionY` | 0 |  |  |
| `scale` | 1 |  | The multiplier for the element size<br>Scales all other elements that have defaultRendering set to true except Abilities and Analysis0.0 ~ Any |
| `side` | 0 |  | Setting to 1 will make the element to render from left to right and vice versa if 2<br>Setting to 0 will allow the renderer to decide dynamically<br>Will also move other elements that have defaultRendering set to true<br><br>0 ~ 2 |
| `render` | true |  | Separate check if this specific element should render<br>Ignored if tensuraHud = false |
| `defaultRendering` | true |  | If true, dynamically adjusts the element |

## `[decorations.air]`

Properties notes:  
positionX = Horizontal position; Ignored if defaultRendering is true  
positionY = Vertical position; Ignored if defaultRendering is true  
side = 0 means dynamic rendering, 1 makes it render from left to right, 2 mirrors it; Ignored if defaultRendering is true  
0 ~ 2  
scale = Size multiplier for the element, such as 0.8 or 1.2; Uses Status's scale if defaultRendering is true  
0.05 ~ 5  
render = Separate check if the element should render; Ignored if tensuraHud is false  
defaultRendering = Dynamically adjust everything

| Option | Default | Range | Description |
|---|---|---|---|
| `positionX` | 0 |  |  |
| `positionY` | 0 |  |  |
| `side` | 0 |  |  |
| `scale` | 1 |  |  |
| `render` | true |  |  |
| `defaultRendering` | true |  |  |

## `[decorations.food]`

| Option | Default | Range | Description |
|---|---|---|---|
| `positionX` | 0 |  |  |
| `positionY` | 0 |  |  |
| `side` | 0 |  |  |
| `scale` | 1 |  |  |
| `render` | true |  |  |
| `defaultRendering` | true |  |  |

## `[decorations.armor]`

| Option | Default | Range | Description |
|---|---|---|---|
| `positionX` | 0 |  |  |
| `positionY` | 0 |  |  |
| `side` | 0 |  |  |
| `scale` | 1 |  |  |
| `render` | true |  |  |
| `defaultRendering` | true |  |  |

## `[decorations.barrier]`

| Option | Default | Range | Description |
|---|---|---|---|
| `positionX` | 0 |  |  |
| `positionY` | 0 |  |  |
| `side` | 0 |  |  |
| `scale` | 1 |  |  |
| `render` | true |  |  |
| `defaultRendering` | true |  |  |

## `[decorations.mountHp]`

| Option | Default | Range | Description |
|---|---|---|---|
| `positionX` | 0 |  |  |
| `positionY` | 0 |  |  |
| `side` | 0 |  |  |
| `scale` | 1 |  |  |
| `render` | true |  |  |
| `defaultRendering` | true |  |  |

## `[decorations.mountSpiritualHp]`

| Option | Default | Range | Description |
|---|---|---|---|
| `positionX` | 0 |  |  |
| `positionY` | 0 |  |  |
| `side` | 0 |  |  |
| `scale` | 1 |  |  |
| `render` | true |  |  |
| `defaultRendering` | true |  |  |

## `[statusBars]`

| Option | Default | Range | Description |
|---|---|---|---|
| `positionX` | 0 |  | Ignored if defaultRendering is true |
| `positionY` | 0 |  |  |
| `scale` | 1 |  | The multiplier for the element size<br>Uses Status's scale if defaultRendering is true<br>0.05 ~ 5 |
| `side` | 0 |  | Setting to 1 will force the element to render from left to right and vice versa if 2<br>Uses Status's side if defaultRendering is true<br>0 ~ 2 |
| `render` | true |  | Separate check if this specific element should render<br>Ignored if tensuraHud = false |
| `defaultRendering` | true |  | If true, dynamically adjusts the element |

## `[abilities]`

| Option | Default | Range | Description |
|---|---|---|---|
| `positionX` | 0 |  | Ignored if defaultRendering is true |
| `positionY` | 0 |  |  |
| `scale` | 1 |  | The multiplier for the element size<br>0.05 ~ 5 |
| `side` | 0 |  | Setting to 1 will make the element to render from left to right and vice versa if 2<br>Setting to 0 will allow the renderer to decide dynamically<br>0 ~ 2 |
| `render` | true |  | Separate check if this specific element should render<br>Ignored if tensuraHud = false |
| `defaultRendering` | true |  | If true, dynamically adjusts the element |

## `[analysis]`

| Option | Default | Range | Description |
|---|---|---|---|
| `positionX` | 0 |  | Ignored if defaultRendering is true |
| `positionY` | 0 |  |  |
| `scale` | 1 |  | The multiplier for the element size<br>0.05 ~ 5 |
| `opacity` | 0.8 |  | How opaque the element should be when rendering<br>0.0 ~ 1.0 |
| `side` | 2 |  | Setting to 1 will make the element to render from left to right and vice versa if 2<br>Setting to 0 will allow the renderer to decide dynamically<br>0 ~ 2 |
| `useHearts` | false |  | If true, will render target's hearts instead of HP (1 heart = 2 HP) |
| `render` | true |  | Separate check if this specific element should render<br>Ignored if tensuraHud = false |
| `defaultRendering` | true |  | If true, dynamically adjusts the element |
