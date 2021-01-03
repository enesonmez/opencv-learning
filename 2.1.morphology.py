"""
    1) Dilation
    Genişletme anlamı vardır. Beyaz noktaları daha geniş bir hale getirir. Kesik alanları birleştiremede kullanılır.

    2) Erosion
    Dilation nın tam tersi beyaz noktaları daraltma işleminde kullanılır. Gürültüleri yok eder.

    3) Opening
    İlk önce erosion sonrasında dilation işlemi yapan bir yöntemdir.

    4) Closing
    İlk önce dilation sonrasında erosion işlemi yapan bir yöntemdir.

    5) Gradyan
    Dilation'dan erosion'ı çıkarırsanız gradyan yöntemine ulaşmış olursunuz.

    6) Tophat
    Opening ile orginal resmimiz arasındaki farktır.

    7) Blackhat
    Closing ile original resmimiz arasındaki farktır.

"""
import cv2
import numpy as np

image = cv2.imread("img/binary_noise.png")

kernel = np.ones((5,5), np.uint8)

dilation = cv2.dilate(image,kernel,iterations=2)
erosion = cv2.erode(image,kernel,iterations=1)

opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
gradyan = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("original", image)
cv2.imshow("dilation", dilation)
cv2.imshow("erosion", erosion)
cv2.imshow("opening", opening)
cv2.imshow("closing", closing)
cv2.imshow("gradyan", gradyan)
cv2.imshow("blackhat", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()