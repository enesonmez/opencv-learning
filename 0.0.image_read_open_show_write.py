import cv2
import numpy as np

path = "img/lenna.png"

image = cv2.imread(path) # resmi okur. 
imageGray = cv2.imread(path, 0) # ikinci parametre olarak 0 verirsek resmi griye çevirir.

cv2.imwrite("img/grayLenna.png",imageGray) # resmi kaydeder.

cv2.imshow("Gray Lenna", imageGray) # gri resmi gösterir.
cv2.imshow("Lenna", image) # resmi gösterir.
cv2.waitKey(0) # Bir tuşa basıldığında program kapatılır.
cv2.destroyAllWindows() # opencv'ye bağlı pencereyi kapatır.