import apriltag
import cv2

print('[INFO] loading image...')
image = cv2.imread('/home/user/Загрузки/Telegram Desktop/photo_2021-08-20_11-33-09.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print('[INFO] detecting AprilTags...')
options = apriltag.DetectorOptions(families='tag36h11')
detector = apriltag.Detector(options)
results = detector.detect(gray)
print('[INFO] {} total AprilTags detected.'.format(len(results)))

for r in results:

    (ptA, ptB, ptC, ptD) = r.corners
    ptB = (int(ptB[0]), int(ptB[1]))
    ptC = (int(ptC[0]), int(ptC[1]))
    ptD = (int(ptD[0]), int(ptD[1]))
    ptA = (int(ptA[0]), int(ptA[1]))

    cv2.line(image, ptA, ptB, (0, 255, 0), 2)
    cv2.line(image, ptB, ptC, (0, 255, 0), 2)
    cv2.line(image, ptC, ptD, (0, 255, 0), 2)
    cv2.line(image, ptD, ptA, (0, 255, 0), 2)

    (cX, cY) = (int(r.center[0]), int(r.center[1]))
    cv2.circle(image, (cX, cY), 5, (0, 0, 255), -1)

    tagFamily = r.tag_family.decode('utf-8')
    cv2.putText(image, tagFamily, (ptA[0]), ptA[1] - 15),
    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    print('[INFO] tag family: {}'.format(tagFamily))

cv2.imshow('Image', image)
cv2.waitKey(0)
