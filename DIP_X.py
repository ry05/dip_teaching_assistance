"""
MAIN CODE FILE FOR DIPTA

TODO LIST :
1. Document the behaviour of each function using docstrings
2. Place the .py files with image processing functions into a separate folder; call it "IP_Methods"
3. Place all the graphic content into a separate folder; call it "Graphic_Content"
4. Package the code as executable software
5. Prepare a "How to use" guide
6. Prepare a list of dependencies (with appropriate version numbers)
7. Provide references that were used while creating the product
8. Redefine the GUI (The current one looks very bad)
9. Watch the logo...should be R,G,B

DOCUMENTATION REQUIREMENTS :
1. User Manual cum Guide
2. Block Diagrams
3. References for official opencv or python material
4. List of dependencies
"""

# Search for the following in the code beneath to rectify -------------------------
# IMAGE - Signifies graphic content
# INPUT_IMAGE - Signifies an image that is taken as input 
# ---------------------------------------------------------------------------------


"""
============================================================================
STYLE GUIDE FOR THE DIPTA INTERFACE
============================================================================
UNIFIED FONT STYLES---------------------

Heading : (Agency FB, 48)
Sub-heading : (Agency FB, 32)
Buttons : (Agency FB, 26)
Text : (Arial, 10)
Labels :

UNIFIED GRAPHIC CONTENT SIZES----------

Icons : 128x128
Block Diagrams :
Flow Control Buttons(Eg. Back Button) : (Height=50, Width=50)

POP-UP BOXES---------------------------

Organizational Style :

 ---------------------------
 | ======================= |
 | Title of the Pop-up Box |
 | ======================= |
 | Text....                |
 ---------------------------

UNIFIED COLOR PALETTE------------------

Background : #ffffff (white)
Headings : #1e365c
Sub-headings : #000000 (black) OR #1e365c 
Text : #000000 (black)

"""
from tkinter import *
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import *
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import filedialog
import tkinter.messagebox
from PIL import Image, ImageTk
import cv2

import os
import sys


"""---------------------------Global Variables-------------------------------"""
### This section contains all the variables pertaining to the style of the DIP

#----------FONT STYLES-----------------------
heading_font = "Agency FB"
heading_size = 48
sub_heading_font = "Agency FB"
sub_heading_size = 32
text_font = "Arial"
text_size = 10
button_font = "Agency FB"
button_size = 26

#------------COLOR PALETTE--------------------
bkground = "#ffffff"
heading_color = "#1e365c"
sub_heading_color = "#000000"
text = "#1e365c"

"""----------------------------Global Functions------------------------------- """
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
def samp_quant_demo(pic_n):
    if(pic_n==0):
        return ("Graphic_Content\samp_quant_illustrations\\5.png")
    elif(pic_n==1):
        return ("Graphic_Content\samp_quant_illustrations\\6.png")
    elif(pic_n==2):
        return ("Graphic_Content\samp_quant_illustrations\\7.png")
    else:
        return ("Graphic_Content\samp_quant_illustrations\\8.png")
"""
Functions that are independent IP operations :

> guibase.py (grayscale)
> geomterictrans.py (afflinetrans)
> basic_arithmetic.py (image arithmetic)
> gamma_correction.py (gammacorrection)
> thresholding.py (threshold)
> histogram_equivalence.py (histogram_gen)
> smoothing.py (smoothing)
"""


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


"""----------------------------Classes------------------------------- """
class DipApp(tk.Tk):
    """
    =========================================================================
    This is the main class that encompasses the the DIPTA Desktop Application
    
    It consists of 2 member functions :
    > __init__()
    > show_frame()
    =========================================================================
    """

    def __init__(self, *args, **kwargs):
        """
        Task : Constructor method; it assigns all the respective pages of the application to a DipApp object
        """
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=48, weight="bold")

        # Container into which the frames go
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        #-----Initializing the multiple frames-------------
        """ Each frame represents a page """
        self.frames={}
        for F in (StartPage, Menu, Image_Def, Eye, Sampling_Quantization, Dist_Measure, Intensity_Trans1, Intensity_Trans2, 
                  Dip_Core, Image_Enhancement, Neighbours):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self,page_name):
        """
        Task : Display a respective page (page_name)
        """
        frame = self.frames[page_name]
        frame.tkraise()


