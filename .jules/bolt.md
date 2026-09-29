## 2024-05-21 - Optimize poly_nms by precomputing geometries
**Learning:** Re-creating Shapely polygons and buffering them inside an O(N^2) inner loop is extremely expensive for IOU calculations during Non-Maximum Suppression (NMS). Hoisting object creation to an O(N) precomputation step is critical for performance.
**Action:** Always look for expensive object creations (like `Polygon()`) or calculations (like `.buffer()`) inside nested loops. Precompute and store these objects in a list or dictionary before the loop starts to reduce time complexity.
