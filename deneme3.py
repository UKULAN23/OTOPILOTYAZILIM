import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Kameranın görüş açısı (derece cinsinden)
viewing_angle_degrees = 60

# Piksel uzunluğunu santimetre cinsine dönüştürmek için kullanılan dönüşüm faktörü
conversion_factor = 10  # Örnek: 1 cm'yi kaç piksel olarak görmek istediğinizi belirleyin

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.medianBlur(frame, 7)
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([170, 50, 50])
    upper_red = np.array([180, 255, 255])

    red_mask = cv2.inRange(hsv_frame, lower_red, upper_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)

    contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    largest_contour = None
    largest_contour_area = 0

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > largest_contour_area:
            largest_contour = contour
            largest_contour_area = area

    if largest_contour is not None:
        x, y, w, h = cv2.boundingRect(largest_contour)

        rect_center_x = x + w // 2
        rect_center_y = y + h // 2

        w1, h1, c1 = frame.shape

        screen_center_x = h1 // 2
        screen_center_y = w1 // 2

        arrow_length = int(np.sqrt((screen_center_x - rect_center_x) ** 2 + (screen_center_y - rect_center_y) ** 2))
        
        # Ok uzunluğunu santimetre cinsinden hesapla
        arrow_length_cm = arrow_length / conversion_factor

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.arrowedLine(frame, (rect_center_x, rect_center_y), (screen_center_x, screen_center_y), (0, 255, 0), 2)

        cv2.rectangle(red, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.arrowedLine(red, (rect_center_x, rect_center_y), (screen_center_x, screen_center_y), (0, 255, 0), 2)

        # Ok uzunluğunu ekrana yazdır
        cv2.putText(frame, f"Ok Uzunluğu: {arrow_length_cm:.2f} cm", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.rectangle(frame, ((h1 // 2 - 20), (w1 // 2 - 20)), ((h1 // 2 + 20), (w1 // 2 + 20)), (204, 0, 0), 2)
    cv2.line(frame, (h1 // 2, 0), (h1 // 2, w1), (204, 255, 255), 1)
    cv2.line(frame, (0, w1 // 2), (h1, w1 // 2), (204, 255, 255), 1)

    cv2.imshow("Capture", frame)
    cv2.imshow("Red Mask", red)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()