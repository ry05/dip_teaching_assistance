'''Smoothing by Averaging'''

# import the necessary packages
from tkinter import Tk, Label, Menu, Button, Frame, LEFT, TOP, X, SUNKEN, W, \
    BOTTOM, Entry, PhotoImage
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import cv2
import matplotlib.pyplot as plt

def average():
    img = cv2.imread('cameraman.jpg')
    size = int(n.get())
    kernel = np.ones((size, size), np.float32) / (size*size)
    dst = cv2.filter2D(img, -1, kernel)

    plt.subplot(121), plt.imshow(img), plt.title('Before applying Averaging filter')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(dst), plt.title('After applying Averaging Filter')
    plt.show()

root = Tk()
root.geometry("900x650")
root.resizable(width=False, height=False)
root.configure(background='#000034')
panelA = None
panelB = None

#---------------Body---------------------

title = Label(root, text="Smoothing Averaging Filter", font=('Agency FB', 50), background='#000034',
              foreground='white')
title.pack()

picture = ImageTk.PhotoImage(Image.open('cameraman.jpg'))
pic = Label(root, image=picture)
pic.place(x=100, y=150)

text = Label(root, text='Smoothing filters are used to blur the image.\n'
                        ' They do the task of removing unwanted noise in an image.\n'
                        'An averaging filter is used here.', bg='#000034',
             font=('Arial', 12), fg='#ffffff'
            )
text.place(x=400, y=200)

button = Button(root, text="Show Averaged Image", command=average, height=2)
# button.pack(side="bottom", fill="x", expand="yes", padx="10", pady="10")
button.pack(side="bottom", fill='x', padx='20', pady='20')

n= Entry(root)
n.place(x=600, y=500)

instruction = Label(root, text='Notice the above image. This is our original image.\n'
                               'Enter n for nxn averaging filter.', bg='#000034',
                    fg='#ffffff', font=('Arial', 12))
instruction.place(x=40, y=450)

#----------------------
root.mainloop()