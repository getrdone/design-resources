# themes/

Organized color-scheme theme libraries for design work.

## Structure

```
themes/
  INDEX.md                 # summary table of all themes + hexes
  README.md                # this file
  <theme-kebab>/
    *.jpg|*.png            # reference / source imagery
    palette.json           # 5â€“6 colors with role guesses
    palette.css            # CSS variables --theme-*
    palette.png            # horizontal swatch strip
    palettes/              # optional per-image palette JSON
    materials/             # materials mood board + MATERIALS.txt recreate brief
  antichrist/
    BRIEF.md
    references/
    palettes/
    generated/             # generated mood / board / geometry assets
    materials/             # materials mood board + MATERIALS.txt recreate brief
    palette.json|css|png
```

## Naming

- Theme folder names use **kebab-case** (`lux-red`, `gilded-dune`, `royal-amethyst`).
- Image stems follow `theme--descriptor--NN.ext` when imported from the source library.

## Palette roles

Typical roles in `palette.json`: `background`, `primary`, `accent`, `highlight`, `muted`, `ink`.
The `antichrist` theme uses named roles: `purple`, `scarlet`, `pearl`, `gold`, `ink`.

## Materials

Each theme includes a `materials/` folder:

- `{theme}--materials-mood--01.png` â€” photoreal flat-lay mood board of surfaces/textures for the palette
- `MATERIALS.txt` â€” concise agent recreate brief (mood, surfaces, light, avoid list, prompt seed)

Use these when regenerating texture style or matching material language across assets.

## Privacy

This pack lives in the private `design-resources` repo. Do not publish assets publicly without clearance.

## Gallery
Browse all materials mood boards in one place: repo-root `materials/` (flat PNGs + per-theme subfolders).

