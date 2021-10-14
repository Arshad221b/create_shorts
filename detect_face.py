import numpy as np 
import pandas as pd
import cv2
from mtcnn.mtcnn import MTCNN


class detect_face(self):

    def __init__(self) -> None:
        pass


    def detect_all_faces(self, img):

        detector    = MTCNN() # add detector in the config
        x, y, w, h  = 0, 0, len(img), len(img[0])
        k           = int(len(img)*9/32)
        max_area    = 0
        max_face    = (0,0,0,0)
        faces       = detector.detect_faces(img)
        x_prev, y_prev, w_prev, h_prev = 0,0,len(img),len(img[0])

        for result in faces:
            x, y, w, h  = result['box']
            area        = w*h

            if max_area < area:
                max_area = area
                max_face = result

            x, y, w, h = max_face['box']

            w  = k
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            if abs(x-all_x[-1][0])<50:
                x = all_x[-1][0]
                w = k

            if x != 0:
                all_x.append([x, k])
                
        else:
            if x == 0:
                print('x_', x)
                x_prev, y_prev, w_prev, h_prev = all_x[-1][0], y, all_x[-1][1], h
    
        
        print('x',x)

        if x != 0 and y != 0:
            if abs(x- x_prev)>3:
                x = x + int(k/2)
                print('w', abs(w - w_prev))
                cropped_img = img[:, x-k : x+k]
                print(len(cropped_img), len(cropped_img[0]))
            else:
                # x = all_x[-1][0]
                x = x_prev
                x = x + int(k/2)
                print(x-k, x+k)
                cropped_img = img[:, x-k : x+k]
                print(len(cropped_img), len(cropped_img[0]))
        else:
            print(x)
            print('prev', x_prev)
            x = x_prev
            x = x + int(k/2)
            cropped_img = img[:, x-k : x+k]
            print(len(cropped_img), len(cropped_img[0]))

        cv2.imshow('img', img)
        # cv2.waitKey()
        return cropped_img

