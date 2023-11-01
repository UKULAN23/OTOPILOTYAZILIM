import cv2
import numpy as np

# Kamerada görüntüyü alır 
cap = cv2.VideoCapture(0)

# Kameranın görüş açısı (derece cinsinden)
viewing_angle_degrees = 60

# Piksel uzunluğunu santimetre cinsine dönüştürmek için kullanılan dönüşüm faktörü
conversion_factor = 10  # 1 cm'yi kaç piksel olarak görmek istediğinizi belirleriz.

while True:

    #Kameradan sağlıklı olarak görüntü aldığında bu frame'leri frame değişkeni ile okuyup ret değişkeninde tutar  
    ret, frame = cap.read()
    # Aynalı görüntü olmaması için eksende düzellik
    # Birinci parametre yansıma yapılacak değişken 
    # İkinci parametre yansımanın yapılacağı ekseni ifade eder
    frame = cv2.flip(frame, 1)
    
    # Gürültü azaltmak için blur 
    #frame = cv2.bilateralFilter(frame, 9, 75, 75)
    #frame = cv2.GaussianBlur(frame, (7,7), 8)
    #frame = cv2.medianBlur(frame, 9)
    
    # Renk değerleri RGB formatında değil HSV formatında alınacak 
    # Frame den alınan
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı için renk aralığı
    lower_red = np.array([170, 50, 50])
    upper_red = np.array([180, 255, 255])

    # Birinci parametredekdi değişken için sadece ikinci ve üçüncü parametre aralığında verilen renkleri gösterecek
    red_mask = cv2.inRange(hsv_frame, lower_red, upper_red)
    # Maskelenen nesnenin kendi renginde gözükmesi için bitwise_and ile karşılaştırıp red olarak döndürürü 
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

    # Kontur tespiti yapılır
    contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Ekrandan çizilen en büyük dikdörtgen tespit edilir
    largest_contour = None
    largest_contour_area = 0

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > largest_contour_area:
            largest_contour = contour
            largest_contour_area = area

    #Ekran merkezinden bulunan en büyük dikdörtgenden bir ok çizilir 
    if largest_contour is not None:
        x, y, w, h = cv2.boundingRect(largest_contour)

        rect_center_x = x + w // 2
        rect_center_y = y + h // 2

        w1, h1, c1 = frame.shape

        screen_center_x = h1 // 2
        screen_center_y = w1 // 2

        # Ok uzunluğu
        arrow_length = int(np.sqrt((screen_center_x - rect_center_x) ** 2 + (screen_center_y - rect_center_y) ** 2))
        arrow_length_cm = arrow_length / conversion_factor

        arrow_direction = (screen_center_x - rect_center_x, screen_center_y - rect_center_y) 

        # Capture penceresine çizdirir
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.arrowedLine(frame, (screen_center_x, screen_center_y), (rect_center_x, rect_center_y), (0, 255, 0), 2)

        # Red Mask penceresine çizdirir
        cv2.rectangle(red, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.arrowedLine(red, (screen_center_x, screen_center_y), (rect_center_x, rect_center_y), (0, 255, 0), 2)

        # Ok uzunluğunu ekranda ve "Red Mask" penceresinde yazdır
        text = f"Mesafe: {arrow_length_cm:.2f}"
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(red, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Ekran merkezindeki ana cizgiler ve kare
    cv2.rectangle(frame, ((h1 // 2 - 20), (w1 // 2 - 20)), ((h1 // 2 + 20), (w1 // 2 + 20)), (204, 0, 0), 2)
    cv2.line(frame, (h1 // 2, 0), (h1 // 2, w1), (204, 255, 255), 1)
    cv2.line(frame, (0, w1 // 2), (h1, w1 // 2), (204, 255, 255), 1)

    # Pencereleri görüntüler 
    cv2.imshow("Capture", frame)
    cv2.imshow("Red Mask", red)

    # waitkey ile 1 ms beklerve q tuşuna basılınca döngüden çıkıp program durdurulur.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Donanımı serbest bırakır 
cap.release()
# Tüm pencerleri kapar
cv2.destroyAllWindows()