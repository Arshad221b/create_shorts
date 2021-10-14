from tkinter import Frame
import numpy as np 
import pandas as pd
import cv2


class detect_face():
    def __init__(self) -> None:
        pass

    def face_detection(self, img, all_x):
        # Load the cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # Read the input image
        # img = cv2.imread(img)
        # Convert into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw rectangle around the faces
        
        x,y, w, h = 0,0, len(img),len(img[0])
        # print(w, h)
        x_prev, y_prev, w_prev, h_prev = 0,0,len(img),len(img[0])
        

        if len(faces) != 0:

            for face in faces:
                (x, y, w, h) = face
                if abs(x-all_x[-1][0])<50:
                    x = all_x[-1][0]
                if x != 0:
                    print('x', x)
                    all_x.append([x, w])
                # print(face)
                # print([(x, y), (x+w, y+h)])
                # cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        else:
            if x == 0:
                print('x_', x)
                x_prev, y_prev, w_prev, h_prev = all_x[-1][0], y, all_x[-1][1], h
    
        # Display the output
        k = int(len(img)*9/32)
        # x = 0

        if x != 0 and y != 0:
            if abs(x-all_x[-1][0])>50:
                x = x + int(w/2)
                cropped_img = img[:, x-k : x+k]
            else:
                x = all_x[-1][0]
                x = x + int(w/2)
                cropped_img = img[:, x-k : x+k]
            # print(len(cropped_img), len(cropped_img[0]))

        else:
            print(x)
            print('prev', x_prev)
            x = x_prev
            x = x + int(w_prev/2)
            cropped_img = img[:, x-k : x+k]

        cv2.imshow('img', img)
        # cv2.waitKey()
        return cropped_img


    def get_video(self):
        result = cv2.VideoWriter('output2.avi', cv2.VideoWriter_fourcc(*"MJPG"), 30.0, (202,360))

        cap = cv2.VideoCapture('avengers2.mp4')
        if (cap.isOpened()== False): 
            print("Error opening video  file")
        all_x = [[0,0]]
        while(cap.isOpened()):
      
        # Capture frame-by-frame
            ret, frame = cap.read()
            if ret == True:
            
                # Display the resulting frame
                
                frame = self.face_detection(frame, all_x)
                # print(frame)
                cv2.imshow('Frame', frame)
                result.write(frame)
                # Press Q on keyboard to  exit
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            
            # Break the loop
            else: 
                break
        
        # When everything done, release 
        # the video capture object

        
        result.release()
        cap.release()
        
        # Closes all the frames
        cv2.destroyAllWindows()


detect_face().get_video()
