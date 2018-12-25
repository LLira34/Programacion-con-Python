# TextEditor2.py
from tkinter import *

PROGRAM_NAME = "Editor 1.0"
root = Tk()
root.title(PROGRAM_NAME)
root.geometry("350x350")
nav_bar = Menu(root)

# Events
def cut():
    content_text.event_generate("<<Cut>>")
    return "break"

def copy():
    content_text.event_generate("<<Copy>>")
    return "break"

def paste():
    content_text.event_generate("<<Paste>>")
    return "break"

def undo():
    content_text.event_generate("<<Undo>>")
    return "break"

def redo(event = None):
    content_text.event_generate("<<Redo>>")
    return "break"

def find_text(event = None):
    search_toplevel = Toplevel(root)
    search_toplevel.title("Find text")
    search_toplevel.transient(root)
    search_toplevel.resizable(False, False)
    Label(search_toplevel, text = "Find text:").grid(row = 0, column = 0, sticky = "e")
    search_entry = Entry(search_toplevel, width = 25)
    search_entry.focus_set()
    search_entry.grid(row = 0, column = 1, padx = 2, pady = 2, sticky = "we")
    ignore_case_value = IntVar()
    Checkbutton(search_toplevel, text = "Text case", variable = ignore_case_value).grid(row = 1, column = 1, sticky = "e", padx = 2, pady = 2)
    Button(search_toplevel, text = "Find all", underline = 0, command = lambda: search_output(search_entry.get(), ignore_case_value.get(),
                                                                                              content_text, search_toplevel, search_entry)).grid(
                                                                                                  row = 0, column = 2, sticky = EW, padx = 2, pady = 2)
    def close_search_window():
        content_text.tag_remove("match", "1.0", END)
        search_toplevel.destroy()
        
    search_toplevel.protocol("WM_DELETE_WINDOW", close_search_window)
    return "break"

def search_output(needle, if_ignore_case, content_text, search_toplevel, search_box):
    content_text.tag_remove("match", "1.0", END)
    matches_found = 0
    if needle:
        start_pos = "1.0"
        while True:
            start_pos = content_text.search(needle, start_pos, nocase = if_ignore_case, stopindex = END)
            if not start_pos:
                break
            end_pos = "{} + {}c".format(start_pos, len(needle))
            content_text.tag_add("match", start_pos, end_pos)
            matches_found += 1
            start_pos = end_pos
        content_text.tag_config("match", foreground = "red", background = "yellow")
        search_box.focus_set()
        search_toplevel.title("{} matches found".format(matches_found))
    

def select_all(event = None):
    content_text.tag_add("sel", "1.0", "end")
    return "break"
    
# Menu file | nav_bar
file_menu = Menu(nav_bar, tearoff = 1)
nav_bar.add_cascade(label = "File", menu = file_menu)
new_icon = PhotoImage(file = "icons/new_file.gif")
file_menu.add_command(label = "New", accelerator = "Ctrl+N", compound = "left", image = new_icon, underline = 0)

open_icon = PhotoImage(file = "icons/open_file.gif")
file_menu.add_command(label = "Open", accelerator = "Ctrl+O", compound = "left", image = open_icon, underline = 0)

save_icon = PhotoImage(file = "icons/save.gif")
file_menu.add_command(label = "Save", accelerator = "Ctrl+S", compound = "left", image = save_icon, underline = 0)

file_menu.add_command(label = "Save as")

# ------------------ file_menu Separator file
file_menu.add_separator()

file_menu.add_command(label = "Exit", accelerator = "Alt+F4", command = quit)

# Menu edit
edit_menu = Menu(nav_bar, tearoff = 1)
nav_bar.add_cascade(label = "Edit", menu = edit_menu)
undo_icon = PhotoImage(file = "icons/undo.gif")
edit_menu.add_command(label = "Undo", accelerator = "Ctrl+Z", compound = "left", image = undo_icon, command = undo)

