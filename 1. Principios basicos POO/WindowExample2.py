# WindowExample2.py
from tkinter import *

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid()
		self.createWidgets()

	def createWidgets(self):
		self.quitButton = Button(self, text="Quit")
		self.quitButton.bind("<Return>", self.quit)
		self.quitButton.bind("<Button-1>", self.quit)
		self.quitButton.grid()

	def quit(self, event):
		print("Time:", str(event.time))
		print("Event type:", str(event.type))
		print("Event Widget Id:", str(event.widget))
		print("Event Key Symbol:", str(event.keysym))
		self.master.destroy()

app = Application()
app.master.title("Sample Application")
