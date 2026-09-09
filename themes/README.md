# themes/

Organized color-scheme theme libraries for design work.

## Structure

```
themes/
  INDEX.md                 # summary table of all themes + hexes
  README.md                # this file
  <theme-kebab>/
    *.jpg|*.png            # reference / source imagery
    palette.json           # 5–6 colors with role guesses
    palette.css            # CSS variables --theme-*
    palette.png            # horizontal swatch strip
    palettes/              # optional per-image palette JSON
  antichrist/
    BRIEF.md
    references/
    palettes/
    generated/             # generated mood / board / geometry assets
    palette.json|css|png
```

## Naming

- Theme folder names use **kebab-case** (`lux-red`, `gilded-dune`, `royal-amethyst`).
- Image stems follow `theme--descriptor--NN.ext` when imported from the source library.

## Palette roles

Typical roles in `palette.json`: `background`, `primary`, `accent`, `highlight`, `muted`, `ink`.
The `antichrist` theme uses named roles: `purple`, `scarlet`, `pearl`, `gold`, `ink`.

## Privacy

This pack lives in the private `design-resources` repo. Do not publish assets publicly without clearance.
