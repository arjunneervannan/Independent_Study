import matplotlib.pyplot as plt
from algorithms import *
from simulations import *

def display_path(points):
    """
    Display a sequence of points as a path with consecutive points connected by lines.
    
    Parameters:
        points (list of tuples): A list of (x, y) coordinates representing the points in the path.
    """
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    
    plt.plot(x_values, y_values, marker='o', linestyle='-')
    plt.title(f'TSP Shortest Path with {len(points)} points, Distance:{total_distance(points):.2f}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

points = generate_points(1000)
square_ranges = generate_hilbert_curve_squares(4)
final_order = define_order(points, square_ranges)
display_path(final_order)

