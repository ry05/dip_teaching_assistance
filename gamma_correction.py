'''Gamma Correction
s=c.r^1/gamma)
if gamma<1, then lighter image
if gamma>1, then darker image'''

# import the necessary packages
from tkinter import Tk, Label, Menu, Button, Frame, LEFT, TOP, X, SUNKEN, W, \
    BOTTOM, Entry, PhotoImage
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import cv2

# Selecting the image from the user
def gamma_correct():
    # image panels
    image = cv2.imread('dog.jpg')
    gamma=float(gamma_Value.get())
    gamma_corrected = adjust_gamma(image,gamma)

    cv2.imshow("Gamma Corrected Image", gamma_corrected)


def adjust_gamma(image, gamma=0.5):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    table = np.array([((i / 255.0) ** gamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")

    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)

root = Tk()
root.geometry("900x650")
root.resizable(width=False, height=False)
root.configure(background='#000034')
panelA = None
panelB = None

#********************Body***************************

title = Label(root, text="Power Law Conversion OR Gamma Correction", font=('Agency FB', 40), background='#000034',
              foreground='white')
title.pack()

button = Button(root, text="Show Gamma Corrected Image", command=gamma_correct, height=2)
# button.pack(side="bottom", fill="x", expand="yes", padx="10", pady="10")
button.pack(side="bottom", fill='x', padx='20', pady='20')

gamma_Value= Entry(root)
gamma_Value.place(x=600, y=500)

#picture = PhotoImage(file='basics.png')
picture = ImageTk.PhotoImage(Image.open('dog.jpg'))
pic = Label(root, image=picture)
pic.place(x=100, y=150)

text = Label(root, text='Gamma Correction or Power Law transform \n '
                       'is basically a Spatial Domain Image Enhancement Technique\n'
                       'that helps rectify images that are too bleached or too dark.\n'
                       '\n'
                       '\n'
                       'Gamma Correction Formula is as follows: \n\n'
                       'New_image = constant x (old_image^gamma)', bg='#000034',
             font=('Arial', 12), fg='#ffffff'
            )
text.place(x=400, y=200)

instruction = Label(root, text='Notice the above image. This is our original image.\n'
                               'We shall be applying the gamma formula onto this using\n'
                               'different values of gamma.\n Enter your Gamma '
                               'value in the entry field', bg='#000034',
                    fg='#ffffff', font=('Arial', 12))
instruction.place(x=40, y=450)

#************************
root.mainloop()