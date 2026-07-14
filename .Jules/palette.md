## 2025-07-14 - Improve Outdated Version Link Accessibility
**Learning:** The outdated version warning banner (`overrides/main.html`) used a generic "Click here" link text, which is an accessibility anti-pattern as it lacks context for screen reader users when read out of context.
**Action:** Replaced the generic link text with a descriptive call-to-action ("View the latest version.") and added an `aria-label` to provide clear, out-of-context meaning for screen readers. Always ensure link text is descriptive and meaningful on its own.
