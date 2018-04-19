import cv2
import numpy as np 

img = cv2.imread('riju.jpg', 1)
cv2.imshow("Riju", img)

height, width, channels = img.shape

b, g, r = cv2.split(img)
cv2.imshow('Blue color channel',b)
cv2.imshow('Green color channel',g)
cv2.imshow('Red color channel',r)

cv2.waitKey(0)