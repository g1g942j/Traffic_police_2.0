import cv2 as cv
import apriltag

cap = cv.VideoCapture('/home/user/Загрузки/Telegram Desktop/1.mp4')
#cap = cv.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    options = apriltag.DetectorOptions(families="tag36h11")
    detector = apriltag.Detector(options)
    results = detector.detect(gray)
    #print(results)
    print(" {} AprilTags обнаружено".format(len(results)))

    for r in results:

        (ptA, ptB, ptC, ptD) = r.corners
        ptB = (int(ptB[0]), int(ptB[1]))
        ptC = (int(ptC[0]), int(ptC[1]))
        ptD = (int(ptD[0]), int(ptD[1]))
        ptA = (int(ptA[0]), int(ptA[1]))

        cv.line(frame, ptA, ptB, (0,255,0), 2)
        cv.line(frame, ptB, ptC, (0,255,0), 2)
        cv.line(frame, ptC, ptD, (0,255,0), 2)
        cv.line(frame, ptD, ptA, (0,255,0), 2)

        (cX, cY) = (int(r.center[0]), int(r.center[1]))
        cv.circle(frame, (cX, cY), 5, (0,0,255), -1)

        tagId = str(r.tag_id)
        cv.putText(frame, tagId, (ptA[0], ptA[1] - 15),
                    cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv.imshow("f", frame)
    cv.waitKey(1)
