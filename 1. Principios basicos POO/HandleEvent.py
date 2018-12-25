# HandleEvent.py
from tkinter import *

class MyApp:
	def __init__(self, parent):
		self.myParent = parent
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()

		self.button1 = Button(self.myContainer1, text="OK", background="blue", foreground="white")
		self.button1.pack(side="left")
		self.button1.bind("<Button-1>", self.button1Click)
		self.button1.bind("<Return>", self.button1Click)

		self.button2 = Button(self.myContainer1, text="CANCEL", background="red", foreground="white")
		self.button2.pack(side="left")
		self.button2.bind("<Button-1>", self.button2Click)
		self.button1.bind("<Return>", self.button2Click)
		self.button1.focus_force()

	def button1Click(self, event):
		if self.button1["background"] == "blue":
			self.button1["background"] = "pink"
			#self.button1["foreground"] = "black"
			#self.button1["text"] = "Wakanda Forever"
		else:
			self.button1["background"] = "blue"

	def button2Click(self, event):
		self.myParent.destroy()
		print("Bye")


root = Tk()
app = MyApp(root)
root.mainloop()