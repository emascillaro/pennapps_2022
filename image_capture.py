import cv2
import time

def Capture_image():
    # Define which camera to use (0 = webcam)
    videoCaptureObject = cv2.VideoCapture(0)
    #time.sleep(2)

    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        img = cv2.imwrite("Capture_Image.jpg", frame)
        # Resize large images proportionally (1/4)
        #img = cv2.resize(img0, (img0.shape[0] // 4, img0.shape[1] // 4))
        result = False
    videoCaptureObject.release()

    return videoCaptureObject

Capture_image()