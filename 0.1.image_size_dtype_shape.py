import cv2

path = "img/lenna.png"

image = cv2.imread(path)

print(image) # resmin rgb matrislerini bize döndürür.
print(image.size) # resmin width * height * 3 olarak size'ını döndürür.
print(image.dtype) # 8 bitlik int veri tipi kullanılır genellikle.
print(image.shape) # (yükseklik, genişlik, kanal sayısı) verir