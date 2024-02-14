from algorithms import *

num_iters = 10
hilbert_order = 2

for _ in range(num_iters):
    points = generate_points(10)
    # square_ranges = generate_hilbert_curve_squares(4)
    final_order, min_distance = optimal_order(points)
    square_ranges = generate_hilbert_curve_squares(hilbert_order)
    tsp_order = define_order(points, square_ranges)
    display_path(tsp_order)
    display_path(final_order)