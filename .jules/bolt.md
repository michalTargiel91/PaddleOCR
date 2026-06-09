## 2024-05-24 - Avoid O(N^2) Shapely Geometry Redundant Instantiations in NMS
**Learning:** In operations like `poly_nms` where $N$ polygons are compared, instantiating `Polygon` objects inside the nested $O(N^2)$ loop is extremely slow and causes unnecessary overhead from Shapely string-to-object parsing and buffer calculations.
**Action:** Always pre-compute and store Shapely geometries and their properties (like buffered forms and area) in a single $O(N)$ pass before entering complex NMS calculations. Wrap the pre-computation and downstream logic in safe `try...except Exception` fallbacks.
