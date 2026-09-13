"""Extract theme palettes and stage antichrist no-blue references."""
from __future__ import annotations

import colorsys
import json
import math
import os
import shutil
from collections import Counter
from pathlib import Path

from PIL import Image

THEMES_ROOT = Path(r"F:\__ai-projects\design-resources\themes")
COLOR_THEMES_ROOT = Path(r"F:\__ai-projects\design-resources\color-themes")
SOURCE_ROOT = Path(r"C:\Users\vapor\Pictures\color-scheme-images")
AC_WORK = Path(r"F:\__ai-projects\design-resources\color-themes\antichrist")
AC_REPO = Path(r"F:\__ai-projects\design-resources\color-themes\antichrist")

IMG_EXTS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".bmp"}
SKIP_THEME_PREFIX = "_"

ROLE_ORDER = ["background", "primary", "accent", "highlight", "muted", "ink"]


def list_images(folder: Path):
    return sorted(
        p for p in folder.iterdir()
        if p.is_file() and p.suffix.lower() in IMG_EXTS and not p.name.startswith("_")
    )


def rgb_to_hex(rgb):
    r, g, b = [max(0, min(255, int(round(c)))) for c in rgb]
    return f"#{r:02x}{g:02x}{b:02x}"


def luminance(rgb):
    r, g, b = [c / 255.0 for c in rgb]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def saturation(rgb):
    r, g, b = [c / 255.0 for c in rgb]
    mx, mn = max(r, g, b), min(r, g, b)
    if mx == 0:
        return 0.0
    return (mx - mn) / mx


def hue_deg(rgb):
    r, g, b = [c / 255.0 for c in rgb]
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    return h * 360.0, s, v


def is_blueish(rgb, sat_min=0.18, v_min=0.12):
    h, s, v = hue_deg(rgb)
    if s < sat_min or v < v_min:
        return False
    # blue / cyan / teal-blue range
    return 185 <= h <= 260


def quantize_palette(img: Image.Image, n_colors=6):
    # Downsample for speed
    img = img.convert("RGB")
    w, h = img.size
    max_side = 320
    if max(w, h) > max_side:
        scale = max_side / max(w, h)
        img = img.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.Resampling.BILINEAR)
    q = img.quantize(colors=n_colors, method=Image.Quantize.MEDIANCUT)
    palette = q.getpalette()
    counts = Counter(q.getdata())
    colors = []
    for idx, count in counts.most_common(n_colors):
        r, g, b = palette[idx * 3 : idx * 3 + 3]
        colors.append({"rgb": [r, g, b], "hex": rgb_to_hex((r, g, b)), "count": int(count), "share": 0.0})
    total = sum(c["count"] for c in colors) or 1
    for c in colors:
        c["share"] = round(c["count"] / total, 4)
    return colors


def assign_roles(colors):
    """Guess roles from luminance/saturation/share."""
    items = []
    for c in colors:
        rgb = c["rgb"]
        items.append({
            **c,
            "lum": luminance(rgb),
            "sat": saturation(rgb),
            "hue": hue_deg(rgb)[0],
        })

    used = set()
    roles = {}

    # background: darkest high-share or darkest
    by_dark = sorted(items, key=lambda x: (x["lum"], -x["share"]))
    roles["background"] = by_dark[0]
    used.add(id(by_dark[0]))

    # ink: near-black if available else darkest unused
    remaining = [x for x in items if id(x) not in used]
    ink_candidates = sorted(remaining, key=lambda x: x["lum"])
    roles["ink"] = ink_candidates[0]
    used.add(id(ink_candidates[0]))

    remaining = [x for x in items if id(x) not in used]
    # highlight: lightest
    if remaining:
        hi = max(remaining, key=lambda x: x["lum"])
        roles["highlight"] = hi
        used.add(id(hi))

    remaining = [x for x in items if id(x) not in used]
    # primary: most saturated among mid-share
    if remaining:
        prim = max(remaining, key=lambda x: (x["sat"], x["share"]))
        roles["primary"] = prim
        used.add(id(prim))

    remaining = [x for x in items if id(x) not in used]
    # accent: next most saturated
    if remaining:
        acc = max(remaining, key=lambda x: x["sat"])
        roles["accent"] = acc
        used.add(id(acc))

    remaining = [x for x in items if id(x) not in used]
    # muted: lowest saturation remaining or mid luminance
    if remaining:
        mut = min(remaining, key=lambda x: x["sat"])
        roles["muted"] = mut
        used.add(id(mut))

    # fill any missing role slots with leftover colors
    leftover = [x for x in items if id(x) not in used]
    for role in ROLE_ORDER:
        if role not in roles and leftover:
            roles[role] = leftover.pop(0)

    ordered = []
    for role in ROLE_ORDER:
        if role in roles:
            c = roles[role]
            ordered.append({
                "role": role,
                "hex": c["hex"],
                "rgb": c["rgb"],
                "share": c.get("share", 0),
            })
    # also include any extras as color-N
    i = 1
    for c in leftover:
        ordered.append({
            "role": f"extra-{i}",
            "hex": c["hex"],
            "rgb": c["rgb"],
            "share": c.get("share", 0),
        })
        i += 1
    return ordered


