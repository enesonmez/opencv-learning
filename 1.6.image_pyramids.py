""" Resmi 2 kat büyütme veya 2 kat küçültme işlemleri için görüntü piramitleri kullanılmaktadır.
"""
import cv2


image = cv2.imread("img/lenna.png")

bigImage = cv2.pyrUp(image) # Orjinal görüntüyü iki katına çıkarır.
smallImage = cv2.pyrDown(image) # Orjinal görüntüyü iki kat küçültür.

print("Original : ",image.shape)
print("Big Image : ",bigImage.shape)
print("Small Image : ",smallImage.shape)

cv2.imshow("Original",image)
cv2.imshow("Big Image",bigImage)
cv2.imshow("Small Image",smallImage)

cv2.waitKey(0)
cv2.destroyAllWindows()