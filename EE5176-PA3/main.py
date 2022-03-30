import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from CRF import estimateCRF
from utils import sampler

def main():
    ### Load Images ###
    Z = np.array([np.array(Image.open(f"Data/exposure{i}.jpg")) for i in range(1,17)])
    Z = np.transpose(Z, (1,2,3,0))
    Z = Z.reshape((-1, 3, 16))
    ZR, ZG, ZB = [Z[:, i, :] for i in range(3)] # Separating Color Channels
    w = [z if z<=255/2 else 255-z for z in range(256)] # Weightage of each pixel value
    ZR = sampler(ZR, w)
    ZG = sampler(ZR, w)
    ZB = sampler(ZR, w)

    ### CRF Estimation ###
    l = 0.1 # Smoothness Constant
    B = [np.log((1/2048)*np.float_power(2, k)) for k in range(16)] # Log Exposures

    gR = estimateCRF(ZR, B, l, w)
    gG = estimateCRF(ZR, B, l, w)
    gB = estimateCRF(ZR, B, l, w)
    plt.plot(gR)
    plt.savefig('CRF.png')

if __name__=="__main__":
    main()