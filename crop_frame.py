from detect_face import DetectFace
# crop frame
#     |- crop get the required the width 

class CropFrame():
    def __init__(self, img, x) -> None:
        self.img    = img
        self.x      = x


    def crop_fame(self):
        width, height   = len(self.img), len(self.img[0])
        req_width       = int(width*9/32)                                  # based on the height what should be the width (9:16 ratio)
        crop_img        = self.img[:, self.x-req_width : self.x+req_width]

        return crop_img 

# import cv2
# img  = cv2.imread('test.jpg')
# face = DetectFace(img).detect_req_face()
# c = CropFrame(img, face).crop_fame()
# cv2.imshow("c", c)
# cv2.waitKey()

