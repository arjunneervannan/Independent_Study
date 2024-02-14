import matplotlib.pyplot as plt
from algorithms import *
from simulations import *


points = generate_points(1000)
square_ranges = generate_hilbert_curve_squares(4)
final_order = define_order(points, square_ranges)
display_path(final_order)

