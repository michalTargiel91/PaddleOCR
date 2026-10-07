## 2024-10-07 - Optimize poly_nms
**Learning:** In poly_nms, shapely polygons were being converted from points (and their buffers calculated) repeatedly within an O(N^2) double loop, causing a massive performance bottleneck.
**Action:** By precomputing the shapely polygons, their buffered versions, and their areas in a linear O(N) loop before the NMS loop, the time complexity of the geometric operations is significantly reduced (measured from ~8.1s to ~1.6s for 300 polygons).
