import time
import numpy as np
from shapely.geometry import Polygon
import shapely.errors
from ppocr.utils.poly_nms import poly_nms as old_poly_nms, boundary_iou

def points2polygon(points):
    if isinstance(points, list):
        points = np.array(points)
    assert isinstance(points, np.ndarray)
    assert (points.size % 2 == 0) and (points.size >= 8)
    point_mat = points.reshape([-1, 2])
    return Polygon(point_mat)

def poly_nms_new(polygons, threshold):
    assert isinstance(polygons, list)

    polygons = np.array(sorted(polygons, key=lambda x: x[-1]))

    keep_poly = []
    index = [i for i in range(polygons.shape[0])]

    # Precompute polygons to avoid O(N^2) instantiations
    precomputed = []
    for p in polygons:
        pts = p[:-1]
        try:
            poly = points2polygon(pts)
            area = poly.area
            if not poly.is_valid or area <= 0:
                buf_poly = poly.buffer(0.0001)
            else:
                buf_poly = None
            precomputed.append((poly, area, buf_poly))
        except Exception:
            precomputed.append(None)

    while len(index) > 0:
        keep_poly.append(polygons[index[-1]].tolist())
        A_idx = index[-1]
        A_pts = polygons[A_idx][:-1]
        A_data = precomputed[A_idx]

        index = np.delete(index, -1)
        iou_list = np.zeros((len(index),))

        for i in range(len(index)):
            B_idx = index[i]
            B_pts = polygons[B_idx][:-1]
            B_data = precomputed[B_idx]

            # Fallback for anomalies
            if A_data is None or B_data is None or A_data[1] <= 0 or B_data[1] <= 0:
                iou_list[i] = boundary_iou(A_pts, B_pts)
                continue

            polyA, areaA, bufA = A_data
            polyB, areaB, bufB = B_data

            try:
                # Use buffered polygon if invalid, else use intersection directly
                pA = bufA if bufA is not None else polyA
                pB = bufB if bufB is not None else polyB

                # prefer intersection() over &
                inter = pA.intersection(pB)
                area_inter = inter.area

                area_union = areaA + areaB - area_inter
                if area_union == 0:
                    iou = 0.0
                else:
                    iou = area_inter / area_union
                iou_list[i] = iou
            except shapely.errors.TopologicalError:
                iou_list[i] = boundary_iou(A_pts, B_pts)

        remove_index = np.where(iou_list > threshold)
        index = np.delete(index, remove_index)

    return keep_poly

# Generate some dummy polygons
np.random.seed(0)
dummy_polygons = []
for _ in range(100):
    # A rectangle
    cx, cy = np.random.rand(2) * 100
    w, h = np.random.rand(2) * 10 + 5
    pts = [cx-w/2, cy-h/2, cx+w/2, cy-h/2, cx+w/2, cy+h/2, cx-w/2, cy+h/2]
    score = np.random.rand()
    pts.append(score)
    dummy_polygons.append(pts)

t0 = time.time()
res_old = old_poly_nms(dummy_polygons, 0.5)
t1 = time.time()
res_new = poly_nms_new(dummy_polygons, 0.5)
t2 = time.time()

print(f"Old time: {t1-t0:.4f}s")
print(f"New time: {t2-t1:.4f}s")

# Ensure results are exactly the same
assert len(res_old) == len(res_new)
for r1, r2 in zip(res_old, res_new):
    assert np.allclose(r1, r2)
print("Results match exactly!")
