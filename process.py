import cv2
import numpy as np

mouseX, mouseY  = -1, -1
def locateMouse(event, x, y ,flags, param):
    global mouseX, mouseY
    if event == cv2.EVENT_MOUSEMOVE:
        mouseX, mouseY = x, y

cap = cv2.VideoCapture()
cap.open("rtmp://rtmp.open.ys7.com/openlive/3500ecdfeb404eb883c0fe662c5bc297.hd")
cv2.namedWindow("success")
cv2.setMouseCallback('success', locateMouse)

pts1 = np.float32([[225, 18], [918, 30], [172, 675], [943, 685]])
pts2 = np.float32([[42, 23], [1215, 28], [60, 676], [1215, 675]])
M = cv2.getPerspectiveTransform(pts1, pts2)

while(1):
    _, frame = cap.read()

    dst = cv2.warpPerspective(frame,M,(1280, 720))
    cv2.imshow('success',dst)


    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):
        print (mouseX, mouseY)

cap.release()
cv2.destroyAllWindows()