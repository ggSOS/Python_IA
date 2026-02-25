import cv2
from matplotlib import pyplot as plt
import numpy as np

# import direto em Gray
img = cv2.imread("assets/abeia.jpg", 0)
plt.imshow(img, cmap="gray")
plt.title("Imagem Original")
# Imagem original em Gray
plt.show()


# dilatacao/borrao de 5 pixels na imagem
kernel = np.ones((5,5), np.uint8)
# priorizar matrizes impares
# maior a matriz = maior o borrao
dilation = cv2.dilate(img, kernel, iterations=1)


# contorno da imagem
dlt = dilation - img
# Utizar cmap em toda imagem Gray para melhor visualizacao
plt.imshow(dilation, cmap="gray")
plt.title("Imagem Borrada/Dilatada")
# Imagem borrada em Gray
plt.show()


# Utizar cmap em toda imagem Gray para melhor visualizacao
plt.imshow(dlt, cmap="gray")
plt.title("Contornos da Imagem")
# Contorno da imagem em Gray
plt.show()