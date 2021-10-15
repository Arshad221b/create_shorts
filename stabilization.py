from crop_frame import CropFrame
from detect_face import DetectFace
# stablize the face
#     |- check if the privoious image had x value above/below threshold

class StabilizeFrame():
    def __init__(self, face, k_prev) -> None:
        self.face   = face
        self.k_prev = k_prev
        # self.x      = x


    def find_current_k(self):                           # finding the center of the face (box)
        x, _, w, _ = self.face['box']

        return int(x + w/2)


    def check_stabilization(self):
        k = self.find_current_k()

        if abs(self.k_prev - k)> 50:               # finding the threshould (move to config)
            self.k_prev = k
        
        return self.k_prev, k 


# import cv2
# img = cv2.imread('test.jpg')
# d   = DetectFace(img).detect_req_face()
# k_prev, k   = StabilizeFrame(d, 100).check_stabilization()
# print(k_prev, k)