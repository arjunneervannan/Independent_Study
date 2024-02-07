import numpy as np
import matplotlib.pyplot as plt

def generate_points(num_points):
    np.random.seed(0)
    return np.random.rand(num_points, 2)


test_points = generate_points(10)
plt.scatter(test_points[:, 0], test_points[:, 1])
plt.show()
