import cv2
import numpy as np

def locateMouse(event, x, y ,flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        print (x ,y)

cap = cv2.VideoCapture()
cap.open("rtmp://rtmp.open.ys7.com/openlive/3500ecdfeb404eb883c0fe662c5bc297.hd")
cv2.namedWindow("success")
# cv2.setMouseCallback('success', locateMouse)

pts1 = np.float32([[198, 19], [923, 28], [176, 678], [918, 690]])
pts2 = np.float32([[40, 40], [1250, 40], [40, 690], [1250, 690]])
M = cv2.getPerspectiveTransform(pts1, pts2)

while(1):
    _, frame = cap.read()

    dst = cv2.warpPerspective(frame,M,(1280, 720))
    cv2.imshow('success',dst)


    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()