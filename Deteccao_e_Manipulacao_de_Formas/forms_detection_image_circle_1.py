import cv2
from matplotlib import pyplot as plt
import numpy as np


img = cv2.imread("assets/coins.png")
## BGR -> RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
## RGB -> cinza
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


## Deteccao de circulos
edges = cv2.Canny(img_gray, 50, 100)
circles = cv2.HoughCircles(edges, method=cv2.HOUGH_GRADIENT, dp=1,
                           minDist=80, param1=10, param2=30, minRadius=70, maxRadius=90)
#dp - maior detecta bordas mais tênues
#minDist - distancia minima entre circulos
#minRadius - tamanho minimo do raio do circulo
#maxRadius - tamanho minimo do raio do circulo


## cinza -> RGB
bordas_rgb = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
output = bordas_rgb


## Desenho dos circulos baseado nas informacoes coletadas
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(output, (i[0], i[1]), i[2], (0, 0, 255), 5)
        cv2.circle(output, (i[0], i[1]), 2, (255, 0, 0), 5)


## Plot
plt.imshow(output, cmap="gray")
plt.show()