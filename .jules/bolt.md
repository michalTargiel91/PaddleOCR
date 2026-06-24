## 2024-06-24 - Pre-compute Shapely objects in poly_nms
**Learning:** In geometric operations like NMS, converting points to Shapely `Polygon` objects repeatedly in O(N^2) inner loops causes massive overhead.
**Action:** Always pre-compute and store Shapely `Polygon` objects, their `area`, and their `buffer(0.0001)` in O(N) before entering O(N^2) loops (like NMS). Use inline intersection/union calculations instead of calling helper functions to avoid redundant object recreation and overhead.
