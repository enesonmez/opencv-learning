import cv2


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv2.rectangle(frame, (100,200), (150,100), (0,0,255), 2)

    cv2.imshow("camera",frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()