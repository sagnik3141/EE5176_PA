import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def estimateCRF(Z, B, l, w):
    """
    Z[i][j]: Pixel value of pixel location i of image j
    B : Log Shutter Speeds
    l : Smoothness Constant
    w(z) : Weighting Function for pixel value z
    """

    n = 256 # Range of Pixel Values

    # Ax=b
    A = np.zeros(Z.shape[0]*Z.shape[1]+n+1, n+Z.shape[0])
    b = np.zeros(A.shape[0], 1)

    # Setting up equations
    eqn_num = 0

    for i in range(Z.shape[0]):
        for j in range(Z.shape[1]):
            A[eqn_num][Z[i][j]] = w[Z[i][j]]
            A[eqn_num][n+i] = -w[Z[i][j]]
            b[eqn_num][0] = w[Z[i][j]]*B[j]
            eqn_num+=1

    # Setting Middle Value
    A[eqn_num][128] = 1
    eqn_num+=1

    # Smoothness Equations
    for i in range(n-2):
        A[eqn_num][i] = l*w[i+1]
        A[eqn_num][i+1] = -2*l*w[i+1]
        A[eqn_num][i+2] = l*w[i+1]
        eqn_num+=1

    return np.linalg.solve(A, b, rcond = None)[0]