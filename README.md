# design-resources (private)

**Machine path (all local agents):**  
`F:\__ai-projects\design-resources\`  
`/mnt/f/__ai-projects/design-resources/`

Paid / proprietary design packs live here so **every agent** can open the same files.  
Do **not** publish this tree publicly.

## Packs

| Folder | What | Notes |
|--------|------|--------|
| `dynamic-symmetry-grids/` | Tavis Leaf Glover dynamic symmetry PNG armatures + method PDFs | ~508MB; **black-line grids are the working files** |

### Dynamic symmetry — quick agent rule

1. Soft standard for layout, spacing, hierarchy, thumbs, heroes.  
2. Full method: `agent-skills/skills/curiosity-driven-scripture-journey/references/dynamic-symmetry.md`  
3. Prefer `US grid sizes/` or `A4 grid sizes/` → `BLACK PNG HORIZONTAL` or `VERTICAL`.  
4. **Never** put nude/sexually explicit study images from the PDFs into any deliverable. Humans: prefer only *The Simplicity and Beauty of Dynamic Symmetry* PDF.

### Sync from original H: pack

```bash
rsync -a --exclude '.DS_Store' --exclude 'Thumbs.db' \
  "/mnt/h/-- Four44/-- design helps/Dynamic Symmetry Grids/" \
  "/mnt/f/__ai-projects/design-resources/dynamic-symmetry-grids/"
```

## Privacy

- GitHub remote (if configured) must stay **private**.  
- Do not attach these grids to public sites or public repos.  
