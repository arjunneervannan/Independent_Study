import math
import numpy as np
from algorithms import *
from tqdm import tqdm


def euclidean_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return (point2[0] - point1[0])**2 + (point2[1] - point1[1])**2

def total_distance(points):
    """Calculate the total distance to visit all points and loop back to the starting point."""
    total = 0
    num_points = len(points)
    
    # Calculate distance between consecutive points
    for i in range(num_points - 1):
        total += euclidean_distance(points[i], points[i+1])
    
    # Add distance from the last point back to the first point to form a loop
    total += euclidean_distance(points[num_points - 1], points[0])
    
    return total


def generate_points(num_points):
    return np.random.rand(num_points, 2)


if __name__ == '__main__':
    dimensions = 2
    num_points = 10000
    num_iterations = 1000
    hilbert_order = 7
    distance_list = []
    
    for iter in tqdm(range(num_iterations)):
        points = generate_points(num_points)
        square_ranges = generate_hilbert_curve_squares(2)
        final_order = define_order(points, square_ranges)
        distance_list.append(total_distance(final_order))
    
    print(f"Average distance: {np.mean(distance_list)}")
    print(f"Standard deviation: {np.std(distance_list)}")
    print(f"Minimum distance: {np.min(distance_list)}")
    print(f"Maximum distance: {np.max(distance_list)}")
