import cv2
import numpy as np


vc = cv2.VideoCapture(0)

while True:
    ret, frame = vc.read()
    if not ret:
        break
    # Apertar ESC para finalizar programa
    if cv2.waitKey(1) & 0xFF == 27:
        break


    img_blur = cv2.blur(frame, (3,3))
    img_canny = cv2.Canny(img_blur, 50, 100)


    # BGR para HSV
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Intervalo de azul escuro em HSV
    ## H - cor mesmo - como metade de 210
    ## S - intensidade- em 50 por padrao
    ## V - luminosidade - em 50 por padrao
    lower_color = np.array([98, 50, 20])
    upper_color = np.array([128, 255, 100])
    # Mascara para isolar o azul
    mask_blue = cv2.inRange(frame_hsv, lower_color, upper_color)
    # Aplicar a mascara na imagem original
    result = cv2.bitwise_and(frame, frame, mask=mask_blue)
    
    
    # Primeira Janela
    cv2.imshow("Original", frame)
    # Segunda Janela
    cv2.imshow("Com Filtro de Borda", img_canny)
    # Terceira Janela
    cv2.imshow('Filtro Apenas Azul', result)

    
vc.release()
cv2.destroyAllWindows()