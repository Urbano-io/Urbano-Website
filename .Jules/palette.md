## 2026-02-26 - Replacing Raw HTML Buttons with Markdown
**Learning:** `mkdocs-material` allows using markdown syntax inside HTML containers if the `markdown` attribute is present on the container. This enables using theme features like icons and button styles more cleanly than raw HTML.
**Action:** Use `markdown` attribute on wrapper `div`s when needing complex layout but wanting to use markdown components.

## 2025-03-09 - Added prefers-reduced-motion
**Learning:** MkDocs material theme and custom CSS animations (like hover scaling on team photos and color transitions) did not respect the user's OS-level motion preferences, which can cause discomfort for users with vestibular disorders.
**Action:** When adding custom CSS transitions (like `:hover` transforms or filter changes) in documentation sites, always wrap them or provide an override in a `@media (prefers-reduced-motion: reduce)` block to set `transition: none !important;` and `transform: none !important;`.

## 2025-03-09 - Silencing Duplicative Image Announcements in MkDocs
**Learning:** In MkDocs Material feature cards, when an image represents the exact same concept as the adjacent bold heading (e.g., an icon for "Simulation" next to the text "Simulation"), screen readers will announce it twice. Markdown's `attr_list` extension allows overriding the default filename-based alt text by injecting `{ alt="" }` directly after the image definition (e.g., `![alt](url){ alt="" }`).
**Action:** When creating visually rich feature cards with icons and headings in MkDocs, set the image alt text to empty (`alt=""`) via `attr_list` to reduce screen reader noise and improve navigation flow.
