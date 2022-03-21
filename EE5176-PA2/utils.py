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

def create_frame(img_fg, img_bg, fg_trans, bg_trans):
    """
    This function translates the foreground by 'fg_trans' pixels
    and merges it with the background which is transalted by 'bg_trans' pixels.
    """
    img_fg = np.concatenate((img_fg, np.zeros((img_fg.shape[0], 53, 3))), axis = 1)
    img_bg = np.concatenate((img_bg, np.zeros((img_bg.shape[0], 53, 3))), axis = 1)
    if fg_trans:
        img_fg_translated = np.concatenate((np.zeros((img_fg.shape[0], fg_trans, 3)), img_fg[:,:-fg_trans]), axis = 1)
    else:
        img_fg_translated = img_fg

    if bg_trans:
        img_bg_translated = np.concatenate((np.zeros((img_bg.shape[0], bg_trans, 3)), img_bg[:,:-bg_trans]), axis = 1)
    else:
        img_bg_translated = img_bg

    bg_mask = img_fg_translated[:,:,0]==0
    bg_mask = np.stack([bg_mask for i in range(3)], axis = 2)
    
    merged_img = img_fg_translated + img_bg_translated*bg_mask

    return merged_img
