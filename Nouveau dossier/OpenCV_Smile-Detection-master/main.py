import cv2
import numpy as np
from time import time

#Cascade Classifier definations for face and smile
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

#Webcam Video Capture Setup
cap = cv2.VideoCapture(0)
font=cv2.FONT_HERSHEY_COMPLEX_SMALL

#Timer Class to measure duration of smile
class Timer:
    def __init__(self):
        self.t0 = 0
        self.d0 = 0
    def startTime(self):
        self.t0 = time()
        return
    def stopTimer(self):
        self.d0 = time() - self.t0
        return
    def resetTime(self):
        print(self.d0)
        self.t0 = 0
        self.d0 = 0
        return
        
while True:
    #Capture Data Frame by Frame for Processing
    ret, frame = cap.read()
    #Convert Frame Data to Grayscale for operations
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Face Detection and Cascading
    faces, faceRejectLevels, faceLevelWeights = face_cascade.detectMultiScale3(gray, 1.3, 5, outputRejectLevels=True)
    f=0
    for (x,y,w,h) in faces:
        if (round(faceLevelWeights[f][0],3)) <= 5:
            continue
        #print(round(faceLevelWeights[f][0],3)) #To Display Accurary of Face detection
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        #cv2.putText(frame, str(round(faceLevelWeights[f][0],3)), (x,y),font, 1, (255,255,255), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        #Feature Extraction
        eyes, rejectLevels, levelWeights = smile_cascade.detectMultiScale3(roi_gray, outputRejectLevels=True)
        i = 0;
        for (ex,ey,ew,eh) in eyes:
            if(round(levelWeights[i][0],3)>=4.65):
                #print(round(levelWeights[i][0],3))       #To Display Smile Confidence
                cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)
                #cv2.putText(roi_color,str(round(levelWeights[i][0],3)),(ex,ey), font,1,(255,255,255),2)
            i+=1
        f+=1
        
    #Display Frame Data to User
    cv2.imshow('Smile Detector', frame)

    #Exit Condition
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


#Release Camera Resources
cap.release()
cv2.destroyAllWindows()

