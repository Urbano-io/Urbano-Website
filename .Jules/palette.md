## 2026-03-24 - MkDocs Built-In Color Contrast & Links
**Learning:** MkDocs Material built-in utility features (like the `.md-banner` announcement bar and `.md-copyright` footer text) can sometimes trigger accessibility violations such as `color-contrast` and `link-in-text-block`, particularly when combining dark modes/themes with default link colors (like the default blue), or lowering opacity on footer text too much.
**Action:** When working with MkDocs Material, verify the color contrast of custom announcement links and footer text. explicitly override these classes in `extra.css` with `!important` tags if necessary to guarantee WCAG 2.0 AA compliance, and ensure links inside text blocks (like the "Material for MkDocs" footer link) have an explicit `text-decoration: underline`.

## 2026-02-26 - Replacing Raw HTML Buttons with Markdown
**Learning:** `mkdocs-material` allows using markdown syntax inside HTML containers if the `markdown` attribute is present on the container. This enables using theme features like icons and button styles more cleanly than raw HTML.
**Action:** Use `markdown` attribute on wrapper `div`s when needing complex layout but wanting to use markdown components.

## 2025-03-09 - Added prefers-reduced-motion
**Learning:** MkDocs material theme and custom CSS animations (like hover scaling on team photos and color transitions) did not respect the user's OS-level motion preferences, which can cause discomfort for users with vestibular disorders.
**Action:** When adding custom CSS transitions (like `:hover` transforms or filter changes) in documentation sites, always wrap them or provide an override in a `@media (prefers-reduced-motion: reduce)` block to set `transition: none !important;` and `transform: none !important;`.

## 2025-03-09 - Silencing Duplicative Image Announcements in MkDocs
**Learning:** In MkDocs Material feature cards, when an image represents the exact same concept as the adjacent bold heading (e.g., an icon for "Simulation" next to the text "Simulation"), screen readers will announce it twice. Markdown's `attr_list` extension allows overriding the default filename-based alt text by injecting `{ alt="" }` directly after the image definition (e.g., `![alt](url){ alt="" }`).
**Action:** When creating visually rich feature cards with icons and headings in MkDocs, set the image alt text to empty (`alt=""`) via `attr_list` to reduce screen reader noise and improve navigation flow.

## 2025-03-09 - Accessible Visual Focus on Non-Interactive Semantic Elements
**Learning:** When using `tabindex="0"` on non-interactive semantic elements (like `<figure>`) to enable visual CSS hover/focus effects (like grayscale-to-color transitions) for keyboard users, screen readers will announce them as contextless, potentially confusing focus stops.
**Action:** If a static element must be focusable for visual accessibility reasons, always provide semantic context by explicitly adding appropriate ARIA labeling, such as `role="group"` and an `aria-label` describing the content.

## 2025-03-09 - Maintaining Tactile Metaphor with Interactive Transforms
**Learning:** A continuous tactile button interaction (lifting on `:hover`/`:focus-visible`, and pressing down on `:active`) requires coordinating the transforms between states. If `:active` overrides `transform` with just `scale()`, the `translateY` from the hover state is abruptly lost, causing a disjointed visual snap.
**Action:** Always combine transforms on `:active` (e.g., `transform: translateY(0) scale(0.98)`) to smoothly resolve previous transforms and complete the physical interaction metaphor.
