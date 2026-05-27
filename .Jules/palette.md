## 2026-05-27 - [Add alt text to images]
**Learning:** `test_tipc/web` tests expect a browser environment and uses puppeteer to test a web app locally using `node_modules/@paddlejs-models/ocr`.
**Action:** Always install the `@paddlejs-models` and `jest-puppeteer` to properly test web-based model invocations, however make sure not to include those lockfiles in PR changes if they are missing upstream.
