import cv2
import sys

cam = 0
if len(sys.argv) > 1:
    cam = sys.argv[1]

source = cv2.VideoCapture(cam)

wind = cv2.namedWindow('Camera', cv2.WINDOW_NORMAL)

while cv2.waitKey(1) != 27:
    ret, frame = source.read()
    if not ret:
        break
    cv2.imshow(wind, frame)

source.release()
cv2.destroyAllWindows()
