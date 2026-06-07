## 2024-05-18 - Pre-compute Polygons in NMS
**Learning:** In object detection post-processing (NMS), repeatedly converting arrays to Shapely Polygons and buffering them in O(N^2) inner loops causes a major performance bottleneck.
**Action:** Pre-compute Polygon instances, their buffered forms, and properties like `.area` in an O(N) loop before the NMS O(N^2) IOU comparisons. Wrap topological operations in `try-except` blocks.
