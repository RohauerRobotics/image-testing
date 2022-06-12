# contour detection
import cv2
import matplotlib.pyplot as plt
import numpy as np
path = "orange_on_table.jpg"
img = cv2.imread(path)
img = cv2.resize(img, (256,256))

# convert to greyscale
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
_, thresh = cv2.threshold(gray, np.mean(gray),255, cv2.THRESH_BINARY_INV)
edges = cv2.dilate(cv2.Canny(thresh,0,255),None)

cnt = sorted(cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2],key=cv2.contourArea)[-1]
mask = np.zeros((256,256), np.uint8)
masked = cv2.drawContours(mask,[cnt],-1,255,-1)

dst = cv2.bitwise_and(img, img, mask=mask)
segmented = cv2.cvtColor(dst,cv2.COLOR_BGR2RGB)

cv2.imshow("segmented", segmented)
cv2.waitKey(0)
