## 2024-05-18 - Precomputing Polygons in NMS
**Learning:** Pre-buffering polygons before intersection drastically reduces performance. Intersecting unbuffered polygons directly is much faster but may fail on irregular shapes.
**Action:** Pre-compute the base unbuffered polygons and their areas. Intersect the unbuffered polygons in the inner loop, and use a `try...except Exception:` block to fall back to the unoptimized helper function `boundary_iou` if an error occurs.
