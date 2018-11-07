''' Day 1 : We get the gui to show output of image.Need to do it for options
and also resize images according to gui screen '''

from tkinter import Tk, Label, Menu, Button, Frame, LEFT, TOP, X, SUNKEN, W, BOTTOM
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2


def doNothing():
    print("ok ok I won't...")


def select_image():
    # image panels
    global panelA, panelB

    # choose image from files
    path = filedialog.askopenfilename()

    if len(path) > 0:
        image = cv2.imread(path)
        gray = showGrayScale(image)

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # convert to PIL format
        image = Image.fromarray(image)
        gray = Image.fromarray(gray)

        # to ImageTk format
        image = ImageTk.PhotoImage(image)
        gray = ImageTk.PhotoImage(gray)

        if panelA is None or panelB is None:
            panelA = Label(image=image)
            panelA.image = image
            panelA.pack(side="left", padx=10, pady=10)

            panelB = Label(image=gray)
            panelB.image = gray
            panelB.pack(side="right", padx=10, pady=10)

        else:
            # update the pannels
            panelA.configure(image=image)
            panelB.configure(image=gray)
            panelA.image = image
            panelB.image = gray


def showGrayScale(image):
    img = image
    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return imggray


root = Tk()
root.geometry("900x650")
root.resizable(width=False, height=False)
root.configure(background='#000034')
panelA = None
panelB = None

# root.geometry("500x250") # sets the size
# root.resizable(width=False, height=False) # this stops resizing

# **********Menu**************
'''
menu = Menu(root)
root.config(menu=menu)  # configuring the menu

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)  # creates a file button and makes subMenu
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator()  # adding a line to separate a group
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)  # creates a file button and makes subMenu
editMenu.add_command(label="Edit pic", command=doNothing)
editMenu.add_command(label="Redo", command=doNothing)
'''
# ***************Body**********************

title = Label(root, text="Grayscale Converter", font=('Arial', 50), background='#000034',
              foreground='white')
title.pack()

button = Button(root, text="Select an Image", command=select_image, height=2)
# button.pack(side="bottom", fill="x", expand="yes", padx="10", pady="10")
button.pack(side="bottom", fill='x', padx='20', pady='20')

# ***********Toolbar*************
'''
toolbar = Frame(root, bg="blue")
insertButt = Button(toolbar, text="Insert Image", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)  # padding too done
printButt = Button(toolbar, text="Print", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)  # padding too done

toolbar.pack(side=TOP, fill=X)

# *******Status Bar*********

status = Label(root, text="Prepare to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
'''
root.mainloop()

