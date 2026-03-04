import cv2


vc = cv2.VideoCapture(0)

while True:
    ret, frame = vc.read()
    if not ret:
        break

    img_blur = cv2.blur(frame, (3,3))
    img_canny = cv2.Canny(img_blur, 50, 100)
    
    
    # Primeira Janela
    cv2.imshow("Original", frame)
    #Segunda Janela
    cv2.imshow("Com Filtro", img_canny)


    # Apertar ESC para finalizar programa
    if cv2.waitKey(1) & 0xFF == 27:
        break
vc.release()
cv2.destroyAllWindows()