import cv2
from matplotlib import pyplot as plt
import numpy as np

# import direto em Gray
img = cv2.imread("assets/abeia.jpg", 0)
plt.imshow(img, cmap="gray")
# Imagem original em Gray
plt.show()


# dilatacao/borrao de 5 pixels na imagem
kernel = np.ones((5,5), np.uint8)
dilation = cv2.dilate(img, kernel, iterations=1)
# Utizar cmap em toda imagem Gray para melhor visualizacao
plt.imshow(dilation, cmap="gray")
# Imagem borrada em Gray
plt.show()


# ou
img_blur = cv2.blur(img, (5,5))
plt.imshow(img_blur, cmap="gray")
plt.show()