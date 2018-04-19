import numpy as np 
import cv2 

cap = cv2.VideoCapture(0)

global frame

color = (0, 255, 0)
line_width = 3
radius = 100
point = (0,0)

def click(event, x, y, flags, param):
	global point, pressed
	if event == cv2.EVENT_LBUTTONDOWN:
		print("Pressed", x, y)
		point = (x,y)


cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", click)

while(True):
	ret, frame = cap.read()
	frame = cv2.resize(frame, (0,0), fx=0.9, fy=0.9)
	cv2.circle(frame, point, radius, color, line_width)
	cv2.imshow("Frame", frame)

	ch = cv2.waitKey(1) # Run every q mimisec

	if ch & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()