redo_icon = PhotoImage(file = "icons/redo.gif")
edit_menu.add_command(label = "Redo", accelerator = "Ctrl+Y", compound = "left", image = redo_icon, command = redo)

# ------------------ edit_menu Separator edit
edit_menu.add_separator()

cut_icon = PhotoImage(file = "icons/cut.gif")
edit_menu.add_command(label = "Cut", accelerator = "Ctrl+X", compound = "left", image = cut_icon, command = cut)

copy_icon = PhotoImage(file = "icons/copy.gif")
edit_menu.add_command(label = "Copy", accelerator = "Ctrl+C", compound = "left", image = copy_icon, command = copy)

paste_icon = PhotoImage(file = "icons/paste.gif")
edit_menu.add_command(label = "Paste", accelerator = "Ctrl+V", compound = "left", image = paste_icon, command = paste)

# ------------------ edit_menu Separator edit
edit_menu.add_separator()

find_icon = PhotoImage(file = "icons/find_text.gif")
edit_menu.add_command(label = "Find", accelerator = "Ctrl+F", compound = "left", image = find_icon, underline = 0, command = find_text)

edit_menu.add_command(label = "Select All", accelerator = "Ctrl+A", underline = 7, command = select_all)

# Menu view
view_menu = Menu(nav_bar, tearoff = 1)
nav_bar.add_cascade(label = "View", menu = view_menu)

# ** Variable checkbutton **
show_line_no = IntVar()
show_line_no.set(0)
show_cursor_location_bottom = IntVar()
highlight_current_line = IntVar()
theme_choice = StringVar()
theme_choice.set("Default")

# Colour scheme
colour_schemes = {
	"Default" : "#000000.#FFFFFF",
	"Greygarious" : "#83406A.##D1D4D1", 
	"Cobalt Blue" : "#ffffBB.#3333AA",
	"Bold Beige" : "#4B4620.#FFF0E1",
	"Night Mode" : "#FFFFFF.#000000",
	"Olive Green" : "#D1E7E0.#5B8340"
}

view_menu.add_checkbutton(label = "Show Line Number", variable = show_line_no)
view_menu.add_checkbutton(label = "Show Cursor Location at bottom", variable = show_cursor_location_bottom)
view_menu.add_checkbutton(label = "Highlight Current Line", variable = highlight_current_line)

themes_menu = Menu(nav_bar, tearoff = 0)
view_menu.add_cascade(label = "Themes", menu = themes_menu)

for K in sorted(colour_schemes):
    themes_menu.add_radiobutton(label = K, variable = theme_choice)

# Menu about
about_menu = Menu(nav_bar, tearoff = 1)
nav_bar.add_cascade(label = "About", menu = about_menu)
about_icon = PhotoImage(file = "icons/about.gif")
about_menu.add_command(label = "About us", compound = "left", image = about_icon)

about_menu.add_command(label = "Help")

# Frame 
shortcut_bar = Frame(root, height = 25, bg = "light sea green")
shortcut_bar.pack(expand = "no", fill = "x")

# Line numbers
line_number_bar = Text(root, width = 4, padx = 3, takefocus = 0, border = 0, bg = "khaki", state = "disable", wrap = "none")
line_number_bar.pack(side = "left", fill = Y)

# Content text
content_text = Text(root, wrap = "word", undo = 1)
content_text.pack(expand = "yes", fill = "both")
content_text.bind("<Control-y>", redo)
content_text.bind("<Control-Y>", redo)
content_text.bind("<Control-a>", select_all)
content_text.bind("<Control-A>", select_all)
content_text.bind("<Control-f>", find_text)
content_text.bind("<Control-F>", find_text)

scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand = scroll_bar.set)
scroll_bar.config(command = content_text.yview)
scroll_bar.pack(side = "right", fill = Y)

# Window
root.config(menu = nav_bar)
