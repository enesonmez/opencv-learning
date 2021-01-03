import cv2
import numpy as np


image = cv2.imread("img/lenna.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imageBlur = cv2.GaussianBlur(gray,(3,3),0)


def autoCanny(image, sigma=0.33):
    median = np.median(image)
    print(median)
    lower = int(max(0,(1.0 - sigma)*median))
    upper = int(min(255, (1.0+sigma)*median))
    cannyEdge = cv2.Canny(image,lower,upper)

    return cannyEdge


wide = cv2.Canny(imageBlur,20,200)
tight = cv2.Canny(imageBlur,200,220)
auto = autoCanny(imageBlur)


cv2.imshow("blur image",imageBlur)
cv2.imshow("canny edge image",np.hstack([wide,tight,auto]))

cv2.waitKey(0)
cv2.destroyAllWindows()