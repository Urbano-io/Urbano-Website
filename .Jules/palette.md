## 2024-XX-XX - Empty `alt` tags and Markdown Images
**Learning:** In standard Markdown syntax `![Alt Text](image.jpg)`, the string inside `[]` automatically generates the HTML `alt="Alt Text"` attribute. Adding `{alt=""}` to override it when the image is structurally important (like an organizational logo followed by a screen-reader-only "and") strips the valid alternative text, creating an accessibility regression where the user loses the critical context of the images.
**Action:** Do not forcefully apply empty `alt=""` attributes to Markdown images if they are the primary source of context, and always verify what the surrounding semantic structure implies. Use empty `alt` only for strictly decorative images or when an alternative ARIA label makes the `alt` redundant.

## 2024-10-25 - Tactile Hover Effects for Transparent Logo Cards
**Learning:** Applying standard `box-shadow` on cards (e.g., `<a class="card"><img></a>`) that contain transparent PNG/SVG logos produces an awkward rectangular shadow that ignores the image's contours. The user doesn't see a nice lifted logo, but a rigid bounding box.
**Action:** Use `filter: drop-shadow(...)` instead of `box-shadow` for interactive image link cards. This correctly follows the alpha channel of the inner transparent images, providing a far more organic and pleasant tactile lift effect on `:hover` and `:active`.

## 2024-11-20 - Inline Links and Screen Reader Phrasing
**Learning:** For inline links embedded directly within a continuous sentence (e.g., "You can [download the video here]."), adding a full `aria-label` to the anchor tag (like `aria-label="Download the video (opens in a new tab)"`) breaks the grammatical structure for screen reader users. The screen reader reads the surrounding sentence text ("You can...") and then stops and abruptly reads the entirely separate, redundant label on the anchor tag ("Download the video..."), rather than naturally reading the phrase inline.
**Action:** When adding accessibility context to a link that flows within a continuous sentence block, use a visually hidden span (like `<span class="sr-only"> (opens in a new tab)</span>`) appended inside the anchor tag rather than overriding the whole text with `aria-label`. This preserves the natural sentence flow for screen readers while still providing the necessary context.

## 2024-XX-XX - MkDocs Inline Link Styling Collisions
**Learning:** Adding global hover/focus styles (like `text-decoration: underline`) to `.md-typeset a` in a Material for MkDocs project unintentionally breaks the styling of explicitly designed interactive components like `.md-button`s, `.card`s, and `.headerlink`s.
**Action:** When applying standard UX/A11y hover and focus affordances to inline text links in MkDocs, strictly scope the CSS selector using exclusions (e.g., `.md-typeset a:not(.md-button):not(.card):not(.headerlink)`) to ensure the changes only affect standard prose links without causing UI regressions on buttons or cards.

## 2024-05-18 - Video Focus States in Hidden Overflow Containers
**Learning:** When embedded elements like `<video>` or `<iframe>` are placed inside styled container divs with `border-radius` and `overflow: hidden` (a common pattern for UI cards and teasers), standard outer focus rings (`outline-offset: 2px` or similar) can be completely clipped and hidden by the container's overflow property.
**Action:** Use a negative `outline-offset` (e.g., `outline-offset: -2px`) on elements that fill their overflow-hidden containers to ensure the focus ring draws inwards and remains fully visible to keyboard users.

## 2024-XX-XX - Focus Rings in `overflow: hidden` Containers
**Learning:** When standard focus rings (`outline`) are applied to embedded media elements (like `<video>`) that fill parent containers with `overflow: hidden` (like a `.workflow-teaser`), the focus indicator gets completely clipped out of view, rendering the element seemingly inaccessible to keyboard users despite actually having focus.
**Action:** When applying focus rings (like `:focus-visible`) to elements filling an `overflow: hidden` parent, use a negative `outline-offset` (e.g., `-2px`) to pull the focus indicator inward, ensuring it remains fully visible to keyboard users.

## 2024-XX-XX - Dead Tab Stops on Non-Interactive Figures
**Learning:** Applying `tabindex="0"` to non-interactive `<figure>` elements solely to trigger CSS pseudo-class effects (like `:focus-visible`) creates "dead" tab stops. Screen reader and keyboard users expect focusable elements to be actionable. This is a severe WCAG accessibility violation.
**Action:** Never use `tabindex="0"` just for visual effects. Instead, either wrap the content in a semantic interactive element (like an `<a>` tag with a verified URL) or remove the focusability entirely if the element is purely static.

## 2024-XX-XX - `aria-label` Overriding Internal DOM Tree Semantics
**Learning:** Applying an `aria-label` to an `<a>` tag that wraps a complex semantic structure (like a `<figure>` and `<figcaption>`) completely overrides the internal DOM tree for screen readers. The screen reader will announce the label and ignore the internal semantic blocks (e.g., it will skip announcing that it is an image and a caption, stripping away rich structural context).
**Action:** When adding accessibility context like "(opens in a new tab)" to complex interactive elements like `<figure>` cards, do not place an `aria-label` on the wrapper link. Instead, append a visually hidden span (like `<span class="sr-only"> (opens in a new tab)</span>`) inside the textual component (e.g., the `<figcaption>`) to preserve the internal semantic structure.

## 2024-XX-XX - MkDocs Material Core Accessibility Overrides
**Learning:** MkDocs Material core components (like `.md-search` and `.md-progress`) may occasionally lack comprehensive ARIA attributes for strict `axe-core` accessibility compliance out-of-the-box. Attempting to fix this via client-side JavaScript is brittle and degrades the core experience for users without JS.
**Action:** When a core MkDocs Material component is missing critical accessibility attributes (like `aria-label`s on core dialogs/progress bars), use the `docs/overrides/partials/` templating feature to explicitly inject the missing native HTML/ARIA attributes at build time, rather than relying on JS or custom CSS logic.

## 2024-XX-XX - Distinguishing Inline Links from Surrounding Text
**Learning:** Depending solely on color contrast to distinguish inline text links from surrounding body text is brittle and often fails WCAG `link-in-text-block` requirements, particularly when using custom themes or palettes. Only showing an underline on `:hover` or `:focus` means mobile users or users simply scanning the text cannot easily identify interactive links.
**Action:** Always provide a permanent, non-color visual indicator for inline links embedded in text blocks. Applying a semi-transparent `text-decoration: underline` that becomes fully opaque on hover provides an elegant solution that satisfies accessibility requirements without visually overwhelming dense text paragraphs.
