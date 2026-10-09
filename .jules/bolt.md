## 2024-10-09 - Precomputing Shapely Objects inside O(N^2) NMS loop
**Learning:** `poly_nms` calls `boundary_iou`, which recreates `Polygon` objects and calls `.buffer(0.0001)` on them for every O(N^2) pairing. The Shapely geometry construction and buffering are exceptionally expensive overheads in Python.
**Action:** When implementing NMS algorithms over complex geometric objects like polygons, precompute the geometry objects, their areas, and any static buffer transformations ahead of the pairwise nested loop to vastly improve execution speed.
