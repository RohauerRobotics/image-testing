# thresholding
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu
import cv2
path = "orange_on_table.jpg"
img = cv2.imread(path)

# convert to grayscale
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

def filter_image(image, mask):
    r = image[:,:,0] * mask
    g = image[:,:,1] * mask
    b = image[:,:,2] * mask
    return np.dstack([r,g,b])

thresh = threshold_otsu(img_gray)
img_otsu = img_gray < thresh
filtered = filter_image(img, img_otsu)
cv2.imshow("threshold", filtered)
cv2.waitKey(0)
