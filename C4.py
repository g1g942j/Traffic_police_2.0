import numpy as np
import cv2 as cv
img = cv.imread('/home/user/Загрузки/Telegram Desktop/Screenshot_2021-08-19 OpenCV pptx pdf(1).png')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 125, 255, cv.THRESH_BINARY)
contours, hirerarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours (img, contours, 0, (0,255,0), 3)
cv.imshow('s', thresh)
#cv.imshow('q', img)
cv.waitKey(0)