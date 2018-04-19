import cv2
import numpy as np 

img = cv2.imread('specriju.jpg',1)

# Convert from RGB to Gray
grey = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imwrite('grayspecriju.jpg', grey)

# Pick first color channel
b = img[:, :, 0]
# Pick second color channel
g = img[:, :, 1]
# Pick third color channel
r = img[:, :, 2]

# Add the third color channel or transparency channel
rgba = cv2.merge([b,g,r,g])

cv2.imwrite('transparent_specriju.png', rgba)