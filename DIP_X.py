from tkinter import *
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import filedialog
import tkinter.messagebox
from PIL import Image, ImageTk
import cv2

import os
import sys


class DipApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        '''Font of Title in Start Page'''
        self.title_font = tkfont.Font(family='Helvetica', size=48, weight="bold")

        # Container into which the frames go

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames={}
        for F in (StartPage, Basics, What_Image, Dip_Core,
                  Image_Enhancement, Eye, Neighbours):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self,page_name):
        '''Show the Page for the given frame'''
        frame = self.frames[page_name]
        frame.tkraise()

def about_this_popup():
    tkinter.messagebox.showinfo("About the Project","The DIP Teaching Assistance is an Open Source Project "
                                "that has been started by Ramshankar Yadhunath (BL.EN.U4CSE16106)"
                                "of Amrita School of Engineering, Bangalore as a part "
                                "of his 5th Semester DIP Project under the guidance of Mrs. "
                                "Jyotsana(CSE Department, ASE-B). With its first official release on 8th November, 2018"
                                " , the project is open "
                                "to contributions future DIP students want to make."
                                "This project aims at making it easier for teachers to teach the "
                                "complex DIP topics in the classroom."
                                "")

def pixel_popup():
    tkinter.messagebox.showinfo("Pixel", "A pixel is the smallest unit of an image.\n"
                                        "Each pixel is represented as (x,y) and has a "
                                        "unique intensity value.")

def grayscalefunc():
    os.system('guibase.py')

def afflinetrans():
    os.system('geometrictrans.py')

def arithmeticfunc():
    os.system('basic_arithmetic.py')

def gammacorrection():
    os.system('gamma_correction.py')

def threshold():
    os.system('thresholding.py')

def histogram_gen():
    os.system('histogram_equivalence.py')

def smoothing():
    os.system('smoothing.py')

'''StartPage GUI'''
class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent, bg='#5d8aa8') # we have set background to white
        self.controller = controller

        '''background_image = ImageTk.PhotoImage(Image.open('home.jpg'))
        background_label = Label(self, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image
        '''

        title = Label(self, text="DIP Teaching Assistance", font=('systemfixed',36,"bold"),
                      bg="#5d8aa8")

        title.pack()
        # title.grid(row=10, column=5, sticky=E)


        icon = PhotoImage(file="image-processing.png")
        image_label = Label(self, image=icon, bg="#5d8aa8")
        image_label.image = icon # keep a reference of the image
        image_label.place(x=230, y=80)

        start_button = Button(self, text='Start!', font=('Arial', 26),
                              bg='black', activebackground='grey',
                              fg='white', padx=5, pady=5, width=15,
                              command=lambda: controller.show_frame("Basics"))

        #exit_button.pack(side=RIGHT)
        start_button.place(x=300,y=550)

        about_this = Button(self, text='About the Project!', font=('Arial',18),
                            bg='white', fg='black', padx=5, pady=5, width=15,
                            command=about_this_popup)
        about_this.place(x=50,y=570)

