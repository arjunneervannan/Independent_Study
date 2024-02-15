from algorithms import *


# Example usage
N = 50  # Number of people
lambda_val = 1  # Poisson distribution parameter
p = 0.5  # Probability of infection

infection_status, parent, generation, num_generation = simulate_infection(N, lambda_val, p)
print(f'num iterations: {num_generation}')
visualize_tree(parent, generation, True)

