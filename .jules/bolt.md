## 2024-06-03 - NMS Polygon Instantiation Optimization
**Learning:** O(N^2) instantiation of Shapely Polygons and buffer calculations in NMS loops causes significant performance overhead.
**Action:** Pre-compute Polygon objects and their buffered forms in O(N) rather than redundantly instantiating and buffering them inside O(N^2) operations (e.g., in Non-Maximum Suppression loops).
