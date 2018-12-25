# DemoTopLevelWindow.py
from tkinter import *

root = Tk()
root.title("Top Level Window")
root.geometry("300x300")
Label(root, text = "I am the main TopLevelWindow\n All other windows here are my children").pack()
child_toplevel = Toplevel(root)
Label(child_toplevel, text = "I am a child of root\n If i loose focus, I may hide below the top level\nI am destroyed if root is destroy").pack()
child_toplevel.geometry("400x100+300+300")

transient_toplevel = Toplevel(root)
Label(transient_toplevel, text = "I am transient window of root \n I always stay on top of my parent \n I get hidden if my parent window is minimize").pack()
transient_toplevel.transient(root)

no_window_decoration = Toplevel(root, bg = "black")
Label(no_window_decoration, text = "I am a toplevel with no window manager\n I cannot be resized or moved", bg = "black", fg = "white").pack()
no_window_decoration.overrideredirect(1)
no_window_decoration.geometry("250x100+700+500")
