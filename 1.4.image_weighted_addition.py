import cv2


image = cv2.imread("img/lenna.png")
image2 = cv2.imread("img/adile_nasit.jpg")

print(image[100,100])
print(image2[100,100])

cv2.imshow("lenna",image)
cv2.imshow("adile nasit",image2)
# Piksel değerlerini toplama
print(image[100,100] + image2[100,100])


adile_nasit = cv2.resize(image2,(400,400)) # resmi yeniden boyutlandırma
lenna = cv2.resize(image,(400,400))

# İki fotoğrafı piksel toplama yöntemi ile birleştirme (iki fotoğraf aynı size'da olmalı)
add = adile_nasit + lenna
cv2.imshow("pixel add",add)

# İki fotoğrafı add fonksiyonu ile birleştirme
func = cv2.add(adile_nasit, lenna)
cv2.imshow("add func",func)

# Belli oranlarla (ağırlıklarla) iki fotoğrafı birleştirme
func = cv2.addWeighted(adile_nasit, 0.3, lenna, 0.7, 0)
cv2.imshow("weighted add func",func)

cv2.waitKey(0)
cv2.destroyAllWindows()