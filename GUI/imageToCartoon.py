

# importing the required libraries
import cv2
import numpy as np 

# reading the image of png, jpg, jpeg format
img = cv2.imread("image_file_path.png")

# generating edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY, 9, 9)

# Cartonizing our image
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask = edges)

cv2.imshow("Image", img)
cv2.imshow("edges", edges)
cv2.imshow("Cartoonized Image", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()

