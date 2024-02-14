from algorithms import *

num_iters = 10
hilbert_order = 2

distance_differences = []
square_ranges = generate_hilbert_curve_squares(hilbert_order)

for _ in range(num_iters):
    points = generate_points(10)
    tsp_optimal_order, _ = optimal_order(points)
    hilbert_order = define_order(points, square_ranges)
    tsp_optimal_distance = total_distance_squared(tsp_optimal_order)
    hilbert_distance = total_distance_squared(hilbert_order)
    print(f"Optimal TSP distance: {tsp_optimal_distance}") 
    print(f"Hilbert TSP distance: {hilbert_distance}\n-----\n")
    
    distance_differences.append(abs(tsp_optimal_distance - hilbert_distance))

print(f"average distance difference: {np.mean(distance_differences)}")
    
    