# MyFirstWindow.py
from tkinter import *

root = Tk()
myContainer1 = Frame(root)
myContainer1.pack()

button1 = Button(myContainer1)
button1["text"] = "Hello World!"
button1["background"] = "blue"
button1["foreground"] = "pink"
button1.pack(side=LEFT)

buttonA = Button(myContainer1)
buttonA["text"] = "Button A"
buttonA["background"] = "pink"
buttonA["foreground"] = "purple"
buttonA.pack(side=LEFT)

buttonB = Button(myContainer1)
buttonB["text"] = "Button B"
buttonB["background"] = "#01DFD7"
buttonB["foreground"] = "black"
buttonB.pack(side=LEFT)

buttonC = Button(myContainer1)
buttonC["text"] = "Button C"
buttonC["background"] = "#2EFE2E"
buttonC["foreground"] = "black"
buttonC.pack(side=LEFT)
root.mainloop()