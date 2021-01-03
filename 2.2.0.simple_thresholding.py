import cv2

image = cv2.imread("img/lenna.png",0)

ret, thres1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY) # 127'nin altındaki değerleri 0, üstündekileri 255 yapar.
ret, thres2 = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV) # 127'nin altındaki değerleri 255, üstündekileri 0 yapar.
ret, thres3 = cv2.threshold(image,127,255,cv2.THRESH_TRUNC) # 127'den büyükse pixel 127 yapılır, değilse aynen bırakılır.
ret, thres4 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO) # 127'nin üzerndeyse pixel aynen bırakılır aksi takdirde 0 olur.
ret, thres5 = cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV) # 127'nin altındaysa aynen bırakılır aksi takdirde 0 olur.



cv2.imshow("original",image)
cv2.imshow("binary threshold", thres1)
cv2.imshow("binary inv threshold", thres2)
cv2.imshow("trunc threshold", thres3)
cv2.imshow("tozero threshold", thres4)
cv2.imshow("tozero inv threshold", thres5)

cv2.waitKey(0)
cv2.destroyAllWindows()