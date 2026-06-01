## 2026-06-01 - Added alt attribute to OCR test image
**Learning:** Found a missing alt attribute on the primary OCR test image in the web app. Screen readers and users who disable images would have no context. Adding an `alt` tag ensures accessibility for this critical test component.
**Action:** Always verify that images in test interfaces and documentation have descriptive `alt` attributes to maintain a11y standards.
