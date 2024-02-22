import math
import numpy as np
from algorithms import *


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
                distance_list.append(total_distance_squared(final_order))
            
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
    

