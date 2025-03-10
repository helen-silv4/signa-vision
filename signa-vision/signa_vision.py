# bibliotecas
import cv2
import mediapipe as mp
import numpy as np
from time import sleep
from pynput.keyboard import Controller
from pynput.keyboard import Key
import os

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
teclas = [['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
          ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
          ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
          ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', ' ']]
offset = 50
tamanho_tecla = 50
contador = 0
texto = '>'
teclado = Controller()
bloco_notas = False

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

# função para imprimir os botões do teclado    
def imprime_botoes(img, posicao, letra, tamanho, cor_retangulo = BRANCO):
    cv2.rectangle(img, posicao, (posicao[0]+tamanho, posicao[1]+tamanho), cor_retangulo, cv2.FILLED) # retangulo
    cv2.rectangle(img, posicao, (posicao[0]+tamanho, posicao[1]+tamanho), AZUL, 1) # borda
    cv2.putText(img, letra, (posicao[0]+15, posicao[1]+30), cv2.QT_FONT_NORMAL, 1, PRETO, 2) # letra
    
    return img    
while True:
    sucesso, img = webcam.read()
    img = cv2.flip(img, 1)
    
    img, todas_maos = encontra_coordenas_maos(img)
    
    if len(todas_maos) == 1:
        info_dedos_mao1 = dedos_levantados(todas_maos[0])
        if todas_maos[0]['lado'] == 'Right':
            if info_dedos_mao1 == [False, True, False, False, True]: # fechamento do programa
               break
            
            if info_dedos_mao1 == [False, True, True, False, False] and bloco_notas == False:
                bloco_notas = True
                os.startfile(r'C:\Windows\system32\notepad.exe')
            elif info_dedos_mao1 == [False, False, False, False, False] and bloco_notas == True:
                bloco_notas = False
                os.system('TASKKILL /IM notepad.exe')
                
        elif todas_maos[0]['lado'] == 'Left':
            indicador_x, indicador_y, indicador_z = todas_maos[0]['coordenadas'][8]
            
            cv2.putText(img, f'Distancia webcam: {indicador_z}', (850, 50), cv2.QT_FONT_NORMAL, 1, BRANCO, 2)

            for indice_linha, linha_teclado in enumerate(teclas):
                for indice_coluna, letra in enumerate(linha_teclado):
                    if sum(info_dedos_mao1) <= 1:
                        letra = letra.lower()
                    img = imprime_botoes(img, (offset + (indice_coluna*(tamanho_tecla+30)), offset+(indice_linha*(tamanho_tecla+30))), letra, tamanho_tecla)
                    
                    # verifica se o dedo indicador está posicionado dentro da área da tecla 
                    if offset + (indice_coluna*(tamanho_tecla+30)) < indicador_x < 100+(indice_coluna*(tamanho_tecla+30)) and offset+(indice_linha*(tamanho_tecla+30)) < indicador_y < 100+(indice_linha*(tamanho_tecla+30)):
                        img = imprime_botoes(img, (offset + (indice_coluna*(tamanho_tecla+30)), offset+(indice_linha*(tamanho_tecla+30))), letra, tamanho_tecla, cor_retangulo = VERDE) 
                        if indicador_z < -85:
                            contador = 1
                            escreve = letra
                            img = imprime_botoes(img, (offset + (indice_coluna*(tamanho_tecla+30)), offset+(indice_linha*(tamanho_tecla+30))), letra, tamanho_tecla, cor_retangulo = AZUL_CLARO)     
            
            # o texto só é escrito quando o dedo for retirado e o contador retorne ao valor 0
            if contador:
                contador += 1
                if contador == 3:
                    texto += escreve 
                    contador = 0 
                    # comando para digitar no em qualquer programa do computador
                    teclado.press(escreve)
            
            # apagar letra com o dedo mindinho        
            if info_dedos_mao1 == [False, False, False, False, True] and len(texto) > 1:
               texto = texto[:-1] # apaga o último digito
               teclado.press(Key.backspace) # apaga com a tecla backspace do teclado em qualquer outro programa
               sleep(0.15)
                   
            # mostrar texto na tela        
            cv2.rectangle(img, (offset, 450), (830, 500), BRANCO, cv2.FILLED) # retangulo
            cv2.rectangle(img, (offset, 450), (830, 500), AZUL, 1) # borda
            cv2.putText(img, texto[-40:], (offset, 480), cv2.QT_FONT_NORMAL, 1, PRETO, 2) # texto
            
            # circulo sobreposto
            cv2.circle(img, (indicador_x, indicador_y), 7, AZUL, cv2.FILLED)
                
    # verifica se há duas mãos levantadas
    elif len(todas_maos) == 2:       
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
            
        # desenha na tela só se o indicador estiver levantado
        if info_dedos_mao1 == [False, True, False, False, False]:
            if x_quadro == 0 and y_quadro == 0: 
               x_quadro, y_quadro = indicador_x, indicador_y 
               
            # desenha a linha   
            cv2.line(img_quadro, (x_quadro, y_quadro), (indicador_x, indicador_y), cor_pincal, espessura_pincel)
            
            # atualiza as coordenadas do ponto inicial
            x_quadro, y_quadro = indicador_x, indicador_y
        else:
            x_quadro, y_quadro = 0, 0 
        
        # função para sobrepor uma imagem na outra
        img = cv2.addWeighted(img, 1, img_quadro, 0.2, 0)
                    
    cv2.imshow('SignaVision', img)
    cv2.imshow('Quadro', img_quadro)
    
    letra = cv2.waitKey(1)
    if letra == 27:
        break    

cv2.imwrite('quadro.png', img_quadro)

# armazenando o texto digitado em um arquivo    
with open ('texto.txt', 'w') as arquivo:
    arquivo.write(texto)