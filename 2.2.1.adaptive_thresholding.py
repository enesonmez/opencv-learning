""" 
    Küçük bir bölge için bir pikselin eşiği alınıyor ve bu resmin her bölgesi için yapılıyor.
    Mean => bölgenin ortalaması alınarak eşik değeri belirlenir.
    Gauss => bölgenin ağırlıklı toplamı alınarak eşik değeri belirlenir.
"""
import cv2

image = cv2.imread("img/lenna.png",0)

thresMean = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,23,8)
thresGauss = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,23,8)

cv2.imshow("adaptive mean", thresMean)
cv2.imshow("adaptive gauss", thresGauss)
cv2.waitKey(0)
cv2.destroyAllWindows()