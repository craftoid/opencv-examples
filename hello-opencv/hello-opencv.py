import cv2
import numpy as np
from matplotlib import pyplot as plt

# use OpenCV to load the image
img = cv2.imread('python.jpg', 0)

# show image as plot
plt.imshow(img, cmap='gray', interpolation='bicubic')

# hide tick values on X and Y axis
plt.xticks([]), plt.yticks([]) 

# display the plot
plt.show()
