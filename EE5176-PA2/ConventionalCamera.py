import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import scipy.io
import scipy.linalg

def zeropad(img, left_pad, right_pad):
    
    if left_pad:
        img = np.concatenate((np.zeros((img.shape[0], left_pad, 3)), img), axis = 1)
    if right_pad:
        img = np.concatenate((img, np.zeros((img.shape[0], right_pad, 3))), axis = 1)

    return img

def get_args():
    pass

def main():
    ### Read Image ###
    img = np.array(Image.open(r"data/fish.png"))
    img = img/255.0

    ### Generate Blurred Image ###
    blurred_img = np.zeros((img.shape[0], img.shape[1]+51, 3))
    for i in range(52):
        img_transalted = zeropad(img, i, 51-i)
        blurred_img+=img_transalted/52.0

    noise = scipy.io.loadmat(r"data/gaussNoise")['gaussNoise']/255.0
    blurred_img+=noise
    plt.imshow(blurred_img)
    plt.show()

    ### Generate Toeplitz Matrix ###
    A = np.zeros((851, 800))
    for i in range(800):
        A[i:i+52,i] = 1/52.0

    plt.imshow(A)
    plt.show()

    ### Deblurring - Least Squares ###
    R_channel = scipy.linalg.lstsq(A, blurred_img[:,:,0].T)[0].T
    G_channel = scipy.linalg.lstsq(A, blurred_img[:,:,1].T)[0].T
    B_channel = scipy.linalg.lstsq(A, blurred_img[:,:,2].T)[0].T

    deblurred = np.stack([R_channel, G_channel, B_channel], axis = 2)
    plt.imshow(deblurred)
    plt.show()

if __name__=="__main__":
    main()
