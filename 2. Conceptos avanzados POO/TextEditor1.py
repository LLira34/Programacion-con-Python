# TextEditor1.py
from tkinter import *

root = Tk()
root.title("NotePad IDE")
root.geometry("260x160")
menu_bar = Menu(root)

# Menu file | nav_bar
file_menu = Menu(menu_bar, tearoff = 1)
menu_bar.add_cascade(label = "File", menu = file_menu)
new_icon = PhotoImage(file = "img/new.png")
file_menu.add_command(label = "New", accelerator = "Ctrl+N", compound = "left", image = new_icon)

open_icon = PhotoImage(file = "img/open.png")
file_menu.add_command(label = "Open", accelerator = "Ctrl+O", compound = "left", image = open_icon)

save_icon = PhotoImage(file = "img/save.png")
file_menu.add_command(label = "Save", accelerator = "Ctrl+S", compound = "left", image = save_icon)

file_menu.add_command(label = "Save as")

file_menu.add_command(label = "Exit", accelerator = "Alt+F4")

# Menu edit
edit_menu = Menu(menu_bar, tearoff = 1)
menu_bar.add_cascade(label = "Edit", menu = edit_menu)
undo_icon = PhotoImage(file = "img/undo.png")
edit_menu.add_command(label = "Undo", accelerator = "Ctrl+Z", compound = "left", image = undo_icon)

# Menu view
view_menu = Menu(menu_bar, tearoff = 1)
menu_bar.add_cascade(label = "View", menu = view_menu)

# Menu about
about_menu = Menu(menu_bar, tearoff = 1)
menu_bar.add_cascade(label = "About", menu = about_menu)

# Window
root.config(menu = menu_bar)
