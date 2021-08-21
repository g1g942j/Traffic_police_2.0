import cv2 as cv
import numpy as np
img = cv.imread('/home/user/Загрузки/Telegram Desktop/Screenshot_2021-08-19 OpenCV pptx pdf.png')
edge = cv.Canny(img, 50, 150)
rho_accuracy = 1
theta_accuracy = np.pi/180
min_length = 200
lines = cv.HoughLines(edge, rho_accuracy, theta_accuracy, min_length)
for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv.imshow('3', img)
cv.waitKey(0)
