# copyright (c) 2022 PaddlePaddle Authors. All Rights Reserve.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
from shapely.geometry import Polygon


def points2polygon(points):
    """Convert k points to 1 polygon.

    Args:
        points (ndarray or list): A ndarray or a list of shape (2k)
            that indicates k points.

    Returns:
        polygon (Polygon): A polygon object.
    """
    if isinstance(points, list):
        points = np.array(points)

    assert isinstance(points, np.ndarray)
    assert (points.size % 2 == 0) and (points.size >= 8)

    point_mat = points.reshape([-1, 2])
    return Polygon(point_mat)


def poly_intersection(poly_det, poly_gt, buffer=0.0001):
    """Calculate the intersection area between two polygon.

    Args:
        poly_det (Polygon): A polygon predicted by detector.
        poly_gt (Polygon): A gt polygon.

    Returns:
        intersection_area (float): The intersection area between two polygons.
    """
    assert isinstance(poly_det, Polygon)
    assert isinstance(poly_gt, Polygon)

    if buffer == 0:
        poly_inter = poly_det & poly_gt
    else:
        poly_inter = poly_det.buffer(buffer) & poly_gt.buffer(buffer)
    return poly_inter.area, poly_inter


def poly_union(poly_det, poly_gt):
    """Calculate the union area between two polygon.

    Args:
        poly_det (Polygon): A polygon predicted by detector.
        poly_gt (Polygon): A gt polygon.

    Returns:
        union_area (float): The union area between two polygons.
    """
    assert isinstance(poly_det, Polygon)
    assert isinstance(poly_gt, Polygon)

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
    """Calculate the IOU between two boundaries.

    Args:
       src (list): Source boundary.
       target (list): Target boundary.

    Returns:
       iou (float): The iou between two boundaries.
    """
    assert valid_boundary(src, False)
    assert valid_boundary(target, False)
    src_poly = points2polygon(src)
    target_poly = points2polygon(target)

    return poly_iou(src_poly, target_poly)


def poly_iou(poly_det, poly_gt):
    """Calculate the IOU between two polygons.

    Args:
        poly_det (Polygon): A polygon predicted by detector.
        poly_gt (Polygon): A gt polygon.

    Returns:
        iou (float): The IOU between two polygons.
    """
    assert isinstance(poly_det, Polygon)
    assert isinstance(poly_gt, Polygon)
    area_inters, _ = poly_intersection(poly_det, poly_gt)
    area_union = poly_union(poly_det, poly_gt)
    if area_union == 0:
        return 0.0
    return area_inters / area_union


def poly_nms(polygons, threshold):
    assert isinstance(polygons, list)

    polygons = np.array(sorted(polygons, key=lambda x: x[-1]))

    keep_poly = []
    index = [i for i in range(polygons.shape[0])]

    # Precompute Shapely polygons to optimize O(N^2) NMS loops
    precomputed_polys = []
    for poly_arr in polygons:
        poly_info = {'buffered': None, 'area': 0.0}
        pts = poly_arr[:-1]
        if valid_boundary(pts, False):
            try:
                poly = points2polygon(pts)
                buffered = poly.buffer(0.0001)
                poly_info['buffered'] = buffered
                poly_info['area'] = buffered.area
            except Exception:
                pass
        precomputed_polys.append(poly_info)

    while len(index) > 0:
        keep_poly.append(polygons[index[-1]].tolist())
        A = polygons[index[-1]][:-1]
        poly_a_dict = precomputed_polys[index[-1]]
        index = np.delete(index, -1)
        iou_list = np.zeros((len(index),))
        for i in range(len(index)):
            B = polygons[index[i]][:-1]
            poly_b_dict = precomputed_polys[index[i]]

            if not valid_boundary(A, False) or not valid_boundary(B, False):
                iou_list[i] = 0.0
                continue

            if poly_a_dict['buffered'] is None or poly_b_dict['buffered'] is None:
                iou_list[i] = 0.0
                continue

            try:
                inter = poly_a_dict['buffered'].intersection(poly_b_dict['buffered'])
                area_inters = inter.area
            except Exception:
                area_inters = 0.0

            area_union = poly_a_dict['area'] + poly_b_dict['area'] - area_inters
            if area_union == 0:
                iou = 0.0
            else:
                iou = area_inters / area_union
            iou_list[i] = iou

        remove_index = np.where(iou_list > threshold)
        index = np.delete(index, remove_index)

    return keep_poly
