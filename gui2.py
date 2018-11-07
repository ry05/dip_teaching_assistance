from tkinter import *

root = Tk()

one = Label(root, text="One", fg='black', bg='green')
one.pack() # stays the same size irrespective of parent's size
two = Label(root, text="Two", fg='black', bg='white')
two.pack(fill=X) # gets as wide as the parent
three = Label(root, text="Three", fg='red', bg='white')
three.pack(side=LEFT, fill=Y) # gets as tall as the parent

root.mainloop()