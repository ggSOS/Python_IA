import cv2
from matplotlib import pyplot as plt

# import direto em Gray
img = cv2.imread("assets/abeia.jpg", 0)
plt.imshow(img, cmap="gray")
# Imagem original em Gray
plt.show()

# Borrao de 5 pixels na imagem
img_blur = cv2.blur(img, (5,5))
plt.imshow(img_blur, cmap="gray")
plt.show()