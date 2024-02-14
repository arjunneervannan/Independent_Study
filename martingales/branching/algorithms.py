import numpy as np
import itertools
import random


def generate_pairs(N):
    """Generate all permutations of pairs from a list of numbers from 1 to N."""
    numbers = list(range(1, N+1))
    pairs = list(itertools.combinations(numbers, 2))
    # random.shuffle(pairs)
    return pairs


def simulate_infection(N, lambda_val, p, num_iterations):
    # Initialize the infection status of each person
    infection_status = np.zeros(N)
    parent = np.zeros(N)
    generation = np.zeros(N)
    infection_status[0] = 1  # Set the first person as infected
    next_round_infection_status = np.zeros(N)
    next_round_infection_status[0] = 1
    parent[0] = -1
    generation[0] = 0
    pairs = generate_pairs(N)

    for current_generation in range(num_iterations):
        # Iterate over all pairs of people
        for pair in pairs:
            if np.random.poisson(lambda_val) > 0:
                if infection_status[pair[0]-1] == 1 and infection_status[pair[1]-1] == 0:
                    if np.random.rand() < p:
                        next_round_infection_status[pair[1]-1] = 1
                        parent[pair[1] - 1] = pair[0] - 1
                        generation[pair[1] - 1] = current_generation + 1
                elif infection_status[pair[0]-1] == 0 and infection_status[pair[1]-1] == 1:
                    if np.random.rand() < p:
                        next_round_infection_status[pair[0]-1] = 1
                        parent[pair[0] - 1] = pair[1] - 1
                        generation[pair[0] - 1] = current_generation + 1
        infection_status = next_round_infection_status

    return infection_status, parents, generation

# Example usage
N = 100  # Number of people
lambda_val = 0.5  # Poisson distribution parameter
p = 0.2  # Probability of infection
num_iterations = 5  # Number of iterations

infection_status = simulate_infection(N, lambda_val, p, num_iterations)
print(infection_status)