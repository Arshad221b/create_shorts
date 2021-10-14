from detect_face import DetectFace
# crop frame
#     |- crop get the required the width 
#     |- get the face data 

class CropFrame():
    def __init__(self, img, face) -> None:
        self.img    = img
        self.face   = face

    def get_face_data(self):
        x, _, _, _ = self.face['box']
        # x, y, w, h = self.face['box']
        # cv2.rectangle(self.img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        return x

    def crop_fame(self):
        width, height   = len(self.img), len(self.img[0])
        req_width       = int(width*9/32)                                  # based on the height what should be the width (9:16 ratio)
        x               = self.get_face_data()
        crop_img        = self.img[:, x-req_width : x+req_width]

        return crop_img 

# import cv2
# img  = cv2.imread('test.jpg')
# face = DetectFace(img).detect_req_face()
# c = CropFrame(img, face).crop_fame()
# cv2.imshow("c", c)
# cv2.waitKey()
