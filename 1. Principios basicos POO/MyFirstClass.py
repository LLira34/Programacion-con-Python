# MyFirstClass.py
from tkinter import *

class MyApp:
	def __init__(self, myParent):
		self.myContainer1 = Frame()
		self.myContainer1.pack()

		self.button1 = Button(self.myContainer1, text="Hello World", 
			background="green")
		self.button1.pack(side=LEFT)

		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Off to join the circus")
		self.button2.configure(background="#FAFAFA")
		self.button2.configure(foreground="purple")
		self.button2.pack(side=RIGHT)

		self.button3 = Button(self.myContainer1)
		self.button3.configure(text="OK", background="#58FAF4", 
			foreground="#FE2EF7")
		self.button3.pack(side="top")


root = Tk()
myapp = MyApp(root)
root.mainloop()