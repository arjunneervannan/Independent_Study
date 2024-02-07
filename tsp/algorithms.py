import numpy as np
import matplotlib.pyplot as plt
from hilbertcurve.hilbertcurve import HilbertCurve


def get_subsquare_ranges(point, order):
  """
  point: (x,y) coordinate for bottom left corner of subsquare
  order: order of hilbert curve
  returns: list of ranges for point's corresponding subsquare -> 
          [tuple of x-range inclusive, tuple of y-range inclusive]
  """
  offset = 1/(2 ** (order))
  return [
          (point[0], point[0] + offset), 
          (point[1], point[1] + offset)
          ]


def generate_hilbert_curve_squares(order):
    dimensions = 2
    hilbert_curve = HilbertCurve(order, dimensions)
    distances = list(range(4 ** order))
    points = np.asarray(hilbert_curve.points_from_distances(distances)) / 2 ** order
    square_ranges = []
    for point, dist in zip(points, distances):
        square_ranges.append(get_subsquare_ranges(point, order))
    return square_ranges


def define_order(points, square_ranges):
    point_order = []
    for point in points:
        for index, range in enumerate(square_ranges):
            if range[0][0] <= point[0] <= range[0][1] and range[1][0] <= point[1] <= range[1][1]:
                point_order.append([index, point])
                break
    point_order.sort(key=lambda x: x[0])
    output_point_order = [x[1] for x in point_order]
    return np.asarray(output_point_order)


