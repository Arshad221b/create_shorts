from detect_face    import DetectFace
from stabilization  import StabilizeFrame
from crop_frame     import CropFrame

import cv2

class Main():
    def __init__(self, video) -> None:
        self.video = video

    def resulting_video(self, width, height):
        result  = cv2.VideoWriter('mkbhd2.avi', cv2.VideoWriter_fourcc(*"MJPG"), 30.0, (width,height))
        return result

    def capture_frames(self, k_prev_list):
        
        cap     = cv2.VideoCapture(self.video)

        if (cap.isOpened()== False): 
            print("Error opening video  file")

        i = 0
        ret, frame = cap.read()
        # if i == 0:
        width   = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height  = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # width, height   = len(frame), len(frame[0])
        print(width, height)
        # print(width, height)
        req_width = int(height*9/16)
        # print(req_width)
        result = self.resulting_video(req_width, height)
        print(req_width, height)

        while(cap.isOpened()):
            ret, frame = cap.read()
             
            if ret == True:
                # frame       = .face_detection(frame)
                face        = DetectFace(frame).detect_req_face()
                (x, y, w, h) = face
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                k_prev, k   = StabilizeFrame(face, k_prev_list[-1]).check_stabilization()
                width, height   = len(frame), len(frame[0])
                req_width       = int(width*9/32)    
                # print(req_width)
                crp_frm     = CropFrame(frame, k, req_width).crop_fame()
                # print(len(crp_frm), len(crp_frm[0]))
                cv2.imshow('Frame', crp_frm)
                cv2.imshow('Frame_ori', frame)
                # cv2.waitKey()
                k_prev_list.append(k_prev)
                result.write(crp_frm)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    # result.write(crp_frm)
                    cv2.destroyAllWindows()
            
            else:
                break

        result.release()
        cap.release()  
        cv2.destroyAllWindows()


    def main(self):
        k_prev_list = [0]
        self.capture_frames(k_prev_list)


Main('test_video.mp4').main()

