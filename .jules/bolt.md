## 2024-06-12 - Poly NMS Pre-computation
**Learning:** Using `poly.area` (unbuffered area) alongside the buffered intersection correctly mirrors `poly_union` logic while allowing caching, speeding up NMS significantly without negative IoU issues.
**Action:** When caching polygon operations, ensure the cached variables correctly reflect the original unbuffered area logic to maintain exact backward compatibility.
