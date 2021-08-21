import cv2
import cv2 as cv
import numpy as np
img = cv.imread('/home/user/Загрузки/Telegram Desktop/Screenshot_2021-08-19 OpenCV pptx pdf.png',0)
img1 = cv.imread('/home/user/Загрузки/Telegram Desktop/Screenshot_2021-08-19 OpenCV pptx pdf(1).png')
#ret, thresh1 = cv.threshold (img, 127, 255, cv.THRESH_TRUNC)
thresh1 = cv.Canny(img, 100, 200)
ret, thresh2 = cv.threshold (img1, 127, 255, cv.THRESH_TOZERO_INV)
#cv.imshow('g',thresh1)
#cv.waitKey(0)
#cv.imshow('w',thresh2)
#cv.waitKey(0)
#cv.imwrite('filename', img1)
hsv = cv.cvtColor(img1, cv.COLOR_BGR2HSV)
lower_orange = np.array([7,50,50])
upper_orange = np.array([13,255,255])
mask = cv.inRange(hsv, lower_orange, upper_orange)
res = cv.bitwise_and(hsv,hsv, mask= mask)
cv.imshow('a', res)
cv.imshow('q', img1)
cv.waitKey(0)


