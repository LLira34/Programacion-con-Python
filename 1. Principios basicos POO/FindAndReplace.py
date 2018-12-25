# FindAndReplace.py
from tkinter import *

root = Tk()
root.title("Find and replace")
root.geometry("310x130")

Label(root, text = "Find:").grid(column = 0, row = 0, sticky = W)
Entry(root, bd = 5).grid(column = 1, row = 0)
Button(root, text = "Find", bg = "#0085cf", fg = "white").grid(column = 2, row = 0, sticky = NSEW)

Label(root, text = "Replace:").grid(column = 0, row = 1, sticky = W)
Entry(root, bd = 5).grid(column = 1, row = 1)
Button(root, text = "Find All").grid(column = 2, row = 1, sticky = NSEW)

Checkbutton(root, text = "Match whole").grid(column = 0, row = 3, sticky = W)
Checkbutton(root, text = "Match case").grid(column = 0, row = 4, sticky = W)
Checkbutton(root, text = "Wrap around").grid(column = 0, row = 5, sticky = W)

Label(root, text = "Direction").grid(column = 1, row = 3, sticky = W)

Button(root, text = "Replace").grid(column = 2, row = 3, sticky = NSEW)
Radiobutton(root, text = "Up").grid(column = 1, row = 4, sticky = W)
Radiobutton(root, text = "Down").grid(column = 1, row = 4, sticky = E)

Button(root, text = "Replace All").grid(column = 2, row = 4, sticky = NSEW)



