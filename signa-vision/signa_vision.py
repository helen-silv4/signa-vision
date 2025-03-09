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

while True:
    sucesso, img = webcam.read()
    img =  cv2.flip(img, 1)
    
    cv2.imshow('SignaVision', img)
    
    letra = cv2.waitKey(1)
    if letra == 27:
        break