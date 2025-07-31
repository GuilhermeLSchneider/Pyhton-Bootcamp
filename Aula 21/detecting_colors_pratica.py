import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # H (Hue): matiz (0 a 179 no OpenCV) – define o tipo de cor (vermelho, verde, azul, etc.)
    # S (Saturation): saturação (0 a 255) – quão intensa está a cor (0 = cinza, 255 = cor vibrante)
    # V (Value): valor (0 a 255) – quão claro ou escuro está (0 = preto, 255 = mais claro possível)
    
    # Define outro intervalo para detectar o azul
    lower_blue = np.array([100, 50, 0])
    high_blue = np.array([140, 255, 255])
    mask_blue = cv2.inRange(hsv_frame, lower_blue, high_blue)
    blue = cv2.bitwise_and(frame, frame, mask=mask_blue)
    
    # Detecta a cor verde
    lower_green = np.array([40, 0, 0])
    higher_green = np.array([80, 255, 255])
    mask_green = cv2.inRange(hsv_frame, lower_green, higher_green)
    green = cv2.bitwise_and(frame, frame, mask=mask_green)
    
    # Detecta apenas as cores verde e azul, ignorando o vermelho
    mask_combined = cv2.bitwise_or(mask_blue, mask_green)
    combined_colors = cv2.bitwise_and(frame, frame, mask=mask_combined)
    
    # Utilizando o bitwise_not para inverter a máscara combinada
    mask_not = cv2.bitwise_not(mask_combined)
    not_colors = cv2.bitwise_and(frame, frame, mask=mask_not)
    
    # cv2.imshow("Original Frame", frame)
    # cv2.imshow("Blue Mask", blue)
    # cv2.imshow("Green Mask", green)
    # cv2.imshow("Combined Colors (Blue and Green)", combined_colors)
    cv2.imshow("NOT Colors (Blue and Green)", not_colors)
    
    key = cv2.waitKey(1)
    if key == 27:
        break