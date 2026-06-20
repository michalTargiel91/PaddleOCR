import numpy as np
from ppocr.utils.poly_nms import poly_nms

polygons = [
    [0, 0, 10, 0, 10, 10, 0, 10, 0.9],
    [1, 1, 11, 1, 11, 11, 1, 11, 0.8], # IOU is high, should be suppressed
    [20, 20, 30, 20, 30, 30, 20, 30, 0.85] # IOU is 0, should be kept
]

print(poly_nms(polygons, 0.5))
