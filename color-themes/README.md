# color-themes/

Named, expanding color-theme catalog for bots and humans.

This is **not** the mood/idea library. Source-scheme inspiration stays in `../idea-generators/`.
Themes here are intentional, named systems (briefs, locked roles, gradients, materials) that grow over time.

## Structure

```
color-themes/
  INDEX.md
  README.md
  _extract_palettes.py     # optional helper; paths point here + ../idea-generators
  <theme-kebab>/
    BRIEF.md               # constraints + role names (when locked)
    palette.json|css|png
    palettes/              # gradients, swatches, per-pass JSON
    references/            # curated stills (often drawn from idea-generators/)
    generated/             # generated boards / geometry / mood
    materials/             # materials mood + MATERIALS.txt
```

## Naming

- Theme folder ids: **kebab-case** (`antichrist`, `beast-mark-imperial`).
- New themes land here as first-class folders; do not bury them under `idea-generators/`.
- When a theme pulls reference stills from the idea library, keep originals in `idea-generators/<source>/` and copy curated picks into `references/`.

## Relationship to `idea-generators/`

| Folder | Role |
|--------|------|
| `idea-generators/` | Idea-generation resource — organized color-scheme image libraries + extracted palettes |
| `color-themes/` | Separate named themes — expanding catalog with briefs and locked systems |

Shared materials gallery remains at repo-root `# materials/`.

## Privacy

Lives in the private `design-resources` repo. Do not publish assets publicly without clearance.

<!-- Agent: grok · Model: Grok 4.5 · Date: 2026-09-13 · Renamed companion path themes/ → idea-generators/; dropped top-level junction. -->
