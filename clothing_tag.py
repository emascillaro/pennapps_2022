import cv2
#from image_capture import Capture_image
import pytesseract

def ImageToTextString():
    # Takes image
    #capture_image()

    # Reads Image
    img = cv2.imread("image_capture.jpg")

    # Converts Image to String
    text = pytesseract.image_to_string(img)
    #print(text)

    return text.lower()
