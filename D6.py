f = open('/home/user/Загрузки/Telegram Desktop/apriltagsDB.yaml', 'r')
f1 = []
f2 = []
import cv2 as cv
img1 = cv.imread('/home/user/Загрузки/Telegram Desktop/Screenshot_2021-08-19 OpenCV pptx pdf(1).png')
frame = cv.putText(img1,'Нарушение!!!', (10, 60), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 1)
cv.imshow('f',frame)
cv.waitKey(0)