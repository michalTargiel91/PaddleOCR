## 2024-05-30 - Shapely Polygon Operations in NMS
**Learning:** Instantiating Shapely Polygons directly within O(N^2) NMS loops (like in `standard_nms`, `nms`, `soft_nms` inside `locality_aware_nms.py` and `poly_nms` in `poly_nms.py`) creates massive overhead due to C-extensions context switching.
**Action:** Pre-compute the `Polygon` objects (and `.buffer(0)` if needed) in O(N) at the beginning of the function, and reuse them during the O(N^2) comparisons. This drops the NMS runtime significantly.
