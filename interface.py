import tkinter as tk
import webbrowser
import PIL

from tkinter import *
from ttkthemes import ThemedStyle
from PIL import ImageTk, Image

def CreateDisplay(materials_present):
    root = Tk()
    root.bind('<Escape>', lambda e: root.quit())

    root.configure(bg = 'white')

    if "cotton" in materials_present:
        cotton_img = ImageTk.PhotoImage(Image.open("cotton_info_7.jpeg"))
        label = Label(root, image = cotton_img)
        label.pack()

    if "denim" in materials_present:
        denim_img = ImageTk.PhotoImage(Image.open("denim_info_7.jpeg"))
        label = Label(root, image = denim_img)
        label.pack()

    if "leather" in materials_present:
        leather_img = ImageTk.PhotoImage(Image.open("leather_info_7.jpeg"))
        label = Label(root, image = leather_img)
        label.pack()

    if "polyester" in materials_present:
        polyester_img = ImageTk.PhotoImage(Image.open("polyester_info_7.jpeg"))
        label = Label(root, image = polyester_img)
        label.pack()

    if "rayon" in materials_present:
        rayon_img = ImageTk.PhotoImage(Image.open("rayon_info_7.jpeg"))
        label = Label(root, image = rayon_img)
        label.pack()


    #Define a callback function
    def callback(url):
        webbrowser.open_new_tab(url)

    reduce_footprint_button = tk.Button(text = "How Can I Reduce My Footprint?", bg = 'red', fg= '#fff', activebackground='green', activeforeground='#fff')
    reduce_footprint_button.pack(side = BOTTOM, padx=15, pady=70)
    reduce_footprint_button.bind("<Button-1>", lambda e: callback("file:///home/emascillaro/Documents/Emma/Hackathons/PennApps%202022/pennapps_2022/index.html"))


    print("Opening Application")

    root.title('Material Details')
    root.geometry("300x200+10+20")
    root.mainloop()