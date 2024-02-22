from algorithms import *


# Example usage
N = 100  # Number of people
lambda_val = 1  # Poisson distribution parameter
p = 0.01  # Probability of infection
recovery_time = 4

# infection_status, parent, generation, num_generation = simulate_infection_old(N, lambda_val, p)
infection_status, parent, generation, num_generation, num_infected, num_recovered, num_uninfected = simulate_infection_fixed_p(N, p, recovery_time)
print(f'num iterations: {num_generation}')
visualize_tree(parent, generation, True)

