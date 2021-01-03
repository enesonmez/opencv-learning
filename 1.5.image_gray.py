import cv2

image = cv2.imread("img/adile_nasit.jpg")

imageGray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # Resmi griye çevirir.

cv2.imshow("original",image)
cv2.imshow("gray",imageGray)

cv2.waitKey(0)
cv2.destroyAllWindows()