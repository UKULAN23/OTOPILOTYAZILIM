"""
# Çemberler çizdirildi 
import cv2
import numpy as np

# Kameradan video yakalama işlemi
videoCapture = cv2.VideoCapture(0)

while True:
    ret, frame = videoCapture.read()
    if not ret:
        break

    # Kareyi gri tona dönüştür
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Gürültüyü azaltmak için Gaussian bulanıklaştırma uygula
    blurFrame = cv2.GaussianBlur(grayFrame, (5, 5), 0)

    # Canny kenar algılama ile kenarları belirle
    edges = cv2.Canny(blurFrame, 50, 150)

    # Kontur bulma
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            # Konturun içine en küçük çemberi oturt
            if len(contour) > 5:  # Çember çizebilmek için en az 5 nokta gerekli
                (x, y), radius = cv2.minEnclosingCircle(contour)
                center = (int(x), int(y))
                radius = int(radius)
                # Çemberin dış kenarını çiz
                cv2.circle(frame, center, radius, (0, 255, 0), 2)
                # Çemberin iç kenarını çiz (biraz daha küçük bir çember)
                inner_radius = int(radius * 0.8)  # İç çemberin yarıçapı dış çemberin %80'i kadar
                cv2.circle(frame, center, inner_radius, (0, 255, 0), 2)

    cv2.imshow("Circle Detection", frame)
    cv2.imshow("Edges", edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

videoCapture.release()
cv2.destroyAllWindows()
"""


"""
# CEMBERLER + MESAFE

import cv2
import numpy as np

# Kameradan video yakalama işlemi
videoCapture = cv2.VideoCapture(0)

while True:
    ret, frame = videoCapture.read()
    if not ret:
        break

    # Kareyi gri tona dönüştür
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Gürültüyü azaltmak için Gaussian bulanıklaştırma uygula
    blurFrame = cv2.GaussianBlur(grayFrame, (5, 5), 0)

    # Canny kenar algılama ile kenarları belirle
    edges = cv2.Canny(blurFrame, 50, 150)

    # Kontur bulma
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            # Konturun içine en küçük çemberi oturt
            if len(contour) > 5:  # Çember çizebilmek için en az 5 nokta gerekli
                (x, y), radius = cv2.minEnclosingCircle(contour)
                center = (int(x), int(y))
                radius = int(radius)
                # Çemberin dış kenarını çiz
                cv2.circle(frame, center, radius, (0, 255, 0), 2)
                # Çemberin iç kenarını çiz (biraz daha küçük bir çember)
                inner_radius = int(radius * 0.8)  # İç çemberin yarıçapı dış çemberin %80'i kadar
                cv2.circle(frame, center, inner_radius, (0, 255, 0), 2)
                
                # İç ve dış çemberler arasındaki mesafeyi hesapla
                distance_between_circles = radius - inner_radius
                # Mesafeyi ekrana yazdır
                cv2.putText(frame, f"Distance: {distance_between_circles}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow("Circle Detection", frame)
    cv2.imshow("Edges", edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

videoCapture.release()
cv2.destroyAllWindows()
"""


"""
# ÇEMBERLER + DIKDORTGEN

import cv2
import numpy as np

# Kameradan video yakalama işlemi
videoCapture = cv2.VideoCapture(0)

while True:
    ret, frame = videoCapture.read()
    if not ret:
        break

    # Kareyi gri tona dönüştür
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Gürültüyü azaltmak için Gaussian bulanıklaştırma uygula
    blurFrame = cv2.GaussianBlur(grayFrame, (5, 5), 0)

    # Canny kenar algılama ile kenarları belirle
    edges = cv2.Canny(blurFrame, 50, 150)

    # Kontur bulma
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            # Konturun içine en küçük çemberi oturt
            if len(contour) > 5:  # Çember çizebilmek için en az 5 nokta gerekli
                (x, y), radius = cv2.minEnclosingCircle(contour)
                center = (int(x), int(y))
                radius = int(radius)
                # Çemberin dış kenarını çiz
                cv2.circle(frame, center, radius, (0, 255, 0), 2)
                # Çemberin iç kenarını çiz (biraz daha küçük bir çember)
                inner_radius = int(radius * 0.8)  # İç çemberin yarıçapı dış çemberin %80'i kadar
                cv2.circle(frame, center, inner_radius, (0, 255, 0), 2)
                
                # İç ve dış çemberler arasındaki mesafeyi hesapla
                distance_between_circles = radius - inner_radius
                # Mesafeyi ekrana yazdır
                cv2.putText(frame, f"Distance: {distance_between_circles}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                
                # Çemberin dışına dikdörtgen çiz
                x1, y1 = int(x - radius), int(y - radius)
                x2, y2 = int(x + radius), int(y + radius)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv2.imshow("Circle Detection", frame)
    cv2.imshow("Edges", edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

videoCapture.release()
cv2.destroyAllWindows()
"""


