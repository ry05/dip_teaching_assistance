'''Histogram Displaying Code'''

# import the necessary packages
from tkinter import Tk, Label, Menu, Button, Frame, LEFT, TOP, X, SUNKEN, W, \
    BOTTOM, Entry, PhotoImage
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Histogram Functions
def histogram1():
    img= cv2.imread("cameraman.jpg")
    plt.hist(img.ravel(), 256, [0, 256]);plt.show()

def histogram2():
    img = cv2.imread("girl.png")
    plt.hist(img.ravel(),256,[0,256]);plt.show()


root = Tk()
root.geometry("900x650")
root.resizable(width=False, height=False)
root.configure(background='#000034')
panelA = None
panelB = None

#********************Body***************************

title = Label(root, text="Histograms of an Image", font=('Agency FB', 50), background='#000034',
              foreground='white')
title.pack()


picture1 = ImageTk.PhotoImage(Image.open('cameraman.jpg'))
pic = Label(root, image=picture1)
pic.place(x=100, y=150)
button1 = Button(root, text="Show Histogram", command=histogram1, height=2)
# button.pack(side="bottom", fill="x", expand="yes", padx="10", pady="10")
button1.place(x=150, y=400)

picture2 = PhotoImage(file='girl.png')
pic = Label(root, image=picture2)
pic.place(x=550, y=125)
button2 = Button(root, text="Show Histogram", command=histogram2, height=2)
# button.pack(side="bottom", fill="x", expand="yes", padx="10", pady="10")
button2.place(x=625, y=400)


#************************
root.mainloop()