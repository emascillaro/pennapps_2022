import cv2
import time

def capture_image():
    # Define which camera to use (0 = webcam)
    videoCaptureObject = cv2.VideoCapture(0)
    #time.sleep(2)

    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        img = cv2.imwrite("Capture_Image.jpg", frame)
        result = False
    videoCaptureObject.release()

    return videoCaptureObject
