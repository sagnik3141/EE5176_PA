import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import imageio
import scipy.io
import scipy.linalg
from scipy.fft import fft
from utils import zeropad, deblur, RMSE

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

    imageio.imwrite('results/FS_blurred1.png', blurred_img1*255.0)
    imageio.imwrite('results/FS_blurred2.png', blurred_img2*255.0)
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

    imageio.imwrite('results/FS_toeplitz1.png', A1*255.0)
    imageio.imwrite('results/FS_toeplitz2.png', A2*255.0)
    plt.imshow(A1)
    plt.show()
    plt.imshow(A2)
    plt.show()

    ### DFT Plots ###
    # DFT Plot of Conventional Camera
    code = np.zeros((851,))
    code[:52] = 1/52.0
    plt.magnitude_spectrum(code, Fs = 1, scale = 'dB')
    plt.title(r"DFT of Conventional Code")
    plt.grid(True)
    plt.savefig("results/CC_DFT.png")
    plt.show()

    # DFT Plot of Code 1
    plt.magnitude_spectrum(A1[:,0], Fs = 1, scale = 'dB')
    plt.title(r"DFT of Flutter Shutter Code 1")
    plt.grid(True)
    plt.savefig("results/FS1_DFT.png")
    plt.show()

    # DFT Plot of Code 2
    plt.magnitude_spectrum(A2[:,0], Fs = 1, scale = 'dB')
    plt.title(r"DFT of Flutter Shutter Code 2")
    plt.grid(True)
    plt.savefig("results/FS2_DFT.png")
    plt.show()

    ### Deblurring - Least Squares ###
    deblurred1 = deblur(A1, blurred_img1)
    deblurred2 = deblur(A2, blurred_img2)

    imageio.imwrite('results/FS_deblurred1.png', deblurred1*255.0)
    imageio.imwrite('results/FS_deblurred2.png', deblurred2*255.0)
    plt.imshow(deblurred1)
    plt.show()
    plt.imshow(deblurred2)
    plt.show()

    ### RMSE Values ###
    print(f"RMSE between Original And Deblurred using Code 1 = {RMSE(img, np.clip(deblurred1, 0 ,1))}")
    print(f"RMSE between Original And Deblurred using Code 2 = {RMSE(img, np.clip(deblurred2, 0 ,1))}")

    ### Deblurring without noise ###
    # Generate Toeplitz Matrix for Conventional Camera
    A = np.zeros((851, 800))
    for i in range(800):
        A[i:i+52,i] = 1/52.0
    # Generate Blurred Image for Conventional Camera
    blurred_img = np.zeros((img.shape[0], img.shape[1]+51, 3))
    for i in range(52):
        img_transalted = zeropad(img, i, 51-i)
        blurred_img+=img_transalted/52.0
    # Deblurring
    deblurredcc_nn = deblur(A, blurred_img)
    deblurred1_nn = deblur(A1, blurred_img1-noise)
    deblurred2_nn = deblur(A2, blurred_img2-noise)

    # RMSE
    print(f"RMSE between Original And Deblurred using Conventional Camera without Noise = {RMSE(img, np.clip(deblurredcc_nn, 0, 1))}")
    print(f"RMSE between Original And Deblurred using Code 1 without Noise = {RMSE(img, np.clip(deblurred1_nn, 0 ,1))}")
    print(f"RMSE between Original And Deblurred using Code 2 without Noise = {RMSE(img, np.clip(deblurred2_nn, 0, 1))}")

    imageio.imwrite('results/CC_deblurred_nn.png', deblurredcc_nn*255.0)
    imageio.imwrite('results/FS_deblurred1_nn.png', deblurred1_nn*255.0)
    imageio.imwrite('results/FS_deblurred2_nn.png', deblurred2_nn*255.0)
    plt.imshow(deblurredcc_nn)
    plt.show()
    plt.imshow(deblurred1_nn)
    plt.show()
    plt.imshow(deblurred2_nn)
    plt.show()

if __name__=="__main__":
    main()