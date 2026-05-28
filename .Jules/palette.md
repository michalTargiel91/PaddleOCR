## 2026-05-28 - Test tipc web components testing limitations
**Learning:** The jest tests in `test_tipc/web` rely heavily on external PaddleJS models which are often missing or throw 404 errors, making e2e testing unreliable in the sandbox environment.
**Action:** When verifying simple HTML accessibility modifications like adding `alt` tags in this repo, prefer utilizing custom mock scripts using `fs.readFileSync` over `pnpm test` to prevent long timeouts and dependency resolution failures.
