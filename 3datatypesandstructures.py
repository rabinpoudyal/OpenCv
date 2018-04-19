import cv2
import numpy as np 

# Create a black box 1 of 200 rows 150 columns and 1 color channel and the range is unsigned integer
black = np.zeros([200, 150, 1], 'uint8')
cv2.imshow("Black", black)
print(black[0, 0, :]) # Print first row first column and all the image channels

ones = np.ones([200, 150, 3], 'uint8')
cv2.imshow('Ones',ones)
print(ones[0, 0 , :])

white = np.ones([200, 150, 3], 'uint16')
white *= (2**16 - 1) # Since the value started at 0
cv2.imshow('White', white)
print(white[0, 0, :])

# Deep copy means it is completely copied all of its memory spaes and are no longer connected
# The format is BGR
color = ones.copy()
# [:,:] means across all rows and columns through both directions
color[:,:] = (255, 0, 0)
cv2.imshow("Blue",color)

# Now green window
color[:,:] = (0,255,0)
cv2.imshow("Green", color)

# Now red window
color[:,:] = (0,0,255)
cv2.imshow("Red", color)
print(color[0,0,:])

cv2.waitKey(0)
cv2.destroyAllWindows()