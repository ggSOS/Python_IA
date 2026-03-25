import cv2
import numpy as np

cap = cv2.VideoCapture(0) # utiliza a webcam padrão do sistema
img1 = cv2.imread('chrome.jpg',0)

# inicializa com o construtor ORB
orb = cv2.ORB_create()

# cria a janela com tamanho 1024x768
cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Original', (1024, 768))

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    # Redimensiona o frame para uma resolução menor (metade da largura e altura original)
    #frame = cv2.resize(frame, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_AREA)
    
    # calcula os keypoints e descritores do frame capturado
    kp1, des1 = orb.detectAndCompute(img1,None)
    
    # calcula os keypoints e descritores da imagem de referência
    kp2, des2 = orb.detectAndCompute(frame,None)

    gray1 = cv2.drawKeypoints(img1, kp1, outImage=np.array([]), flags=0)
    gray2 = cv2.drawKeypoints(frame, kp2, outImage=np.array([]), flags=0)

    # cria o objeto bf (best featuare)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # a função match devolve os matches encontrados
    if des1 is not None and des2 is not None:
        matches = bf.match(des1, des2)
    else:
        print("Warning: One of the descriptors is empty. Skipping match.")

    print("Foram encontrados: {} matches".format(len(matches)))

    # ordenamos o vetor matches para ficar os melhores (menor distancia) no inicio da lista
    matches = sorted(matches, key = lambda x:x.distance)

    ## matches[:15] menor aumenta confianca
    img3 = cv2.drawMatches(img1,kp1,frame,kp2,matches[:10],None, flags=2)

    cv2.imshow('Original',img3)
    
    ## waitKey menor acelera o processamento
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