"""
# BİRDEN FAZLA ÇEMBER TESPİTİ + MESAFE + DİKDÖRTGEN + ORTA NOKTA 
import cv2
import numpy as np

# Kameradan video yakalama işlemi
videoCapture = cv2.VideoCapture(0)

while True:
    ret, frame = videoCapture.read()
    if not ret:
        break

    # Kareyi gri tona dönüştür
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Gürültüyü azaltmak için Gaussian bulanıklaştırma uygula
    blurFrame = cv2.GaussianBlur(grayFrame, (5, 5), 0)

    # Canny kenar algılama ile kenarları belirle
    edges = cv2.Canny(blurFrame, 50, 150)

    # Kontur bulma
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            # Konturun içine en küçük çemberi oturt
            if len(contour) > 5:  # Çember çizebilmek için en az 5 nokta gerekli
                (x, y), radius = cv2.minEnclosingCircle(contour)
                center = (int(x), int(y))
                radius = int(radius)
                # Çemberin dış kenarını çiz
                cv2.circle(frame, center, radius, (0, 255, 0), 2)
                # Çemberin iç kenarını çiz (biraz daha küçük bir çember)
                inner_radius = int(radius * 0.8)  # İç çemberin yarıçapı dış çemberin %80'i kadar
                cv2.circle(frame, center, inner_radius, (0, 255, 0), 2)
                
                # İç ve dış çemberler arasındaki mesafeyi hesapla
                distance_between_circles = radius - inner_radius
                # Mesafeyi ekrana yazdır
                cv2.putText(frame, f"Distance: {distance_between_circles}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                
                # Çemberin dışına dikdörtgen çiz
                x1, y1 = int(x - radius), int(y - radius)
                x2, y2 = int(x + radius), int(y + radius)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                
                # Çemberin merkezine nokta ekle
                cv2.circle(frame, center, 5, (255, 0, 0), -1)

    cv2.imshow("Circle Detection", frame)
    cv2.imshow("Edges", edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

videoCapture.release()
cv2.destroyAllWindows()
"""


import cv2
import numpy as np

# Kameradan video yakalama işlemi
videoCapture = cv2.VideoCapture(0)

while True:
    ret, frame = videoCapture.read()
    if not ret:
        break

    # Kareyi gri tona dönüştür
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Gürültüyü azaltmak için Gaussian bulanıklaştırma uygula
    blurFrame = cv2.GaussianBlur(grayFrame, (5, 5), 0)

    # Canny kenar algılama ile kenarları belirle
    edges = cv2.Canny(blurFrame, 50, 150)

    # Ekranın genişlik ve yüksekliğini al
    height, width = frame.shape[:2]

    # Orta çizgileri çiz
    cv2.line(frame, (width // 2, 0), (width // 2, height), (255, 255, 0), 1)
    cv2.line(frame, (0, height // 2), (width, height // 2), (255, 255, 0), 1)

    # Kontur bulma
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            # Konturun içine en küçük çemberi oturt
            if len(contour) > 5:  # Çember çizebilmek için en az 5 nokta gerekli
                (x, y), radius = cv2.minEnclosingCircle(contour)
                center = (int(x), int(y))
                radius = int(radius)
                # Çemberin dış kenarını çiz
                cv2.circle(frame, center, radius, (0, 255, 0), 2)
                # Çemberin iç kenarını çiz (biraz daha küçük bir çember)
                inner_radius = int(radius * 0.8)  # İç çemberin yarıçapı dış çemberin %80'i kadar
                cv2.circle(frame, center, inner_radius, (0, 255, 0), 2)
                
                # İç ve dış çemberler arasındaki mesafeyi hesapla
                distance_between_circles = radius - inner_radius
                # Mesafeyi ekrana yazdır
                cv2.putText(frame, f"Distance: {distance_between_circles}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                
                # Çemberin dışına dikdörtgen çiz
                x1, y1 = int(x - radius), int(y - radius)
                x2, y2 = int(x + radius), int(y + radius)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                
                # Çemberin merkezine nokta ekle
                cv2.circle(frame, center, 5, (255, 0, 0), -1)

    cv2.imshow("Circle Detection", frame)
    cv2.imshow("Edges", edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

videoCapture.release()
cv2.destroyAllWindows()

