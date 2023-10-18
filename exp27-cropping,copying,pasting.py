import cv2
import numpy as np
image = cv2.imread("C:/Users/Hari Naidu/Desktop/POM/computer vision/col.jpg")
img2 = cv2.imread("C:/Users/Hari Naidu/Desktop/POM/computer vision/logo.jpg")
print(image.shape)
cv2.imshow("original", image)
imageCopy = image.copy()
cv2.circle(imageCopy, (100, 100), 30, (255, 0, 0), -1)
cv2.imshow('image', image)
cv2.imshow('image copy', imageCopy)
cropped_image = image[80:280, 150:330]
cv2.imshow("cropped", cropped_image)
cv2.imwrite("Cropped Image.jpg", cropped_image)
dst = cv2.addWeighted(image, 0.5, img2, 0.7,0)
img_arr = np.hstack((image, img2))
cv2.imshow('Input Images',img_arr)
cv2.imshow('Blended Image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
image_path ="C:/Users/Hari Naidu/Desktop/POM/computer vision/col.jpg"
image = cv2.imread(image_path)
x1, y1, x2, y2 = 100, 150, 400, 350
cropped_image = image[y1:y2, x1:x2]
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


