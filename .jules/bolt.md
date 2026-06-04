## 2024-05-24 - Pre-computing Shapely geometries inside Python Non-Maximum Suppression loops
**Learning:** When writing Non-Maximum Suppression (NMS) functions in Python using geometric boundaries (like Shapely Polygons), avoiding redundant geometry instantiations and buffering operations in O(N^2) loops provides massive performance boosts (~12x).
**Action:** Pre-compute reusable objects (Polygons, buffered polygons, Base areas) in an O(N) loop before entering nested O(N^2) iteration blocks.