def aggregate_theme_colors(images, n_colors=6):
    # Sample pixels from all images into one mosaic-ish quantize
    tiles = []
    for p in images:
        try:
            im = Image.open(p).convert("RGB")
        except Exception as e:
            print(f"  skip {p.name}: {e}")
            continue
        w, h = im.size
        side = 160
        scale = side / max(w, h)
        im = im.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.Resampling.BILINEAR)
        tiles.append(im)
    if not tiles:
        return []
    # stitch horizontally limited
    max_tiles = min(len(tiles), 24)
    tiles = tiles[:max_tiles]
    tw = sum(t.width for t in tiles)
    th = max(t.height for t in tiles)
    canvas = Image.new("RGB", (tw, th), (0, 0, 0))
    x = 0
    for t in tiles:
        canvas.paste(t, (x, 0))
        x += t.width
    return quantize_palette(canvas, n_colors=n_colors)


def make_swatch(colors, out_path: Path, width=600, height=80):
    n = max(1, len(colors))
    sw = Image.new("RGB", (width, height))
    slice_w = width // n
    for i, c in enumerate(colors):
        rgb = tuple(c["rgb"] if "rgb" in c else c.get("rgb", [128, 128, 128]))
        if isinstance(c.get("rgb"), list):
            rgb = tuple(c["rgb"])
        x0 = i * slice_w
        x1 = width if i == n - 1 else (i + 1) * slice_w
        for x in range(x0, x1):
            for y in range(height):
                sw.putpixel((x, y), rgb)
    # faster fill
    from PIL import ImageDraw
    sw = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(sw)
    for i, c in enumerate(colors):
        rgb = tuple(c["rgb"])
        x0 = i * slice_w
        x1 = width if i == n - 1 else (i + 1) * slice_w
        draw.rectangle([x0, 0, x1, height], fill=rgb)
    sw.save(out_path)


def write_palette_files(theme_dir: Path, theme_name: str, colors_raw, roles):
    palette = {
        "theme": theme_name,
        "colors": roles,
        "raw": [{"hex": c["hex"], "rgb": c["rgb"], "share": c["share"]} for c in colors_raw],
    }
    (theme_dir / "palette.json").write_text(json.dumps(palette, indent=2), encoding="utf-8")

    lines = [f"/* Theme: {theme_name} */", ":root {"]
    for c in roles:
        var = c["role"].replace(" ", "-")
        lines.append(f"  --theme-{var}: {c['hex']};")
        r, g, b = c["rgb"]
        lines.append(f"  --theme-{var}-rgb: {r}, {g}, {b};")
    lines.append("}")
    (theme_dir / "palette.css").write_text("\n".join(lines) + "\n", encoding="utf-8")
    make_swatch(roles, theme_dir / "palette.png")
    return palette


