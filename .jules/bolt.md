## 2024-05-23 - Optimizing poly_nms in PaddleOCR

**Learning:** When calculating IoU between polygons using Shapely, standard unoptimized `poly_nms` dynamically buffers and converts coordinates to polygons repeatedly inside nested O(N^2) loops. This causes massive overhead. Precomputing polygons, buffered polygons, area, and validity checks into a single list before the loops significantly boosts performance (1.3x+ speedup), skipping repeated geometry instantiation.

**Action:** Whenever an O(N^2) loop calculates geometric metrics (IoU, intersections), lift all geometry construction (`points2polygon`), properties (`area`, `is_valid`), and buffer operations (`buffer(0.0001)`) into an O(N) precomputation phase. Always include fallback logic inside the loop for unexpected Shapely topologies or mathematical edge cases (e.g., negative union area) to ensure the optimization remains backward compatible.
