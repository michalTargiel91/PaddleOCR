## 2024-06-27 - Test environment accessibility
**Learning:** Even internal test HTML files (like `test_tipc/web/index.html`) can omit basic semantic elements like `alt` tags on images, propagating bad practices if copied by users as examples.
**Action:** Always ensure test files follow the same accessibility standards as production code, particularly for informative/example image tags.
