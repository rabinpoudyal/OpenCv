import cv2
import numpy as np 

# Read the output.png image
img = cv2.imread('riju.jpg',1)

# Print the data from the image
print("The followint is the data from the image")
print(img)

print("The type of data the image has is: ")
print(type(img))
print("This means that the image is numpy nd array of numbers")

print("If you print out the length of image then: ")
print(len(img))
print("This is the number of rows in the image.")

print("Likewise if you do the length in the top row or any row then you would see ")
print(len(img[0]))
print("This is the number of columns in the image")

print("If you want to print out the number of color channels in the image then: ")
print(len(img[0][0]))
print("If 3 is printed then it is RGB color channel")
print("If there is transparency layer in the image ie alpha channel then it would actually print 4")

print("You can get all these information easily by: ")
print(img.shape)
print("(Rows, Columns, Number of channels)")

print("If you want to print the data type of image")
print(img.dtype)
print("If it prints unsigned integer 8 then it means that there is maximum of 2^8 in each pixel ie range of pixel is 0-255")

print("If you were to access the pixel directly then")
print(img[2][2])
print("If it is 255 255 255 then i can say it is a white pixel")

print("If you want to see the single channel for example then what you can do is: ")
print(cv2.imshow('Image',img[:, :, 2])) # 0-2 is the channel number
cv2.waitKey(0)

print("Another property that you can use in numpy array is size it will print total no of pixels in image")
print(img.size)