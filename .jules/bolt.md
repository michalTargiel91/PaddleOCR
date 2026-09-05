## 2024-09-05 - Optimize Shapely Polygon Intersections in poly_nms
**Learning:** In highly repetitive geometric operations (like O(N^2) IoU calculation loops in NMS), recreating `shapely.geometry.Polygon` objects and calling `.buffer()` in every inner loop iteration creates a massive bottleneck due to C-extension overhead and object creation.
**Action:** Pre-compute the `Polygon` instantiation and constant buffer operations in an O(N) loop before entering the O(N^2) comparison loop to drastically reduce execution time (e.g., a 6.7x speedup in this case).
