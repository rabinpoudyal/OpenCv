import cv2
import numpy as np 

# Read image file second param 1 means read as it is 0 means read as greyscale
img = cv2.imread('/home/rabin/Pictures/Wallpapers/20170918_162954-01.jpeg',1)

cv2.namedWindow('Rabin', cv2.WINDOW_NORMAL)
cv2.imshow('Rabin', img)

# Wait indefinitely to exit till the user press some key
cv2.waitKey(0)

# Write image to the file the output can be anything .png, .jpg and other
cv2.imwrite('output.png',img)