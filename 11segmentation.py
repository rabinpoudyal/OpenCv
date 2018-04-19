import numpy as np 
import cv2

bw = cv2.imread('detect_blob.png', 0)

height, width = bw.shape[0:2]

threshold = 85

cv2.imshow("Original bnw", bw)

binary = np.zeros([height, width, 1], 'uint8')

for row in range(0, height):
	for col in range(0, width):
		if bw[row][col] > threshold:
			binary[row][col] = 255

# This is very slow segmentation technique
cv2.imshow("Image after segmentation", binary)

# Faster segmentation built in cv

ret, threshold = cv2.threshold(bw, threshold, 255, cv2.THRESH_BINARY)
cv2.imshow("Cv segmentation", threshold)

cv2.waitKey()
cv2.destroyAllWindows()