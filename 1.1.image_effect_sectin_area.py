import cv2


image = cv2.imread("img/lenna.png")

section = image[50:150,300:400] # 50 -150 arası satırları ve 300 - 400 arası sütunların kesiştiği alanları alır ve değişkene atar.

image[0:100,0:100] = section # aldığımız kesiti orjinal resimde bir yere kopyalayabiliyoruz.

image[:,:,0] = 255 # 0 yaparsak blue filtre uygular, 1 yaparsak green filtre uygular, 2 yaparsak red filtre uygular.
image[300:350,400:450] = (0,150,255) # belli bir alanı boyar.
image[255:280,240:380,1] = 255 # belli bir alana efekt uygular.

cv2.imshow("lenna",image)
cv2.waitKey(0)
cv2.destroyAllWindows()