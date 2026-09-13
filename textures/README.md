# textures/

Paid / working **texture and pattern** source pack for graphic design: bitmap textures, fabric, halftones, photocopy grit, overspray, vintage print, vector pattern elements, web/background source material.

Layout armatures (dynamic symmetry grids) are **not** here — they stay in [`../dynamic-symmetry-grids/`](../dynamic-symmetry-grids/).

## Layout

One kebab-case pack per folder. JPEG and TIFF of the same texture sit together (no `JPEG/` vs `BITMAP TIFF/` split). Unzip-in-folder wrappers (`BITMAP-TEXTURES/BITMAP-TEXTURES/`) were flattened.

```
textures/
  analog-halftones/
  analog-shapes/
  aquacolour-bleeds/
  bad-photocopy/                 # photocopy textures + template
  banners/
  bitmap-textures/               # general + fabric bitmaps
  cross-hatch-brushes/
  decorative-line-dividers/
  designers-toolkit/             # crests, engravings, flourishes, frames, nature, vector-patterns
  distressed-borders/
  _docs/                          # workshop / instruction PDFs
  dry-marker/
  fabric-texture-brushes/
  gritty-halftone-brushes/       # includes CS5-era brush
  inside-out-reverse-print/
  marker-brushes/
  overspray-gradients/
  page-decor/
  page-rules/
  paint-splatter-brushes/
  pattern-brushes/
  plastisol/                     # plastisol 1 + vintage-tee 2
  stipple-brushes/
  t-shirt-mockups/mens|womens/
  t-shirt-squares/
  thrift-shop/
  time-machine-textures/
  typography-templates/
  vector-textures/
  vintage-line-frames/
  vintage-workwear-logo-templates/
```

Tool-only subfolders (when needed): `brushes/`, `illustrator/`, `photoshop/`, `displacement-maps/`.

Human-readable instructions and workshop PDFs go in **`_docs/`**, not `docs/`.

## How agents should use this

- Source for generating or matching **surface texture, print grit, fabric, halftone, distressed overlay, repeating pattern, web background**.
- Do **not** publish these assets publicly. Private `design-resources` repo.
- Do **not** copy `__MACOSX`, `.DS_Store`, or `._*` AppleDouble files.

## Combined on purpose

| Combined into | From |
|---------------|------|
| `bad-photocopy` | `BAD_PHOTOCOPY` + `BAD-PHOTOCOPY-TEMPLATE` |
| `bitmap-textures` | `BITMAP-TEXTURES` + `BITMAP-TEXTURES-FABRIC` |
| `plastisol` | `PLASTISOL` + `PLASTISOL-2-VINTAGE-TEE-TEXTURES` |
| `gritty-halftone-brushes` | current + CS5-earlier brush |
| `t-shirt-mockups` | mens + womens mockup templates |
| `time-machine-textures` | T-shirt pack + Vector Lab copy |

Designer-toolkit **sample** photocopy/bitmap files were dropped (duplicates of the full packs). Unique EPS sets remain.

## Privacy

Paid The Vector Lab / Affinity design packs. Repo must stay **private**.

<!-- Agent: grok · Model: Grok 4.5 · Date: 2026-09-13 · Created textures pack; merged unique T-shirt/vector-lab sources; excluded Mac junk and zip originals. -->
<!-- Agent: grok · Model: Grok 4.5 · Date: 2026-09-13 · Deleted duplicate HD copies and original-download zips; this folder is canonical. -->
<!-- Agent: grok · Model: Grok 4.5 · Date: 2026-09-13 · Flattened unzip wrappers and JPEG/TIFF splits; kebab-case packs; combined overlaps. -->
<!-- Agent: grok · Model: Grok 4.5 · Date: 2026-09-13 · Instruction folder is _docs/ (user rename verified). -->
