import math
import numpy as np
import itertools
import matplotlib.pyplot as plt
from hilbertcurve.hilbertcurve import HilbertCurve
from tqdm import tqdm


def display_path(points):
    """
    Display a sequence of points as a path with consecutive points connected by lines.
    
    Parameters:
        points (list of tuples): A list of (x, y) coordinates representing the points in the path.
    """
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    
    plt.plot(x_values, y_values, marker='o', linestyle='-')
    plt.title(f'TSP Shortest Path with {len(points)} points, Distance:{total_distance_squared(points):.2f}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

def generate_points(num_points):
    return np.random.rand(num_points, 2)


def euclidean_distance_squared(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return (point2[0] - point1[0])**2 + (point2[1] - point1[1])**2


def total_distance_squared(points):
    """Calculate the total distance to visit all points and loop back to the starting point."""
    total = 0
    num_points = len(points)
    
    # Calculate distance between consecutive points
    for i in range(num_points - 1):
        total += euclidean_distance_squared(points[i], points[i+1])
    
    # Add distance from the last point back to the first point to form a loop
    total += euclidean_distance_squared(points[num_points - 1], points[0])
    
    return total


def euclidean_distance(point1, point2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def total_distance(points, route):
    """Calculate the total distance of a route."""
    total = 0
    for i in range(len(route) - 1):
        total += euclidean_distance(points[route[i]], points[route[i + 1]])
    total += euclidean_distance(points[route[-1]], points[route[0]])  # Close the loop
    return total


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


def optimal_order(points):
    """Find the shortest route that visits all points."""
    num_points = len(points)
    min_distance = float('inf')
    shortest_route = None
     # Generate all permutations of indices
    number = 0
     
    for permutation in tqdm(itertools.permutations(range(num_points))):
        number = number + 1
        distance = total_distance(points, permutation)
        if distance < min_distance:
            min_distance = distance
            shortest_route = permutation
    
    final_order = []
    for city in shortest_route:
        final_order.append((points[city][0], points[city][1]))
    return np.asarray(final_order), min_distance


