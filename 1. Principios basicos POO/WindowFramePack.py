# WindowFramePack.py
from tkinter import *

root = Tk()
parent = Frame(root)

Button(parent, text = "All is well").pack(fill = X)
Button(parent, text = "Back to Basics").pack(fill = X)
Button(parent, text = "Catch me if you can").pack(fill = X)

Button(parent, text = "LEFT").pack(side = LEFT)
Button(parent, text = "Center").pack(side = LEFT)
Button(parent, text = "RIGHT").pack(side = LEFT)

parent.pack()