import numpy as np
import cv2
from skimage.transform import resize
from skimage.feature import hog
from skimage.color import rgb2gray
from skimage import feature

def fd_hog_descriptor(image):
    # skimage HOG descriptor
    orientations=9
    pixels_per_cell=(20,20)
    cells_per_block=(2,2)
    visualize=False
    multichannel=False
    transform_sqrt=True  
    block_norm="L2"
    
    resized_img = resize(image, (100,100)) 
    
    if resized_img.shape[-1] == 3:
        gray_img = rgb2gray(resized_img)
    else:
        gray_img=resized_img
        
        
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
    
    
def fd_local_binary_pattern(image):
    numPoints = 24
    radius = 8
    eps=1e-7
    
    if image.shape[-1] == 3:
        gray_img = rgb2gray(image)
    else:
        gray_img=image
        
    lbp = feature.local_binary_pattern(gray_img, numPoints, radius, method="uniform")

    (hist, _) = np.histogram(lbp.ravel(),
                             bins=np.arange(0, numPoints + 3), 
                             range=(0, numPoints + 2))

    # normalize the histogram
    hist = hist.astype("float")
    hist /= (hist.sum() + eps)
    
    return hist, lbp