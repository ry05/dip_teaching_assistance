from tkinter import *

def doNothing():
    print("ok ok I won't...")


root = Tk()
root.geometry("500x250") # sets the size
root.resizable(width=False, height=False) # this stops resizing

# **********Menu**************

menu = Menu(root)
root.config(menu=menu) # configuring the menu

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu) # creates a file button and makes subMenu
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator() # adding a line to separate a group
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu) # creates a file button and makes subMenu
editMenu.add_command(label="Edit pic", command=doNothing)
editMenu.add_command(label="Redo", command=doNothing)

#***********Toolbar*************

toolbar = Frame(root, bg="blue")
insertButt = Button(toolbar, text= "Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2) # padding too done
printButt = Button(toolbar, text= "Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2) # padding too done

toolbar.pack(side=TOP, fill=X)

# *******Status Bar*********

status = Label(root, text="Prepare to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()



