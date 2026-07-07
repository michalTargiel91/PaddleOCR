## 2024-05-24 - Precomputing Shapely Geometries in NMS
**Learning:** In NMS algorithms using Shapely, calculating geometric buffers and intersections inside an O(N^2) loop is a massive bottleneck. Precomputing the Polygon objects, their buffered forms, and their unbuffered areas in O(N) avoids redundant Shapely operations.
**Action:** Always extract static geometry initialization and property retrieval out of hot nested loops, and handle exceptions safely by falling back to unoptimized functions.
