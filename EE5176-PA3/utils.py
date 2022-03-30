import numpy as np

def sampler(Z, w):
    num_samples = Z.shape[0]*1e-4
    #grid = [[(i, j) for j in range(16)] for i in range(Z.shape[0])]
    p_dist = np.array([w[Z[i][7]] for i in range(Z.shape[0])])
    p_dist = p_dist/np.sum(p_dist)
    idx = np.random.choice(Z.shape[0], int(num_samples), replace = False, p = p_dist)

    return Z[idx]
