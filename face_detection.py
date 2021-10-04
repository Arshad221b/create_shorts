from tkinter import Frame
import numpy as np 
import pandas as pd
import cv2

class detect_face():
    def __init__(self) -> None:
        pass

    def face_detection(self, img):
        # Load the cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # Read the input image
        # img = cv2.imread(img)
        # Convert into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Display the output
        k = int(len(img)*9/32)
        # x = 0
        x = x + int(w/2)
        cropped_img = img[:, x-k : x+k]
        # cv2.imshow('img', cropped_img)
        # cv2.waitKey()
        return cropped_img


    def get_video(self):

        cap = cv2.VideoCapture('haha3.mp4')
        if (cap.isOpened()== False): 
            print("Error opening video  file")

        while(cap.isOpened()):
      
        # Capture frame-by-frame
            ret, frame = cap.read()
            if ret == True:
            
                # Display the resulting frame
                
                frame = self.face_detection(frame)
                cv2.imshow('Frame', frame)
                # Press Q on keyboard to  exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            
            # Break the loop
            else: 
                break
        
        # When everything done, release 
        # the video capture object
        cap.release()
        
        # Closes all the frames
        cv2.destroyAllWindows()


detect_face().get_video()