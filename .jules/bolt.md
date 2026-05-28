## 2024-05-28 - Shapely Polygon NMS Performance
**Learning:** O(N^2) Shapely Polygon creation and buffering in `poly_nms` is a huge performance bottleneck.
**Action:** Pre-compute the Shapely polygon objects and their buffered forms before NMS loop, instead of re-instantiating and re-buffering them repeatedly for each pairwise IoU check.
