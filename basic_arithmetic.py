from tkinter import *
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import filedialog
import tkinter.messagebox
from PIL import Image, ImageTk
import cv2
from math import *

import os
import sys

def test():
    print ("M just a test")

def select_image():
    # image panels
    global panelA, panelB

    # choose image from files
    path = filedialog.askopenfilename()

    if len(path) > 0:
        image = cv2.imread(path)
        gray = arithmetic(image)

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

def sub_image():
    # image panels
    global panelA, panelB

    # choose image from files
    path = filedialog.askopenfilename()

    if len(path) > 0:
        image = cv2.imread(path)
        gray = sub_image1(image)

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


def arithmetic(image):
    img = image
    #k = str(eval(ent.get()))
    addimg = cv2.imread('dots.jpg')
    imgarith = cv2.addWeighted(img, 0.6, addimg, 0.4, 0)
    #imgarith = cv2.subtract(img,addimg)
    return imgarith

def sub_image1(image):
    img = image
    # k = str(eval(ent.get()))
    addimg = cv2.imread('dots.jpg')
    #imgarith = cv2.addWeighted(img, 0.6, addimg, 0.4, 0)
    imgarith = cv2.subtract(img, addimg)
    return imgarith



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

title = Label(root, text="Basic Arithmetic in Images", font=('Arial', 50), background='#000034',
              foreground='white')
title.pack()

'''Label(root, width=15)
ent = Entry(root)
ent.place(x=400, y=300)
ent.bind("<Return>", arithmetic)
'''

addimage = PhotoImage(file="dots.gif")
image_label = Label(root, image = addimage, bg='#5d8aa8')
image_label.image = addimage # keep a reference of the image
image_label.place(x=325, y=200)

button = Button(root, text="Select an Image(Addition)", command=select_image, height=2)
# button.pack(side="bottom", fill="x", expand="yes", padx="10", pady="10")
button.pack(side="bottom", fill='x', padx='20', pady='20')

button_sub = Button(root, text="Select an Image(Subtraction)", command=sub_image, height=2)
button_sub.pack(side="bottom", fill='x', padx='20', pady='20')

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
