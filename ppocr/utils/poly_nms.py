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
    index = list(range(polygons.shape[0]))

    # Precompute polygons and their unbuffered areas, buffered geometries
    # to avoid redundant O(N^2) Shapely creations and intersections.
    poly_cache = {}
    for i in range(polygons.shape[0]):
        pts = polygons[i][:-1]
        try:
            poly = points2polygon(pts)
            poly_area = poly.area
            poly_buf = poly.buffer(0.0001)
            poly_cache[i] = (poly, poly_area, poly_buf)
        except Exception:
            poly_cache[i] = None

    while len(index) > 0:
        curr_idx = index[-1]
        keep_poly.append(polygons[curr_idx].tolist())
        index.pop()

        curr_cache = poly_cache[curr_idx]

        remove_indices = []
        for i_idx, i in enumerate(index):
            B_cache = poly_cache[i]
            iou = 0.0

            if curr_cache is None or B_cache is None:
                # Fallback to original
                A = polygons[curr_idx][:-1]
                B = polygons[i][:-1]
                iou = boundary_iou(A, B)
            else:
                poly_A, area_A, buf_A = curr_cache
                poly_B, area_B, buf_B = B_cache

                # Inline intersection and union calculation using unbuffered areas
                try:
                    inter_geom = buf_A & buf_B
                    area_inters = inter_geom.area

                    # Original logic uses unbuffered areas for the union
                    area_union = area_A + area_B - area_inters

                    if area_union <= 0:
                        # Revert to exact fallback if math edge case hits
                        A = polygons[curr_idx][:-1]
                        B = polygons[i][:-1]
                        iou = boundary_iou(A, B)
                    else:
                        iou = area_inters / area_union
                except Exception:
                    # Fallback just in case
                    A = polygons[curr_idx][:-1]
                    B = polygons[i][:-1]
                    iou = boundary_iou(A, B)

            if iou > threshold:
                remove_indices.append(i_idx)

        # Remove from index in reverse order to not mess up indices
        for idx in reversed(remove_indices):
            index.pop(idx)

    return keep_poly
