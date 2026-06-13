## 2024-06-11 - Pre-computing Shapely Polygons in PaddleOCR NMS

**Learning:** In PaddleOCR's `poly_nms`, the non-maximum suppression loop iterates in an O(N^2) fashion, comparing each polygon to all others. The unoptimized implementation called `boundary_iou`, which in turn invoked `points2polygon` to instantiate new Shapely `Polygon` objects inside the nested loop. This redundant instantiation was a massive bottleneck.
**Action:** When calculating IoUs or geometric intersections over collections, pre-compute the Shapeley objects (and their buffered/area properties) in a single O(N) pass, then use these cached objects in the O(N^2) comparison loop to dramatically reduce overhead.
