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
    palette.json|css|png   # canonical theme palette at the theme root
    palettes/              # named gradients, variants, swatches, and per-pass JSON
    references/            # curated stills (often drawn from idea-generators/)
    generated/             # generated boards / geometry / mood
    materials/             # materials mood + MATERIALS.txt
```

## Naming

- Theme folder ids: **kebab-case** (`antichrist`, `beast-mark-imperial`).
- New themes land here as first-class folders; do not bury them under `idea-generators/`.
- When a theme pulls reference stills from the idea library, keep originals in `idea-generators/<source>/` and copy curated picks into `references/`.

## Palette authority and provenance

- `palette.json` and `palette.css` at a theme root are the canonical implementation files. Do not create a second mirror under `palettes/`; reserve that directory for named variants and gradients.
- A few historical `palettes/palette.json` and `palettes/palette.css` mirrors remain byte-identical to their root files for backward compatibility. The root file wins if a legacy mirror is encountered; do not update the mirror or create another one.
- Catalog values are source-provided anchors, not automatically official brand values. Treat them as `extracted` unless a theme `BRIEF.md` explicitly locks them or identifies their official source.
- Use `agent-skills/skills/color-palette-composition` to create or materially revise a theme: it supplies field/partner/spark allocation, Itten/Munsell rationale, mixing, placement, theory summary, and provenance. Use the design directives to translate an approved theme into canonical story names, semantic tokens, and named gradients.

## Relationship to `idea-generators/`

| Folder | Role |
|--------|------|
| `idea-generators/` | Idea-generation resource — organized color-scheme image libraries + extracted palettes |
| `color-themes/` | Separate named themes — expanding catalog with briefs and locked systems |

Shared materials gallery remains at repo-root `# materials/`.

## Privacy

Lives in the private `design-resources` repo. Do not publish assets publicly without clearance.

<!-- Agent: grok · Model: Grok 4.5 · Date: 2026-09-13 · Renamed companion path themes/ → idea-generators/; dropped top-level junction. -->
<!-- Agent: Codex | Model: GPT-5 | Thinking: not exposed | Date: 2026-09-13 | Declared root palette files canonical and documented the master palette-composition bridge. -->
