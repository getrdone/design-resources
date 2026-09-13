# design-resources (private)

**GitHub source of truth:** https://github.com/getrdone/design-resources (**private**)  
**Local continuously synced clone:** `F:\__ai-projects\design-resources\`  

Machine map: `F:\__ai-projects\SOURCES-OF-TRUTH.md`  
Sync: `F:\__ai-projects\_agent-control\bin\sync-canonical-repos.sh`

Paid / proprietary design packs. Do **not** make this repo public.

## Packs

| Folder | What | Notes |
|--------|------|--------|
| `dynamic-symmetry-grids/` | Dynamic symmetry PNG armatures + gauges + method PDFs | **black-line PNGs** are working files |

### Dynamic symmetry — quick agent rule

1. Soft standard for layout, spacing, hierarchy, thumbs, heroes.  
2. **Skim glossary:** `dynamic-symmetry-grids/GLOSSARY.md` → **symlink** into **agent-skills** (one file, one history).  
3. Full method: `F:\__ai-projects\agent-skills\skills\curiosity-driven-scripture-journey\references\dynamic-symmetry.md`  
4. Prefer `US grid sizes/` or `A4 grid sizes/` → `BLACK PNG HORIZONTAL` or `VERTICAL`.  
5. **Never** put nude/sexually explicit study images from the PDFs into any deliverable.

### How content is owned

| Content | Repo history |
|---------|----------------|
| PNG grids, gauges, PDFs | **this repo** (`design-resources`) |
| Glossary text + skill method docs | **agent-skills** (GLOSSARY.md is a symlink) |

### Importing new files from H: (purchase archive)

Only when updating the pack; then **commit + push** so GitHub stays SOT:

```bash
rsync -a --exclude '.DS_Store' --exclude 'Thumbs.db' \
  "/mnt/h/-- Four44/-- design helps/Dynamic Symmetry Grids/" \
  "/mnt/f/__ai-projects/design-resources/dynamic-symmetry-grids/"
cd /mnt/f/__ai-projects/design-resources && git add -A && git commit && git push
```

## Privacy

- Repo must stay **private**.  
- Do not attach these grids to public sites or public repos.

## Color packs

| Folder | Role |
|--------|------|
| `idea-generators/` | Idea-generation color-scheme libraries (source: `C:\Users\vapor\Pictures\color-scheme-images`) |
| `color-themes/` | Named, expanding theme systems (briefs, locked roles, gradients) |

See `idea-generators/INDEX.md` and `color-themes/INDEX.md` for hex palettes.

<!-- Agent: grok · Model: Grok 4.5 · Date: 2026-09-13 · Renamed themes/ → idea-generators/; removed top-level color-themes junction. -->
