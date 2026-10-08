## 2025-02-18 - Precomputing Shapely Objects in Polygon NMS
**Learning:** In highly nested loops like Object Detection NMS, calling geometry instantiation (`points2polygon`) and morphological operations (`polygon.buffer`) is a massive O(N^2) performance bottleneck.
**Action:** Precompute these expensive immutable spatial geometries (and properties like area) in an O(N) loop before NMS processing, enabling rapid O(N^2) inline intersection/union comparisons inside the critical path loop while properly handling bounding box failures with try/except wrappers.
