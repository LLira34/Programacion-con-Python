# Practica1LFLG.py
# @ Author: Luis Fernando Lira García
# Group: GITI10071-E

from tkinter import *
from tkinter import ttk, font

class Application():
    def __init__(self):
        self.root = Tk()
        self.root.title("Entrada")

        self.root.resizable(0,0)
        f = font.Font(weight = "bold")

        # Frame
        self.container = ttk.Frame(self.root, borderwidth = 2)

        # Image
        img = PhotoImage(file = "p3.png")
        self.imageLabel = Label(self.container, image = img)

        # Labels
        self.aLabel = ttk.Label(self.container, text = "a.", font = f, padding = (2,2))
        self.bLabel = ttk.Label(self.container, text = "b.", font = f, padding = (2,2))
        self.cLabel = ttk.Label(self.container, text = "c.", font = f, padding = (5,5))
        self.dLabel = ttk.Label(self.container, text = "d.", font = f, padding = (5,5))

        # Labels
        self.aQLabel = ttk.Label(self.container, text = "Hola.", font = f, padding = (2,2))
        self.bQLabel = ttk.Label(self.container, text = "Como estas?", font = f, padding = (5,5))
        self.cQLabel = ttk.Label(self.container, text = "Adios", font = f, padding = (5,5))
        self.dQLabel = ttk.Label(self.container, text = "Salir", font = f, padding = (5,5))

        # Text box
        self.inputText = ttk.Entry(self.container,width = 60)

        # Buttons
        self.acceptButton = Button(self.container, text = "Aceptar", height = 2, width = 10)
        self.cancelButton = Button(self.container, text = "Cancelar", height = 2, width = 10)

        # Grid
        self.container.grid(column = 0, row = 0) # Container
        
        self.aLabel.grid(column = 1, row = 0) 
        self.aQLabel.grid(column = 2, row = 0) # Res
        self.bLabel.grid(column = 1, row = 1)
        self.bQLabel.grid(column = 2, row = 1) # Res
        self.cLabel.grid(column = 1, row = 2)
        self.cQLabel.grid(column = 2, row = 2) # Res
        self.dLabel.grid(column = 1, row = 3)
        self.dQLabel.grid(column = 2, row = 3) # Res
        self.inputText.grid(column = 2, row = 4)
        self.acceptButton.grid(column = 2, row = 5)
        self.cancelButton.grid(column = 3, row = 5)
        self.imageLabel.grid(column = 0, row = 0)
        
        # show image
        self.root.mainloop()
       
# Instance
myapp = Application()
myapp2 = Application()
myapp3 = Application()

