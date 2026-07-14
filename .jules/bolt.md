## 2024-05-24 - Optimizing O(N^2) geometry computations
**Learning:** In NMS (Non-Maximum Suppression) functions like `poly_nms`, creating Shapely `Polygon` objects and computing buffers inside the O(N^2) hot loop is a major performance bottleneck, slowing down execution by over 10x.
**Action:** Pre-compute the `Polygon` objects, their buffers, and areas in an O(N) pre-computation phase before the O(N^2) pairwise comparison loop. Fallback gracefully if geometry validation fails.
