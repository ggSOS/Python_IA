import cv2
from matplotlib import pyplot as plt
import numpy as np


img = cv2.imread("assets/lambari.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

img_blur = cv2.blur(img, (3,3))
plt.imshow(img_blur)
plt.show()

img_canny = cv2.Canny(img_blur, 100, 200)
## threshold menor
## threshold maior
### If the edges are too noisy, increase the thresholds
### If edges are missing, decrease them
### A common practice is setting the upper threshold 2-3 times higher than the lower threshold
plt.imshow(img_canny, cmap="gray")
plt.show()