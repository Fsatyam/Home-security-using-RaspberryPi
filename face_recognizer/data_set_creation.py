import time
import cv2
import os

i=1
def detect_face(img):
    face_cascade = cv2.CascadeClassifier('opencv-files/haarcascade_frontalface_alt.xml')
    faces = face_cascade.detectMultiScale(img)
    if (len(faces) == 0):
        return None, None
    (x, y, w, h) = faces[0]
    return img[y-40:y+w+40, x-40:x+h+40], faces[0]

time.sleep(1)
cap = cv2.VideoCapture(0)
while True:
    if (i<21):
        ret,image = cap.read()
        face, rect = detect_face(image)
        if face is not None:
            cv2.imshow("Frame", face)
            cv2.imwrite("training-data/s4/%i.jpg" % i, face)
            print("Clicking %i image!" % i)
            i=i+1
            time.sleep(0.1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
