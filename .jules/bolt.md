## 2024-05-17 - Optimize Polygon Instantiation in NMS
**Learning:** Precomputing `shapely.geometry.Polygon` objects outside of nested O(N^2) Non-Maximum Suppression (NMS) loops significantly reduces execution time by avoiding redundant array formatting and object initialization.
**Action:** Identify and hoist expensive geometry parsing and object instantiations out of inner NMS loops in prediction post-processing steps.
