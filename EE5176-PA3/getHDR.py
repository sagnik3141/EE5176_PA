import numpy as np

def getHDR(ZC, g, w, B):
    """
    ZC[i][j]: Pixel value of pixel location i of image j
    B : Log Shutter Speeds
    w(z) : Weighting Function for pixel value z
    g: CRF
    
    Returns:
    E: Radiance Values
    """
    lE = np.zeros(ZC.shape[0])
    w_sum = 0
    for i in range(16):
        lE+=w[ZC[:,i]]*(g[ZC[:,i]]-B[i])
        w_sum+=w[ZC[:,i]]
    lE = lE/w_sum
    return lE

def getHDRColor(ZR, ZG, ZB, gR, gG, gB, w, B, X_dim, Y_dim):
    """
    ZC[i][j] : Pixel value of pixel location i of image j for channel C
    gC : CRF for channel C
    B : Log Shutter Speeds
    w(z) : Weighting Function for pixel value z
    
    Returns:
    E: Radiance Values
    """
    R_HDR = getHDR(ZR, gR, w, B)
    G_HDR = getHDR(ZG, gG, w, B)
    B_HDR = getHDR(ZB, gB, w, B)
    
    RGB_HDR = np.stack([R_HDR, G_HDR, B_HDR], axis = 1)
    RGB_HDR = np.reshape(RGB_HDR, (X_dim, Y_dim, -1))
    RGB_HDR = np.exp(RGB_HDR)
    
    return RGB_HDR