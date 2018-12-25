# ImageWindow.py
from tkinter import *
from tkinter import ttk, font

class Application():
    def __init__(self):
        image1 = PhotoImage(file = "cook.png")
        self.root = Tk()
        self.root.title("Image on Window")
        self.imageLabel = Label(self.root, image = image1, anchor = "center")
        self.imageLabel.pack(side = TOP, fill = BOTH, expand = True, padx = 10, pady = 10)
        self.root.mainloop()

myapp = Application()
