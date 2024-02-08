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
    test_num_pts = [5, 10, 50, 100, 500, 1000]
    hilbert_orders = [1, 2, 3, 4]
    num_iterations = 1000
    average_distances = []
    standard_deviations = []
    minimum_distances = []
    maximum_distances = []
    
    for hilbert_order in hilbert_orders:
        avg_dists = []
        std_devs = []
        min_dists = []
        max_dists = []
        for num_points in test_num_pts:
            distance_list = []
            for iter in tqdm(range(num_iterations)):
                points = generate_points(num_points)
                square_ranges = generate_hilbert_curve_squares(hilbert_order)
                final_order = define_order(points, square_ranges)
                distance_list.append(total_distance(final_order))
            
            avg_dists.append(np.mean(distance_list))
            std_devs.append(np.std(distance_list))
            min_dists.append(np.min(distance_list))
            max_dists.append(np.max(distance_list))
            
        average_distances.append(avg_dists)
        standard_deviations.append(std_devs)
        minimum_distances.append(min_dists)
        maximum_distances.append(max_dists)
    
    plt.title("Average Distance over Increasing Number of Points")
    for i in range(len(hilbert_orders)):
        legend_label = f"Order: {hilbert_orders[i]}"
        plt.plot(test_num_pts, average_distances[i], label=legend_label)
        
    plt.legend()
    plt.show()
        
    plt.title("Std Dev of Distance over Increasing Number of Points")
    for i in range(len(hilbert_orders)):
        legend_label = f"Order: {hilbert_orders[i]}"
        plt.plot(test_num_pts, standard_deviations[i], label=legend_label)
        
    plt.legend()
    plt.show()
        
    plt.title("Minimum Distance over Increasing Number of Points")
    for i in range(len(hilbert_orders)):
        legend_label = f"Order: {hilbert_orders[i]}"
        plt.plot(test_num_pts, minimum_distances[i], label=legend_label)
        
    plt.legend()
    plt.show()
        
    plt.title("Maximum Distance over Increasing Number of Points")
    for i in range(len(hilbert_orders)):
        legend_label = f"Order: {hilbert_orders[i]}"
        plt.plot(test_num_pts, maximum_distances[i], label=legend_label)
        
    plt.legend()
    plt.show()
    
    
    
#             print(f"Number of Points: {num_points}")
#             print(f"Hilbert Curve Order (Log base 4): {hilbert_order}")
#             print(f"Number of Iterations: {num_iterations}")
#             print(f"Average distance: {np.mean(distance_list)}")
#             print(f"Standard deviation: {np.std(distance_list)}")
#             print(f"Minimum distance: {np.min(distance_list)}")
#             print(f"Maximum distance: {np.max(distance_list)}")
