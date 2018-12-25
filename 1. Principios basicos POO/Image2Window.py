# Image2Window.py
from tkinter import *

class Application():
    def __init__(self):
        self.root = Tk()
        self.root.title("Image on Window")
        img = PhotoImage(file = "coco.png")
        self.imageLabel = Label(self.root, image = img, anchor = "center").pack()
        self.button = Button(self.root, text="Close", background = "#04B486", foreground="white", command = quit)
        self.button.pack()
        self.root.mainloop()

myapp = Application()
