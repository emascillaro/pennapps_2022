import PIL
from PIL import Image,ImageTk
import PIL.Image
import pytesseract
import cv2
import tkinter as tk

from tkinter import *
from ttkthemes import ThemedStyle


width, height = 800, 600
cap = cv2.VideoCapture(-1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root = Tk()
root.bind('<Escape>', lambda e: root.quit())
lmain = Label(root)
lmain.pack()

#style = ThemedStyle(root)
#style.set_theme("black")

root.configure(bg = 'black')

def ShowFrame():
    ret, frame = cap.read()
    if ret:
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = PIL.Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, ShowFrame)
        lmain.pack(padx=15, pady=20)

def CaptureImage():
    #videoCaptureObject = cv2.VideoCapture(0)
    videoCaptureObject = cap
    ret, frame = videoCaptureObject.read()
    img = cv2.imwrite("image_capture.jpg", frame)
    #videoCaptureObject.release()

# Button Picture
im = PIL.Image.open("/home/emascillaro/Documents/Emma/Hackathons/MakeMIT_2022/MakeMIT2022/thumbnail_capture_button3.png")
ph = ImageTk.PhotoImage(im)

image_capture = tk.Button(image = ph, command = CaptureImage, bg = 'red', fg= '#fff', activebackground='green', activeforeground='#fff')
image_capture.pack(side = BOTTOM, padx=15, pady=70)

print("Opening Application")

ShowFrame()
root.mainloop()