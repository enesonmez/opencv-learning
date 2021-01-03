import cv2

image = cv2.imread("img/adile_nasit.jpg")

mirrorImage = cv2.copyMakeBorder(image,125,125,50,50,cv2.BORDER_REFLECT)
stretchImage = cv2.copyMakeBorder(image,100,100,60,60,cv2.BORDER_REPLICATE)
repeatImage = cv2.copyMakeBorder(image,100,100,100,100,cv2.BORDER_WRAP)
frameImage = cv2.copyMakeBorder(image,50,50,50,50,cv2.BORDER_CONSTANT,value=(125,65,196)) # value vermezsek siyah çerçeve olur.

cv2.imshow("aynalanan adile nasit",mirrorImage)
cv2.imshow("uzatilan adile nasit",stretchImage)
cv2.imshow("tekrarlanan adile nasit",repeatImage)
cv2.imshow("cerceveli adile nasit",frameImage)
cv2.waitKey(0)
cv2.destroyAllWindows()