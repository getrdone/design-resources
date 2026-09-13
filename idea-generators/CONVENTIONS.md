# Idea-generator library conventions

- Top-level materials gallery folder is named `# materials` (sorts first).
- When adding any new **idea library** under `idea-generators/` (download import or generated), always place `{library}--materials-mood--01.png` in `# materials/` and keep `# materials/{library}/MATERIALS.txt`.
- When adding a **named theme** (locked brief / expanding catalog), put it under `../color-themes/<theme-kebab>/` and still mirror its materials mood into `# materials/`.
- Do not mix the two: `idea-generators/` = idea libraries; `color-themes/` = named systems.

<!-- Agent: grok · Model: Grok 4.5 · Date: 2026-09-13 · Renamed themes/ → idea-generators/. -->
