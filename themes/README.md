# themes/

Idea-generation color-scheme libraries for bots and humans.

Organized source imagery + extracted palettes. For **named, expanding theme systems** (briefs, locked roles, gradients), use `../color-themes/` instead.

## Structure

```
themes/
  INDEX.md                 # summary table of all idea libraries + hexes
  README.md                # this file
  CONVENTIONS.md
  MATERIALS-MOOD-STANDARD.md
  <theme-kebab>/
    *.jpg|*.png            # reference / source imagery
    palette.json           # 5–6 colors with role guesses
    palette.css            # CSS variables --theme-*
    palette.png            # horizontal swatch strip
    palettes/              # optional per-image palette JSON
    materials/             # materials mood board + MATERIALS.txt recreate brief
```

## Naming

- Theme folder names use **kebab-case** (`lux-red`, `gilded-dune`, `royal-amethyst`).
- Image stems follow `theme--descriptor--NN.ext` when imported from the source library.

## Palette roles

Typical roles in `palette.json`: `background`, `primary`, `accent`, `highlight`, `muted`, `ink`.

## Materials

Each library includes a `materials/` folder:

- `{theme}--materials-mood--01.png` — photoreal flat-lay mood board of surfaces/textures for the palette
- `MATERIALS.txt` — concise agent recreate brief (mood, surfaces, light, avoid list, prompt seed)

**Always** also add `{theme}--materials-mood--01.png` to the repo-root `# materials/` gallery when creating or importing a new library.

## Relationship to `color-themes/`

| Folder | Role |
|--------|------|
| `themes/` | Idea-generation resource — color-scheme image libraries |
| `color-themes/` | Named themes catalog that continues to expand |

## Privacy

This pack lives in the private `design-resources` repo. Do not publish assets publicly without clearance.

## Gallery

Browse all materials mood boards in one place: repo-root `# materials/` (sorts first; flat PNGs + per-theme subfolders).

<!-- Agent: grok · Model: Grok 4.5 · Date: 2026-09-13 · Clarified themes/ as idea library; named systems moved to color-themes/. -->
