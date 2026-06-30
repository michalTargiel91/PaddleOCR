## 2025-05-18 - Pre-computing Geometry Objects for O(N^2) Loops
**Learning:** When performing NMS operations on polygons (e.g., Shapely Polygon), redundantly creating Polygon objects and their buffered forms inside the nested NMS loops causes massive O(N^2) overhead.
**Action:** Always pre-compute Polygon objects and their `.buffer()` forms in O(N) before the NMS loop. Wrap the pre-computation in a `try...except` block, storing `None` for invalid degenerate polygons to safely skip them in downstream logic. Use the unbuffered `.area` plus buffered intersections to match original area logics.
