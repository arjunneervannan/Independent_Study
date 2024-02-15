from algorithms import *


if __name__ == '__main__':
    num_iterations = 1000
    N = [10, 50, 100, 500, 1000]
    lambda_val = [0.5, 1, 2, 3]
    p = [0.2, 0.4, 0.6, 0.8]
    mean_iterations = []
    
    for num_points in N:
        for lambda_val in lambda_val:
            for p_val in p:
                avg_generations = []
                for iter in range(num_iterations):
                    infection_status, parent, generation, num_generation = simulate_infection(num_points, lambda_val, p_val)
                    avg_generations.append(num_generation)
                
                print(f'Average number of generations for {num_points} people, lambda = {lambda_val}, p = {p_val}: {np.mean(avg_generations)}')
                mean_iterations.append(np.mean(avg_generations))
    