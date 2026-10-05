## 2024-10-05 - Optimize Shapely Polygon Conversion in NMS
**Learning:** In highly nested, O(N^2) algorithms like non-maximum suppression (NMS) over complex shapes, calling heavy functions like Shapely's `Polygon.buffer()` and `points2polygon()` repeatedly for the same boundaries inside the inner loop creates a massive performance bottleneck.
**Action:** Precompute these heavy geometries and properties (like buffered polygons and area) in a linear pass O(N) beforehand and reuse them within the O(N^2) loop to avoid redundant computation.
