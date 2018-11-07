from tkinter import *
import tkinter.messagebox


root=Tk()

tkinter.messagebox.showinfo('Window Title', 'Monkesy can live upto 300 years')

answer = tkinter.messagebox.askquestion('Question 1', 'Do you like silly faces?')

if answer == 'yes':
    print("Silly faces")

root.mainloop()
