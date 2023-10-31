import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.medianBlur(frame, 9)
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
            largest_contour_area = area
            largest_contour = contour

    if largest_contour is not None:
        x, y, w, h = cv2.boundingRect(largest_contour)
        center_x = x + w // 2
        center_y = y + h // 2

        w1, h1, c1 = frame.shape

        # Merkezden en büyük yeşil kutuya ok çizme
        cv2.arrowedLine(frame, (h1 // 2, w1 // 2), (center_x, center_y), (0, 255, 0), 2)

    cv2.line(frame, (h1 // 2, 0), (h1 // 2, w1), (204, 255, 255), 1)
    cv2.line(frame, (0, w1 // 2), (h1, w1 // 2), (204, 255, 255), 1)
    cv2.imshow("Capture", frame)
    cv2.imshow("Red Mask", red)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()