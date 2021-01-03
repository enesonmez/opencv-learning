import cv2

path = "img/lenna.png"

image = cv2.imread(path)


print(image[230,80]) # BGR olarak piksel değerini döndürür. [85 70 175]
print("image size : ", image.size)
print("image shape : ", image.shape)
print("image data type : ", image.dtype)

h, w, _ = image.shape

for i in range(w):
    image[50,i] = [255,255,255] # piksellere bgr değeri atayarak pikselin değerlerini değiştirebiliyoruz.

cv2.imshow("lenna",image) 

cv2.waitKey(0)
cv2.destroyAllWindows()