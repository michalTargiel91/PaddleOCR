import time
import numpy as np
import shapely.errors
from shapely.geometry import Polygon

def points2polygon(points):
    if isinstance(points, list):
        points = np.array(points)
    point_mat = points.reshape([-1, 2])
    return Polygon(point_mat)

def poly_intersection(poly_det, poly_gt, buffer=0.0001):
    if buffer == 0:
        poly_inter = poly_det & poly_gt
    else:
        poly_inter = poly_det.buffer(buffer) & poly_gt.buffer(buffer)
    return poly_inter.area, poly_inter

def poly_union(poly_det, poly_gt):
    area_det = poly_det.area
    area_gt = poly_gt.area
    area_inters, _ = poly_intersection(poly_det, poly_gt)
    return area_det + area_gt - area_inters

def valid_boundary(x, with_score=True):
    num = len(x)
    if num < 8:
        return False
    if num % 2 == 0 and (not with_score):
        return True
    if num % 2 == 1 and with_score:
        return True
    return False

def boundary_iou(src, target):
    assert valid_boundary(src, False)
    assert valid_boundary(target, False)
    src_poly = points2polygon(src)
    target_poly = points2polygon(target)
    area_inters, _ = poly_intersection(src_poly, target_poly)
    area_union = poly_union(src_poly, target_poly)
    if area_union == 0:
        return 0.0
    return area_inters / area_union

def poly_nms_old(polygons, threshold):
    polygons = np.array(sorted(polygons, key=lambda x: x[-1]))
    keep_poly = []
    index = [i for i in range(polygons.shape[0])]
    while len(index) > 0:
        keep_poly.append(polygons[index[-1]].tolist())
        A = polygons[index[-1]][:-1]
        index = np.delete(index, -1)
        iou_list = np.zeros((len(index),))
        for i in range(len(index)):
            B = polygons[index[i]][:-1]
            iou_list[i] = boundary_iou(A, B)
        remove_index = np.where(iou_list > threshold)
        index = np.delete(index, remove_index)
    return keep_poly

def poly_nms_new(polygons, threshold):
    polygons = np.array(sorted(polygons, key=lambda x: x[-1]))
    keep_poly = []
    index = [i for i in range(polygons.shape[0])]

    precomputed = {}
    for i in range(polygons.shape[0]):
        pts = polygons[i][:-1]
        if not valid_boundary(pts, False):
            precomputed[i] = None
            continue
        try:
            poly = points2polygon(pts)
            area = poly.area
            buf_poly = poly.buffer(0.0001)
            if area <= 0 or not poly.is_valid:
                precomputed[i] = None
            else:
                precomputed[i] = (poly, area, buf_poly)
        except Exception:
            precomputed[i] = None

    while len(index) > 0:
        curr_idx = index[-1]
        keep_poly.append(polygons[curr_idx].tolist())

        A_pts = polygons[curr_idx][:-1]
        A_data = precomputed[curr_idx]

        index = np.delete(index, -1)
        iou_list = np.zeros((len(index),))

        for i in range(len(index)):
            B_idx = index[i]
            B_data = precomputed[B_idx]

            if A_data is None or B_data is None:
                iou_list[i] = boundary_iou(A_pts, polygons[B_idx][:-1])
                continue

            poly_A, area_A, buf_A = A_data
            poly_B, area_B, buf_B = B_data

            try:
                poly_inter = buf_A.intersection(buf_B)
                area_inters = poly_inter.area
                area_union = area_A + area_B - area_inters

                if area_union == 0:
                    iou_list[i] = 0.0
                else:
                    iou_list[i] = area_inters / area_union
            except shapely.errors.TopologicalError:
                iou_list[i] = boundary_iou(A_pts, polygons[B_idx][:-1])

        remove_index = np.where(iou_list > threshold)
        index = np.delete(index, remove_index)
    return keep_poly

np.random.seed(0)
# Generate random polygons (8 coordinates + 1 score)
N = 100
polygons = []
for _ in range(N):
    x, y = np.random.rand() * 100, np.random.rand() * 100
    pts = [x, y, x+10, y, x+10, y+10, x, y+10]
    score = np.random.rand()
    polygons.append(pts + [score])

t0 = time.time()
res1 = poly_nms_old(polygons, 0.3)
t1 = time.time()
print(f"Old time: {t1 - t0:.4f}s")

t0 = time.time()
res2 = poly_nms_new(polygons, 0.3)
t1 = time.time()
print(f"New time: {t1 - t0:.4f}s")

# Verify equality
for p1, p2 in zip(res1, res2):
    assert np.allclose(p1, p2)
print("Results match perfectly!")
