from mtcnn.mtcnn import MTCNN
import cv2
# detect face
#     |-detect all faces
#     |-get the required face

class DetectFace():
    def __init__(self, img) -> None:
        self.img = img


    def required_face(self, faces):                         # face should have maximum area
        max_area = 0
        max_face = (0,0,0,0)

        for face in faces:
            # x, y, w, h = face['box']
            x, y, w, h = face                               # haar cascade
            area = w*h
            if max_area < area:
                max_area = area
                max_face = face

        return max_face        


    def detect_all_faces(self):
        # detector    = MTCNN()                               # using the detector best fit (move to config)
        # faces       = detector.detect_faces(self.img)       # detect all the faces available
        face_cascade    = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        gray            = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        faces           = face_cascade.detectMultiScale(gray, 1.1, 4)


        return faces


    def detect_req_face(self):
        faces   = self.detect_all_faces()
        face = (0,0,0,0)
        if len(faces) != 0:
            face    = self.required_face(faces)

        return face

# import cv2
# img     = cv2.imread('test.jpg')
# f       = DetectFace(img)
# print(f.detect_req_face())