import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import scipy.io
import scipy.linalg
import imageio
from utils import zeropad, deblur, RMSE

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
    imageio.imwrite('results/CC_blurred.png', blurred_img*255.0)
    plt.imshow(blurred_img)
    plt.show()

    ### Generate Toeplitz Matrix ###
    A = np.zeros((851, 800))
    for i in range(800):
        A[i:i+52,i] = 1/52.0

    imageio.imwrite('results/CC_toeplitz.png', A*255.0)
    plt.imshow(A)
    plt.show()

    ### Deblurring - Least Squares ###
    deblurred = deblur(A, blurred_img)

    imageio.imwrite('results/CC_deblurred.png', deblurred*255.0)
    plt.imshow(deblurred)
    plt.show()

    ### RMSE Value ###
    print(f"RMSE between Original And Deblurred = {RMSE(img, np.clip(deblurred, 0, 1))}")

if __name__=="__main__":
    main()
