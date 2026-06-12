## 2024-06-12 - Optimize poly_nms and fix negative IoU
**Learning:** Pre-computing Shapely polygons and their buffers avoids O(N^2) instantiation during NMS loops. Additionally, when computing unions of buffered polygons, using unbuffered polygon areas causes negative union areas for degenerate polygons.
**Action:** Always pre-compute polygons and their buffers in O(N) with try-except blocks, and use buffered areas when unioning buffered intersection areas.
