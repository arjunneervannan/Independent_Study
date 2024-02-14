import numpy as np

def simulate_infection(N, lambda_val, p, num_iterations):
    # Initialize the infection status of each person
    infection_status = np.zeros(N)
    infection_status[0] = 1  # Set the first person as infected

    for _ in range(num_iterations):
        # Iterate over all pairs of people
        for i in range(N):
            for j in range(i+1, N):
                # Check if the pair meets
                if np.random.poisson(lambda_val) > 0:
                    # Check if one person is infected and the other is not
                    if infection_status[i] == 1 and infection_status[j] == 0:
                        # Check if the non-infected person gets infected
                        if np.random.rand() < p:
                            infection_status[j] = 1

                    elif infection_status[i] == 0 and infection_status[j] == 1:
                        # Check if the non-infected person gets infected
                        if np.random.rand() < p:
                            infection_status[i] = 1

    return infection_status

# Example usage
N = 100  # Number of people
lambda_val = 0.5  # Poisson distribution parameter
p = 0.2  # Probability of infection
num_iterations = 1000  # Number of iterations

infection_status = simulate_infection(N, lambda_val, p, num_iterations)
print(infection_status)