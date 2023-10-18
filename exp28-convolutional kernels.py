import cv2
import numpy as np
img = cv2.imread("C:/Users/Hari Naidu/Desktop/POM/computer vision/col.jpg", 
cv2.IMREAD_GRAYSCALE)
dx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
dy = cv2.Sobel(img, cv2.CV_64F, 0, 1)
edges = cv2.magnitude(dx, dy)
thresh = 100
edges[edges < thresh] = 0
edges[edges >= thresh] = 255
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
import numpy as np
image_path = "C:/Users/Hari Naidu/Desktop/POM/computer vision/col.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
gradient_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
gradient_magnitude = np.uint8(gradient_magnitude)
cv2.imshow('Original Image', image)
cv2.imshow('Gradient Magnitude (Boundary Detection)', gradient_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()
