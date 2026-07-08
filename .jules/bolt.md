## 2024-07-08 - O(N^2) Shapely Geometry Object Creation Bottleneck in NMS
**Learning:** In NMS calculations for text detection (like `poly_nms`), re-creating `Shapely` Polygon geometries and re-running expensive `.buffer()` operations inside the O(N^2) comparison loop causes massive performance degradation.
**Action:** Pre-compute the Polygon objects, their unbuffered areas, and buffered geometries in an initial O(N) pass and cache them. Inline the intersection checks using these cached objects, and always keep a fallback to the original robust logic for degenerate geometry edge cases.
