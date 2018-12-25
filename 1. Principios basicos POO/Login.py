# Login.py
# Basic elements tkinter
from tkinter import *
# New elements 8.5 version
from tkinter import ttk, font
# Get user logged
import getpass 

class Application():
    def __init__(self):
        self.root = Tk()
        self.root.title("Login")
        f = font.Font(weight = "bold")

        self.userLabel = ttk.Label(self.root, text = "User:", font = f)
        self.passwordLabel = ttk.Label(self.root, text = "Password:", font = f)
        
        self.user = StringVar()
        self.password = StringVar()

        self.user.set(getpass.getuser())

        # Text box
        self.userText = ttk.Entry(self.root, textvariable = self.user, width = 30)
        self.passwordText = ttk.Entry(self.root, textvariable = self.password, width = 30, show = "*")

        # Separator
        self.separator = ttk.Separator(self.root, orient = HORIZONTAL)

        # Buttons
        self.loginButton = ttk.Button(self.root, text = "Login", command = self.login)
        self.cancelButton = ttk.Button(self.root, text = "Cancel", command = quit)

        # Customize with pack
        self.userLabel.pack(side = TOP, fill = BOTH, expand = True, padx = 5, pady = 5)
        self.userText.pack(side = TOP, fill = X, expand = True, padx = 5, pady = 5)
        self.passwordLabel.pack(side = TOP, fill = BOTH, expand = True, padx = 5, pady = 5)
        self.passwordText.pack(side = TOP, fill = X, expand = True, padx = 5, pady = 5)
        self.separator.pack(side = TOP, fill = BOTH, expand = True, padx = 5, pady = 5)
        self.loginButton.pack(side = LEFT, fill = BOTH, expand = True, padx = 5, pady = 5)
        self.cancelButton.pack(side = RIGHT, fill = BOTH, expand = True, padx = 5, pady = 5)

    def login(self):
        if self.password.get() == "berenice":
            print("Successful login")
        else:
            print("Bad password")

# Object
myapp = Application()
    
