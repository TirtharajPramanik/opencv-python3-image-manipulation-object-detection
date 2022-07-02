#!/Users/tirtharaj/Practice/python-cvml/venv/bin/python3

import pathlib
import cv2

cascade_path = str(pathlib.Path(cv2.__file__).parent.absolute(
) / "data/haarcascade_frontalface_default.xml")

clf = cv2.CascadeClassifier(cascade_path)

camera = cv2.VideoCapture(0)
# camera = cv2.VideoCapture('assets/1058579989-preview.mp4')

try:
    while True:
        _, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = clf.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        cv2.imshow('Face Detection', frame)
        if cv2.waitKey(1) == ord("q"):
            break
except cv2.error:
    print("\n[!] VideoEnded!")

camera.release()
cv2.destroyAllWindows()
