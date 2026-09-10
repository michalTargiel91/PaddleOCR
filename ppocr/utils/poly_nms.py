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


def boundary_iou(src, target, src_poly=None, target_poly=None):
    """Calculate the IOU between two boundaries.

    Args:
       src (list): Source boundary.
       target (list): Target boundary.
       src_poly (Polygon): Precomputed source polygon.
       target_poly (Polygon): Precomputed target polygon.

    Returns:
       iou (float): The iou between two boundaries.
    """
    assert valid_boundary(src, False)
    assert valid_boundary(target, False)
    if src_poly is None:
        src_poly = points2polygon(src)
    if target_poly is None:
        target_poly = points2polygon(target)

    if src_poly is None or target_poly is None:
        return 0.0

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

    # Precompute Shapely Polygons, Areas, and Buffered Polygons
    shapely_polygons = []
    buffer = 0.0001
    for i in range(polygons.shape[0]):
        try:
            poly = Polygon(polygons[i][:-1].reshape([-1, 2]))
            poly_area = poly.area
            poly_buffered = poly.buffer(buffer)
        except Exception:
            poly = None
            poly_area = 0.0
            poly_buffered = None
        shapely_polygons.append((poly, poly_area, poly_buffered))

    while len(index) > 0:
        keep_poly.append(polygons[index[-1]].tolist())
        A = polygons[index[-1]][:-1]
        poly_a, area_a, poly_a_buffered = shapely_polygons[index[-1]]
        index = np.delete(index, -1)

        iou_list = np.zeros((len(index),))
        if poly_a is not None:
            for i in range(len(index)):
                B = polygons[index[i]][:-1]
                poly_b, area_b, poly_b_buffered = shapely_polygons[index[i]]
                if poly_b is not None:
                    # Inline intersection, union, and iou math perfectly matching original
                    poly_inter = poly_a_buffered & poly_b_buffered
                    area_inters = poly_inter.area
                    area_union = area_a + area_b - area_inters
                    if area_union == 0:
                        iou_list[i] = 0.0
                    else:
                        iou_list[i] = area_inters / area_union
                else:
                    iou_list[i] = 0.0
        else:
            # If poly_a is None, IOUs are 0
            pass

        remove_index = np.where(iou_list > threshold)
        index = np.delete(index, remove_index)

    return keep_poly
