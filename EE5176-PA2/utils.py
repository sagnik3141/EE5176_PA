import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import scipy.io
import scipy.linalg

def zeropad(img, left_pad, right_pad):
    """
    This function translates images to the right by zero-padding the image.
    """
    if left_pad:
        img = np.concatenate((np.zeros((img.shape[0], left_pad, 3)), img), axis = 1)
    if right_pad:
        img = np.concatenate((img, np.zeros((img.shape[0], right_pad, 3))), axis = 1)

    return img

def deblur(A, blurred_img):
    """
    This function returns the deblurred image (using least squares)
    given the Toeplitz Matrix A and the blurred image.
    """
    R_channel = scipy.linalg.lstsq(A, blurred_img[:,:,0].T)[0].T
    G_channel = scipy.linalg.lstsq(A, blurred_img[:,:,1].T)[0].T
    B_channel = scipy.linalg.lstsq(A, blurred_img[:,:,2].T)[0].T

    deblurred = np.stack([R_channel, G_channel, B_channel], axis = 2)

    return deblurred