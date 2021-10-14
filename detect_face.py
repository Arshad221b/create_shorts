import numpy as np 
import pandas as pd
import cv2
from mtcnn.mtcnn import MTCNN

# detect face
#     |-detect all faces
#     |-get the required face
    

class detect_face():
    def __init__(self, img) -> None:
        self.img = img

    def required_face(self, faces):                         # face should have maximum area
        max_area = 0
        max_face = (0,0,0,0)
        for face in faces:
            x, y, w, h = face['box']
            area = w*h
            if max_area < area:
                max_area = area
                max_face = face

        return max_face        


    def detect_all_faces(self):
        detector    = MTCNN()                               # using the detector best fit (move to config)
        faces       = detector.detect_faces(self.img)       # detect all the faces available
        
        return faces


    def detect_req_face(self):
        faces   = self.detect_all_faces()
        face    = self.required_face(faces)

        return face

# img  = cv2.imread('test.jpg')
# f = detect_face(img)
# print(f.detect_req_face())