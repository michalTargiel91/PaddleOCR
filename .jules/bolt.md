## 2025-02-28 - Optimize poly_nms by caching Shapely geometries

**Learning:** Shapely Polygon parsing (`Polygon(points)`) via PaddleOCR's `boundary_iou` inside dense `poly_nms` loops caused severe O(N^2) overhead bottlenecks. Attempting to buffer the polygons degraded performance further.

**Action:** Cache the instantiations (`points2polygon`) before the loops to effectively turn the `poly_nms` object overhead back down to O(N), maintaining geometry states cleanly. Be sure to use standard `except Exception:` blocks exclusively to fallback onto base functions (`boundary_iou`) during irregular topological calculations, instead of importing version-specific `shapely.errors`.
