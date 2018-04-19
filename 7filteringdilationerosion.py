# In this module, we will take a look at a few useful filtering functions often used to pre-process or
# adjust an image prior to doing more complex operations. These operations help reduce noise or unwanted 
# variances of an image or threshold. The goal is to make the image easier to work with. The three filters
# are the 
# =Gaussian Blur, 
# =Erosion, and 
# =Dilation filters. The Gaussian Blur filter smooths an image by averaging
# pixel values with its neighbors. It's called a Gaussian Blur because the average has a Gaussian falloff 
#effect.

# In other words, pixels that are closer to the target pixel have a higher impact with the average than pixels 
# that are far away. This is how the smoothing works.
# It is often used as a decent way to smooth out noise in an image as a precursor to other processing. 

#As you can see, the Dilation effect works to turn black pixels, or background pixels, into white pixels,
#while an erosion filter looks to turn white pixels into black pixels, essentially eating away at the foreground.
#The small structuring element that was moved across the image is called the kernel and defines where and how to
#mark a pixel changed by that filter.


import cv2
import numpy as np 

img = cv2.imread('noisyimage.png', 1)
#img_for_blur = cv2.imread('butterfly.jpg', 1)

# The structuring element should be of odd type

blur = cv2.GaussianBlur(img, (5, 55), 10)

cv2.imshow('Blur Butterfly', blur)

# Lets define our kernel item for the dilation and erosion element

kernel = np.ones((5,5), 'uint8')

dilate = cv2.dilate(img, kernel, iterations = 1)
erode = cv2.erode(img, kernel, iterations = 1)

cv2.imshow("Dilation effect", dilate)
cv2.imshow("Erosion effect", erode)

#cv2.imshow("Original", img)

cv2.waitKey(0)