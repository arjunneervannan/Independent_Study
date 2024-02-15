from algorithms import *
from tqdm import tqdm


if __name__ == '__main__':
    num_iterations = 50
    N = [10, 50, 100, 500, 1000]
    lambda_vals = [0.3, 0.5, 1, 2]
    p_val = 0.3
    
    all_mean_iterations = []
    
    for lambda_val in lambda_vals:
        mean_iterations = []
        for num_points in tqdm(N):
            avg_generations = []
            for iter in tqdm(range(num_iterations)):
                infection_status, parent, generation, num_generation = simulate_infection(num_points, lambda_val, p_val)
                avg_generations.append(num_generation)
            
            # print(f'Average number of generations for {num_points} people, lambda = {lambda_val}, p = {p_val}: {np.mean(avg_generations)}')
            mean_iterations.append(np.mean(avg_generations))
        all_mean_iterations.append(mean_iterations)
    
    for i in range(len(lambda_vals)):
        legend_label = f"Lambda: {lambda_vals[i]}"
        plt.plot(N, all_mean_iterations[i], label=legend_label)
        
    plt.title("Average Number of Iterations over Increasing Number of People")
    plt.xlabel("Number of People")
    plt.ylabel("Average Number of Iterations")
    plt.legend()
    plt.show()
    