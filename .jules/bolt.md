## 2024-05-24 - Pre-computing Shapely objects
**Learning:** Pre-computing Shapely objects (`Polygon`, `buffer`, `area`) in O(N) avoids massive redundant overhead in O(N^2) comparison loops like NMS.
**Action:** Always precompute expensive geometry object instantiations and intermediate results (like buffers and area) outside of O(N^2) distance or IOU loops.
