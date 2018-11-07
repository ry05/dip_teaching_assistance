''' Now there are many transformation techniques, but here, the code written is only for
Affline Transformations '''

from tkinter import Tk, Label, Menu, Button, Frame, LEFT, TOP, X, SUNKEN, W, BOTTOM
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

def doNothing():
    print("ok ok I won't...")

def select_image():
    # image panels
    global panelA, panelB

    # choose image from files
    path = filedialog.askopenfilename()

    if len(path) > 0:
        image = cv2.imread(path)
        gray = afflinetransform(image)

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

def afflinetransform(image):
    rows, cols, ch = image.shape

    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

    M = cv2.getAffineTransform(pts1, pts2)

    dst = cv2.warpAffine(image, M, (cols, rows))

    return dst

root = Tk()
root.geometry("900x650")
root.resizable(width=False, height=False)
root.configure(background='#002d34')
panelA = None
panelB = None

# ****************Body*********************
title = Label(root, text="Affline Transformations", font=('Agency FB', 50),
              background='#002d34',
              foreground='white')
title.pack()

button = Button(root, text="Select an Image", command=select_image, height=2)
# button.pack(side="bottom", fill="x", expand="yes", padx="10", pady="10")
button.pack(side="bottom", fill='x', padx='20', pady='20')

#**************End of Body*****************

root.mainloop()