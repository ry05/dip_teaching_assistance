from tkinter import Tk, Label
from PIL import Image, ImageTk

root = Tk()

img = ImageTk.PhotoImage(Image.open('genral.png').resize(10, 20)) # the one-liner I used in my app
label = Label(root, image=img)
label.image = img # this feels redundant but the image didn't show up without it in my app
label.pack()

root.mainloop()