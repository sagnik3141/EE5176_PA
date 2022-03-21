import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import scipy.io

from utils import create_frame, deblur

def main():
    ### Read Images ###
    img_fg = np.array(Image.open(r"data/redcar.png"))
    img_fg = img_fg/255.0
    img_bg = np.array(Image.open(r"data/background.png"))
    img_bg = img_bg/255.0

    ### Generating Blurred Image (Static Camera) ###
    blurred_img1 = np.zeros((img_bg.shape[0], img_bg.shape[1]+53, 3))
    for i in range(53):
        blurred_img1+=create_frame(img_fg, img_bg, i, 0)/53.0

    plt.imshow(blurred_img1)
    plt.show()

    ### Generating Blurred Image (With Camera Motion) ###
    blurred_img2 = np.zeros((img_bg.shape[0], img_bg.shape[1]+53, 3))
    bg_trans = np.rint(scipy.io.loadmat('data/CameraT.mat')['CameraT'].flatten()).astype(int)
    for i in range(53):
        blurred_img2+=create_frame(img_fg, img_bg, bg_trans[i]+i, bg_trans[i])/53.0

    plt.imshow(blurred_img2)
    plt.show()

    ### Generating PSF ###
    PSF = np.zeros((53,))
    a=1/13
    for i in bg_trans:
        if i:
            PSF[i]+=1/np.sqrt(a*i)
        else:
            PSF[i]+=1/np.sqrt(a*0.1)
    PSF = PSF/np.sum(PSF)

    A = np.zeros((653,600))
    for i in range(600):
        A[i:i+53, i] = PSF

    deblurred = deblur(A, blurred_img2)

    plt.imshow(deblurred)
    plt.show()

if __name__=="__main__":
    main()