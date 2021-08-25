import cv2
from datetime import datetime
from icecream import ic

class WebCam:
    def __init__(self):
        self.port_num = None

    # 포트번호 설정
    def set_port(self, portNum):
        self.port_num = portNum

    # Get Webcam List
    def get_valid_camera_list(self, max_port_num=3):
        camera_port_list = []

        for index in range(max_port_num):
            # CAP_DSHOW(DirectShow (via videoInput)): remove terminating async callback
            cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
            ret, frame = cap.read()
            if ret is True and frame is not None:
                camera_port_list.append(index)
            else:
                break
            cap.release()

        return camera_port_list


if __name__ == "__main__":
    webCam = WebCam()
    ic(webCam.get_valid_camera_list(5))
