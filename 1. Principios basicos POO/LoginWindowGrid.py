# LoginWindowGrid.py
from tkinter import *
from tkinter import ttk, font
import getpass

class Application():
    def __init__(self):
        self.root = Tk()
        self.root.title("Login")

        self.root.resizable(0,0)
        f = font.Font(weight = "bold")

        # Frame
        self.container = ttk.Frame(self.root, borderwidth = 2, relief = "raised", padding = (10,10))

        # Labels
        self.userLabel = ttk.Label(self.container, text = "User", font = f, padding = (5,5))
        self.passwordLabel = ttk.Label(self.container, text = "Password", font = f, padding = (5,5))

        self.user = StringVar()
        self.password = StringVar()
        self.user.set(getpass.getuser())

        # Text box
        self.userText = ttk.Entry(self.container, textvariable = self.user, width = 30)
        self.passwordText = ttk.Entry(self.container, textvariable = self.password, width = 30, show = "*")

        # Message
        self.message = StringVar()
        self.messageLabel = ttk.Label(self.container, textvariable = self.message, font = f, foreground = "blue")
        
        # Separator
        self.separator = ttk.Separator(self.container, orient = HORIZONTAL)

        # Buttons
        self.loginButton = ttk.Button(self.container, text = "Login", padding = (5,5), command = self.login)
        self.cancelButton = ttk.Button(self.container, text = "Cancel", padding = (5,5), command = quit)

        # Grid
        self.container.grid(column = 0, row = 0) # Container
        self.userLabel.grid(column = 0, row = 0)
        self.userText.grid(column = 1, row = 0)
        self.passwordLabel.grid(column = 0, row = 1)
        self.passwordText.grid(column = 1, row = 1)
        self.messageLabel.grid(column = 0, row = 2, columnspan = 2) # Message
        self.separator.grid(column = 0, row = 3, columnspan = 2)
        self.loginButton.grid(column = 0, row = 4)
        self.cancelButton.grid(column = 1, row = 4)

        self.passwordText.bind("<Button-1>", self.clearData)

    def login(self):
        if self.password.get() == "berenice":
            self.messageLabel.configure(foreground = "blue")
            self.message.set("Successful login!")
            #print("Successful login")
        else:
            self.messageLabel.configure(foreground = "red")
            self.message.set("¡Bad password!")
            #print("Bad password")
            
    def clearData(self, event):
        self.password.set("")
        self.message.set("")

# Object
myapp = Application()
