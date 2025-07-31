import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # H (Hue): matiz (0 a 179 no OpenCV) – define o tipo de cor (vermelho, verde, azul, etc.)
    # S (Saturation): saturação (0 a 255) – quão intensa está a cor (0 = cinza, 255 = cor vibrante)
    # V (Value): valor (0 a 255) – quão claro ou escuro está (0 = preto, 255 = mais claro possível)
    
    # Define um intervalo de cor para detectar vermelho
    lower_red = np.array([0, 100, 100])
    higher_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv_frame, lower_red, higher_red) # Cria uma máscara para a cor vermelha
    red = cv2.bitwise_and(frame, frame, mask=mask) # Aplica a máscara ao frame original para isolar a cor vermelha
    
    # Define outro intervalo para detectar o azul
    lower_blue = np.array([100, 150, 0])
    high_blue = np.array([140, 255, 255])
    mask_blue = cv2.inRange(hsv_frame, lower_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=mask_blue)
    
    # Detecta a cor verde
    lower_green = np.array([40, 100, 100])
    higher_green = np.array([80, 255, 255])
    mask_green = cv2.inRange(hsv_frame, lower_green, higher_green)
    green = cv2.bitwise_and(frame, frame, mask=mask_green)
    
    # Detectando cores exceto branco
    lower_white = np.array([0, 42, 0])
    higher_white = np.array([179, 255, 255])
    mask_white = cv2.inRange(hsv_frame, lower_white, higher_white)
    white = cv2.bitwise_and(frame, frame, mask=mask_white)
    
    # cv2.imshow("Original Frame", frame)
    # cv2.imshow("Red Mask", red)   
    # cv2.imshow("Blue Mask", blue)
    cv2.imshow("Green Mask", green)
    # cv2.imshow("White Mask", white)
    
    key = cv2.waitKey(1)
    if key == 27:
        break