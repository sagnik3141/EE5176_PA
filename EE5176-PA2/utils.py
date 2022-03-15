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

def RMSE(img1, img2):
    """
    Returns RMSE given two images.
    """
    assert img1.shape == img2.shape, "Dimensions of images do not match."
    img_diff = np.sum((img1-img2)**2)
    img_len = img1.shape[0]*img1.shape[1]*img1.shape[2]

    return np.sqrt(img_diff/img_len)

def create_frame(img_fg, img_bg, time_step):
    """
    This function translates the foreground by 'time_step' pixels
    and merges it with the background.
    """
    if time_step:
        img_fg_translated = np.concatenate((np.zeros((img_fg.shape[0], time_step, 3)), img_fg[:,:-time_step]), axis = 1)
    else:
        img_fg_translated = img_fg

    bg_mask = img_fg[:,:,0]==0
    bg_mask = np.stack([bg_mask for i in range(3)], axis = 2)

    merged_img = img_fg + img_bg*bg_mask

    return merged_img