'''StartPage GUI'''
class StartPage(tk.Frame):
    """
    =========================================================================
    Home page of the app
    
    It consists of 2 member functions :
    > about_this_popup()
    > __init__()
    =========================================================================
    """    
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent, bg=bkground) # we have set background to white
        self.controller = controller
        
        #-----DIPTA LOGO------
        icon = PhotoImage(file="Graphic_Content\main_logo.png")
        image_label = Label(self, image=icon, bg=bkground)
        image_label.image = icon
        image_label.place(x=250, y=80)
        
        #------START BUTTON------
        start_button = Button(self, text='START', font=(button_font, button_size),
                              bg='#1e365c', 
                              fg='white', height=1, width=10,
                              command=lambda: controller.show_frame("Menu"))
        start_button.place(x=380,y=550)
        
        #------ABOUT THE PROJECT BUTTON-------
        about_proj = PhotoImage(file="Graphic_Content\\about_project.png")
        about_button = Button(self, image=about_proj, bg='white', height=50, width=50, command=about_this_popup)
        about_button.image = about_proj
        about_button.place(x=20,y=570)

class Menu(tk.Frame):
    """
    =========================================================================
    - Main menu page of the app
    - 9 different choices
    
    It consists of 1 member function :
    > __init__()
    =========================================================================
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=bkground)
        self.controller = controller
        
        #------HEADING LABEL--------------
        title = Label(self, text="Main Menu", font=(heading_font, heading_size, "bold"),
                      bg="#ffffff", fg='#1e365c')
        title.pack()
        
        #------IMAGE DEFINITION BUTTON------
        definition = PhotoImage(file="Graphic_Content\definitions.png") #IMAGE
        def_button = Button(self, image=definition, bg='white',
                            command=lambda: controller.show_frame("Image_Def"))
        def_button.image = definition  # keep a reference of the image
        def_button.place(x=100, y=100)
        
        #------HUMAN EYE DIAGRAM BUTTON------
        eye = PhotoImage(file="Graphic_Content\human_eye.png") #IMAGE
        eye_button = Button(self, image=eye, bg='white',
                            command=lambda: controller.show_frame("Eye"))
        eye_button.image = eye  # keep a reference of the image
        eye_button.place(x=375, y=100)
        
        #------SAMPLING AND QUANTIZATION BUTTON------
        definition = PhotoImage(file="Graphic_Content\sampling_quant.png") #IMAGE
        def_button = Button(self, image=definition, bg='white',
                            command=lambda: controller.show_frame("Sampling_Quantization"))
        def_button.image = definition  # keep a reference of the image
        def_button.place(x=650, y=100)
        
        #------PIXEL NEIGHBOURS BUTTON------
        basics = PhotoImage(file="Graphic_Content\\neighbours.png") #IMAGE
        basics_button = Button(self, image=basics, bg='white',
                               command=lambda: controller.show_frame("Neighbours"))
        basics_button.image = basics  # keep a reference of the image
        basics_button.place(x=100, y=250)
        
        #------DISTANCE MEASURES BUTTON------
        definition = PhotoImage(file="Graphic_Content\distance_measures.png") #IMAGE
        def_button = Button(self, image=definition, bg='white', 
                            command=lambda: controller.show_frame("Dist_Measure"))
        def_button.image = definition  # keep a reference of the image
        def_button.place(x=375, y=250)
        
        #------INTENSITY TRANSFORMATIONS BUTTON------
        dip = PhotoImage(file="Graphic_Content\intensity_trans.png") #IMAGE
        dip_button = Button(self, image=dip, bg='white',
                            command=lambda: controller.show_frame("Intensity_Trans1"))
        dip_button.image = dip  # keep a reference of the image
        dip_button.place(x=650, y=250)
        
        #------COLOR IMAGE PROCESSING BUTTON------
        dip = PhotoImage(file="Graphic_Content\cip.png") #IMAGE
        dip_button = Button(self, image=dip, bg='white',
                            command=lambda: controller.show_frame("Dip_Core"))
        dip_button.image = dip  # keep a reference of the image
        dip_button.place(x=100, y=400)
        
        #------MORPHOLOGICAL IMAGE PROCESSING BUTTON------
        dip = PhotoImage(file="Graphic_Content\mip.png") #IMAGE
        dip_button = Button(self, image=dip, bg='white',
                            command=lambda: controller.show_frame("Dip_Core"))
        dip_button.image = dip  # keep a reference of the image
        dip_button.place(x=375, y=400)
        
        #------IMAGE SEGMENTATION BUTTON------
        dip = PhotoImage(file="Graphic_Content\image_seg.png") #IMAGE
        dip_button = Button(self, image=dip, bg='white',
                            command=lambda: controller.show_frame("Dip_Core"))
        dip_button.image = dip  # keep a reference of the image
        dip_button.place(x=650, y=400)

        #------BACK BUTTON------
        back = PhotoImage(file="Graphic_Content\\back_button.png")
        back_button = Button(self, image=back, bg='white', height=30, width=40, command=lambda: controller.show_frame("StartPage"))
        back_button.image = back
        back_button.place(x=20, y=600)
        
        #------FORWARD BUTTON------ # ADD FUNCTIONALITY HERE
        back = PhotoImage(file="Graphic_Content\\forward_button.png")
        back_button = Button(self, image=back, bg='white', height=30, width=40, command=lambda: controller.show_frame("StartPage"))
        back_button.image = back
        back_button.place(x=830, y=600)


class Image_Def(tk.Frame):
    """
    =========================================================================
    - Image Definition page
    - Defintion of image, pixel
    - Types of images
    
    It consists of 1 member function :
    > __init__()
    =========================================================================
    """   
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=bkground) #sets background to orange
        self.controller = controller

        #--------HEADING LABEL------------------
        title = Label(self, text="The Image", font=(heading_font, heading_size, "bold"),
                      bg="#ffffff", fg='#1e365c')
        title.pack()
        
        #--------DEFINITION OF AN IMAGE----------------        
        definition_im = Label(self, text="Image Definition", font=(sub_heading_font, sub_heading_size), bg="#ffffff", fg="#000000")
        definition_im.place(x=100,y=100)
        answer_im = Label(self, text="An image is defined as a two dimensional function, F(x,y) "
                       "where x and y are spatial coordinates,\n"
                       "and the amplitude of F at any pair of coordinates (x,y) is the intensity of that point"
                       ,bg="#ffffff", fg='#1e365c', justify=LEFT)
        answer_im.place(x=100, y=160)
        
        #------------DEFINITION OF A PIXEL------------
        definition_px = Label(self, text="Pixel Definition", font=(sub_heading_font, sub_heading_size), bg="#ffffff", fg="#000000")
        definition_px.place(x=100,y=200)
        answer_px = Label(self, text="> Smallest addressable element OR the most basic unit in an image\n"
                       "> A pixel's value gives the intensity of the pixel\n"
                       "> For an N-bit gray-scale image, each pixel can have a value between 0 and (N-1)\n"
                       ,bg="#ffffff", fg='#1e365c', justify=LEFT)
        answer_px.place(x=100, y=260)
        
        #-----------TYPES OF IMAGES------------------
        img_type = Label(self, text="Types of Images", font=(sub_heading_font, sub_heading_size), bg="#ffffff", fg="#000000")
        img_type.place(x=100,y=310)
        types= PhotoImage(file="Graphic_Content\\image_types.png")
        types_button = Label(self, image=types, bg='white',height=80, width=400, justify=CENTER)
        types_button.image = types
        types_button.place(x=100, y=400)

        #------BACK BUTTON------
        back = PhotoImage(file="Graphic_Content\\back_button.png")
        back_button = Button(self, image=back, bg='white', height=30, width=40, command=lambda: controller.show_frame("Menu"))
        back_button.image = back
        back_button.place(x=20, y=600)

class Eye(tk.Frame):
    """
    =========================================================================
    - Diagrammatic Representation of the Human Eye
    
    It consists of 1 member function :
    > __init__()
    =========================================================================
    """ 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=bkground) #sets background to orange
        self.controller = controller

        #--------HEADING LABEL------------------
        title = Label(self, text="The Human Eye Anatomy", font=(heading_font, heading_size, "bold"),
                      bg="#ffffff", fg='#1e365c')
        title.pack()
        
        #----------THE HUMAN EYE ANATOMY DIAGRAM-----------------
        diagram_eye = PhotoImage(file="Graphic_Content\\eye_anatomy.png") #IMAGE
        dia_label = Label(self, image=diagram_eye, bg='#ffffff')
        dia_label.image = diagram_eye  # keep a reference of the image
        dia_label.pack()

        #------BACK BUTTON------
        back = PhotoImage(file="Graphic_Content\\back_button.png")
        back_button = Button(self, image=back, bg='white', height=30, width=40, command=lambda: controller.show_frame("Menu"))
        back_button.image = back
        back_button.place(x=20, y=600)
        
class Sampling_Quantization(tk.Frame):
    """
    =========================================================================
    - Sampling and Quantization Basics
    - Working Example
    
    It consists of 4 members function :
    > __init__()
    > show_next()
    > incr()
    > decr()
    =========================================================================
    """ 
    pic_n = 0
                                  
    def show_next(self):
        image_path = samp_quant_demo(self.pic_n)
        img = cv2.imread(image_path)
        cv2.imshow("Sampling and Quantization", img)
        
    def incr(self):
        self.pic_n = self.pic_n+1
        self.show_next()
            
    def decr(self):
        self.pic_n = self.pic_n-1
        self.show_next()
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=bkground) #sets background to orange
        self.controller = controller

        #--------HEADING LABEL------------------
        title = Label(self, text="Sampling and Quantization", font=(heading_font, heading_size, "bold"),
                      bg="#ffffff", fg='#1e365c')
        title.pack()
        
        #---------DEFINITIONS-------------------
        definition_sa = Label(self, text="Sampling", font=(sub_heading_font, sub_heading_size), bg="#ffffff", fg="#000000")
        definition_sa.place(x=100,y=100)
        answer_sa = Label(self, text="It is the discretization of SPATIAL COORDINATES."
                       ,bg="#ffffff", fg='#1e365c', justify=LEFT)
        answer_sa.place(x=100, y=160)
        
        definition_qt = Label(self, text="Quantization", font=(sub_heading_font, sub_heading_size), bg="#ffffff", fg="#000000")
        definition_qt.place(x=100,y=200)
        answer_qt = Label(self, text="It is the discretization of INTENSITY VALUES."
                       ,bg="#ffffff", fg='#1e365c', justify=LEFT)
        answer_qt.place(x=100, y=260)
        
        #------PREVIOUS BUTTON------
        prev = PhotoImage(file="Graphic_Content\\prev_button.png")
        prev_button = Button(self, image=prev, bg='white', height=30, width=40, command=self.decr)
        prev_button.image = prev
        prev_button.place(x=150, y=400)
        
        #------NEXT BUTTON------
        nex = PhotoImage(file="Graphic_Content\\next_button.png")
        nex_button = Button(self, image=nex, bg='white', height=30, width=40, command=self.incr)
        nex_button.image = nex
        nex_button.place(x=750, y=400)
        
        #-----------QUANTIZATION DEMO--------------
        image_path = samp_quant_demo(self.pic_n)
        
        self.demo_img = PhotoImage(file=image_path) #IMAGE
        self.demo_label = Label(self, image=self.demo_img, bg='#ffffff',height=300, width=300,justify=CENTER)
        self.demo_label.image = self.demo_img  # keep a reference of the image
        self.demo_label.place(x=300, y=280)
        
        #------BACK BUTTON------
        back = PhotoImage(file="Graphic_Content\\back_button.png")
        back_button = Button(self, image=back, bg='white', height=30, width=40, command=lambda: controller.show_frame("Menu"))
        back_button.image = back
        back_button.place(x=20, y=600)
        
class Neighbours(tk.Frame):
    """
    =========================================================================
    - Working Demo of neighbours of a pixel
    
    It consists of 1 member function :
    > __init__()
    =========================================================================
    """ 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=bkground) #sets background to orange
        self.controller = controller

        #--------HEADING LABEL------------------
        title = Label(self, text="Neighbours of a Pixel", font=(heading_font, heading_size, "bold"),
                      bg="#ffffff", fg='#1e365c')
        title.pack()
        
        #------------BUTTON FUNCTIONALITIES----------------
        def neighbours4():
            reset()
            highlight = "red"
            p2.config(bg=highlight)
            p4.config(bg=highlight)
            p7.config(bg=highlight)
            p9.config(bg=highlight)

        def neighboursd():
            reset()
            highlight = "red"
            p1.config(bg=highlight)
            p3.config(bg=highlight)
            p5.config(bg=highlight)
            p8.config(bg=highlight)

        def neighbours8():
            reset()
            highlight = "red"
            p2.config(bg=highlight)
            p4.config(bg=highlight)
            p7.config(bg=highlight)
            p9.config(bg=highlight)
            p1.config(bg=highlight)
            p3.config(bg=highlight)
            p5.config(bg=highlight)
            p8.config(bg=highlight)

        def reset():
            normal = "#96b7c8"
            p1.config(bg=normal)
            p2.config(bg=normal)
            p3.config(bg=normal)
            p4.config(bg=normal)
            p5.config(bg=normal)
            p7.config(bg=normal)
            p8.config(bg=normal)
            p9.config(bg=normal)

        #-------------THE PIXEL SIMULATION------------
        p1 = Button(self, height=5, width=10, bg='#96b7c8')
        p1.place(x=300, y=100)
        p2 = Button(self, height=5, width=10, bg='#96b7c8')
        p2.place(x=300, y=190)
        p3 = Button(self, height=5, width=10, bg='#96b7c8')
        p3.place(x=300, y=280)
        p4 = Button(self, height=5, width=10, bg='#96b7c8')
        p4.place(x=385, y=100)
        p5 = Button(self, height=5, width=10, bg='#96b7c8')
        p5.place(x=470, y=100)
        p6 = Button(self, height=5, width=10, bg='#1e365c')
        p6.place(x=385, y=190)
        p7 = Button(self, height=5, width=10, bg='#96b7c8')
        p7.place(x=385, y=280)
        p8 = Button(self, height=5, width=10, bg='#96b7c8')
        p8.place(x=470, y=280)
        p9 = Button(self, height=5, width=10, bg='#96b7c8')
        p9.place(x=470, y=190)
        
        #----------PLACING THE BUTTONS---------------------
        n4p = Button(self, text="N4P Neighbours", font=(button_font, 15),
                     bg='#1e365c', fg='white', height=1, width=15,command=neighbours4)
        n4p.place(x=650, y=110)

        ndp = Button(self, text="NDP Neighbours", font=(button_font, 15),
                     bg='#1e365c', fg='white', height=1, width=15, command=neighboursd)
        ndp.place(x=650, y=210)

        n8p = Button(self, text="N8P Neighbours", font=(button_font, 15), 
                     bg='#1e365c', fg='white', height=1, width=15, command=neighbours8)
        n8p.place(x=650, y=310)

        restButton = Button(self, text="Reset", font=(button_font, 15),
                            bg='#1e365c', fg='white', height=1, width=15, command=reset)
        restButton.place(x=400, y=500)
        
        #------BACK BUTTON------
        back = PhotoImage(file="Graphic_Content\\back_button.png")
        back_button = Button(self, image=back, bg='white', height=30, width=40, command=lambda: controller.show_frame("Menu"))
        back_button.image = back
        back_button.place(x=20, y=600)

class Dist_Measure(tk.Frame):
    """
    =========================================================================
    - Distance Measures Formulae
    - Static Page
    
    It consists of 1 member function :
    > __init__()
    =========================================================================
    """ 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=bkground) #sets background to orange
        self.controller = controller

        #--------HEADING LABEL------------------
        title = Label(self, text="Distance Measures", font=(heading_font, heading_size, "bold"),
                      bg="#ffffff", fg='#1e365c')
        title.pack()
        
        #--------FORMULAE GRAPHIC--------------
        form = PhotoImage(file="Graphic_Content\dist_measures.png")
        form_label = Label(self, image=form, bg=bkground)
        form_label.image = form
        form_label.place(x=250, y=80)
        
        #------BACK BUTTON------
        back = PhotoImage(file="Graphic_Content\\back_button.png")
        back_button = Button(self, image=back, bg='white', height=30, width=40, command=lambda: controller.show_frame("Menu"))
        back_button.image = back
        back_button.place(x=20, y=600)
        

class Intensity_Trans1(tk.Frame):
    """
    =========================================================================
    - Basic Constant Arithmetic of Images
    
    It consists of 3 member functions :
    > add_img()
    > sub_img()
    > thresh()
    > __init__()
    =========================================================================
    """ 
    def add_img(self):
        img = cv2.imread("Input_Images\\doggo.png",0) # load it in grayscale
        const = float(self.const_value.get())
        img = cv2.add(img,const)
        cv2.imshow("Adding a Constant", img)
        
    def sub_img(self):
        img = cv2.imread("Input_Images\\doggo.png",0) # load it in grayscale
        const = -(float(self.const_value.get()))
        img = cv2.add(img,const)
        cv2.imshow("Adding a Constant", img)
        
    def thresh(self):
        img = cv2.imread("Input_Images\\doggo.png",0) # load it in grayscale
        thresh = float(self.thresh_value.get())
        retval, threshold = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
        cv2.imshow("Thresholded Image", threshold)
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=bkground) #sets background to orange
        self.controller = controller

        #--------HEADING LABEL------------------
        title = Label(self, text="Intensity Transformations", font=(heading_font, heading_size, "bold"),
                      bg="#ffffff", fg='#1e365c')
        title.pack()
        
        #-------BASIC ARITHMETIC ON IMAGES--------------
        arith = Label(self, text="Basic Arithmetic - With Constant", font=(sub_heading_font, sub_heading_size),
                      bg="#ffffff", fg=sub_heading_color)
        arith.place(x=100, y=100)
        
        #--------------INPUT IMAGE---------------------
        #doggo = PhotoImage(file="Input_Images\dog.jpg")
        doggo=PhotoImage(file="Input_Images\\doggo.png")
        doggo_label = Label(self, image=doggo, bg=bkground)
        doggo_label.image = doggo
        doggo_label.place(x=100, y=180)
        
        #-----------ADD / SUBTRACT BUTTON SET------------
        add = PhotoImage(file="Graphic_Content\\add.png")
        add_button = Button(self, image=add , bg='white', height=80, width=80, command=self.add_img)
        add_button.image = add 
        add_button.place(x=400, y=240)
        
        sub = PhotoImage(file="Graphic_Content\\subtract.png")
        sub_button = Button(self, image=sub, bg='white', height=80, width=80, command=self.sub_img)
        sub_button.image = sub
        sub_button.place(x=600, y=240)
        
        #----------ENTRY BOX FOR ENTERING CONSTANT VALUE---------------
        value_label = Label(self, text="Enter the Constant", font=(sub_heading_font, 20),
                      bg="#ffffff", fg=sub_heading_color)
        value_label.place(x=400, y=370)
        self.const_value = Entry(self, bg='white')
        self.const_value.place(x=570, y=380)
        
        #-----------THRESHOLDING THE IMAGE-------------------
        thresh = Label(self, text="Thresholding Image", font=(sub_heading_font, sub_heading_size),
                      bg="#ffffff", fg=sub_heading_color)
        thresh.place(x=100, y=430)
        
        #----------ENTRY BOX FOR ENTERING THRESHOLD VALUE---------------
        thresh_label = Label(self, text="Enter the Threshold", font=(sub_heading_font, 20),
                      bg="#ffffff", fg=sub_heading_color)
        thresh_label.place(x=100, y=500)
        self.thresh_value = Entry(self, bg='white')
        self.thresh_value.place(x=270, y=510)
        
        #------PLAY BUTTON------
        play = PhotoImage(file="Graphic_Content\\next_button.png")
        play_button = Button(self, image=play, bg='white', height=30, width=40, command=self.thresh)
        play_button.image = play
        play_button.place(x=500, y=500)
        
        #------BACK BUTTON------
        back = PhotoImage(file="Graphic_Content\\back_button.png")
        back_button = Button(self, image=back, bg='white', height=30, width=40, command=lambda: controller.show_frame("Menu"))
        back_button.image = back
        back_button.place(x=20, y=600)
        
        #------FORWARD BUTTON------
        back = PhotoImage(file="Graphic_Content\\forward_button.png")
        back_button = Button(self, image=back, bg='white', height=30, width=40, command=lambda: controller.show_frame("Intensity_Trans2"))
        back_button.image = back
        back_button.place(x=830, y=600)
        
class Intensity_Trans2(tk.Frame):
    """
    =========================================================================
    - Basic Intensity Transformation Operations
    - Histogram Processing
    
    It consists of 1 member function :
    > __init__()
    =========================================================================
    """ 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=bkground) #sets background to orange
        self.controller = controller

        #--------HEADING LABEL------------------
        title = Label(self, text="Intensity Transformations", font=(heading_font, heading_size, "bold"),
                      bg="#ffffff", fg='#1e365c')
        title.pack()
        
        #-------BASIC ARITHMETIC ON IMAGES--------------
        trans_basic = Label(self, text="Basic Transformations", font=(sub_heading_font, sub_heading_size),
                      bg="#ffffff", fg=sub_heading_color)
        trans_basic.place(x=100, y=100)
        
        
         #------BACK BUTTON------
        back = PhotoImage(file="Graphic_Content\\back_button.png")
        back_button = Button(self, image=back, bg='white', height=30, width=40, command=lambda: controller.show_frame("Intensity_Trans1"))
        back_button.image = back
        back_button.place(x=20, y=600)
        
        #------FORWARD BUTTON------ # ADD FUNCTIONALITY HERE
        back = PhotoImage(file="Graphic_Content\\forward_button.png")
        back_button = Button(self, image=back, bg='white', height=30, width=40, command=lambda: controller.show_frame("StartPage"))
        back_button.image = back
        back_button.place(x=830, y=600)

class Dip_Core(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=bkground) #sets background to orange
        self.controller = controller

        #--------HEADING LABEL------------------
        title = Label(self, text="Intensity Transformations", font=(heading_font, heading_size, "bold"),
                      bg="#ffffff", fg='#1e365c')
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

        #------BACK BUTTON------
        back = PhotoImage(file="Graphic_Content\\back_button.png")
        back_button = Button(self, image=back, bg='white', height=30, width=40, command=lambda: controller.show_frame("Menu"))
        back_button.image = back
        back_button.place(x=20, y=600)

class Image_Enhancement(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black') #sets background to orange
        self.controller = controller




        '''we need a back button now'''
        back = Button(self, text="Go Back", font=('Helvetica', 18),
                      padx=5, pady=5, command=lambda: controller.show_frame("Basics"))
        back.place(x=770, y=580)
        '''Back button placed'''

"""--------------------Main Control Flow------------------"""
if __name__ == "__main__":
    app = DipApp()
    # to set the dimensions of the window
    app.geometry("900x650")
    app.resizable(width=False, height=False)
    app.configure(background='white')
    app.mainloop()
