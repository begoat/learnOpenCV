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

    # transformation
    tramsFrame = cv2.warpPerspective(frame,M,(1280, 720))

    gray = cv2.cvtColor(tramsFrame, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)
    dst = cv2.dilate(dst,None)
    tramsFrame[dst>0.01*dst.max()]=[0,0,255]

    # dst = cv2.cornerHarris(dst,2,3,0.04)

    cv2.imshow('success',tramsFrame)


    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):
        print (mouseX, mouseY)

cap.release()
cv2.destroyAllWindows()