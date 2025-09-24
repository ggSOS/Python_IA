import cv2, dlib, numpy as np, pickle, os, time

PREDICTOR = "shape_predictor_5_face_landmarks.dat"
RECOG = "dlib_face_recognition_resnet_model_v1.dat"
DB_FILE = "db.pkl"
THRESH = 0.5
## menor = mais precisão de identificacao

db = pickle.load(open(DB_FILE,"rb")) if os.path.exists(DB_FILE) else {}
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(PREDICTOR)
rec = dlib.face_recognition_model_v1(RECOG)

time.sleep(2)

cap = cv2.VideoCapture(0)
validando = False
ultimo = 0
cooldown = 3

modelo_investidor = {
    "conservador": "Bem-vindo, investidor conservador! Focamos em investimentos de baixo risco para garantir sua segurança financeira.",
    "moderado": "Bem-vindo, investidor moderado! Vamos buscar um equilíbrio entre risco e retorno para alcançar bons resultados.",
    "agressivo": "Bem-vindo, investidor agressivo! Prepare-se para explorar oportunidades de alto risco com grandes potenciais de retorno!"
}

print("\t[e] = Cadastrar\n\t[v] = Validar ON/OFF\n\t[q] = Sair")

while True:
    ok, frame = cap.read()
    if not ok: break
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rects = detector(rgb, 0)
    ## maior para mais zoom/precisao, mas fica mais pesado

    for r in rects:
        shape = sp(rgb, r)
        chip = dlib.get_face_chip(rgb, shape)
        vec = np.array(rec.compute_face_descriptor(chip), dtype=np.float32)

        if validando and db:
            tipo_investidor, nome, dist = "Desconhecido", "Desconhecido", 999
            for n, (v, t) in db.items():
                d = np.linalg.norm(vec - v)
                if d < dist:
                    tipo_investidor, nome, dist = t, n, d
            if dist > THRESH:
                nome = "Desconhecido"

            if nome == "Desconhecido":
                frase_frame = f"{nome}(tipo não definido)"
            else:
                frase_frame = f"{nome}({tipo_investidor})"

            color = (0,255,0) if nome != "Desconhecido" else (0,0,255)
            cv2.rectangle(frame, (r.left(), r.top()), (r.right(), r.bottom()), color, 2)
            cv2.putText(frame, frase_frame, (r.left(), r.top()-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

            print(nome)
            if nome != "Desconhecido" and time.time()-ultimo > cooldown:
                print(modelo_investidor[tipo_investidor])

    cv2.imshow("Faces", frame)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'): break
    if k == ord('v'): validando = not validando
    if k == ord('e') and len(rects) == 1:
        nome = input("Nome para Cadastro:\n\t- ").strip()
        while not nome:
            print("\nNome Inválido!\n")
            nome = input("Nome para Cadastro:\n\t- ").strip()

        tipo_investidor = input("Tipo de investidor:\n-conservador\n-moderado\n-agressivo\n\t- ").strip().lower()
        while not tipo_investidor or tipo_investidor not in modelo_investidor.keys():
            print("\nTipo Inválido!\n")
            tipo_investidor = input("Tipo de investidor:\n-conservador\n-moderado\n-agressivo\n\t- ").strip().lower()
        
        db[nome] = (vec, tipo_investidor)
        pickle.dump(db, open(DB_FILE,"wb"))
        print(f"Salvo: {nome}\n")
            

cap.release()
cv2.destroyAllWindows()
