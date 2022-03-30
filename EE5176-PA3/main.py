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
    print(ZR.shape)
    w = [z if z<=255/2 else 255-z for z in range(256)] # Weightage of each pixel value
    ZR = sampler(ZR, w)
    print(ZR.shape)
    ZG = sampler(ZG, w)
    ZB = sampler(ZB, w)
    print(ZB.shape)

    ### CRF Estimation ###
    l = 0.1 # Smoothness Constant
    B = [np.log((1/2048)*np.float_power(2, k)) for k in range(16)] # Log Exposures

    gR = estimateCRF(ZR, B, l, w)
    gG = estimateCRF(ZG, B, l, w)
    gB = estimateCRF(ZB, B, l, w)
    plt.plot(gR)
    plt.plot(gG)
    plt.plot(gB)
    plt.savefig('CRF.png')

if __name__=="__main__":
    main()
