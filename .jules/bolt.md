## 2024-05-24 - Pre-compute Shapely Polygons in NMS

**Learning:** Shapely Polygon instantiation `Polygon(coords)` and buffering `poly.buffer(0)` are relatively expensive operations. Placing them inside O(N^2) inner loops (like Non-Maximum Suppression) creates a massive performance bottleneck. The original `standard_nms` took ~18.7s for 500 boxes, but pre-computing the polygons dropped it to ~4.7s.

**Action:** When dealing with computational geometry (especially Shapely) and distance/intersection calculations over arrays, always analyze the loop structure to ensure object creation and invariant transforms (like `.buffer(0)`) are hoisted into an O(N) pre-computation pass before the O(N^2) comparison loops.
