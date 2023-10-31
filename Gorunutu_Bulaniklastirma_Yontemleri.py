import cv2

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow("Capture", frame)

    # GaussianBlur
    gaussianB = cv2.GaussianBlur(frame, (7,7), 0)
    cv2.imshow("Gaussian Blur", gaussianB)

    # MedianBlur
    medianB = cv2.medianBlur(frame, 9) # 9 bulanıklık derecesini ifade eder
    cv2.imshow("Median Blur", medianB)
    
    # BilateralFilter
    bilateral = cv2.bilateralFilter(frame, 9, 75, 75)
    cv2.imshow("Bilateral Filter", bilateral)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()