# import the necessary header files
from tkinter import *

# the code

root = Tk() # ctor that creates a blank window

# frame : an invisible rectangle into which you can put stuff in
topFrame = Frame(root)
topFrame.pack(side=TOP)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button 1", fg="#0000ff")
button2 = Button(topFrame, text="Button 2", fg="#ff0000")
button3 = Button(topFrame, text="Button 3", fg="#00ff00")
button4 = Button(bottomFrame, text="Button 4", fg="#000000")

button1.pack(side=LEFT) # places it as far left as possible
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

# by default, every time you pack things, they are packed on top of each other : pack()

root.mainloop() # puts it into an infinite loop until we press the close button




