import cv2

title = "Contour Detection"

# size limits for the contour area
amin, amax = 100, 10000

# contour color and stroke
ccolor = (255, 0, 0)
stroke = 3

def main():

	mode = 0
	modes = (drawAllContours, drawContours, drawCircles)

	camera = cv2.VideoCapture(0);

	# loop forever
	while True:

		# load image
		rval, image = camera.read()

		if image is not None:
			# thereshold image 
		    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		    ret, threshold_image = cv2.threshold(grayscale_image, 127, 255, 0)

		    # get contours
		    contours, hierarchy = cv2.findContours(threshold_image, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

		    # get one of the contour drawing functions
		    # drawingFunction = modes[mode]
		    drawAllContours(contours=contours, frame=image)

		    # apply the function
		    # drawingFunction(image, contours)

		    # show the image in the window
		    cv2.imshow(title, image)

		# handle keyboard events

		key = cv2.waitKey(1) & 0xFF 
		if key == 0xFF: # no key pressed
			continue
		elif key == 27: # "ESC" to quit
			break
		elif key == 32: # "SPACE" to switch modes
			mode = (mode + 1) % len(modes)
		else:
			print("key code: {}".format(key))


def drawAllContours(frame, contours, color=ccolor):
	""" draw all the contours """
	cv2.drawContours(frame, contours, -1, color, stroke)


def drawContours(frame, contours, minArea=amin, maxArea=amax, color=ccolor):
	""" only pick contours in a certain range """
	for i in range(len(contours)):
		if minArea < cv2.contourArea(contours[i]) < maxArea:
			cv2.drawContours(frame, (contours[i],), -1, color, stroke)


def drawCircles(frame, contours, minArea=amin, maxArea=amax, color=ccolor):
	""" draw the enclosing circles of the contours """
	for i in range(len(contours)):
		if minArea < cv2.contourArea(contours[i]) < maxArea:
			(x,y),radius = cv2.minEnclosingCircle(contours[i])
			center = (int(x), int(y))
			radius = int(radius)
			cv2.circle(frame,center,radius, color, stroke)

if __name__ == "__main__":
	main()
