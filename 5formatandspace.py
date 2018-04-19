# Images come in various space and formats it is important to transform from one space to another like full color to black n white
# Or from RGB to hue saturation and value
import cv2
import numpy as np 

img = cv2.imread('butterfly.jpg',1)

cv2.imshow("Image",img)
cv2.moveWindow("Image", 0, 0)
print(img.shape)

height, width, channel = img.shape

# Split into the separate color channels

b,g,r = cv2.split(img)

# np.split is the command to create the uninitialized array matrix
rgb_split = np.empty([height, width*3, 3], 'uint8')
rgb_split[:, 0:width] = cv2.merge([b,b,b])
rgb_split[:, width:width*2] = cv2.merge([g,g,g])
rgb_split[:, width*2:width*3] = cv2.merge([r,r,r])

cv2.imshow("Channels",rgb_split)

# Conversion from BGR to heu saturation value hsv
# Hew = type of color that we will see in 360 degree format
# Saturation = how staturated an individual color is 
# Value = How illuminance the channel is

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

hsv_split = np.empty([height, width*3, 3], 'uint8')
hsv_split = np.concatenate((h,s,v), axis=1)
cv2.imshow("Split hsv", hsv_split)


cv2.waitKey(0)
cv2.distroyAllWindow()