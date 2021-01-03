""" Dikdörtgen oluşturabilmek için öncelikle sol alt köşe bulunur ve ardınadan sağ üst köşe bulunur.
    Bu iki nokayı bulursak kare veya dikdötgen çizebiliriz.
"""
import cv2
import numpy as np

image = np.zeros((400,600,3),dtype="uint8")


cv2.line(image, (0,0), (100,100), [0,0,255], 3) # çizginin başlangıç be bitiş konumları, renk, kalınlık
cv2.circle(image, (150,150), 25, [0,255,0], 2) # çemberin merkezi ve yarıçapı istenir.
cv2.rectangle(image,(200,100),(250,40),[0,0,255],3) # Noktalar (x,y) olarak belirtilmektedir. Renk ve border kalınlığı belirtilir.
cv2.putText(image,"Text", (200,200), cv2.FONT_HERSHEY_COMPLEX, 4, (255,0,0))

cv2.imshow("people",image)
cv2.waitKey(0)
cv2.destroyAllWindows()