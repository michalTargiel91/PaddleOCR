## 2025-03-01 - Optimize Shapely intersection in poly_nms
**Learning:** Instantiating Shapely Polygons and buffering them (`buffer(0.0001)`) repeatedly in inner O(N^2) loops (like NMS) is extremely slow and a major performance bottleneck for dense OCR text bounding boxes.
**Action:** When performing geometry intensive intersection calculations, precompute the raw Shapely Polygons outside the loop, use unbuffered `.intersection()` directly in the inner loop, and implement a `try...except` fallback for irregular topological errors instead of proactively buffering polygons.
## 2025-03-01 - Handle None polygons in poly_nms
**Learning:** During geometry precomputation, `points2polygon` can return `None` or raise exceptions for invalid input bounding boxes. Attempting to directly access `poly.area` without a `None` check causes an `AttributeError`.
**Action:** Always include a `try...except` block and an explicit `if poly is not None:` check when instantiating raw Shapely polygons to gracefully fallback to `(None, 0.0)`, and ensure the inner NMS loop skips intersection if either polygon is `None`.
