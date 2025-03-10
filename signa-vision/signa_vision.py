# bibliotecas
import cv2
import mediapipe as mp
import numpy as np

# detecção das mão e coordenadas
mp_maos = mp.solutions.hands
mp_desenhos = mp.solutions.drawing_utils

maos = mp_maos.Hands()

# configuração da webcam
resolucao_x = 1280
resolucao_y = 720

webcam = cv2.VideoCapture(0)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, resolucao_x)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, resolucao_y)

# constantes
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (255, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (0, 0, 255)
AZUL_CLARO = (255, 255, 0)

# variáveis
img_quadro = np.ones((resolucao_y, resolucao_x, 3), np.uint8) * 255
cor_pincal = (255, 0, 0)
espessura_pincel = 7
x_quadro, y_quadro = 0, 0

# função para encontrar as coordenadas
def encontra_coordenas_maos(img, lado_invertido = False):   
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    resultado = maos.process(img_rgb)
    
    todas_maos = []
    
    if resultado.multi_hand_landmarks:
        for lado_mao, pontos_maos in zip(resultado.multi_handedness, resultado.multi_hand_landmarks):
            info_mao = {}
            
            coordenadas = []
            
            #print(pontos_maos)
            
            for ponto in pontos_maos.landmark:
                coord_x = int(ponto.x * resolucao_x)
                coord_y = int(ponto.y * resolucao_y)
                coord_z = int(ponto.z * resolucao_x)
                
                #print(coord_x, coord_y, coord_z)
                
                coordenadas.append((coord_x, coord_y, coord_z))
                
            #print(coordenadas)
                
            info_mao['coordenadas'] = coordenadas   
            
            if lado_invertido:
                if lado_mao.classification[0].label == 'Left':
                    info_mao['lado'] = 'Right'
                else: 
                    info_mao['lado'] = 'Left'
            else: 
                info_mao['lado'] = lado_mao.classification[0].label
            
            todas_maos.append(info_mao)
            
            #print(todas_maos)
           
            mp_desenhos.draw_landmarks(img, pontos_maos, mp_maos.HAND_CONNECTIONS) 
            
    return img, todas_maos

# função para verificar dedos levantados
def dedos_levantados(mao):
    dedos = []
    
    if mao['lado'] == 'Right':
        if mao['coordenadas'][4][0] < mao['coordenadas'][3][0]:
            dedos.append(True)
        else:
            dedos.append(False)
    else:
        if mao['coordenadas'][4][0] > mao['coordenadas'][3][0]:
            dedos.append(True)
        else:
            dedos.append(False)
        
    for ponta_dedo in [8, 12, 16, 20]:
        if mao['coordenadas'][ponta_dedo][1] < mao['coordenadas'][ponta_dedo - 2][1]:
            dedos.append(True)
        else:
            dedos.append(False)
    
    return dedos
    
while True:
    sucesso, img = webcam.read()
    img = cv2.flip(img, 1)
    
    img, todas_maos = encontra_coordenas_maos(img)
    
    # verifica se há duas mãos levantadas
    if len(todas_maos) == 2:       
        info_dedos_mao1 = dedos_levantados(todas_maos[0])
        info_dedos_mao2 = dedos_levantados(todas_maos[1]) 
        
        indicador_x, indicador_y, indicador_z = todas_maos[0]['coordenadas'][8] 
        
        # uma das mãos escolhe a cor do pincel
        if sum(info_dedos_mao2) == 1:
            cor_pincal = AZUL
        elif sum(info_dedos_mao2) == 2:
            cor_pincal = VERDE
        elif sum(info_dedos_mao2) == 3:
            cor_pincal = VERMELHO
        elif sum(info_dedos_mao2) == 4:
            cor_pincal = AZUL_CLARO
        elif sum(info_dedos_mao2) == 5:
            cor_pincal = BRANCO # borracha
        else:
            # caso a mão esteja fechada o quadro volta ao estado inicial
            img_quadro = np.ones((resolucao_y, resolucao_x, 3), np.uint8) * 255 
            
        cv2.circle(img, (indicador_x, indicador_y), espessura_pincel, cor_pincal, cv2.FILLED) # pincel
        
        # espessura do pincel com base na distância
        espessura_pincel = (int(abs(indicador_z)) // 3) + 5
        if indicador_z < -40:
            espessura_pincel = 30
        elif indicador_z <= -30:
            espessura_pincel = 20
        else:
            espessura_pincel = 10
                                 
    cv2.imshow('SignaVision', img)
    
    letra = cv2.waitKey(1)
    if letra == 27:
        break    