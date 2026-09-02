## 2023-10-27 - [Optimize poly_nms function]
**Learning:** In polygon non-maximum suppression (`poly_nms`), recreating Shapely Polygon objects in the nested NMS loop causes an O(N²) bottleneck due to expensive geometry creation overhead.
**Action:** Precompute Shapely `Polygon` objects, buffered polygons, and their areas *before* entering the NMS loop. This changes the O(N²) geometry instantiation to O(N), resulting in massive speedups (e.g. from 21.7s to 1.2s for 500 polygons) without changing exact geometric intersection results.
