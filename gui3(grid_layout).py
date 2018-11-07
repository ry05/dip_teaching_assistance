# Grid Layout in Tkinter

from tkinter import *

root = Tk()

label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")

# entry is for input

entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, column=0, sticky=E) # sticky takes N,S,E,W
label_2.grid(row=1, column=0, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me logged in!")
c.grid(columnspan=2)

root.mainloop()