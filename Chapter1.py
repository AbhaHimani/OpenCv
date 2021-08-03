import cv2
import numpy as np
kernel= np.ones((5,5),np.uint8)
img= cv2.imread("david-hinkle-9djrpJKPUfo-unsplash.jpg")
imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",imgGray)
bluring= cv2.GaussianBlur(img,(7,7),0)
cv2.imshow("Blur Image",bluring)
canny= cv2.Canny(img,150,200)
cv2.imshow("Canny Image", canny)
erroded= cv2.erode(img,kernel,iterations=1)
cv2.imshow("Eroded Image",erroded)
cv2.waitKey(0)
