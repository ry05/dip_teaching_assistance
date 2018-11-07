import numpy as np
import matplotlib.pyplot as plt
import cv2

#Gray Image
img = cv2.imread("C:\\Users\\Ramshankar Yadhunath\\Desktop\\tiger.jpg",1)

imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray Image',imggray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Gray Image
img = cv2.imread("C:\\Users\\Ramshankar Yadhunath\\Desktop\\tiger.jpg",1)

imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('HSV Image',imghsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Thresholding

# First, convert the given image into grayscale

img = cv2.imread("C:\\Users\\Ramshankar Yadhunath\\Desktop\\tiger.jpg",0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

