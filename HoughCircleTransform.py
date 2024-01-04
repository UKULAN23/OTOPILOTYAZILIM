"""

import cv2
import numpy as np

# Kameradan video yakalama işlemi
videoCapture = cv2.VideoCapture(0)
# Önceki dairenin konumunu tutacak değişken
prevCircle = None
# İki nokta arasındaki mesafeyi hesaplayan fonksiyon
dist = lambda x1, y1, x2, y2: (x1-x2)**2 + (y1-y2)**2

while True:
    ret, frame = videoCapture.read()
    if not ret: break

    # Kareyi gri tona dönüştür
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Gürültüyü azaltmak için Gaussian bulanıklaştırma uygula
    blurFrame = cv2.GaussianBlur(grayFrame, (7,7), 0)
    #blurFrame = cv2.medianBlur(grayFrame, 5)

    # Hough dönüşümleri ile daireleri bul
    circles = cv2.HoughCircles(blurFrame, cv2.HOUGH_GRADIENT, 1.2, 100, 
                              param1=100, param2=30, minRadius=70, maxRadius=400) #75, 400
    
    #circles = cv2.HoughCircles(medianBlur, cv2.HOUGH_GRADIENT, 1, 120, 
    #                          param1=100, param2=30, minRadius=0, maxRadius=0)
    
    if circles is not None:
        # Daireler varsa işleme al
        circles = np.uint16(np.around(circles))
        chosen = None

        # En uygun daireyi seç
        for i in circles[0, :]:
            if chosen is None: 
                chosen = i
            if prevCircle is not None:
                if dist(chosen[0], chosen[1], prevCircle[0], prevCircle[1]) <= dist(i[0], i[1], prevCircle[0], prevCircle[1]):
                        chosen = i  # Önceki dairenin konumunu güncelle
        
        # Seçilen daireyi çiz
        cv2.circle(frame, (chosen[0], chosen[1]), 1, (0, 100, 100), 3)
        cv2.circle(frame, (chosen[0], chosen[1]), chosen[2], (255, 0, 255), 3)
        prevCircle= chosen

    cv2.imshow("Circles", frame)
    cv2.imshow("Gray", blurFrame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
         break

videoCapture.release()
cv2.destroyAllWindows()


"""
import cv2
import numpy as np

# Kameradan video yakalama işlemi
videoCapture = cv2.VideoCapture(0)
# Önceki dairenin konumunu tutacak değişken
prevCircle = None
# İki nokta arasındaki mesafeyi hesaplayan fonksiyon
dist = lambda x1, y1, x2, y2: (x1-x2)**2 + (y1-y2)**2

while True:
    ret, frame = videoCapture.read()
    if not ret: break

    # Kareyi gri tona dönüştür
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Gürültüyü azaltmak için Gaussian bulanıklaştırma uygula
    blurFrame = cv2.GaussianBlur(grayFrame, (7,7), 0)
    #blurFrame = cv2.medianBlur(grayFrame, 5)

    # Hough dönüşümleri ile daireleri bul
    circles = cv2.HoughCircles(blurFrame, cv2.HOUGH_GRADIENT, 1.2, 100, 
                              param1=100, param2=20, minRadius=70, maxRadius=400) #75, 400
    
    """circles = cv2.HoughCircles(medianBlur, cv2.HOUGH_GRADIENT, 1, 120, 
                               param1=100, param2=30, minRadius=0, maxRadius=0)
    """
    if circles is not None:
        # Daireler varsa işleme al
        circles = np.uint16(np.around(circles))
        chosen = None

        # En uygun daireyi seç
        for i in circles[0, :]:
            if chosen is None: 
                chosen = i
            if prevCircle is not None:
                if dist(chosen[0], chosen[1], prevCircle[0], prevCircle[1]) <= dist(i[0], i[1], prevCircle[0], prevCircle[1]):
                        chosen = i  # Önceki dairenin konumunu güncelle
        
        # Seçilen daireyi çiz
        cv2.circle(frame, (chosen[0], chosen[1]), 1, (0, 100, 100), 3)
        cv2.circle(frame, (chosen[0], chosen[1]), chosen[2], (255, 0, 255), 3)
        prevCircle= chosen

    cv2.imshow("Circles", frame)
    cv2.imshow("Gray", blurFrame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
         break

videoCapture.release()
cv2.destroyAllWindows()