def process_theme(theme_dir: Path):
    name = theme_dir.name
    images = list_images(theme_dir)
    print(f"Theme {name}: {len(images)} images")
    if not images:
        return None
    # per-image optional (limit time: only if <= 20 images)
    palettes_dir = theme_dir / "palettes"
    if len(images) <= 20:
        palettes_dir.mkdir(exist_ok=True)
        for img_path in images:
            try:
                im = Image.open(img_path)
                raw = quantize_palette(im, n_colors=5)
                roles = assign_roles(raw)
                stem = img_path.stem
                data = {"image": img_path.name, "theme": name, "colors": roles}
                (palettes_dir / f"{stem}.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
            except Exception as e:
                print(f"  per-image fail {img_path.name}: {e}")

    raw = aggregate_theme_colors(images, n_colors=6)
    roles = assign_roles(raw)
    return write_palette_files(theme_dir, name, raw, roles)


def image_has_strong_blue(img_path: Path) -> bool:
    try:
        im = Image.open(img_path).convert("RGB")
    except Exception:
        return True  # reject unreadable
    w, h = im.size
    side = 200
    scale = side / max(w, h)
    im = im.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.Resampling.BILINEAR)
    colors = quantize_palette(im, n_colors=8)
    blue_share = 0.0
    blue_count = 0
    for c in colors:
        if is_blueish(c["rgb"]):
            blue_share += c["share"]
            blue_count += 1
    # mean hue check on non-neutral pixels
    pixels = list(im.getdata())
    # sample every Nth
    step = max(1, len(pixels) // 4000)
    hues = []
    for px in pixels[::step]:
        h, s, v = hue_deg(px)
        if s >= 0.2 and v >= 0.15:
            hues.append(h)
    mean_h = sum(hues) / len(hues) if hues else -1
    mean_is_blue = 185 <= mean_h <= 260 and len(hues) > 50

    # strict: reject if blue among top 3 OR blue_share > 0.08 OR mean hue blue
    top3_blue = any(is_blueish(c["rgb"]) for c in colors[:3])
    reject = top3_blue or blue_share > 0.08 or mean_is_blue or blue_count >= 2
    return reject


def candidate_antichrist_sources():
    # Prefer purple/scarlet/pearl/gold themes; still filter blue
    preferred = ["royal-amethyst", "lux-red", "gilded-dune", "autumn-earth", "mono-neutral", "cosmic-aurora", "bright-jewel"]
    paths = []
    for theme in preferred:
        d = SOURCE_ROOT / theme
        if d.is_dir():
            paths.extend(list_images(d))
    return paths


def stage_antichrist():
    refs_work = AC_WORK / "references"
    refs_repo = AC_REPO / "references"
    pal_work = AC_WORK / "palettes"
    refs_work.mkdir(parents=True, exist_ok=True)
    refs_repo.mkdir(parents=True, exist_ok=True)
    pal_work.mkdir(parents=True, exist_ok=True)
    (AC_WORK / "generated").mkdir(parents=True, exist_ok=True)
    (AC_REPO / "generated").mkdir(parents=True, exist_ok=True)
    (AC_REPO / "palettes").mkdir(parents=True, exist_ok=True)

    passed = []
    rejected = []
    for p in candidate_antichrist_sources():
        if image_has_strong_blue(p):
            rejected.append(p.name)
            print(f"  REJECT blue: {p.name}")
            continue
        # also require some affinity: purple OR red/scarlet OR gold/cream presence
        try:
            im = Image.open(p).convert("RGB")
            raw = quantize_palette(im, n_colors=6)
        except Exception:
            rejected.append(p.name)
            continue
        affinity = False
        for c in raw:
            h, s, v = hue_deg(c["rgb"])
            # purple/violet/magenta
            if s >= 0.15 and v >= 0.1 and ((h >= 265 and h <= 330) or (h >= 280 and h <= 320)):
                affinity = True
            # scarlet/red
            if s >= 0.25 and v >= 0.15 and (h <= 20 or h >= 345):
                affinity = True
            # warm gold / amber
            if s >= 0.2 and v >= 0.35 and 35 <= h <= 55:
                affinity = True
            # pearl / cream (high lum low sat warm)
            if luminance(c["rgb"]) > 0.75 and saturation(c["rgb"]) < 0.25:
                affinity = True
        if not affinity:
            rejected.append(p.name)
            print(f"  REJECT no affinity: {p.name}")
            continue
        dest_name = p.name
        shutil.copy2(p, refs_work / dest_name)
        shutil.copy2(p, refs_repo / dest_name)
        passed.append(dest_name)
        print(f"  PASS: {dest_name}")

    # starter palette (named roles) — fixed brief colors, no blue
    starter = {
        "theme": "antichrist",
        "brief": "purple / scarlet / pearl / gold — NO blues/teals/cyan",
        "colors": [
            {"role": "purple", "name": "imperial-amethyst", "hex": "#4a1a6b", "rgb": [74, 26, 107]},
            {"role": "scarlet", "name": "blood-flame", "hex": "#b01030", "rgb": [176, 16, 48]},
            {"role": "pearl", "name": "luminous-pearl", "hex": "#f4efe6", "rgb": [244, 239, 230]},
            {"role": "gold", "name": "warm-metallic-gold", "hex": "#c9a227", "rgb": [201, 162, 39]},
            {"role": "ink", "name": "near-black", "hex": "#12080f", "rgb": [18, 8, 15]},
            {"role": "muted", "name": "dusty-plum", "hex": "#6b4a5e", "rgb": [107, 74, 94]},
        ],
        "reference_count": len(passed),
        "references": passed,
    }
    for target in [AC_WORK / "palette.json", AC_REPO / "palette.json", pal_work / "palette.json"]:
        target.write_text(json.dumps(starter, indent=2), encoding="utf-8")

    css = """/* Theme: antichrist — purple / scarlet / pearl / gold (NO blue) */
:root {
  --theme-purple: #4a1a6b;
  --theme-purple-rgb: 74, 26, 107;
  --theme-scarlet: #b01030;
  --theme-scarlet-rgb: 176, 16, 48;
  --theme-pearl: #f4efe6;
  --theme-pearl-rgb: 244, 239, 230;
  --theme-gold: #c9a227;
  --theme-gold-rgb: 201, 162, 39;
  --theme-ink: #12080f;
  --theme-ink-rgb: 18, 8, 15;
  --theme-muted: #6b4a5e;
  --theme-muted-rgb: 107, 74, 94;
}
"""
    (AC_WORK / "palette.css").write_text(css, encoding="utf-8")
    (AC_REPO / "palette.css").write_text(css, encoding="utf-8")
    make_swatch(starter["colors"], AC_WORK / "palette.png")
    make_swatch(starter["colors"], AC_REPO / "palette.png")

    brief = """# Antichrist theme brief

## Palette constraints
- **purple** — deep imperial / amethyst
- **scarlet** — blood / flame red
- **pearl** — off-white luminous
- **gold** — metallic warm gold
- **ink** (optional) — near-black grounding

## Hard rule
**NO blues / teals / cyan.** Reject any reference or generated asset with strong blue among top colors or mean hue in the blue range.

## Folders
- `references/` — filtered source stills (no blue)
- `palettes/` — palette JSON / CSS / swatches
- `generated/` — reserved for parent-agent generated images

## Naming
Use kebab-case theme ids. Keep this brief updated if the role names change.
"""
    (AC_WORK / "BRIEF.md").write_text(brief, encoding="utf-8")
    (AC_REPO / "BRIEF.md").write_text(brief, encoding="utf-8")

    return passed, rejected


def main():
    summaries = []
    for theme_dir in sorted(THEMES_ROOT.iterdir()):
        if not theme_dir.is_dir():
            continue
        if theme_dir.name.startswith("_") or theme_dir.name == "antichrist":
            continue
        pal = process_theme(theme_dir)
        if pal:
            hexes = [c["hex"] for c in pal["colors"]]
            summaries.append((theme_dir.name, hexes, [c["role"] for c in pal["colors"]]))

    print("\n=== Antichrist staging ===")
    passed, rejected = stage_antichrist()
    print(f"Passed: {len(passed)}; Rejected: {len(rejected)}")

    # INDEX.md
    lines = [
        "# Color themes index",
        "",
        "Extracted palettes from organized `color-scheme-images` folders. Each theme has `palette.json`, `palette.css`, `palette.png`, and optional per-image JSON under `palettes/`.",
        "",
        "| Theme | Palette (hex) |",
        "|-------|---------------|",
    ]
    for name, hexes, roles in summaries:
        lines.append(f"| `{name}` | {' · '.join(hexes)} |")
    # antichrist
    ac_hex = ["#4a1a6b", "#b01030", "#f4efe6", "#c9a227", "#12080f", "#6b4a5e"]
    lines.append(f"| `antichrist` (starter) | {' · '.join(ac_hex)} |")
    lines.append("")
    lines.append("## Notes")
    lines.append("- Theme folder names are kebab-case.")
    lines.append("- `antichrist` is constrained to purple / scarlet / pearl / gold (no blue).")
    lines.append(f"- Antichrist reference images after no-blue filter: **{len(passed)}**.")
    (THEMES_ROOT / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    readme = """# themes/

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
    generated/             # reserved for generated assets
    palette.json|css|png
```

## Naming

- Theme folder names use **kebab-case** (`lux-red`, `gilded-dune`, `royal-amethyst`).
- Image stems follow `theme--descriptor--NN.ext` when imported from the source library.

## Palette roles

Typical roles in `palette.json`: `background`, `primary`, `accent`, `highlight`, `muted`, `ink`.  
The `antichrist` theme uses named roles: `purple`, `scarlet`, `pearl`, `gold`, `ink`, `muted`.

## Privacy

This pack lives in the private `design-resources` repo. Do not publish assets publicly without clearance.
"""
    (THEMES_ROOT / "README.md").write_text(readme, encoding="utf-8")

    print("\n=== SUMMARY ===")
    for name, hexes, roles in summaries:
        print(f"{name}: {hexes}")
    print(f"antichrist refs passed: {len(passed)}")
    print("DONE")


if __name__ == "__main__":
    main()
