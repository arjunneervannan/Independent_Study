from algorithms import *
from tqdm import tqdm


if __name__ == '__main__':
    num_iterations = 50
    N = [10, 50, 100, 500, 1000]
    lambda_val = [0.3, 0.5, 1, 2]
    p_val = 0.3
    mean_iterations = []
    all_mean_iterations = []
    
    for lambda_val in tqdm(lambda_val):
        for num_points in tqdm(N):
            avg_generations = []
            for iter in tqdm(range(num_iterations)):
                infection_status, parent, generation, num_generation = simulate_infection(num_points, lambda_val, p_val)
                avg_generations.append(num_generation)
            
            # print(f'Average number of generations for {num_points} people, lambda = {lambda_val}, p = {p_val}: {np.mean(avg_generations)}')
            mean_iterations.append(np.mean(avg_generations))
        all_mean_iterations.append(mean_iterations)
    
    for i in range(len(lambda_val)):
        legend_label = f"Lambda: {lambda_val[i]}"
        plt.plot(N, all_mean_iterations[i], label=legend_label)
        
    plt.legend()
    plt.show()
    