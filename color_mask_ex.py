# color masking
import cv2
path = "orange_on_table.jpg"
img = cv2.imread(path)

rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2HSV)

light_orange = (1,190,200)
dark_orange = (55,255,255)

mask = cv2.inRange(hsv_img, light_orange, dark_orange)
result = cv2.bitwise_and(img,img, mask=mask)
cv2.imshow("orange", img)
cv2.imshow("result", result)
cv2.waitKey(0)
