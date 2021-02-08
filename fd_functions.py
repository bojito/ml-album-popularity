import numpy as np
import cv2
from skimage.transform import resize
from skimage.feature import hog


def fd_hog_descriptor(image):
    # skimage HOG descriptor
    orientations=9
    pixels_per_cell=(20,20)
    cells_per_block=(2,2)
    visualize=False
    multichannel=False
    transform_sqrt=True  
    block_norm="L1"
    
    fd = hog(gray_img, 
             orientations=orientations, 
             pixels_per_cell=pixels_per_cell, 
             cells_per_block=cells_per_block, 
             visualize=visualize, 
             multichannel=multichannel,
             transform_sqrt=transform_sqrt,
             block_norm=block_norm)
    
    return fd
    
    
    
def fd_hsv_histogram(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv_hist = cv2.calcHist([hsv_image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    cv2.normalize(hsv_hist, hsv_hist)
    
    return hsv_hist.flatten()