import numpy as np 
import cv2

# Adaptive thresholding is good when the image has lightning shadows.
# Adaptive thresholding is best for lightining shadows

bw = cv2.imread('pencil.jpg', 0)
cv2.imshow("Banepa", bw)

ret, threshold_basic = cv2.threshold(bw, 70, 255, cv2.THRESH_BINARY)
cv2.imshow("Basic threshold", threshold_basic)

thresh_adapt = cv2.adaptiveThreshold(bw, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow("Adaptive Threshold", thresh_adapt)

cv2.waitKey(0)
cv2.destroyAllWindows()
