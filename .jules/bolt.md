## 2024-05-18 - Optimize poly_nms by precomputing shapely polygons
**Learning:** In `ppocr/utils/poly_nms.py`, the `poly_nms` function computes O(N^2) IoUs. By precomputing all polygons and extracting the valid polygon check `valid_boundary`, we can massively reduce the redundant work.
**Action:** When working with Shapely polygons inside nested loops for NMS or similar pairwise algorithms, precompute geometric attributes like `buffer` and `area` outside the loop to avoid recreating heavy objects repetitively.
