import time
import numpy as np
from ppocr.utils.poly_nms import poly_nms

np.random.seed(42)
polygons = []
for _ in range(100):
    x, y = np.random.rand(2) * 100
    pts = [x, y, x+10, y, x+10, y+10, x, y+10]
    score = np.random.rand()
    polygons.append(pts + [score])

start = time.time()
res = poly_nms(polygons, 0.5)
t = time.time() - start
print(f"Executed poly_nms in {t:.4f}s")
