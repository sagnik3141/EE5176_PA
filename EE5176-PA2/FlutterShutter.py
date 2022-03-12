import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import scipy.io
import scipy.linalg
from utils import zeropad, deblur

def main():
    ### Read Image ###
    img = np.array(Image.open(r"data/fish.png"))
    img = img/255.0

    ### Generate Blurred Image ###
    code1 = np.array([int(x) for x in "1010000111000001010000110011110111010111001001100111"])
    code2 = np.array([int(x) for x in "1010101010101010101010101010101010101010101010101010"])

    blurred_img1 = np.zeros((img.shape[0], img.shape[1]+51, 3))
    blurred_img2 = np.zeros((img.shape[0], img.shape[1]+51, 3))

    for i in range(52):
        img_transalted = zeropad(img, i, 51-i)
        if int(code1[i]):
            blurred_img1+=img_transalted/52.0
        if int(code2[i]):
            blurred_img2+=img_transalted/52.0
    
    noise = scipy.io.loadmat(r"data/gaussNoise")['gaussNoise']/255.0
    blurred_img1+=noise
    blurred_img2+=noise

    plt.imshow(blurred_img1)
    plt.show()
    plt.imshow(blurred_img2)
    plt.show()

    ### Generate Toeplits Matrices ###
    A1 = np.zeros((851, 800))
    A2 = np.zeros((851, 800))

    for i in range(800):
        A1[i:i+52,i] = code1/52.0
        A2[i:i+52,i] = code2/52.0

    plt.imshow(A1)
    plt.show()
    plt.imshow(A2)
    plt.show()

    ### Deblurring - Least Squares ###
    deblurred1 = deblur(A1, blurred_img1)
    deblurred2 = deblur(A2, blurred_img2)

    plt.imshow(deblurred1)
    plt.show()
    plt.imshow(deblurred2)
    plt.show()

if __name__=="__main__":
    main()