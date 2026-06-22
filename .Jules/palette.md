## 2024-06-22 - Missing `alt` Text on Test HTML Images
**Learning:** Even internal test HTML files (like `test_tipc/web/index.html`) used to showcase OCR functionalities completely lacked fundamental semantic accessibility tags like `alt` attributes on main structural images, which acts as a poor example when others refer to test suites.
**Action:** Always verify test harness HTML environments for baseline web accessibility standards like missing `alt` tags and ARIA labels.
