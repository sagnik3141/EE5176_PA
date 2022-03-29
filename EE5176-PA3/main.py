import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from CRF import estimateCRF

def main():
    ### Load Images ###
    Z = np.array([np.array(Image.open(f"Data/exposure{i}.jpg")) for i in range(1,17)])
    Z = np.reshape(Z, (-1, 16))

    ### CRF Estimation ###
    w = [z if z<=255/2 else 255-z for z in range(256)] # Weightage of each pixel value
    l = 0.1 # Smoothness Constant
    B = [np.log((1/2048)*np.float_power(2, k)) for k in range(16)] # Log Exposures

    g = estimateCRF(Z, B, l, w)
    plt.plot(g)

if __name__=="__main__":
    main()