'''Image Thresholding. Let's use adaptive thresholding here.'''

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
    thresh=float(thresh_Value.get())
    thresh_image = threshold(image, thresh)

    cv2.imshow("Gamma Corrected Image", thresh_image)


def threshold(image, thresh):
    grayscaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    retval, threshold = cv2.threshold(grayscaled, thresh, 255, cv2.THRESH_BINARY)
    return threshold


root = Tk()
root.geometry("900x650")
root.resizable(width=False, height=False)
root.configure(background='#000034')
panelA = None
panelB = None

#********************Body***************************

title = Label(root, text="Thresholding", font=('Agency FB', 50), background='#000034',
              foreground='white')
title.pack()

button = Button(root, text="Show Threshold Image", command=gamma_correct, height=2)
# button.pack(side="bottom", fill="x", expand="yes", padx="10", pady="10")
button.pack(side="bottom", fill='x', padx='20', pady='20')

thresh_Value= Entry(root)
thresh_Value.place(x=600, y=500)

#picture = PhotoImage(file='basics.png')
picture = ImageTk.PhotoImage(Image.open('dog.jpg'))
pic = Label(root, image=picture)
pic.place(x=100, y=150)

text = Label(root, text='Thresholding is basically a Spatial Domain \nImage Enhancement \n'
                        ' Technique'
                       'that helps convert an image into a complete \nblack and white image.\n'
                       '\n'
                       '\n'
                       'If a particular pixel has a value is above a\n threshold value,it becomes '
                        'white and \n anything less than threshold is black \n\n', bg='#000034',
             font=('Arial', 12), fg='#ffffff'
            )
text.place(x=400, y=200)

instruction = Label(root, text='Notice the above image. This is our original image.\n'
                               'Enter a threshold value into the field.', bg='#000034',
                    fg='#ffffff', font=('Arial', 12))
instruction.place(x=40, y=450)

#************************
root.mainloop()