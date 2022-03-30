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
    ZG = sampler(ZG, w)
    ZB = sampler(ZB, w)

    ### CRF Estimation ###
    l = 0.1 # Smoothness Constant
    B = [np.log((1/2048)*np.float_power(2, k)) for k in range(16)] # Log Exposures

    gR = estimateCRF(ZR, B, l, w)
    gG = estimateCRF(ZG, B, l, w)
    gB = estimateCRF(ZB, B, l, w)
    plt.plot(gR, list(range(256)))
    plt.plot(gG, list(range(256)))
    plt.plot(gB, list(range(256)))
    plt.legend(['CRF - R Channel', 'CRF - G Channel', 'CRF - B Channel'])
    plt.xlabel('Log Exposure')
    plt.ylabel('Pixel Values')
    plt.title('CRF Plots')
    plt.grid(True)
    plt.savefig('results/CRF.png')

if __name__=="__main__":
    main()
