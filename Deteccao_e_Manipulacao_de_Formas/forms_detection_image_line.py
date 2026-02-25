import cv2
from matplotlib import pyplot as plt
import numpy as np
import math


img = cv2.imread("assets/rua.png")
## BGR -> RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
## RGB -> cinza
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# plt.imshow(img_gray)
# plt.show()

## Destaque de Bordas
edges = cv2.Canny(img_gray,50,150)


lines = cv2.HoughLinesP(edges, 1, math.pi/180.0, np.array([]), threshold=95, minLineLength=10, maxLineGap=100)
# input image
# rho accuracy
# theta accuracy
# threshold - valor de certeza de linha
# np.array([])
# minLineLength - tamanho minimo em pixels da linha
# maxLineGap - tamanho maximo permitido entre linhas para agrupa-las

hough_img = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(hough_img, (x1, y1), (x2, y2), (255, 0, 255), 5)


plt.imshow(hough_img)
plt.show()