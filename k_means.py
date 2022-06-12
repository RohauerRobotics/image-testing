# image segmentation test - k-means
import matplotlib as plt
import numpy as np
import cv2
path = 'orange_on_table.jpg'
img = cv2.imread(path)

# preprocessing
# switches to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# converts the image to a 2-D Vector
twoDimage = img.reshape((-1,3))
# converts image to floating point
twoDimage = np.float32(twoDimage)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 3
attempts = 10

ret, label, center = cv2.kmeans(twoDimage, K, None,criteria, attempts,cv2.KMEANS_PP_CENTERS)
center = np.uint8(center)
res = center[label.flatten()]
result_image =  res.reshape((img.shape))
cv2.imshow("kmeans", result_image)
cv2.waitKey(0)
