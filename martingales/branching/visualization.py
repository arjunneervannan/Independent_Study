from algorithms import *


# Example usage
N = 30  # Number of people
lambda_val = 0.5  # Poisson distribution parameter
p = 0.5  # Probability of infection

infection_status, parent, generation, num_generation = simulate_infection(N, lambda_val, p)
visualize_tree(parent, generation)

