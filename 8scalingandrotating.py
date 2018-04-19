import numpy as np
import cv2

# Read an image

img = cv2.imread('butterfly.jpg', 1)

img_half = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
img_streach = cv2.resize(img, (600,600))

img_streach_near = cv2.resize(img, (600,600), interpolation = cv2.INTER_NEAREST)

cv2.imshow("Half Image", img_half)
cv2.imshow("Streach Image", img_streach)
cv2.imshow("Nearest Image Interpolation", img_streach_near)

# Rotate image by matrix transformation

M = cv2.getRotationMatrix2D((0,0), -30, 1) # rotate from origin 0,0 - top lef hand corner, -30 degrees, 1
rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow("Rotated", rotated)

cv2.waitKey(0)
cv2.distroyAllWindows()