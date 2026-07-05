## 2024-05-18 - [Optimize poly_nms with Shapely pre-computation]
**Learning:** Using Shapely geometries inside O(N^2) loops (like NMS with bounding boxes) without pre-computation leads to massive redundancy, calling things like `Polygon(...)` and `.buffer()` repeatedly for the same shape.
**Action:** Always pre-compute heavy geometric objects (Polygons, buffered polygons) in O(N) before entering O(N^2) matching loops, wrapping the pre-computation in a try...except block to handle degenerate polygons safely.
