import cv2 
import numpy as np
kernel = np.ones((5,5),np.uint8)
print(kernel)
path = "C:/Users/Hari Naidu/OneDrive/Pictures/3307522.jpg"
img =cv2.imread(path)
cv2.imshow("original image",img)
cv2.waitKey(0)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale",imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()
