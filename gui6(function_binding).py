# Function Binding

from tkinter import *

root=Tk()

def printName(event):
    print("My name is Ram")


button1 = Button(root, text="Print")
button1.bind("<Button-1>", printName)
button1.pack()


root.mainloop()