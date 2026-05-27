## 2024-05-27 - Bottleneck in ppocr.utils.poly_nms
**Learning:** Re-creating Shapely `Polygon` objects inside nested NMS loops and computing exact intersections for completely disjoint polygons is a major performance bottleneck (O(N^2) complexity with expensive constant factors).
**Action:** Precompute Shapely `Polygon` objects before the loop, precompute their bounding boxes, and use AABB (Axis-Aligned Bounding Box) checks to fast-reject non-overlapping polygons before calculating exact geometric IOUs.
