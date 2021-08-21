import cv2
import cv2 as cv
img = cv.imread('/home/user/Загрузки/Telegram Desktop/Screenshot_2021-08-19 OpenCV pptx pdf.png')
img1 = cv.imread('/home/user/Загрузки/Telegram Desktop/Screenshot_2021-08-19 OpenCV pptx pdf(1).png')
#hsv = cv.cvtColor(img1, cv.COLOR_BGR2HSV)
#cv.imshow('RGB', img1)
#cv.waitKey(0)
#cv.imshow('HSV', hsv)
#cv.waitKey(0)
res_img = cv2.resize(img1,(2, 1), cv2.INTER_NEAREST)
#cv.imshow('sad', res_img)
print('Done')
#cv.waitKey(0)
#cv.destroyAllWindows()
scrop_img = img1[10:411, 45:209]
#cv.imshow('e', scrop_img)
#cv.waitKey(0)
#cv.destroyAllWindows()

(h, w) = img1.shape[:2]
center = (int(w/2), int(h/2))
rotat = cv2.getRotationMatrix2D(center, -87, 0.5)
rotared = cv2.warpAffine(img1, rotat, (w, h))
#cv.imshow('1',rotared)
#cv.waitKey(0)
#cv.destroyAllWindows()

#cv2.imshow('1',out)

#cv.line(img1, (0, 0), (208,406), (0,0,0), 10)
#cv.circle(img1, (103, 201), 50, (0, 0, 255), 3)
#cv.imshow("write", img1)
#cv.waitKey(0)


