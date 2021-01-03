"""
    Gürültülü resimlerde gürültüleri yok etmek için belli filtreler kullanılmaktadır.
    
    1) Mean Filtering
    3x3 lük matrisi resim üzerinde dolandırırız. 3x3'lük matriste yer alan değerlerin ortalamasını resimde 3x3'lük matrisin ortasına denk
    gelen piksele yazılır. Doğrural bir filtredir. filtre matirisini artırdıkça gürültüler azalır ancak görüntü kalitesi düşer.

    2) Median Filtering
    3x3 lük matrisi resmimiz üzerinde gezdiririz 9 karenin medyanını alırız ve resimin ortasına gelen piksele bu değeri yazarız. Doğrusal
    olmayan filtredir.

    3) Gauss Filtering
"""

import cv2

image = cv2.imread("img/noise_image.jpg")

meanFilter = cv2.blur(image,(3,3))
medianFilter = cv2.medianBlur(image, 3)
gaussFilter = cv2.GaussianBlur(image,(3,3),0)

cv2.imshow("noise", image)
cv2.imshow("mean filter", meanFilter)
cv2.imshow("median filter", medianFilter)
cv2.imshow("gauss filter", gaussFilter)
cv2.waitKey(0)
cv2.destroyAllWindows()