## 2026-02-26 - Replacing Raw HTML Buttons with Markdown
**Learning:** `mkdocs-material` allows using markdown syntax inside HTML containers if the `markdown` attribute is present on the container. This enables using theme features like icons and button styles more cleanly than raw HTML.
**Action:** Use `markdown` attribute on wrapper `div`s when needing complex layout but wanting to use markdown components.
