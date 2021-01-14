# import the necessary packages
import time
import cv2
cap = cv2.VideoCapture(0)
while(True):
        ret,image = cap.read()
        face_cascade = cv2.CascadeClassifier('face.xml')
        #Convert to grayscale
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        #Look for faces in the image using the loaded cascade file
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)
        print ("Found "+str(len(faces))+" face(s)")
        #Draw a rectangle around every found face
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)
        # show the frame
        #cv2.imshow("Frame", faces)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
