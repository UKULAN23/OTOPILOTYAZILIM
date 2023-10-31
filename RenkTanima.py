import cv2
import numpy as np

# Kamerada görüntüyü alır 
cap = cv2.VideoCapture(1)

while True:
    #Kameradan sağlıklı olarak görüntü aldığında bu frame'leri frame değişkeni ile okuyup ret değişkeninde tutar  
    ret, frame = cap.read()
    # Aynalı görüntü olmaması için eksende düzellik.
    # Birinci parametre yansıma yapılacak değişken 
    # İkinci parametre yansımanın yapılacağı ekseni ifade eder
    frame = cv2.flip(frame, 1)

    # Renk değerleri RGB formatında değil HSV formatında alınacak 
    # Frame den alınan
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı için renk aralığı
    lower_red = np.array([170,50,50])
    upper_red = np.array([180,255,255])
    # Birinci parametredekdi değişken için sadece ikinci ve üçüncü parametre aralığında verilen renkleri gösterecek
    red_mask = cv2.inRange(hsv_frame, lower_red, upper_red)
    # Maskelenen alaının nesnenin renginde gözükmesi için bitwise_and ile karşılaştırıp red olarak döndürürü 
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

    # Kontur tespiti yapılır
    contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Konturun etrafına bir dikdörtgen çizilir
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Capture için şekil işaretleme 
        cv2.rectangle(red, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Red Mask için şekil işaretleme 

    # Yakalanan frameler ekranda imshow ile gösterilir. 
    # İlk parametre pencere ismi ikinci paramaetre ekranda gösterilecek değerdir. 
    cv2.imshow("Capture", frame)
    # Maskelenen alana beyaz gözükür 
    #cv2.imshow("Mask", red_mask)
    cv2.imshow("Red Mask", red)

    # waitkey ile 1 ms beklerve q tuşuna basılınca döngüden çıkıp program durdurulur.
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

# Donanımı serbest bırakır 
cap.release()
# Tüm pencerleri kapar
cv2.destroyAllWindows()