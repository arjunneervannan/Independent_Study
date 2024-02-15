from algorithms import *


# Example usage
N = 100  # Number of people
lambda_val = 0.2  # Poisson distribution parameter
p = 0.1  # Probability of infection

infection_status, parent, generation, num_generation = simulate_infection(N, lambda_val, p)
visualize_tree(parent, generation, False)

