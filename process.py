import cv2
import numpy as np
from matplotlib import pyplot as plt

mouseX, mouseY  = -1, -1
def locateMouse(event, x, y ,flags, param):
    global mouseX, mouseY
    if event == cv2.EVENT_MOUSEMOVE:
        mouseX, mouseY = x, y

#cv2.setMouseCallback('success', locateMouse)

# cap = cv2.VideoCapture()
# cap.open("rtmp://rtmp.open.ys7.com/openlive/3500ecdfeb404eb883c0fe662c5bc297.hd live=1")

while (1):
    #_, frame = cap.read()
    #img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    img_rgb = cv2.imread('/Users/william/Desktop/chess3.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('/Users/william/Pictures/piece2.png', 0)

    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.4
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    
    cv2.imshow("test", img_rgb)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break