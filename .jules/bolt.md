## 2025-02-23 - Shapely O(N^2) geometric creation bottleneck in NMS
**Learning:** Instantiating `shapely.geometry.Polygon` objects inside nested loops (like O(N^2) NMS bounding box calculations) creates a massive performance bottleneck due to the high overhead of Shapely object creation and validation.
**Action:** Always pre-compute and cache Shapely geometric objects in an O(N) pass before executing O(N^2) logic on them. Remember to handle potential exceptions during instantiation and store safe default values (e.g., `None` or 0-area) to avoid breaking downstream loop execution.
