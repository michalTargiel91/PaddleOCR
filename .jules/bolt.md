## 2025-05-16 - Shapely Polygon Instantiation Bottleneck in NMS
**Learning:** Instantiating `shapely.geometry.Polygon` inside an O(N^2) NMS loop is a severe performance bottleneck. It causes redundant object creation and area calculations.
**Action:** Precompute Shapely polygons, areas, and buffered fallback polygons in an O(N) pre-pass before the N^2 loop, strictly catching `shapely.errors.TopologicalError` and falling back to the original computation for anomalies to ensure exact backwards compatibility.
