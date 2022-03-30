import numpy as np

def sampler(Z, w):
    num_samples = Z.shape[0]*1e-6
    #grid = [[(i, j) for j in range(16)] for i in range(Z.shape[0])]
    p_dist = [w[Z[i][7]] for i in range(Z.shape[0])]
    idx = np.random.choice(num_samples, num_samples, replace = False, p = p_dist)

    return Z[idx]
