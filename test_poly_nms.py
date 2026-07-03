import time
import numpy as np
from shapely.geometry import Polygon
from ppocr.utils.poly_nms import poly_nms as old_poly_nms

def points2polygon(points):
    if isinstance(points, list):
        points = np.array(points)
    assert isinstance(points, np.ndarray)
    assert (points.size % 2 == 0) and (points.size >= 8)
    point_mat = points.reshape([-1, 2])
    return Polygon(point_mat)

def new_poly_nms(polygons, threshold):
    assert isinstance(polygons, list)

    polygons = np.array(sorted(polygons, key=lambda x: x[-1]))

    # Precompute polygons, buffered polygons, and their unbuffered areas
    poly_list = []
    buffered_poly_list = []
    area_list = []
    for poly_pts in polygons:
        pts = poly_pts[:-1]
        try:
            poly = points2polygon(pts)
            buffered_poly = poly.buffer(0.0001)
            area = poly.area
        except Exception:
            poly = None
            buffered_poly = None
            area = 0.0
        poly_list.append(poly)
        buffered_poly_list.append(buffered_poly)
        area_list.append(area)

    keep_poly = []
    index = [i for i in range(polygons.shape[0])]

    while len(index) > 0:
        keep_poly.append(polygons[index[-1]].tolist())
        A_idx = index[-1]
        A_poly = poly_list[A_idx]
        A_buffered = buffered_poly_list[A_idx]
        A_area = area_list[A_idx]

        index = np.delete(index, -1)
        iou_list = np.zeros((len(index),))

        if A_poly is None or A_buffered is None:
            # If A is invalid, IOUs with A are considered 0
            pass
        else:
            for i in range(len(index)):
                B_idx = index[i]
                B_poly = poly_list[B_idx]
                B_buffered = buffered_poly_list[B_idx]
                B_area = area_list[B_idx]

                if B_poly is None or B_buffered is None:
                    iou_list[i] = 0.0
                    continue

                try:
                    poly_inter = A_buffered & B_buffered
                    area_inters = poly_inter.area
                    area_union = A_area + B_area - area_inters
                    if area_union == 0:
                        iou_list[i] = 0.0
                    else:
                        iou_list[i] = area_inters / area_union
                except Exception:
                    iou_list[i] = 0.0

        remove_index = np.where(iou_list > threshold)
        index = np.delete(index, remove_index)

    return keep_poly

# Generate mock data
np.random.seed(42)
polygons = []
for _ in range(100):
    x, y = np.random.rand(2) * 100
    pts = [x, y, x+10, y, x+10, y+10, x, y+10]
    score = np.random.rand()
    polygons.append(pts + [score])

start = time.time()
old_res = old_poly_nms(polygons, 0.5)
t1 = time.time() - start

start = time.time()
new_res = new_poly_nms(polygons, 0.5)
t2 = time.time() - start

print(f"Old time: {t1:.4f}s")
print(f"New time: {t2:.4f}s")
print(f"Results match: {old_res == new_res}")
