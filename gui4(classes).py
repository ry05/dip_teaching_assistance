from tkinter import *


class RamsButtons:

    def __init__(self, master): #a special kind of object, called automatically when an object is created

        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame,text="Print Message", command = self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame,text="Quit Button", command = frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("Wow, this works!")


root = Tk()
b = RamsButtons(root)
root.mainloop()