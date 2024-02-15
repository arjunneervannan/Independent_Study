import copy
import numpy as np
import itertools
import random
import networkx as nx
import matplotlib.pyplot as plt

def visualize_tree(parents, generation):
    """Visualize a tree based on parent array and generation matrix."""
    G = nx.DiGraph()

    for i, parent in enumerate(parents):
        if parent != -1:
            G.add_edge(parent, i)

    pos = {}
    for i, level in enumerate(generation):
        pos[i] = (i, -level)

    nx.draw(G, pos, with_labels=False, node_size=100, node_color="skyblue", font_size=12, font_weight="bold")
    for i, level in enumerate(generation):
        plt.text(i, -level, f'Level: {level}', ha='center', va='center', fontsize=8, color='red')
        
    plt.title("Tree Visualization")
    plt.show()


def generate_pairs(N):
    """Generate all permutations of pairs from a list of numbers from 1 to N."""
    numbers = list(range(1, N+1))
    pairs = list(itertools.combinations(numbers, 2))
    random.shuffle(pairs)
    return pairs


def simulate_infection(N, lambda_val, p):
    # Initialize the infection status of each person
    infection_status = np.zeros(N)
    parent = np.zeros(N)
    generation = np.zeros(N)
    infection_status[0] = 1  # Set the first person as infected
    next_round_infection_status = np.zeros(N)
    next_round_infection_status[0] = 1
    for i in range(N):
        parent[i] = -1
        generation[i] = 0
    generation[0] = 0
    pairs = generate_pairs(N)
    still_infectious = np.any(infection_status == 0)
    current_generation = 0

    while (still_infectious):
        print(f'generation # {current_generation}')
        # Iterate over all pairs of people
        for pair in pairs:
            if np.random.poisson(lambda_val) > 0:
                if infection_status[pair[0]-1] == 1 and infection_status[pair[1]-1] == 1:
                    continue
                elif infection_status[pair[0]-1] == 1 and infection_status[pair[1]-1] == 0:
                    if np.random.rand() < p:
                        next_round_infection_status[pair[1]-1] = 1
                        parent[pair[1] - 1] = pair[0] - 1
                        # if generation[pair[0] - 1] == current_generation + 1:
                        #     print("flag")
                        generation[pair[1] - 1] = current_generation + 1
                elif infection_status[pair[0]-1] == 0 and infection_status[pair[1]-1] == 1:
                    if np.random.rand() < p:
                        next_round_infection_status[pair[0]-1] = 1
                        parent[pair[0] - 1] = pair[1] - 1
                        # if generation[pair[0] - 1] == current_generation + 1:
                        #     print("flag")
                        generation[pair[0] - 1] = current_generation + 1
        infection_status = copy.deepcopy(next_round_infection_status)
        current_generation += 1
        still_infectious = np.any(infection_status == 0)

    return infection_status, parent, generation, current_generation

