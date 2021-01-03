"""
    simple thresholding'ten farklı olarak belli bir aralık veriyoruz ve bu aralıklta resme göre kendi bir threshold değeri belirliyor
    ve onun üzerinden işlemlerini hallediyor.
"""

import cv2

"""
image = cv2.imread("img/lenna.png",0)

ret, otsu = cv2.threshold(image,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)


cv2.imshow("otsu", otsu)
cv2.waitKey(0)
"""

cap = cv2.VideoCapture(0)

# kameradan elde edilen görüntüye threshold uygulama
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    thres = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,4)
    #ret, thres = cv2.threshold(gray,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    cv2.imshow("video", thres)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows