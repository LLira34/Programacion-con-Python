# WindowLoginGrid.py
from tkinter import *

root = Tk()

Label(root, text = "User:").grid(column = 0, row = 0, sticky = NSEW)
Entry(root).grid(column = 1, row = 0, sticky = E)
Label(root, text = "Password:").grid(column = 0, row = 1, sticky = W)
Entry(root).grid(column = 1, row = 1, sticky = E)
Button(root, text = "Login").grid(column = 1, row = 2, sticky = E)
