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

    # Capture webcam ImageFilter
    def capture_image(self, file_name, width=1080, height=720):
        cap = cv2.VideoCapture(self.port_num, cv2.CAP_DSHOW)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)

        ret, frame = cap.read()
        ret = cv2.imwrite(file_name, frame)
        cap.release()

        return ret, file_name

    # Capture Video Stream until 'q' input
    def capture_video(self, width=1080, height=720, isMono=False, flip=None):
        cap = cv2.VideoCapture(self.port_num, cv2.CAP_DSHOW)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)

        while True:
            ret, frame = cap.read()

            if isMono is True:
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

            if flip is not None:
                # flip: 0 -> bottom to top, 1: left to right
                frame = cv2.flip(frame, flip)

            cv2.imshow('frame', frame)

            # 1 is 1/1000
            if cv2.waitKey(1) == ord('q'):
                break
            elif ret is False:
                break

        cap.release()
        # 스트림창 닫기
        cv2.destroyAllWindows()

    # Record video stream until 'q' input
    def record_video(self, video_file_name, width=1080, height=720, flip=None, fps=25.0):
        cap = cv2.VideoCapture(self.port_num, cv2.CAP_DSHOW)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)

        # fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
        fourcc = cv2.VideoWriter_fourcc(*'DIVX')

        frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), # Width
                      int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))) # Height

        out = cv2.VideoWriter(video_file_name + '.avi', fourcc, fps, frame_size)

        while cap.isOpened():
            ret, frame = cap.read()

            if ret is True:
                if flip is not None:
                    frame = cv2.flip(frame, flip)

                # Write Frame
                out.write(frame)

                cv2.imshow('frame', frame)

                # FPS(Frame Per Second): 25
                if cv2.waitKey(int(1000/fps)) == ord('q'):
                    break
            else:
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()

    # Play local video file
    def play_video(self, file_name):
        cap = cv2.VideoCapture(file_name)
        fps = cap.get(cv2.CAP_PROP_FPS)
        print('FPS:', fps)

        cap.set(cv2.CAP_PROP_FPS, fps)
        while cap.isOpened():
            ret, frame = cap.read()

            if ret is True:
                cv2.imshow('frame', frame)

                if cv2.waitKey(int(1000/fps)) == ord('q'):
                    break
            else:
                break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    webCam = WebCam()
    webcam_port_list = webCam.get_valid_camera_list(5)
    ic('WebCam Port List:', webcam_port_list)

    if len(webcam_port_list) != 0:
        portNum = webcam_port_list[0]
        webCam.set_port(portNum)
        ic('Port Number:', portNum)

        #########################################################################################
        # Capture Image(Snapshot)
        # file_name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.png'
        # ic(webCam.capture_image(file_name))

        #########################################################################################
        # Capture Video Stream
        # webCam.capture_video()
        # webCam.capture_video(isMono=True)
        # webCam.capture_video(flip=0)  # 상/하 반전
        # webCam.capture_video(flip=1)  # 좌/우 반전

        #########################################################################################
        # Record Video Stream
        # file_name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        # webCam.record_video(file_name)
        # webCam.record_video(file_name, flip=0) # 상/하 반전
        # webCam.record_video(file_name, flip=1) # 좌/우 반전
