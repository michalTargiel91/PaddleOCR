
## 2024-06-03 - Pre-computing Geometry Objects Outside O(N^2) Loops
**Learning:** Instantiating `shapely.geometry.Polygon` objects and calling their `.buffer()` method inside O(N^2) loops (like Non-Maximum Suppression) creates significant performance bottlenecks due to repetitive Python object creation and library boundary crossings.
**Action:** Always pre-compute Polygon objects and their buffered equivalents in an O(N) step prior to O(N^2) operations when dealing with spatial calculations or array-based NMS in Python.