class Basics(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#5d8aa8') #sets background to orange
        self.controller = controller

        title = Label(self, text="Main Menu", font=('systemfixed', 36, "bold"),
                      bg="#5d8aa8", fg='white')

        title.pack()

        definition = PhotoImage(file="pen.png")
        def_button = Button(self, image=definition, bg='white', text="Definitions",
                            command=lambda: controller.show_frame("What_Image"))
        def_button.image = definition  # keep a reference of the image
        #def_button.grid(row=0,column=0)
        def_button.place(x=100, y=100)
        def_label = Label(self, text='What is an Image ?', font=('Arial',16), bg='#5d8aa8')
        def_label.place(x=70, y=250)

        dip = PhotoImage(file="applications.png")
        dip_button = Button(self, image=dip, bg='white',
                            command=lambda: controller.show_frame("Dip_Core"))
        dip_button.image = dip  # keep a reference of the image
        # def_button.pack()
        dip_button.place(x=100, y=350)
        dip_label = Label(self, text='DIP Techniques', font=('Arial',16), bg='#5d8aa8')
        dip_label.place(x=90, y=500)

        basics = PhotoImage(file="basic.png")
        basics_button = Button(self, image=basics, bg='white',
                               command=lambda: controller.show_frame("Neighbours"))
        basics_button.image = basics  # keep a reference of the image
        #basics_button.grid(row=1d, column=0)
        basics_button.place(x=650, y=100)
        basics_label = Label(self, text='What are \n Neighbours ?', font=('Arial',16), bg='#5d8aa8')
        basics_label.place(x=650, y=250)

        eye = PhotoImage(file="eye.png")
        eye_button = Button(self, image=eye, bg='white',
                            command=lambda: controller.show_frame("Eye"))
        eye_button.image = eye  # keep a reference of the image
        #def_button.pack()
        eye_button.place(x=650, y=350)
        eye_label = Label(self, text='How does the \n Human Eye look?',
                          font=('Arial',16), bg='#5d8aa8')
        eye_label.place(x=630, y=500)

        '''we need a back button now'''
        back = Button(self, text="Go Back", font=('Helvetica', 18),
                      padx=5, pady=5, command=lambda: controller.show_frame("StartPage"))
        back.place(x=770, y=580)
        '''Back button placed'''


class What_Image(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#5d8aa8') #sets background to orange
        self.controller = controller

        '''Let us make the body of this page'''
        title = Label(self, text="The Image", font=('systemfixed', 36, "bold"),
                      bg="#5d8aa8", fg='white')

        title.pack()

        label = Label(self, text="An image is basically a two-dimensional function.\n"
                                 "It is represented as f(x,y) where x and y are the spatial "
                                 "coordinates.\nThe Amplitude of (x,y) at a point is called as "
                                 "the intensity at that point.", bg='#5d8aa8',
                      font=('Arial', 14))
        label.place(x=15, y=100)

        image_logo = PhotoImage(file="image.png")
        logo = Label(self, image=image_logo, bg='#5d8aa8', text="Definitions")
        logo.image = image_logo  # keep a reference of the image
        # def_button.grid(row=0,column=0)
        logo.place(x=700, y=70)

        '''Now, we want to make our Pixel Screen (3x3 array)'''
        b1 = Button(self, text='P', command=pixel_popup)
        b1.place(x=100, y=200)
        b2 = Button(self, text='P', command=pixel_popup)
        b2.place(x=100, y=226)
        b3 = Button(self, text='P', command=pixel_popup)
        b3.place(x=100, y=252)
        b4 = Button(self, text='P', command=pixel_popup)
        b4.place(x=118, y=200)
        b5 = Button(self, text='P', command=pixel_popup)
        b5.place(x=136, y=200)
        b6 = Button(self, text='P', command=pixel_popup)
        b6.place(x=118, y=226)
        b7 = Button(self, text='P', command=pixel_popup)
        b7.place(x=118, y=252)
        b8 = Button(self, text='P', command=pixel_popup)
        b8.place(x=136, y=226)
        b9 = Button(self, text='P', command=pixel_popup)
        b9.place(x=136, y=252)
        '''The pixels have been placed'''
        pixel = Label(self, text='<<<<These buttons basically represent Pixels'
                                 ' of an Image f(x,y). \nClick on one to know more '
                                 'about pixels.', bg='#5d8aa8', font=('Helvetica', 18))
        pixel.place(x=200, y=226)

        picture1 = ImageTk.PhotoImage(Image.open('cameraman.jpg'))
        pic = Label(self, image=picture1)
        pic.image = picture1
        pic.place(x=100, y=350)

        picture2 = ImageTk.PhotoImage(Image.open('dog.jpg'))
        pic = Label(self, image=picture2)
        pic.image = picture2
        pic.place(x=400, y=350)


        '''we need a back button now'''
        back = Button(self, text="Go Back", font=('Helvetica', 18),
                      padx=5, pady=5, command=lambda: controller.show_frame("Basics"))
        back.place(x=770, y=580)
        '''Back button placed'''



class Neighbours(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#5d8aa8') #sets background to orange
        self.controller = controller

        title = Label(self, text="Neighbours of a Pixel", font=('systemfixed', 36, "bold"),
                      bg="#5d8aa8", fg='white')
        title.pack()

        label = Label(self, text="A pixel in an image can have 3 types of \nneighbours :\n"
                                 "1. N4P neighbours\n"
                                 "2. N8P neighbours\n"
                                 "3. NDP neighbours", bg='#5d8aa8',
                      font=('Arial', 14))
        label.place(x=550, y=100)

        p1 = Button(self, height=5, width=10)
        p1.place(x=300, y=100)
        p2 = Button(self, height=5, width=10)
        p2.place(x=300, y=190)
        p3 = Button(self, height=5, width=10)
        p3.place(x=300, y=280)
        p4 = Button(self, height=5, width=10)
        p4.place(x=385, y=100)
        p5 = Button(self, height=5, width=10)
        p5.place(x=470, y=100)
        # the static button
        p6 = Button(self, height=5, width=10, bg='#000034')
        p6.place(x=385, y=190)
        #************
        p7 = Button(self, height=5, width=10)
        p7.place(x=385, y=280)
        p8 = Button(self, height=5, width=10)
        p8.place(x=470, y=280)
        p9 = Button(self, height=5, width=10)
        p9.place(x=470, y=190)

        def neighbours4():
            reset()
            p2.config(bg='red')
            p4.config(bg='red')
            p7.config(bg='red')
            p9.config(bg='red')

        def neighboursd():
            reset()
            p1.config(bg='red')
            p3.config(bg='red')
            p5.config(bg='red')
            p8.config(bg='red')

        def neighbours8():
            reset()
            p2.config(bg='red')
            p4.config(bg='red')
            p7.config(bg='red')
            p9.config(bg='red')
            p1.config(bg='red')
            p3.config(bg='red')
            p5.config(bg='red')
            p8.config(bg='red')

        def reset():
            p1.config(bg='#343434')
            p2.config(bg='#343434')
            p3.config(bg='#343434')
            p4.config(bg='#343434')
            p5.config(bg='#343434')
            p7.config(bg='#343434')
            p8.config(bg='#343434')
            p9.config(bg='#343434')

        '''n4p, ndp, n8p, reset'''
        n4p = Button(self, text="N4P", command=neighbours4)
        n4p.place(x=150, y=500)

        ndp = Button(self, text="NDP", command=neighboursd)
        ndp.place(x=250, y=500)

        n8p = Button(self, text="N8P", command=neighbours8)
        n8p.place(x=350, y=500)

        restButton = Button(self, text="Reset", command=reset)
        restButton.place(x=550, y=500)

        '''we need a back button now'''
        back = Button(self, text="Go Back", font=('Helvetica', 18),
                      padx=5, pady=5, command=lambda: controller.show_frame("Basics"))
        back.place(x=770, y=580)
        '''Back button placed'''


class Dip_Core(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#5d8aa8') #sets background to orange
        self.controller = controller

        title = Label(self, text="Some DIP Techniques Used", font=('systemfixed', 36, "bold"),
                      bg="#5d8aa8", fg='white')
        title.pack()

        arith_theory = Label(self, text="Basic Arithmetic Ops"
                                        "work on Images",
                             font=('systemfixed',20,"bold"), bg="#5d8aa8", fg='#000000')
        arith_theory.place(x=50, y=80)
        image_arithmetic = Button(self, text="Basic Arithmetic", command=arithmeticfunc)
        image_arithmetic.place(x=50, y=120)

        gray_theory = Label(self, text="Grayscale Images are widely used",
                             font=('systemfixed', 20, "bold"), bg="#5d8aa8", fg='#000000')
        gray_theory.place(x=50, y=160)
        grayscale = Button(self, text="Grayscale Converter", command=grayscalefunc)
        grayscale.place(x=50, y=200)

        affline_theory = Label(self, text="Parallel lines stay parallel",
                            font=('systemfixed', 20, "bold"), bg="#5d8aa8", fg='#000000')
        affline_theory.place(x=50, y=240)
        affline = Button(self, text="Affline Transformation", command=afflinetrans)
        affline.place(x=50, y=280)

        image_enhancement = Label(self, text="Image Enhancement Techniques",
                                  bg='#5d8aa8', font=('systemfixed', 20,"bold"), fg='#000000')
        image_enhancement.place(x=50, y=320)

        thresholding = Button(self, text="Thresholding", command=threshold)
        thresholding.place(x=50, y=360)

        power_law = Button(self, text="Power Law Transformation",
                           command=gammacorrection)
        power_law.place(x=50, y=400)

        histogram = Button(self, text="Histogram", command=histogram_gen)
        histogram.place(x=50, y=440)

        smooth = Button(self, text="Smoothing", command=smoothing)
        smooth.place(x=50, y=480)

        '''we need a back button now'''
        back = Button(self, text="Go Back", font=('Helvetica', 18),
                      padx=5, pady=5, command=lambda: controller.show_frame("Basics"))
        back.place(x=770, y=580)
        '''Back button placed'''

class Image_Enhancement(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black') #sets background to orange
        self.controller = controller




        '''we need a back button now'''
        back = Button(self, text="Go Back", font=('Helvetica', 18),
                      padx=5, pady=5, command=lambda: controller.show_frame("Basics"))
        back.place(x=770, y=580)
        '''Back button placed'''




class Eye(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#5d8aa8') #sets background to orange
        self.controller = controller

        title = Label(self, text="The Anatomy of the Human Eye", font=('systemfixed', 36, "bold"),
                      bg="#5d8aa8", fg='white')
        title.pack()

        diagram_eye = PhotoImage(file="eyedi.png")
        dia_label = Label(self, image=diagram_eye, bg='#5d8aa8')
        dia_label.image = diagram_eye  # keep a reference of the image
        dia_label.place(x=10, y= 80)

        '''we need a back button now'''
        back = Button(self, text="Go Back", font=('Helvetica', 18),
                      padx=5, pady=5, command=lambda: controller.show_frame("Basics"))
        back.place(x=770, y=580)
        '''Back button placed'''




''' root = Tk()
root.geometry("900x650")
root.resizable(width=False, height=False)
root.configure(background='white')

title = Label(root, text="DIP_X", font=("Arial", 48), bg='white')

title.pack()
#title.grid(row=10, column=5, sticky=E)

icon = PhotoImage(file="image-processing.png")
image_label = Label(root, image=icon, bg='white')
image_label.pack()

start_button = Button(root, text='Start!', font=('Helvetica', 26), bg='black', activebackground='grey', fg='white', padx=5, pady=5, width=15, command=go_to_page_2)
start_button.pack()
'''

if __name__ == "__main__":
    app = DipApp()
    # to set the dimensions of the window
    app.geometry("900x650")
    app.resizable(width=False, height=False)
    app.configure(background='white')
    app.mainloop()