import cv2
from matplotlib import pyplot as plt
import numpy as np

## Atalho
img = cv2.imread('assets/coins.png',0)
img = cv2.medianBlur(img,9)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=40,
                           minRadius=75,maxRadius=90)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)

plt.imshow(cimg)
plt.show()