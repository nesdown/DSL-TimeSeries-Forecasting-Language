from tkinter import * 
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

root = Tk()
root.title("Timical IDE")
root.geometry("800x600")

# initialize the menu of app
menu_main = Menu(root) 
root.config(menu=menu_main) 

# add the menu labels
menu_file = Menu(menu_main, tearoff=0)
menu_file.add_command(label="Open")
menu_file.add_command(label="New")
menu_file.add_command(label="Save")
menu_file.add_separator()
menu_file.add_command(label="Exit")

menu_edit = Menu(menu_main, tearoff=0)
menu_edit.add_command(label="Undo")
menu_edit.add_command(label="Redo")
 
menu_help = Menu(menu_main, tearoff=0)
menu_help.add_command(label="Help")
menu_help.add_command(label="About")
 
menu_main.add_cascade(label="File",
                        menu=menu_file)
menu_main.add_cascade(label="Edit",
                        menu=menu_edit)
menu_main.add_cascade(label="Help",
                        menu=menu_help)

# code editor field
field_code = Text(root)
field_code.place(x=0, y=0, height=400, width=800)

# just an addition for the design
window_separator = ttk.Separator(root, orient='horizontal')
window_separator.place(x=0, y=425, width=800)

# console
field_console = Text(root, bg="grey")
field_console.place(x=0, y=450, height=150, width=800)

root.mainloop()