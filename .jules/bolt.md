## 2024-05-24 - Precomputing Shapely Polygons in NMS
**Learning:** In NMS algorithms dealing with polygons, constantly converting points to `shapely.geometry.Polygon` objects inside nested loops creates a massive overhead.
**Action:** Precompute Shapely polygons before entering the NMS loop. This reduces redundant instantiations, cutting execution time significantly (e.g., from ~6.2s to ~5.0s for 200 polygons).
