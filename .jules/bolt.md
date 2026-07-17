## 2024-05-08 - Optimize poly_nms $O(N^2)$ calculations
**Learning:** In highly nested NMS loops for polygon comparisons, repeatedly building Shapely polygons and calculating buffered geometry in the inner $O(N^2)$ loop is extremely slow.
**Action:** Precompute polygons, their buffers, and areas in an $O(N)$ pass. In the inner $O(N^2)$ loop, use `buf_A.intersection(buf_B)` directly instead of recalculating, wrapping it in a try/except for `shapely.errors.TopologicalError` to ensure graceful fallback to original logic on invalid geometries.
