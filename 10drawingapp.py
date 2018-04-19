import numpy as np 
import cv2

# Global variables
canvas = np.ones([500,500,3], 'uint8') * 255
radius = 3
color  = (0, 255, 0)
pressed = False

# click callback

def click(event, x, y, flags, params):
	global canvas, pressed
	if event == cv2.EVENT_LBUTTONDOWN:
		pressed = True
		# When the user clicks the mouse
		cv2.circle(canvas, (x , y), radius, color, -1) # -1 means fil circle completely
		cv2.rectangle(canvas,color)
		
	elif event == cv2.EVENT_MOUSEMOVE and pressed == True:
		cv2.circle(canvas, (x , y), radius, color, -1)

	elif event == cv2.EVENT_LBUTTONUP:
		# When mouse button is up
		pressed = False
		

# Window assignment and 

cv2.namedWindow("Canvas")
cv2.setMouseCallback("Canvas", click)

# Forever while loop

while(True):

	cv2.imshow("Canvas", canvas)

	#capture every 1ms
	ch = cv2.waitKey(1)
	if ch & 0xFF == ord('q'):
		break

	if ch & 0xFF == ord('b'):
		color = (255, 0, 0)

	if ch & 0xFF == ord('r'):
		color = (0, 0, 255)

	if ch & 0xFF == ord('g'):
		color = (0, 255, 0)


cv2.destroyAllWindows()