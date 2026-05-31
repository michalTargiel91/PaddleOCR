## 2024-05-31 - [Link and Image Accessibility]
**Learning:** Found an accessibility anti-pattern in `overrides/main.html` using "Click here" as link text, which provides no context for screen readers. Also found an image without an `alt` attribute in `test_tipc/web/index.html`.
**Action:** Always use descriptive link text (e.g., "View the latest version.") and include `alt` attributes on images to ensure accessibility for screen reader users.
