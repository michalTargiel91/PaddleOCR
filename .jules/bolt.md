## 2024-05-30 - Optimize poly_nms precomputations
**Learning:** In PaddleOCR's `poly_nms`, creating Shapely `Polygon` objects and calling `.buffer()` inside the O(N^2) inner IoU loop causes severe CPU bottlenecks due to redundant geometry instantiation.
**Action:** Always precompute `Polygon` objects, their areas, and buffered geometries in an O(N) pass prior to O(N^2) distance/IoU loops to avoid massive redundant overhead.
