## 2024-05-30 - Localized Verification for HTML Changes
**Learning:** Jest tests in `test_tipc/web` often fail due to missing large external dependencies, such as PaddleJS models.
**Action:** When making small HTML/UX changes in these areas, write a small custom Node.js script using `fs` to parse and verify the HTML changes locally instead of relying entirely on the unreliable full Jest test suite.
