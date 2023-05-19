import tkinter
import turtle
from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
import time
from tkinter import messagebox



def main():

    root=Tk()
    app=window1(root)

    root.mainloop()






class window1:

    def __init__(self,master):

        self.master=master
        self.master.title("FOOD APP")
        self.master.geometry("700x700")
        self.frame=Frame(self.master)
        self.frame.pack()


        self.frame1=Label(self.frame,text="welocome to zomato ".center(20),font=("arial 15 bold",40),bg="gray19",fg="white",
                         relief="sunken",width=40,height=1)
        self.frame1.grid(row=0,column=0)

        self.frame2 = Label(self.frame, text="WHAT'S IN YOUR MIND".center(20,"!"), font=("arial 15 bold", 20), bg="hotpink4"
                            ,fg="chartreuse2",
                           relief="sunken", width=50,height=2)
        self.frame2.grid(row=1,column=0,padx=100)
        self.frame4 = Frame(self.master, bd=15, padx=20, relief=RIDGE,background="black")
        self.frame4.place(x=0, y=120, width=1370, height=550)

 #####################################biryani##################################################
        img1 = Image.open('D:\pythonProject6\pppp\Screenshot (356).png')
        img1 = img1.resize((100, 100),Image.ANTIALIAS)
        self.photo_img1 = ImageTk.PhotoImage(img1)
        b1 = Button(self.frame4, image=self.photo_img1, borderwidth=0,command=self.briyani_window)
        b1.grid(row=0, column=0)

        bir_name = Label(self.frame4, text="Briyani", font=("arial 15 bold", 20),
                            bg="gray60"
                            , fg="black",
                            relief="sunken", width=8, height=1)
        bir_name.grid(row=9, column=0,padx=100,pady=10)
########################################################################################################################


###########################################ice cream####################################################################
        img2 = Image.open('D:\pythonProject6\pppp\Screenshot (358).png')
        img2 = img2.resize((100, 100), Image.ANTIALIAS)
        self.photo_img2 = ImageTk.PhotoImage(img2)
        b2 = Button(self.frame4, image=self.photo_img2, borderwidth=0,padx=10,command=self.iceCream_window)
        b2.grid(row=0, column=4)

        ice_name = Label(self.frame4, text="Ice cream", font=("arial 15 bold", 20),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=5, height=1,padx=20)
        ice_name.grid(row=9, column=4,padx=100)
###########################################pizza  #############################################################3
        img3 = Image.open('D:\pythonProject6\pppp\pizza\pizzaaa\Screenshot (369).png')
        img3 = img3.resize((100, 100))
        self.photo_img3 = ImageTk.PhotoImage(img3)
        b3 = Button(self.frame4, image=self.photo_img3, borderwidth=0, padx=10,command=self.pizza_window)
        b3.grid(row=0, column=6)

        pizz_name = Label(self.frame4, text="Pizza", font=("arial 15 bold", 20),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=5, height=1, padx=20)
        pizz_name.grid(row=9, column=6, padx=100)
################################################################################################################3


####################################parrota#########################################################################

        img4 = Image.open('D:\pythonProject6\parota1\Screenshot (372).png')
        img4 = img4.resize((100, 100))
        self.photo_img4 = ImageTk.PhotoImage(img4)
        b4 = Button(self.frame4, image=self.photo_img4, borderwidth=0, padx=10,command=self.Parotta_window)
        b4.grid(row=0, column=8)

        paro_name = Label(self.frame4, text="Parotta", font=("arial 15 bold", 20),
                          bg="gray60"
                          , fg="black",
                          relief="sunken", width=5, height=1, padx=20)
        paro_name.grid(row=9, column=8, padx=100)
############################################################################################################3

##############################################burger################################################3
        img5 = Image.open('D:\\pythonProject6\\burger\\Screenshot (373).png')
        img5 = img5.resize((100, 100))
        self.photo_img5 = ImageTk.PhotoImage(img5)
        b5 = Button(self.frame4, image=self.photo_img5, borderwidth=0, padx=10,command=self.burger_window)
        b5.grid(row=15, column=0)

        paro_name = Label(self.frame4, text="Burger", font=("arial 15 bold", 20),
                          bg="gray60"
                          , fg="black",
                          relief="sunken", width=7, height=1)
        paro_name.grid(row=16, column=0,padx=100,pady=10)
###########################################################################################################


#######################################shake#############################################3
        img6 = Image.open('D:\pythonProject6\shake\Screenshot (374).png')
        img6 = img6.resize((100, 100), Image.ANTIALIAS)
        self.photo_img6 = ImageTk.PhotoImage(img6)
        b6 = Button(self.frame4, image=self.photo_img6, borderwidth=0, padx=10,command=self.shakke_window)
        b6.grid(row=15, column=4)

        ice_name = Label(self.frame4, text="Shake", font=("arial 15 bold", 20),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=5, height=1, padx=20)
        ice_name.grid(row=16, column=4, padx=100)
########################################################################################################


##############################################Rice#####################################################
        img7 = Image.open('D:\pythonProject6\jjjjjjj1\Screenshot (376).png')
        img7 = img7.resize((100, 100))
        self.photo_img7 = ImageTk.PhotoImage(img7)
        b7 = Button(self.frame4, image=self.photo_img7, borderwidth=0, padx=10,command=self.rice_window)
        b7.grid(row=15, column=6)

        pizz_name = Label(self.frame4, text="Rice", font=("arial 15 bold", 20),
                          bg="gray60"
                          , fg="black",
                          relief="sunken", width=5, height=1, padx=20)
        pizz_name.grid(row=16, column=6, padx=100)
#########################################################################################################

#############################################cake################################################################
        img8 = Image.open('D:\pythonProject6\jjjjjjj1\WhatsApp Image 2023-03-15 at 1.51.34 PM (2).jpeg')
        img8 = img8.resize((100, 100))
        self.photo_img8 = ImageTk.PhotoImage(img8)
        b8 = Button(self.frame4, image=self.photo_img8, borderwidth=0, padx=10,command=self.Cake_window)
        b8.grid(row=15, column=8)

        pizz_name = Label(self.frame4, text="Cake", font=("arial 15 bold", 20),
                          bg="gray60"
                          , fg="black",
                          relief="sunken", width=5, height=1, padx=20)
        pizz_name.grid(row=16, column=8, padx=100)

#####################################################################################################

########################33##########Fries#############################################################
        img9 = Image.open('D:\pythonProject6\jjjjjjj1\\fries\Screenshot (378).png')
        img9 = img9.resize((100, 100))
        self.photo_img9 = ImageTk.PhotoImage(img9)
        b9 = Button(self.frame4, image=self.photo_img9, borderwidth=0, padx=10,command=self.fries_window)
        b9.grid(row=17, column=0)

        paro_name = Label(self.frame4, text="Fries", font=("arial 15 bold", 20),
                          bg="gray60"
                          , fg="black",
                          relief="sunken", width=7, height=1)
        paro_name.grid(row=18, column=0, padx=100, pady=10)

##########################################################################################################3

#############################################Juices####################################################
        img10 = Image.open('D:\pythonProject6\jjjjjjj1\juices\Screenshot (379).png')
        img10 = img10.resize((100, 100), Image.ANTIALIAS)
        self.photo_img10 = ImageTk.PhotoImage(img10)
        b10 = Button(self.frame4, image=self.photo_img10, borderwidth=0, padx=10,command=self.juices_window)
        b10.grid(row=17, column=4)

        ice_name = Label(self.frame4, text="Juices", font=("arial 15 bold", 20),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=5, height=1, padx=20)
        ice_name.grid(row=18, column=4, padx=100)
#######################################################################################################

#################################################chatts###########################################
        img11 = Image.open('D:\pythonProject7\\nattii\mango\Screenshot (516).png')
        img11 = img11.resize((100, 100))
        self.photo_img11 = ImageTk.PhotoImage(img11)
        b11 = Button(self.frame4, image=self.photo_img11, borderwidth=0, padx=10,command=self.chatts_window)
        b11.grid(row=17, column=6)

        pizz_name = Label(self.frame4, text="SWEETS", font=("arial 15 bold", 20),
                          bg="gray60"
                          , fg="black",
                          relief="sunken", width=5, height=1, padx=20)
        pizz_name.grid(row=18, column=6, padx=100)
##########################################################################################################

######################################rolls#####################################################################
        img12 = Image.open('D:\pythonProject6\jjjjjjj1\juices\\1rolls1\Screenshot (381).png')
        img12 = img12.resize((100, 100))
        self.photo_img12 = ImageTk.PhotoImage(img12)
        b12 = Button(self.frame4, image=self.photo_img12, borderwidth=0, padx=10,command=self.rolls_window)
        b12.grid(row=17, column=8)

        pizz_name = Label(self.frame4, text="Rolls", font=("arial 15 bold", 20),
                      bg="gray60"
                      , fg="black",
                      relief="sunken", width=5, height=1, padx=20)
        pizz_name.grid(row=18, column=8, padx=100)


    def briyani_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=window2(self.newWindow)
    def iceCream_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=window3(self.newWindow)
    def pizza_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=window4(self.newWindow)
    def Parotta_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=window5(self.newWindow)
    def burger_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = window6(self.newWindow)
    def shakke_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = window7(self.newWindow)
    def rice_window(self):
       self.newWindow = Toplevel(self.master)
       self.app = window8(self.newWindow)
    def Cake_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = window9(self.newWindow)
    def fries_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = window10(self.newWindow)
    def juices_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = window11(self.newWindow)
    def chatts_window(self):
       self.newWindow = Toplevel(self.master)
       self.app = window12(self.newWindow)
    def rolls_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = window13(self.newWindow)


class window2:

    def __init__(self,master):
        self.master=master
        self.master.geometry("700x700")
        self.master.title("briyani session")
        self.frame=Frame(self.master)
        self.frame.pack()



        img13 = Image.open('D:\pythonProject6\jjjjjjj1\jiffff\Screenshot (389).png')
        img13 = img13.resize((120, 120))
        self.photo_img13 = ImageTk.PhotoImage(img13)
        b13 = Button(self.frame,image=self.photo_img13, borderwidth=0)
        b13.grid(row=0, column=0,pady=10)

        self.frame1 = Label(self.frame, text="Briyani".center(20), font=("arial 15 bold", 40), bg="gray15",
                            fg="white", bd=2,
                            relief="sunken", width=30, height=2)
        self.frame1.grid(row=0, column=2, padx=80,pady=10,columnspan=3)#2

        img14 = Image.open('D:\pythonProject6\jjjjjjj1\jiffff\ymmy\Screenshot (390).png')
        img14 = img14.resize((120, 120),Image.ANTIALIAS)
        self.photo_img14 = ImageTk.PhotoImage(img14)
        b14 = Button(self.frame, image=self.photo_img14, borderwidth=0)
        b14.grid(row=0, column=5)#5


#########################################################################################################3####3

########################################UNDER frame2########################################################

        self.Loginframe1 = Frame(self.frame, width=720, height=560, bd=10, relief="groove")
        self.Loginframe1.grid(row=1, column=0,columnspan=3)

        self.Loginframe2 = Frame(self.frame, width=600, height=560, bd=10, relief="groove")
        self.Loginframe2.grid(row=1, column=4,columnspan=3)

        self.Loginframe3 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE,bg="black",pady=15,padx=10)
        self.Loginframe3.place(x=0, y=0)

        self.Loginframe4 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black",pady=5)
        self.Loginframe4.place(x=0, y=180)

        self.Loginframe5 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black",pady=15)
        self.Loginframe5.place(x=0, y=360)
##################################################################################################################3



        img16 = Image.open('D:\pythonProject6\\burger\\nell\Screenshot (394).png')
        img16 = img16.resize((100, 100))
        self.photo_img16 = ImageTk.PhotoImage(img16)
        b16 = Button(self.Loginframe1, image=self.photo_img16, borderwidth=3,padx=10,pady=5)
        b16.place(x=20,y=10)
        nell_name = Label(self.Loginframe1, text="Nellore-Briyani\nRs-100", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        nell_name.place(x=15,y=120)

        img17 = Image.open('D:\pythonProject6\\burger\\nell\khema\Screenshot (395).png')
        img17 = img17.resize((100, 100))
        self.photo_img17 = ImageTk.PhotoImage(img17)
        b17 = Button(self.Loginframe1, image=self.photo_img17, borderwidth=3, padx=10, pady=5)
        b17.place(x=300, y=10)
        kehma_name = Label(self.Loginframe1, text="Mutton khema\nRs-100", font=("arial 15 bold", 15),
                          bg="gray60"
                          , fg="black",
                          relief="sunken", width=10, height=2, padx=10)
        kehma_name.place(x=290, y=120)

        img18 = Image.open('D:\pythonProject6\\burger\\nell\\boneless\Screenshot (396).png')
        img18 = img18.resize((100, 100))
        self.photo_img18 = ImageTk.PhotoImage(img18)
        b18 = Button(self.Loginframe1, image=self.photo_img18, borderwidth=3, padx=10, pady=5)
        b18.place(x=550, y=10)
        boneless_name = Label(self.Loginframe1, text="Boneless-Chiken\nRs-100", font=("arial 15 bold", 15),
                           bg="gray60"
                           , fg="black",
                           relief="sunken", width=13, height=2, padx=10)
        boneless_name.place(x=510, y=120)
    ###############################################################################################################
        img19 = Image.open('D:\pythonProject6\\burger\\nell\\boneless\gutur\Screenshot (401).png')
        img19 = img19.resize((100, 100))
        self.photo_img19 = ImageTk.PhotoImage(img19)
        b19 = Button(self.Loginframe4, image=self.photo_img19, borderwidth=3, padx=10,pady=5)
        b19.place(x=20, y=0)
        gut_name = Label(self.Loginframe4, text="Guturu-Briyani\nRs-300", font=("arial 15 bold", 15),
                          bg="gray60"
                          , fg="black",
                          relief="sunken", width=10, height=2, padx=20)
        gut_name.place(x=5, y=100)

        img20 = Image.open('D:\pythonProject6\\burger\\nell\\boneless\gutur\hydra\Screenshot (402).png')
        img20 = img20.resize((100, 100))
        self.photo_img20 = ImageTk.PhotoImage(img20)
        b20 = Button(self.Loginframe4, image=self.photo_img20, borderwidth=3, padx=10, pady=5)
        b20.place(x=300, y=0)
        hyd_name = Label(self.Loginframe4, text="Hyderaba-Briyani\nRs-300", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=20)
        hyd_name.place(x=280, y=100)

        img21 = Image.open('D:\pythonProject7\\nattii\Screenshot (403).png')
        img21 = img21.resize((100, 100))
        self.photo_img21 = ImageTk.PhotoImage(img21)
        b21 = Button(self.Loginframe4, image=self.photo_img21, borderwidth=3, padx=10, pady=5)
        b21.place(x=550, y=0)
        nati_name = Label(self.Loginframe4, text="Nati-StyleBriyani\nRs-300", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=20)
        nati_name.place(x=520, y=100)

        img22 = Image.open('D:\pythonProject7\\nattii\pepper\Screenshot (407).png')
        img22 = img22.resize((100, 100))
        self.photo_img22 = ImageTk.PhotoImage(img22)
        b22 = Button(self.Loginframe5, image=self.photo_img22, borderwidth=3, padx=10, pady=5)
        b22.place(x=20, y=0)
        pepper_name = Label(self.Loginframe5, text="Chicken-pepper\nRs-500", font=("arial 15 bold", 15),
                          bg="gray60"
                          , fg="black",
                          relief="sunken", width=10, height=2, padx=20)
        pepper_name.place(x=5, y=100)

        img23 = Image.open('D:\pythonProject7\\nattii\pepper\lolli\Screenshot (408).png')
        img23 = img23.resize((100, 100))
        self.photo_img23 = ImageTk.PhotoImage(img23)
        b23 = Button(self.Loginframe5, image=self.photo_img23, borderwidth=3, padx=10, pady=5)
        b23.place(x=300, y=0)
        lolli_name = Label(self.Loginframe5, text="Chicken-lollipop\nRs-500", font=("arial 15 bold", 15),
                            bg="gray60"
                            , fg="black",
                            relief="sunken", width=10, height=2, padx=20)
        lolli_name.place(x=280, y=100)

        img24 = Image.open('D:\pythonProject7\\nattii\\pepper\lolli\egggg\Screenshot (409).png')
        img24 = img24.resize((100, 100))
        self.photo_img24 = ImageTk.PhotoImage(img24)
        b24 = Button(self.Loginframe5, image=self.photo_img24, borderwidth=3, padx=10, pady=5)
        b24.place(x=550, y=0)
        dum_name = Label(self.Loginframe5, text="Egg-briyanir\nRs-500", font=("arial 15 bold", 15),
                            bg="gray60"
                            , fg="black",
                            relief="sunken", width=10, height=2, padx=20)
        dum_name.place(x=520, y=100)

        item_ordered=StringVar()
        quatity=IntVar()
        location=StringVar()
        Phone_num=IntVar()
        Total_price=IntVar()


        self.heading=Label(self.Loginframe2,text="Item selected",font=("arial 15 bold",15),bg="black",fg="white"
                           ,relief=RIDGE,padx=10,pady=10,width=10)
        self.heading.place(x=10,y=30)


        self.heading1 = Label(self.Loginframe2, text="Quantity", font=("arial 15 bold", 15), bg="black", fg="white"
                             , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading1.place(x=10, y=120)

        self.heading2 = Label(self.Loginframe2, text="Location", font=("arial 15 bold", 15), bg="black", fg="white"
                             , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading2.place(x=10, y=200)

        self.heading3 = Label(self.Loginframe2, text="Phone_No", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading3.place(x=10, y=280)

        self.heading4 = Label(self.Loginframe2, text="Total-Price", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading4.place(x=10, y=360)

        e1=Entry(self.Loginframe2,width=20,font=("arial 15 bold",20),fg="black",textvariable=item_ordered)
        e1.place(x=250,y=40)#item

        n=tk.StringVar()
        quantity=ttk.Combobox(self.Loginframe2,width=17,textvariable=n,font=("arial 15 bold",10))
        quantity['values']=["1","2","3","4","5","6"]
        quantity.current()
        quantity.place(x=250,y=130)

        e2 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black",textvariable=location)
        e2.place(x=250, y=210)

        e3 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black",textvariable=Phone_num)
        e3.place(x=250, y=290)

        e4 = Entry(self.Loginframe2, width=10, font=("arial 15 bold", 20), fg="black",text=Total_price)
        e4.place(x=250, y=370)

        button1=Button(self.Loginframe2,text="BACK",bg="black",fg="white",width=10,height=2,command=self.back_but)
        button1.place(x=30,y=490)

        button2 = Button(self.Loginframe2, text="ORDER", bg="black", fg="white", width=10, height=2,command=self.order_info)
        button2.place(x=240, y=490)

        button3 = Button(self.Loginframe2, text="EXIT", bg="black", fg="white", width=10, height=2,command=self.exitt_but)
        button3.place(x=440, y=490)
    def exitt_but(shelf):
        exitt_but=tkinter.messagebox.askretrycancel("status","Are you sure you want to exit")
        if exitt>0:
            return self.root
    def back_but(self):
        back_but=tkinter.messagebox.askretrycancel("status","go back to home home")
        if back>0:
            return self.root
    def order_info(self):
        order_but = tkinter.messagebox.askokcancel("status", "your order is placed successfully")
        if order > 0:
            return self.root








#######################################################################################################################

class window3:

        def __init__(self, master):
            self.master = master
            self.master.geometry("700x700")
            self.master.title("Ice Cream")
            self.frame = Frame(self.master)
            self.frame.pack()
###############################################################################################################
            img13 = Image.open('D:\pythonProject6\jjjjjjj1\jiffff\Screenshot (389).png')
            img13 = img13.resize((150, 120))
            self.photo_img13 = ImageTk.PhotoImage(img13)
            b13 = Button(self.frame, image=self.photo_img13, borderwidth=0)
            b13.grid(row=0, column=0, pady=10)

            self.frame1 = Label(self.frame, text="ICE CREAMS".center(20), font=("arial 15 bold", 40), bg="gray15",
                                fg="white", bd=2,
                                relief="sunken", width=30, height=2)
            self.frame1.grid(row=0, column=2, padx=50, pady=10, columnspan=3)  # 2

            img14 = Image.open('D:\pythonProject6\jjjjjjj1\jiffff\ymmy\Screenshot (390).png')
            img14 = img14.resize((150, 120), Image.ANTIALIAS)
            self.photo_img14 = ImageTk.PhotoImage(img14)
            b14 = Button(self.frame, image=self.photo_img14, borderwidth=0)
            b14.grid(row=0, column=5)  # 5
 #################################################################################################################
 #################################Frames#######################################################################
            self.Loginframe1 = Frame(self.frame, width=720, height=560, bd=10, relief="groove")
            self.Loginframe1.grid(row=1, column=0, columnspan=3)

            self.Loginframe2 = Frame(self.frame, width=693, height=560, bd=10, relief="groove")
            self.Loginframe2.grid(row=1, column=4, columnspan=3)

            self.Loginframe3 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black", pady=15,
                                     padx=10)
            self.Loginframe3.place(x=0, y=0)

            self.Loginframe4 = Frame(self.Loginframe1, width=690, height=180, bd=5, relief=RIDGE, bg="black", pady=5)
            self.Loginframe4.place(x=0, y=180)

            self.Loginframe5 = Frame(self.Loginframe1, width=680, height=180, bd=5, relief=RIDGE, bg="black", pady=15)
            self.Loginframe5.place(x=0, y=360)
  #############################################################################################################
  ######################################photo################################################
            img16 = Image.open('D:\pythonProject7\\nattii\pepper\lolli\egggg\ice2\ice4\Screenshot (423).png')
            img16 = img16.resize((100, 100))
            self.photo_img16 = ImageTk.PhotoImage(img16)
            b16 = Button(self.Loginframe1, image=self.photo_img16, borderwidth=3, padx=10, pady=5)
            b16.place(x=20, y=10)
            sud_name = Label(self.Loginframe1, text="Sundae\nRs-60", font=("arial 15 bold", 15),
                              bg="gray60"
                              , fg="black",
                              relief="sunken", width=10, height=2, padx=10)
            sud_name.place(x=15, y=120)

            img17 = Image.open('D:\pythonProject7\\nattii\pepper\lolli\ice6\Screenshot (424).png')
            img17 = img17.resize((100, 100))
            self.photo_img17 = ImageTk.PhotoImage(img17)
            b17 = Button(self.Loginframe1, image=self.photo_img17, borderwidth=3, padx=10, pady=5)
            b17.place(x=300, y=10)
            val_name = Label(self.Loginframe1, text="Vanilla\nRs-90", font=("arial 15 bold", 15),
                               bg="gray60"
                               , fg="black",
                               relief="sunken", width=10, height=2, padx=10)
            val_name.place(x=290, y=120)

            img18 = Image.open('D:\pythonProject7\\nattii\pepper\lolli\ice6\cho\Screenshot (427).png')
            img18 = img18.resize((100, 100))
            self.photo_img18 = ImageTk.PhotoImage(img18)
            b18 = Button(self.Loginframe1, image=self.photo_img18, borderwidth=3, padx=10, pady=5)
            b18.place(x=550, y=10)
            cho_name = Label(self.Loginframe1, text="Chocolate\nRs-100", font=("arial 15 bold", 15),
                                  bg="gray60"
                                  , fg="black",
                                  relief="sunken", width=13, height=2, padx=10)
            cho_name.place(x=510, y=120)

            img19 = Image.open('D:\pythonProject7\\nattii\mango\Screenshot (434).png')
            img19 = img19.resize((100, 100))
            self.photo_img19 = ImageTk.PhotoImage(img19)
            b19 = Button(self.Loginframe4, image=self.photo_img19, borderwidth=3, padx=10, pady=5)
            b19.place(x=20, y=0)
            man_name = Label(self.Loginframe4, text="Mango-IceCream\nRs-100", font=("arial 15 bold", 15),
                             bg="gray60"
                             , fg="black",
                             relief="sunken", width=10, height=2, padx=20)
            man_name.place(x=5, y=100)

            img20 = Image.open('D:\pythonProject7\\nattii\mango\Screenshot (435).png')
            img20 = img20.resize((100, 100))
            self.photo_img20 = ImageTk.PhotoImage(img20)
            b20 = Button(self.Loginframe4, image=self.photo_img20, borderwidth=3, padx=10, pady=5)
            b20.place(x=300, y=0)
            coff_name = Label(self.Loginframe4, text="Coffee-IceCream\nRs-90", font=("arial 15 bold", 15),
                             bg="gray60"
                             , fg="black",
                             relief="sunken", width=10, height=2, padx=20)
            coff_name.place(x=280, y=100)

            img21 = Image.open('D:\pythonProject7\\nattii\mango\Screenshot (436).png')
            img21 = img21.resize((100, 100))
            self.photo_img21 = ImageTk.PhotoImage(img21)
            b21 = Button(self.Loginframe4, image=self.photo_img21, borderwidth=3, padx=10, pady=5)
            b21.place(x=550, y=0)
            straw_name = Label(self.Loginframe4, text="Strawberry-IceCream\nRs-100", font=("arial 15 bold", 15),
                              bg="gray60"
                              , fg="black",
                              relief="sunken", width=10, height=2, padx=20)
            straw_name.place(x=520, y=100)

            img22 = Image.open('D:\pythonProject7\\nattii\mango\Screenshot (437).png')
            img22 = img22.resize((100, 100))
            self.photo_img22 = ImageTk.PhotoImage(img22)
            b22 = Button(self.Loginframe5, image=self.photo_img22, borderwidth=3, padx=10, pady=5)
            b22.place(x=20, y=0)
            fru_name = Label(self.Loginframe5, text="Fruit-IceCream\nRs-500", font=("arial 15 bold", 15),
                                bg="gray60"
                                , fg="black",
                                relief="sunken", width=10, height=2, padx=20)
            fru_name.place(x=5, y=100)

            img23 = Image.open('D:\pythonProject7\\nattii\mango\Screenshot (438).png')
            img23 = img23.resize((100, 100))
            self.photo_img23 = ImageTk.PhotoImage(img23)
            b23 = Button(self.Loginframe5, image=self.photo_img23, borderwidth=3, padx=10, pady=5)
            b23.place(x=300, y=0)
            butt_name = Label(self.Loginframe5, text="ButterScotch\nRs-100", font=("arial 15 bold", 15),
                               bg="gray60"
                               , fg="black",
                               relief="sunken", width=10, height=2, padx=20)
            butt_name.place(x=280, y=100)

            img24 = Image.open('D:\pythonProject7\\nattii\mango\Screenshot (439).png')
            img24 = img24.resize((100, 100))
            self.photo_img24 = ImageTk.PhotoImage(img24)
            b24 = Button(self.Loginframe5, image=self.photo_img24, borderwidth=3, padx=10, pady=5)
            b24.place(x=550, y=0)
            kul_name = Label(self.Loginframe5, text="Kulfi\nRs-100", font=("arial 15 bold", 15),
                             bg="gray60"
                             , fg="black",
                             relief="sunken", width=10, height=2, padx=20)
            kul_name.place(x=520, y=100)
            item_ordered = StringVar()
            quatity = IntVar()
            location = StringVar()
            Phone_num = IntVar()
            Total_price = IntVar()

            self.heading = Label(self.Loginframe2, text="Item selected", font=("arial 15 bold", 15), bg="black",
                                 fg="white"
                                 , relief=RIDGE, padx=10, pady=10, width=10)
            self.heading.place(x=10, y=30)

            self.heading1 = Label(self.Loginframe2, text="Quantity", font=("arial 15 bold", 15), bg="black", fg="white"
                                  , relief=RIDGE, padx=10, pady=10, width=10)
            self.heading1.place(x=10, y=120)

            self.heading2 = Label(self.Loginframe2, text="Location", font=("arial 15 bold", 15), bg="black", fg="white"
                                  , relief=RIDGE, padx=10, pady=10, width=10)
            self.heading2.place(x=10, y=200)

            self.heading3 = Label(self.Loginframe2, text="Phone_No", font=("arial 15 bold", 15), bg="black", fg="white"
                                  , relief=RIDGE, padx=10, pady=10, width=10)
            self.heading3.place(x=10, y=280)

            self.heading4 = Label(self.Loginframe2, text="Total-Price", font=("arial 15 bold", 15), bg="black",
                                  fg="white"
                                  , relief=RIDGE, padx=10, pady=10, width=10)
            self.heading4.place(x=10, y=360)

            e1 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=item_ordered)
            e1.place(x=250, y=40)  # item

            n = tk.StringVar()
            quantity = ttk.Combobox(self.Loginframe2, width=17, textvariable=n, font=("arial 15 bold", 10))
            quantity['values'] = ["1", "2", "3", "4", "5", "6"]
            quantity.current()
            quantity.place(x=250, y=130)

            e2 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=location)
            e2.place(x=250, y=210)

            e3 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=Phone_num)
            e3.place(x=250, y=290)

            e4 = Entry(self.Loginframe2, width=10, font=("arial 15 bold", 20), fg="black", text=Total_price)
            e4.place(x=250, y=370)

            button1 = Button(self.Loginframe2, text="BACK", bg="black", fg="white", width=10, height=2,command=
            self.back_but)
            button1.place(x=30, y=490)

            button2 = Button(self.Loginframe2, text="ORDER", bg="black", fg="white", width=10, height=2,command=
            self.order_info)
            button2.place(x=240, y=490)

            button3 = Button(self.Loginframe2, text="EXIT", bg="black", fg="white", width=10, height=2,
                             command=self.exitt_but)
            button3.place(x=440, y=490)

        def exitt_but(shelf):
                exitt_but = tkinter.messagebox.askretrycancel("status", "Are you sure you want to exit")
                if exitt > 0:
                    return self.root

        def back_but(self):
                back_but = tkinter.messagebox.askretrycancel("status", "go back to home home")
                if back > 0:
                    return self.root

        def order_info(self):
                order_but = tkinter.messagebox.askokcancel("status", "your order is placed successfully")
                if order > 0:
                    return self.root


####################################################################################################################3####
#### #######################################3pizza####################################################
class window4:

    def __init__(self, master):
        self.master = master
        self.master.geometry("700x700")
        self.master.title("Pizza")
        self.frame = Frame(self.master)
        self.frame.pack()

        img13 = Image.open('D:\pythonProject6\jjjjjjj1\jiffff\Screenshot (389).png')
        img13 = img13.resize((150, 120))
        self.photo_img13 = ImageTk.PhotoImage(img13)
        b13 = Button(self.frame, image=self.photo_img13, borderwidth=0)
        b13.grid(row=0, column=0, pady=10)

        self.frame1 = Label(self.frame, text="PIZZA".center(20), font=("arial 15 bold", 40), bg="gray15",
                            fg="white", bd=2,
                            relief="sunken", width=30, height=2)
        self.frame1.grid(row=0, column=2, padx=50, pady=10, columnspan=3)  # 2

        img14 = Image.open('D:\pythonProject6\jjjjjjj1\jiffff\ymmy\Screenshot (390).png')
        img14 = img14.resize((150, 120), Image.ANTIALIAS)
        self.photo_img14 = ImageTk.PhotoImage(img14)
        b14 = Button(self.frame, image=self.photo_img14, borderwidth=0)
        b14.grid(row=0, column=5)  # 5
    ###############################################################################################################
        self.Loginframe1 = Frame(self.frame, width=720, height=560, bd=10, relief="groove")
        self.Loginframe1.grid(row=1, column=0, columnspan=3)

        self.Loginframe2 = Frame(self.frame, width=693, height=560, bd=10, relief="groove")
        self.Loginframe2.grid(row=1, column=4, columnspan=3)

        self.Loginframe3 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black", pady=15,
                                padx=10)
        self.Loginframe3.place(x=0, y=0)

        self.Loginframe4 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black", pady=5)
        self.Loginframe4.place(x=0, y=180)

        self.Loginframe5 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black", pady=15)
        self.Loginframe5.place(x=0, y=360)

######################################################################################################################
        img16 = Image.open('D:\pythonProject7\\nattii\mango\Screenshot (445).png')
        img16 = img16.resize((140, 150))
        self.photo_img16 = ImageTk.PhotoImage(img16)
        b16 = Button(self.Loginframe1, image=self.photo_img16, borderwidth=3, padx=10, pady=5)
        b16.place(x=20, y=10)
        sud_name = Label(self.Loginframe1, text="tandoori-pizza\nRs-120", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        sud_name.place(x=177, y=8)

        img18 = Image.open('D:\pythonProject7\\nattii\mango\Screenshot (444).png')
        img18 = img18.resize((140, 150))
        self.photo_img18 = ImageTk.PhotoImage(img18)
        b18 = Button(self.Loginframe1, image=self.photo_img18, borderwidth=3, padx=10, pady=5)
        b18.place(x=530, y=10)
        cho_name = Label(self.Loginframe1, text="paneer-pizza\nRs-200", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=13, height=2, padx=10)
        cho_name.place(x=350, y=120)

        img19 = Image.open('D:\pythonProject7\\nattii\mango\Screenshot (443).png')
        img19 = img19.resize((140, 150))
        self.photo_img19 = ImageTk.PhotoImage(img19)
        b19 = Button(self.Loginframe4, image=self.photo_img19, borderwidth=3, padx=10, pady=5)
        b19.place(x=20, y=10)
        sud_name = Label(self.Loginframe4, text="corn-pizza\nRs-180", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        sud_name.place(x=177, y=8)

        img20 = Image.open('D:\pythonProject7\\nattii\Screenshot (438).png')
        img20 = img20.resize((140, 150))
        self.photo_img20 = ImageTk.PhotoImage(img20)
        b20 = Button(self.Loginframe4, image=self.photo_img20, borderwidth=3, padx=10, pady=5)
        b20.place(x=530, y=10)
        cho_name = Label(self.Loginframe4, text="onion-pizza\nRs-150", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=13, height=2, padx=10)
        cho_name.place(x=350, y=110)

        img21 = Image.open('D:\pythonProject7\\nattii\Screenshot (441).png')
        img21 = img21.resize((130, 130))
        self.photo_img21 = ImageTk.PhotoImage(img21)
        b21 = Button(self.Loginframe5, image=self.photo_img21, borderwidth=3, padx=10, pady=5)
        b21.place(x=20, y=10)
        sud_name = Label(self.Loginframe5, text="chessy-pizza\nRs-200", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        sud_name.place(x=177, y=8)

        img22 = Image.open('D:\pythonProject7\\nattii\Screenshot (442).png')
        img22 = img22.resize((130, 130))
        self.photo_img22 = ImageTk.PhotoImage(img22)
        b22 = Button(self.Loginframe5, image=self.photo_img22, borderwidth=3, padx=10, pady=5)
        b22.place(x=530, y=10)
        cho_name = Label(self.Loginframe5, text="Vegkebab-pizza\nRs-100", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=13, height=2, padx=10)
        cho_name.place(x=350, y=100)

        item_ordered = StringVar()
        quatity = IntVar()
        location = StringVar()
        Phone_num = IntVar()
        Total_price = IntVar()

        self.heading = Label(self.Loginframe2, text="Item selected", font=("arial 15 bold", 15), bg="black", fg="white"
                             , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading.place(x=10, y=30)

        self.heading1 = Label(self.Loginframe2, text="Quantity", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading1.place(x=10, y=120)

        self.heading2 = Label(self.Loginframe2, text="Location", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading2.place(x=10, y=200)

        self.heading3 = Label(self.Loginframe2, text="Phone_No", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading3.place(x=10, y=280)

        self.heading4 = Label(self.Loginframe2, text="Total-Price", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading4.place(x=10, y=360)

        e1 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=item_ordered)
        e1.place(x=250, y=40)  # item

        n = tk.StringVar()
        quantity = ttk.Combobox(self.Loginframe2, width=17, textvariable=n, font=("arial 15 bold", 10))
        quantity['values'] = ["1", "2", "3", "4", "5", "6"]
        quantity.current()
        quantity.place(x=250, y=130)

        e2 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=location)
        e2.place(x=250, y=210)

        e3 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=Phone_num)
        e3.place(x=250, y=290)

        e4 = Entry(self.Loginframe2, width=10, font=("arial 15 bold", 20), fg="black", text=Total_price)
        e4.place(x=250, y=370)

        button1 = Button(self.Loginframe2, text="BACK", bg="black", fg="white", width=10, height=2,
                         command=self.back_but)
        button1.place(x=30, y=490)

        button2 = Button(self.Loginframe2, text="ORDER", bg="black", fg="white", width=10, height=2,command=
                         self.order_info)
        button2.place(x=240, y=490)

        button3 = Button(self.Loginframe2, text="EXIT", bg="black", fg="white", width=10, height=2,command=
                         self.exitt_but)
        button3.place(x=440, y=490)

    def exitt_but(shelf):
        exitt_but = tkinter.messagebox.askretrycancel("status", "Are you sure you want to exit")
        if exitt > 0:
            return self.root

    def back_but(self):
        back_but = tkinter.messagebox.askretrycancel("status", "go back to home home")
        if back > 0:
            return self.root

    def order_info(self):
        order_but = tkinter.messagebox.askokcancel("status", "your order is placed successfully")
        if order > 0:
            return self.root


#############################################################################################################

############################################parrotta###############################################################
class window5:

            def __init__(self, master):
                self.master = master
                self.master.geometry("700x700")
                self.master.title("Parotta")
                self.frame = Frame(self.master)
                self.frame.pack()

                img13 = Image.open('D:\pythonProject6\jjjjjjj1\jiffff\Screenshot (389).png')
                img13 = img13.resize((150, 120))
                self.photo_img13 = ImageTk.PhotoImage(img13)
                b13 = Button(self.frame, image=self.photo_img13, borderwidth=0)
                b13.grid(row=0, column=0, pady=10)

                self.frame1 = Label(self.frame, text="PARATA".center(20), font=("arial 15 bold", 40), bg="gray15",
                                    fg="white", bd=2,
                                    relief="sunken", width=30, height=2)
                self.frame1.grid(row=0, column=2, padx=50, pady=10, columnspan=3)  # 2

                img14 = Image.open('D:\pythonProject6\jjjjjjj1\jiffff\ymmy\Screenshot (390).png')
                img14 = img14.resize((150, 120), Image.ANTIALIAS)
                self.photo_img14 = ImageTk.PhotoImage(img14)
                b14 = Button(self.frame, image=self.photo_img14, borderwidth=0)
                b14.grid(row=0, column=5)  # 5
                ###############################################################################################################
                self.Loginframe1 = Frame(self.frame, width=720, height=560, bd=10, relief="groove")
                self.Loginframe1.grid(row=1, column=0, columnspan=3)

                self.Loginframe2 = Frame(self.frame, width=693, height=560, bd=10, relief="groove")
                self.Loginframe2.grid(row=1, column=4, columnspan=3)

                self.Loginframe3 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black",
                                         pady=15,
                                         padx=10)
                self.Loginframe3.place(x=0, y=0)

                self.Loginframe4 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black",
                                         pady=5)
                self.Loginframe4.place(x=0, y=180)

                self.Loginframe5 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black",
                                         pady=15)
                self.Loginframe5.place(x=0, y=360)

                ######################################################################################################################
                img16 = Image.open('D:\pythonProject7\\nattii\Screenshot (463).png')
                img16 = img16.resize((140, 150))
                self.photo_img16 = ImageTk.PhotoImage(img16)
                b16 = Button(self.Loginframe1, image=self.photo_img16, borderwidth=3, padx=10, pady=5)
                b16.place(x=20, y=10)
                sud_name = Label(self.Loginframe1, text="Paneer-paratha\nRs-60", font=("arial 15 bold", 15),
                                 bg="gray60"
                                 , fg="black",
                                 relief="sunken", width=10, height=2, padx=10)
                sud_name.place(x=177, y=8)

                img18 = Image.open('D:\pythonProject7\\nattii\Screenshot (464).png')
                img18 = img18.resize((140, 150))
                self.photo_img18 = ImageTk.PhotoImage(img18)
                b18 = Button(self.Loginframe1, image=self.photo_img18, borderwidth=3, padx=10, pady=5)
                b18.place(x=530, y=10)
                cho_name = Label(self.Loginframe1, text="Aloo-paratha\nRs-100", font=("arial 15 bold", 15),
                                 bg="gray60"
                                 , fg="black",
                                 relief="sunken", width=13, height=2, padx=10)
                cho_name.place(x=350, y=120)

                img19 = Image.open('D:\pythonProject7\\nattii\Screenshot (462).png')
                img19 = img19.resize((140, 150))
                self.photo_img19 = ImageTk.PhotoImage(img19)
                b19 = Button(self.Loginframe4, image=self.photo_img19, borderwidth=3, padx=10, pady=5)
                b19.place(x=20, y=10)
                sud_name = Label(self.Loginframe4, text="Matar-paratha\nRs-60", font=("arial 15 bold", 15),
                                 bg="gray60"
                                 , fg="black",
                                 relief="sunken", width=10, height=2, padx=10)
                sud_name.place(x=177, y=8)

                img20 = Image.open('D:\pythonProject7\\nattii\Screenshot (461).png')
                img20 = img20.resize((140, 150))
                self.photo_img20 = ImageTk.PhotoImage(img20)
                b20 = Button(self.Loginframe4, image=self.photo_img20, borderwidth=3, padx=10, pady=5)
                b20.place(x=530, y=10)
                cho_name = Label(self.Loginframe4, text="Veechu-paratha\nRs-100", font=("arial 15 bold", 15),
                                 bg="gray60"
                                 , fg="black",
                                 relief="sunken", width=13, height=2, padx=10)
                cho_name.place(x=350, y=110)

                img21 = Image.open('D:\pythonProject7\\nattii\Screenshot (459).png')
                img21 = img21.resize((140, 150))
                self.photo_img21 = ImageTk.PhotoImage(img21)
                b21 = Button(self.Loginframe5, image=self.photo_img21, borderwidth=3, padx=10, pady=5)
                b21.place(x=20, y=10)
                sud_name = Label(self.Loginframe5, text="kemma-paratha\nRs-60", font=("arial 15 bold", 15),
                                 bg="gray60"
                                 , fg="black",
                                 relief="sunken", width=10, height=2, padx=10)
                sud_name.place(x=177, y=8)

                img22 = Image.open('D:\pythonProject7\\nattii\Screenshot (460).png')
                img22 = img22.resize((140, 150))
                self.photo_img22 = ImageTk.PhotoImage(img22)
                b22 = Button(self.Loginframe5, image=self.photo_img22, borderwidth=3, padx=10, pady=5)
                b22.place(x=530, y=10)
                cho_name = Label(self.Loginframe5, text="Gobi-paratha\nRs-100", font=("arial 15 bold", 15),
                                 bg="gray60"
                                 , fg="black",
                                 relief="sunken", width=13, height=2, padx=10)
                cho_name.place(x=350, y=100)

                item_ordered = StringVar()
                quatity = IntVar()
                location = StringVar()
                Phone_num = IntVar()
                Total_price = IntVar()

                self.heading = Label(self.Loginframe2, text="Item selected", font=("arial 15 bold", 15), bg="black",
                                     fg="white"
                                     , relief=RIDGE, padx=10, pady=10, width=10)
                self.heading.place(x=10, y=30)

                self.heading1 = Label(self.Loginframe2, text="Quantity", font=("arial 15 bold", 15), bg="black",
                                      fg="white"
                                      , relief=RIDGE, padx=10, pady=10, width=10)
                self.heading1.place(x=10, y=120)

                self.heading2 = Label(self.Loginframe2, text="Location", font=("arial 15 bold", 15), bg="black",
                                      fg="white"
                                      , relief=RIDGE, padx=10, pady=10, width=10)
                self.heading2.place(x=10, y=200)

                self.heading3 = Label(self.Loginframe2, text="Phone_No", font=("arial 15 bold", 15), bg="black",
                                      fg="white"
                                      , relief=RIDGE, padx=10, pady=10, width=10)
                self.heading3.place(x=10, y=280)

                self.heading4 = Label(self.Loginframe2, text="Total-Price", font=("arial 15 bold", 15), bg="black",
                                      fg="white"
                                      , relief=RIDGE, padx=10, pady=10, width=10)
                self.heading4.place(x=10, y=360)

                e1 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black",
                           textvariable=item_ordered)
                e1.place(x=250, y=40)  # item

                n = tk.StringVar()
                quantity = ttk.Combobox(self.Loginframe2, width=17, textvariable=n, font=("arial 15 bold", 10))
                quantity['values'] = ["1", "2", "3", "4", "5", "6"]
                quantity.current()
                quantity.place(x=250, y=130)

                e2 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=location)
                e2.place(x=250, y=210)

                e3 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=Phone_num)
                e3.place(x=250, y=290)

                e4 = Entry(self.Loginframe2, width=10, font=("arial 15 bold", 20), fg="black", text=Total_price)
                e4.place(x=250, y=370)

                button1 = Button(self.Loginframe2, text="BACK", bg="black", fg="white", width=10, height=2,
                                 command=self.back_but)
                button1.place(x=30, y=490)

                button2 = Button(self.Loginframe2, text="ORDER", bg="black", fg="white", width=10, height=2,
                                 command=self.order_info)
                button2.place(x=240, y=490)

                button3 = Button(self.Loginframe2, text="EXIT", bg="black", fg="white", width=10, height=2,
                                 command=self.exitt_but)
                button3.place(x=440, y=490)

            def exitt_but(shelf):
                exitt_but = tkinter.messagebox.askretrycancel("status", "Are you sure you want to exit")
                if exitt > 0:
                    return self.root

            def back_but(self):
                back_but = tkinter.messagebox.askretrycancel("status", "go back to home home")
                if back > 0:
                    return self.root

            def order_info(self):
                order_but = tkinter.messagebox.askokcancel("status", "your order is placed successfully")
                if order > 0:
                    return self.root

#############################################################################################################

        ############################################parrotta###############################################################
class window6:

    def __init__(self, master):
        self.master = master
        self.master.geometry("700x700")
        self.master.title("Burger")
        self.frame = Frame(self.master)
        self.frame.pack()

        img13 = Image.open('D:\pythonProject6\jjjjjjj1\jiffff\Screenshot (389).png')
        img13 = img13.resize((150, 120))
        self.photo_img13 = ImageTk.PhotoImage(img13)
        b13 = Button(self.frame, image=self.photo_img13, borderwidth=0)
        b13.grid(row=0, column=0, pady=10)

        self.frame1 = Label(self.frame, text="BURGER".center(20), font=("arial 15 bold", 40), bg="gray15",
                            fg="white", bd=2,
                            relief="sunken", width=30, height=2)
        self.frame1.grid(row=0, column=2, padx=50, pady=10, columnspan=3)  # 2

        img14 = Image.open('D:\pythonProject6\jjjjjjj1\jiffff\ymmy\Screenshot (390).png')
        img14 = img14.resize((150, 120), Image.ANTIALIAS)
        self.photo_img14 = ImageTk.PhotoImage(img14)
        b14 = Button(self.frame, image=self.photo_img14, borderwidth=0)
        b14.grid(row=0, column=5)  # 5
    ###############################################################################################################
        self.Loginframe1 = Frame(self.frame, width=720, height=560, bd=10, relief="groove")
        self.Loginframe1.grid(row=1, column=0, columnspan=3)

        self.Loginframe2 = Frame(self.frame, width=693, height=560, bd=10, relief="groove")
        self.Loginframe2.grid(row=1, column=4, columnspan=3)

        self.Loginframe3 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black", pady=15,
                                padx=10)
        self.Loginframe3.place(x=0, y=0)

        self.Loginframe4 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black", pady=5)
        self.Loginframe4.place(x=0, y=180)

        self.Loginframe5 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black", pady=15)
        self.Loginframe5.place(x=0, y=360)

######################################################################################################################
        img16 = Image.open('D:\pythonProject7\\nattii\pepper\lolli\egggg\Screenshot (464).png')
        img16 = img16.resize((140, 150))
        self.photo_img16 = ImageTk.PhotoImage(img16)
        b16 = Button(self.Loginframe1, image=self.photo_img16, borderwidth=3, padx=10, pady=5)
        b16.place(x=20, y=10)
        sud_name = Label(self.Loginframe1, text="Chicken-burger\nRs-100", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        sud_name.place(x=177, y=8)

        img18 = Image.open('D:\pythonProject7\\nattii\pepper\lolli\egggg\Screenshot (463).png')
        img18 = img18.resize((140, 150))
        self.photo_img18 = ImageTk.PhotoImage(img18)
        b18 = Button(self.Loginframe1, image=self.photo_img18, borderwidth=3, padx=10, pady=5)
        b18.place(x=530, y=10)
        cho_name = Label(self.Loginframe1, text="Veg-burger\nRs-100", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=13, height=2, padx=10)
        cho_name.place(x=350, y=120)

        img19 = Image.open('D:\pythonProject7\\nattii\pepper\lolli\egggg\Screenshot (462).png')
        img19 = img19.resize((140, 150))
        self.photo_img19 = ImageTk.PhotoImage(img19)
        b19 = Button(self.Loginframe4, image=self.photo_img19, borderwidth=3, padx=10, pady=5)
        b19.place(x=20, y=10)
        sud_name = Label(self.Loginframe4, text="Chees-burger\nRs-180", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        sud_name.place(x=177, y=8)

        img20 = Image.open('D:\pythonProject7\\nattii\pepper\lolli\egggg\Screenshot (461).png')
        img20 = img20.resize((140, 150))
        self.photo_img20 = ImageTk.PhotoImage(img20)
        b20 = Button(self.Loginframe4, image=self.photo_img20, borderwidth=3, padx=10, pady=5)
        b20.place(x=530, y=10)
        cho_name = Label(self.Loginframe4, text="paneer-buger\nRs-100", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=13, height=2, padx=10)
        cho_name.place(x=350, y=110)

        img21 = Image.open('D:\pythonProject7\\nattii\pepper\lolli\egggg\Screenshot (460).png')
        img21 = img21.resize((140, 150))
        self.photo_img21 = ImageTk.PhotoImage(img21)
        b21 = Button(self.Loginframe5, image=self.photo_img21, borderwidth=3, padx=10, pady=5)
        b21.place(x=20, y=10)
        sud_name = Label(self.Loginframe5, text="egg-burger\nRs-60", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        sud_name.place(x=177, y=8)

        img22 = Image.open('D:\pythonProject7\\nattii\pepper\lolli\egggg\Screenshot (459).png')
        img22 = img22.resize((140, 150))
        self.photo_img22 = ImageTk.PhotoImage(img22)
        b22 = Button(self.Loginframe5, image=self.photo_img22, borderwidth=3, padx=10, pady=5)
        b22.place(x=530, y=10)
        cho_name = Label(self.Loginframe5, text="corn-burger\nRs-100", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=13, height=2, padx=10)
        cho_name.place(x=350, y=100)

        item_ordered = StringVar()
        quatity = IntVar()
        location = StringVar()
        Phone_num = IntVar()
        Total_price = IntVar()

        self.heading = Label(self.Loginframe2, text="Item selected", font=("arial 15 bold", 15), bg="black", fg="white"
                             , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading.place(x=10, y=30)

        self.heading1 = Label(self.Loginframe2, text="Quantity", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading1.place(x=10, y=120)

        self.heading2 = Label(self.Loginframe2, text="Location", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading2.place(x=10, y=200)

        self.heading3 = Label(self.Loginframe2, text="Phone_No", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading3.place(x=10, y=280)

        self.heading4 = Label(self.Loginframe2, text="Total-Price", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading4.place(x=10, y=360)

        e1 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=item_ordered)
        e1.place(x=250, y=40)  # item

        n = tk.StringVar()
        quantity = ttk.Combobox(self.Loginframe2, width=17, textvariable=n, font=("arial 15 bold", 10))
        quantity['values'] = ["1", "2", "3", "4", "5", "6"]
        quantity.current()
        quantity.place(x=250, y=130)

        e2 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=location)
        e2.place(x=250, y=210)

        e3 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=Phone_num)
        e3.place(x=250, y=290)

        e4 = Entry(self.Loginframe2, width=10, font=("arial 15 bold", 20), fg="black", text=Total_price)
        e4.place(x=250, y=370)

        button1 = Button(self.Loginframe2, text="BACK", bg="black", fg="white", width=10, height=2,
                         command=self.back_but)
        button1.place(x=30, y=490)

        button2 = Button(self.Loginframe2, text="ORDER", bg="black", fg="white", width=10, height=2,
                         command=self.order_info)
        button2.place(x=240, y=490)

        button3 = Button(self.Loginframe2, text="EXIT", bg="black", fg="white", width=10, height=2,
                         command=self.exitt_but)
        button3.place(x=440, y=490)

    def exitt_but(shelf):
        exitt_but = tkinter.messagebox.askretrycancel("status", "Are you sure you want to exit")
        if exitt > 0:
            return self.root

    def back_but(self):
        back_but = tkinter.messagebox.askretrycancel("status", "go back to home home")
        if back > 0:
            return self.root

    def order_info(self):
        order_but = tkinter.messagebox.askokcancel("status", "your order is placed successfully")
        if order > 0:
            return self.root


#############################################################################################################

############################################parrotta###############################################################
class window7:

    def __init__(self, master):
        self.master = master
        self.master.geometry("700x700")
        self.master.title("Shake")
        self.frame = Frame(self.master)
        self.frame.pack()

        img13 = Image.open('D:\pythonProject6\jjjjjjj1\jiffff\Screenshot (389).png')
        img13 = img13.resize((150, 120))
        self.photo_img13 = ImageTk.PhotoImage(img13)
        b13 = Button(self.frame, image=self.photo_img13, borderwidth=0)
        b13.grid(row=0, column=0, pady=10)

        self.frame1 = Label(self.frame, text="SHAKES".center(20), font=("arial 15 bold", 40), bg="gray15",
                            fg="white", bd=2,
                            relief="sunken", width=30, height=2)
        self.frame1.grid(row=0, column=2, padx=50, pady=10, columnspan=3)  # 2

        img14 = Image.open('D:\pythonProject6\jjjjjjj1\jiffff\ymmy\Screenshot (390).png')
        img14 = img14.resize((150, 120), Image.ANTIALIAS)
        self.photo_img14 = ImageTk.PhotoImage(img14)
        b14 = Button(self.frame, image=self.photo_img14, borderwidth=0)
        b14.grid(row=0, column=5)  # 5
    ###############################################################################################################
        self.Loginframe1 = Frame(self.frame, width=720, height=560, bd=10, relief="groove")
        self.Loginframe1.grid(row=1, column=0, columnspan=3)

        self.Loginframe2 = Frame(self.frame, width=693, height=560, bd=10, relief="groove")
        self.Loginframe2.grid(row=1, column=4, columnspan=3)

        self.Loginframe3 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black", pady=15,
                                padx=10)
        self.Loginframe3.place(x=0, y=0)

        self.Loginframe4 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black", pady=5)
        self.Loginframe4.place(x=0, y=180)

        self.Loginframe5 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black", pady=15)
        self.Loginframe5.place(x=0, y=360)

######################################################################################################################
        img16 = Image.open('D:\pythonProject7\\nattii\pepper\Screenshot (490).png')
        img16 = img16.resize((140, 150))
        self.photo_img16 = ImageTk.PhotoImage(img16)
        b16 = Button(self.Loginframe1, image=self.photo_img16, borderwidth=3, padx=10, pady=5)
        b16.place(x=20, y=10)
        sud_name = Label(self.Loginframe1, text="Chocolate-shake\nRs-60", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        sud_name.place(x=177, y=8)

        img18 = Image.open('D:\pythonProject7\\nattii\pepper\Screenshot (489).png')
        img18 = img18.resize((140, 150))
        self.photo_img18 = ImageTk.PhotoImage(img18)
        b18 = Button(self.Loginframe1, image=self.photo_img18, borderwidth=3, padx=10, pady=5)
        b18.place(x=530, y=10)
        cho_name = Label(self.Loginframe1, text="Vanilla\nRs-100", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=13, height=2, padx=10)
        cho_name.place(x=350, y=120)

        img19 = Image.open('D:\pythonProject7\\nattii\pepper\Screenshot (488).png')
        img19 = img19.resize((140, 150))
        self.photo_img19 = ImageTk.PhotoImage(img19)
        b19 = Button(self.Loginframe4, image=self.photo_img19, borderwidth=3, padx=10, pady=5)
        b19.place(x=20, y=10)
        sud_name = Label(self.Loginframe4, text="Cookie-Cream Shake\nRs-60", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        sud_name.place(x=177, y=8)

        img20 = Image.open('D:\pythonProject7\\nattii\pepper\Screenshot (487).png')
        img20 = img20.resize((140, 150))
        self.photo_img20 = ImageTk.PhotoImage(img20)
        b20 = Button(self.Loginframe4, image=self.photo_img20, borderwidth=3, padx=10, pady=5)
        b20.place(x=530, y=10)
        cho_name = Label(self.Loginframe4, text="Blueberry-shake\nRs-100", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=13, height=2, padx=10)
        cho_name.place(x=350, y=110)

        img21 = Image.open('D:\pythonProject7\\nattii\pepper\Screenshot (486).png')
        img21 = img21.resize((130, 130))
        self.photo_img21 = ImageTk.PhotoImage(img21)
        b21 = Button(self.Loginframe5, image=self.photo_img21, borderwidth=3, padx=10, pady=5)
        b21.place(x=20, y=10)
        sud_name = Label(self.Loginframe5, text="Peanut-Shake\nRs-60", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        sud_name.place(x=177, y=8)

        img22 = Image.open('D:\pythonProject7\\nattii\pepper\Screenshot (485).png')
        img22 = img22.resize((130, 130))
        self.photo_img22 = ImageTk.PhotoImage(img22)
        b22 = Button(self.Loginframe5, image=self.photo_img22, borderwidth=3, padx=10, pady=5)
        b22.place(x=530, y=10)
        cho_name = Label(self.Loginframe5, text="Mango-shake\nRs-100", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=13, height=2, padx=10)
        cho_name.place(x=350, y=100)

        item_ordered = StringVar()
        quatity = IntVar()
        location = StringVar()
        Phone_num = IntVar()
        Total_price = IntVar()

        self.heading = Label(self.Loginframe2, text="Item selected", font=("arial 15 bold", 15), bg="black", fg="white"
                             , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading.place(x=10, y=30)

        self.heading1 = Label(self.Loginframe2, text="Quantity", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading1.place(x=10, y=120)

        self.heading2 = Label(self.Loginframe2, text="Location", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading2.place(x=10, y=200)

        self.heading3 = Label(self.Loginframe2, text="Phone_No", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading3.place(x=10, y=280)

        self.heading4 = Label(self.Loginframe2, text="Total-Price", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading4.place(x=10, y=360)

        e1 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=item_ordered)
        e1.place(x=250, y=40)  # item

        n = tk.StringVar()
        quantity = ttk.Combobox(self.Loginframe2, width=17, textvariable=n, font=("arial 15 bold", 10))
        quantity['values'] = ["1", "2", "3", "4", "5", "6"]
        quantity.current()
        quantity.place(x=250, y=130)

        e2 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=location)
        e2.place(x=250, y=210)

        e3 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=Phone_num)
        e3.place(x=250, y=290)

        e4 = Entry(self.Loginframe2, width=10, font=("arial 15 bold", 20), fg="black", text=Total_price)
        e4.place(x=250, y=370)

        button1 = Button(self.Loginframe2, text="BACK", bg="black", fg="white", width=10, height=2,
                         command=self.back_but)
        button1.place(x=30, y=490)

        button2 = Button(self.Loginframe2, text="ORDER", bg="black", fg="white", width=10, height=2,
                         command=self.order_info)
        button2.place(x=240, y=490)

        button3 = Button(self.Loginframe2, text="EXIT", bg="black", fg="white", width=10, height=2,
                         command=self.exitt_but)
        button3.place(x=440, y=490)

    def exitt_but(shelf):
        exitt_but = tkinter.messagebox.askretrycancel("status", "Are you sure you want to exit")
        if exitt > 0:
            return self.root

    def back_but(self):
        back_but = tkinter.messagebox.askretrycancel("status", "go back to home home")
        if back > 0:
            return self.root

    def order_info(self):
        order_but = tkinter.messagebox.askokcancel("status", "your order is placed successfully")
        if order > 0:
            return self.root


#############################################################################################################

############################################parrotta###############################################################
class window8:

    def __init__(self, master):
        self.master = master
        self.master.geometry("700x700")
        self.master.title("Rice")
        self.frame = Frame(self.master)
        self.frame.pack()

        img13 = Image.open('D:\pythonProject6\jjjjjjj1\jiffff\Screenshot (389).png')
        img13 = img13.resize((150, 120))
        self.photo_img13 = ImageTk.PhotoImage(img13)
        b13 = Button(self.frame, image=self.photo_img13, borderwidth=0)
        b13.grid(row=0, column=0, pady=10)

        self.frame1 = Label(self.frame, text="RICE VARITIES".center(20), font=("arial 15 bold", 40), bg="gray15",
                            fg="white", bd=2,
                            relief="sunken", width=30, height=2)
        self.frame1.grid(row=0, column=2, padx=50, pady=10, columnspan=3)  # 2

        img14 = Image.open('D:\pythonProject6\jjjjjjj1\jiffff\ymmy\Screenshot (390).png')
        img14 = img14.resize((150, 120), Image.ANTIALIAS)
        self.photo_img14 = ImageTk.PhotoImage(img14)
        b14 = Button(self.frame, image=self.photo_img14, borderwidth=0)
        b14.grid(row=0, column=5)  # 5
    ###############################################################################################################
        self.Loginframe1 = Frame(self.frame, width=720, height=560, bd=10, relief="groove")
        self.Loginframe1.grid(row=1, column=0, columnspan=3)

        self.Loginframe2 = Frame(self.frame, width=693, height=560, bd=10, relief="groove")
        self.Loginframe2.grid(row=1, column=4, columnspan=3)

        self.Loginframe3 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black", pady=15,
                                padx=10)
        self.Loginframe3.place(x=0, y=0)

        self.Loginframe4 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black", pady=5)
        self.Loginframe4.place(x=0, y=180)

        self.Loginframe5 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black", pady=15)
        self.Loginframe5.place(x=0, y=360)

######################################################################################################################
        img16 = Image.open('D:\pythonProject7\\nattii\Screenshot (490).png')
        img16 = img16.resize((140, 150))
        self.photo_img16 = ImageTk.PhotoImage(img16)
        b16 = Button(self.Loginframe1, image=self.photo_img16, borderwidth=3, padx=10, pady=5)
        b16.place(x=20, y=10)
        sud_name = Label(self.Loginframe1, text="Rajasthani-talli\nRs-250", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        sud_name.place(x=177, y=8)

        img18 = Image.open('D:\pythonProject7\\nattii\Screenshot (489).png')
        img18 = img18.resize((140, 150))
        self.photo_img18 = ImageTk.PhotoImage(img18)
        b18 = Button(self.Loginframe1, image=self.photo_img18, borderwidth=3, padx=10, pady=5)
        b18.place(x=530, y=10)
        cho_name = Label(self.Loginframe1, text="Rice-Sambar\nRs-150", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=13, height=2, padx=10)
        cho_name.place(x=350, y=120)

        img19 = Image.open('D:\pythonProject7\\nattii\Screenshot (488).png')
        img19 = img19.resize((140, 150))
        self.photo_img19 = ImageTk.PhotoImage(img19)
        b19 = Button(self.Loginframe4, image=self.photo_img19, borderwidth=3, padx=10, pady=5)
        b19.place(x=20, y=10)
        sud_name = Label(self.Loginframe4, text="Pongal\nRs-100", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        sud_name.place(x=177, y=8)

        img20 = Image.open('D:\pythonProject7\\nattii\Screenshot (487).png')
        img20 = img20.resize((130, 130))
        self.photo_img20 = ImageTk.PhotoImage(img20)
        b20 = Button(self.Loginframe4, image=self.photo_img20, borderwidth=3, padx=10, pady=5)
        b20.place(x=530, y=10)
        cho_name = Label(self.Loginframe4, text="Egg-Rice\nRs-180", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=13, height=2, padx=10)
        cho_name.place(x=350, y=110)

        img21 = Image.open('D:\pythonProject7\\nattii\Screenshot (486).png')
        img21 = img21.resize((130, 130))
        self.photo_img21 = ImageTk.PhotoImage(img21)
        b21 = Button(self.Loginframe5, image=self.photo_img21, borderwidth=3, padx=10, pady=5)
        b21.place(x=20, y=10)
        sud_name = Label(self.Loginframe5, text="Rice-Rasam\nRs-150", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        sud_name.place(x=177, y=8)

        img22 = Image.open('D:\pythonProject7\\nattii\Screenshot (485).png')
        img22 = img22.resize((130, 130))
        self.photo_img22 = ImageTk.PhotoImage(img22)
        b22 = Button(self.Loginframe5, image=self.photo_img22, borderwidth=3, padx=10, pady=5)
        b22.place(x=530, y=10)
        cho_name = Label(self.Loginframe5, text="Veg-Palav\nRs-180", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=13, height=2, padx=10)
        cho_name.place(x=350, y=100)

        item_ordered = StringVar()
        quatity = IntVar()
        location = StringVar()
        Phone_num = IntVar()
        Total_price = IntVar()

        self.heading = Label(self.Loginframe2, text="Item selected", font=("arial 15 bold", 15), bg="black", fg="white"
                             , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading.place(x=10, y=30)

        self.heading1 = Label(self.Loginframe2, text="Quantity", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading1.place(x=10, y=120)

        self.heading2 = Label(self.Loginframe2, text="Location", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading2.place(x=10, y=200)

        self.heading3 = Label(self.Loginframe2, text="Phone_No", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading3.place(x=10, y=280)

        self.heading4 = Label(self.Loginframe2, text="Total-Price", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading4.place(x=10, y=360)

        e1 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=item_ordered)
        e1.place(x=250, y=40)  # item

        n = tk.StringVar()
        quantity = ttk.Combobox(self.Loginframe2, width=17, textvariable=n, font=("arial 15 bold", 10))
        quantity['values'] = ["1", "2", "3", "4", "5", "6"]
        quantity.current()
        quantity.place(x=250, y=130)

        e2 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=location)
        e2.place(x=250, y=210)

        e3 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=Phone_num)
        e3.place(x=250, y=290)

        e4 = Entry(self.Loginframe2, width=10, font=("arial 15 bold", 20), fg="black", text=Total_price)
        e4.place(x=250, y=370)

        button1 = Button(self.Loginframe2, text="BACK", bg="black", fg="white", width=10, height=2,
                         command=self.back_but)
        button1.place(x=30, y=490)

        button2 = Button(self.Loginframe2, text="ORDER", bg="black", fg="white", width=10, height=2,
                         command=self.order_info)
        button2.place(x=240, y=490)

        button3 = Button(self.Loginframe2, text="EXIT", bg="black", fg="white", width=10, height=2,
                         command=self.exitt_but)
        button3.place(x=440, y=490)

    def exitt_but(shelf):
        exitt_but = tkinter.messagebox.askretrycancel("status", "Are you sure you want to exit")
        if exitt > 0:
            return self.root

    def back_but(self):
        back_but = tkinter.messagebox.askretrycancel("status", "go back to home home")
        if back > 0:
            return self.root

    def order_info(self):
        order_but = tkinter.messagebox.askokcancel("status", "your order is placed successfully")
        if order > 0:
            return self.root


#############################################################################################################

############################################parrotta###############################################################
class window9:

    def __init__(self, master):
        self.master = master
        self.master.geometry("700x700")
        self.master.title("Cake")
        self.frame = Frame(self.master)
        self.frame.pack()

        img13 = Image.open('D:\pythonProject6\jjjjjjj1\jiffff\Screenshot (389).png')
        img13 = img13.resize((150, 120))
        self.photo_img13 = ImageTk.PhotoImage(img13)
        b13 = Button(self.frame, image=self.photo_img13, borderwidth=0)
        b13.grid(row=0, column=0, pady=10)

        self.frame1 = Label(self.frame, text="CAKES".center(20), font=("arial 15 bold", 40), bg="gray15",
                            fg="white", bd=2,
                            relief="sunken", width=30, height=2)
        self.frame1.grid(row=0, column=2, padx=50, pady=10, columnspan=3)  # 2

        img14 = Image.open('D:\pythonProject6\jjjjjjj1\jiffff\ymmy\Screenshot (390).png')
        img14 = img14.resize((150, 120), Image.ANTIALIAS)
        self.photo_img14 = ImageTk.PhotoImage(img14)
        b14 = Button(self.frame, image=self.photo_img14, borderwidth=0)
        b14.grid(row=0, column=5)  # 5
    ###############################################################################################################
        self.Loginframe1 = Frame(self.frame, width=720, height=560, bd=10, relief="groove")
        self.Loginframe1.grid(row=1, column=0, columnspan=3)

        self.Loginframe2 = Frame(self.frame, width=693, height=560, bd=10, relief="groove")
        self.Loginframe2.grid(row=1, column=4, columnspan=3)

        self.Loginframe3 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black", pady=15,
                                padx=10)
        self.Loginframe3.place(x=0, y=0)

        self.Loginframe4 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black", pady=5)
        self.Loginframe4.place(x=0, y=180)

        self.Loginframe5 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black", pady=15)
        self.Loginframe5.place(x=0, y=360)

######################################################################################################################
        img16 = Image.open('D:\pythonProject7\\nattii\mango\Screenshot (490).png')
        img16 = img16.resize((140, 150))
        self.photo_img16 = ImageTk.PhotoImage(img16)
        b16 = Button(self.Loginframe1, image=self.photo_img16, borderwidth=3, padx=10, pady=5)
        b16.place(x=20, y=10)
        sud_name = Label(self.Loginframe1, text="Chocolate-cake\nRs-400", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        sud_name.place(x=177, y=8)

        img18 = Image.open('D:\pythonProject7\\nattii\mango\Screenshot (489).png')
        img18 = img18.resize((140, 150))
        self.photo_img18 = ImageTk.PhotoImage(img18)
        b18 = Button(self.Loginframe1, image=self.photo_img18, borderwidth=3, padx=10, pady=5)
        b18.place(x=530, y=10)
        cho_name = Label(self.Loginframe1, text="Spong-cake\nRs-200", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=13, height=2, padx=10)
        cho_name.place(x=350, y=120)

        img19 = Image.open('D:\pythonProject7\\nattii\mango\Screenshot (488).png')
        img19 = img19.resize((130, 150))
        self.photo_img19 = ImageTk.PhotoImage(img19)
        b19 = Button(self.Loginframe4, image=self.photo_img19, borderwidth=3, padx=10, pady=5)
        b19.place(x=20, y=10)
        sud_name = Label(self.Loginframe4, text="Fruits_cake-\nRs-400", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        sud_name.place(x=177, y=8)

        img20 = Image.open('D:\pythonProject7\\nattii\mango\Screenshot (487).png')
        img20 = img20.resize((130, 130))
        self.photo_img20 = ImageTk.PhotoImage(img20)
        b20 = Button(self.Loginframe4, image=self.photo_img20, borderwidth=3, padx=10, pady=5)
        b20.place(x=530, y=10)
        cho_name = Label(self.Loginframe4, text="Red-Velvet\nRs-300", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=13, height=2, padx=10)
        cho_name.place(x=350, y=110)

        img21 = Image.open('D:\pythonProject7\\nattii\mango\Screenshot (486).png')
        img21 = img21.resize((130, 130))
        self.photo_img21 = ImageTk.PhotoImage(img21)
        b21 = Button(self.Loginframe5, image=self.photo_img21, borderwidth=3, padx=10, pady=5)
        b21.place(x=20, y=10)
        sud_name = Label(self.Loginframe5, text="Chees-Cakee\nRs-200", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        sud_name.place(x=177, y=8)

        img22 = Image.open('D:\pythonProject7\\nattii\mango\Screenshot (485).png')
        img22 = img22.resize((130, 130))
        self.photo_img22 = ImageTk.PhotoImage(img22)
        b22 = Button(self.Loginframe5, image=self.photo_img22, borderwidth=3, padx=10, pady=5)
        b22.place(x=530, y=10)
        cho_name = Label(self.Loginframe5, text="IceCream-Cake\nRs-400", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=13, height=2, padx=10)
        cho_name.place(x=350, y=100)

        item_ordered = StringVar()
        quatity = IntVar()
        location = StringVar()
        Phone_num = IntVar()
        Total_price = IntVar()

        self.heading = Label(self.Loginframe2, text="Item selected", font=("arial 15 bold", 15), bg="black", fg="white"
                             , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading.place(x=10, y=30)

        self.heading1 = Label(self.Loginframe2, text="Quantity", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading1.place(x=10, y=120)

        self.heading2 = Label(self.Loginframe2, text="Location", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading2.place(x=10, y=200)

        self.heading3 = Label(self.Loginframe2, text="Phone_No", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading3.place(x=10, y=280)

        self.heading4 = Label(self.Loginframe2, text="Total-Price", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading4.place(x=10, y=360)

        e1 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=item_ordered)
        e1.place(x=250, y=40)  # item

        n = tk.StringVar()
        quantity = ttk.Combobox(self.Loginframe2, width=17, textvariable=n, font=("arial 15 bold", 10))
        quantity['values'] = ["1", "2", "3", "4", "5", "6"]
        quantity.current()
        quantity.place(x=250, y=130)

        e2 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=location)
        e2.place(x=250, y=210)

        e3 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=Phone_num)
        e3.place(x=250, y=290)

        e4 = Entry(self.Loginframe2, width=10, font=("arial 15 bold", 20), fg="black", text=Total_price)
        e4.place(x=250, y=370)

        button1 = Button(self.Loginframe2, text="BACK", bg="black", fg="white", width=10, height=2,
                         command=self.back_but)
        button1.place(x=30, y=490)

        button2 = Button(self.Loginframe2, text="ORDER", bg="black", fg="white", width=10, height=2,
                         command=self.order_info)
        button2.place(x=240, y=490)

        button3 = Button(self.Loginframe2, text="EXIT", bg="black", fg="white", width=10, height=2,
                         command=self.exitt_but)
        button3.place(x=440, y=490)

    def exitt_but(shelf):
        exitt_but = tkinter.messagebox.askretrycancel("status", "Are you sure you want to exit")
        if exitt > 0:
            return self.root

    def back_but(self):
        back_but = tkinter.messagebox.askretrycancel("status", "go back to home home")
        if back > 0:
            return self.root

    def order_info(self):
        order_but = tkinter.messagebox.askokcancel("status", "your order is placed successfully")
        if order > 0:
            return self.root


#############################################################################################################

############################################parrotta###############################################################
class window10:

    def __init__(self, master):
        self.master = master
        self.master.geometry("700x700")
        self.master.title("FRIES")
        self.frame = Frame(self.master)
        self.frame.pack()

        img13 = Image.open('D:\pythonProject6\jjjjjjj1\jiffff\Screenshot (389).png')
        img13 = img13.resize((150, 120))
        self.photo_img13 = ImageTk.PhotoImage(img13)
        b13 = Button(self.frame, image=self.photo_img13, borderwidth=0)
        b13.grid(row=0, column=0, pady=10)

        self.frame1 = Label(self.frame, text="FRIES".center(20), font=("arial 15 bold", 40), bg="gray15",
                            fg="white", bd=2,
                            relief="sunken", width=30, height=2)
        self.frame1.grid(row=0, column=2, padx=50, pady=10, columnspan=3)  # 2

        img14 = Image.open('D:\pythonProject6\jjjjjjj1\jiffff\ymmy\Screenshot (390).png')
        img14 = img14.resize((150, 120), Image.ANTIALIAS)
        self.photo_img14 = ImageTk.PhotoImage(img14)
        b14 = Button(self.frame, image=self.photo_img14, borderwidth=0)
        b14.grid(row=0, column=5)  # 5
    ###############################################################################################################
        self.Loginframe1 = Frame(self.frame, width=720, height=560, bd=10, relief="groove")
        self.Loginframe1.grid(row=1, column=0, columnspan=3)

        self.Loginframe2 = Frame(self.frame, width=693, height=560, bd=10, relief="groove")
        self.Loginframe2.grid(row=1, column=4, columnspan=3)

        self.Loginframe3 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black", pady=15,
                                padx=10)
        self.Loginframe3.place(x=0, y=0)

        self.Loginframe4 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black", pady=5)
        self.Loginframe4.place(x=0, y=180)

        self.Loginframe5 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black", pady=15)
        self.Loginframe5.place(x=0, y=360)

######################################################################################################################
        img16 = Image.open('D:\pythonProject7\\nattii\mango\Screenshot (514).png')
        img16 = img16.resize((140, 150))
        self.photo_img16 = ImageTk.PhotoImage(img16)
        b16 = Button(self.Loginframe1, image=self.photo_img16, borderwidth=3, padx=10, pady=5)
        b16.place(x=20, y=10)
        sud_name = Label(self.Loginframe1, text="Disco-fries\nRs-100", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        sud_name.place(x=177, y=8)

        img18 = Image.open('D:\pythonProject7\\nattii\mango\Screenshot (514).png')
        img18 = img18.resize((140, 150))
        self.photo_img18 = ImageTk.PhotoImage(img18)
        b18 = Button(self.Loginframe1, image=self.photo_img18, borderwidth=3, padx=10, pady=5)
        b18.place(x=530, y=10)
        cho_name = Label(self.Loginframe1, text="Poutine-Fries\nRs-100", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=13, height=2, padx=10)
        cho_name.place(x=350, y=120)

        img19 = Image.open('D:\pythonProject7\\nattii\Screenshot (512).png')
        img19 = img19.resize((130, 150))
        self.photo_img19 = ImageTk.PhotoImage(img19)
        b19 = Button(self.Loginframe4, image=self.photo_img19, borderwidth=3, padx=10, pady=5)
        b19.place(x=20, y=10)
        sud_name = Label(self.Loginframe4, text="ChiliChees-Fries\nRs-100",font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        sud_name.place(x=177, y=8)

        img20 = Image.open('D:\pythonProject7\\nattii\Screenshot (511).png')
        img20 = img20.resize((130, 130))
        self.photo_img20 = ImageTk.PhotoImage(img20)
        b20 = Button(self.Loginframe4, image=self.photo_img20, borderwidth=3, padx=10, pady=5)
        b20.place(x=530, y=10)
        cho_name = Label(self.Loginframe4, text="Crne asada-Fries\nRs-150" ,font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=13, height=2, padx=10)
        cho_name.place(x=350, y=110)

        img21 = Image.open('D:\pythonProject7\\nattii\Screenshot (510).png')
        img21 = img21.resize((130, 130))
        self.photo_img21 = ImageTk.PhotoImage(img21)
        b21 = Button(self.Loginframe5, image=self.photo_img21, borderwidth=3, padx=10, pady=5)
        b21.place(x=20, y=10)
        sud_name = Label(self.Loginframe5, text="Waffles-Fries\nRs-200", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        sud_name.place(x=177, y=8)

        img22 = Image.open('D:\pythonProject7\\nattii\Screenshot (509).png')
        img22 = img22.resize((130, 130))
        self.photo_img22 = ImageTk.PhotoImage(img22)
        b22 = Button(self.Loginframe5, image=self.photo_img22, borderwidth=3, padx=10, pady=5)
        b22.place(x=530, y=10)
        cho_name = Label(self.Loginframe5, text="Chess-Fries\nRs-180", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=13, height=2, padx=10)
        cho_name.place(x=350, y=100)

        item_ordered = StringVar()
        quatity = IntVar()
        location = StringVar()
        Phone_num = IntVar()
        Total_price = IntVar()

        self.heading = Label(self.Loginframe2, text="Item selected", font=("arial 15 bold", 15), bg="black", fg="white"
                             , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading.place(x=10, y=30)

        self.heading1 = Label(self.Loginframe2, text="Quantity", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading1.place(x=10, y=120)

        self.heading2 = Label(self.Loginframe2, text="Location", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading2.place(x=10, y=200)

        self.heading3 = Label(self.Loginframe2, text="Phone_No", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading3.place(x=10, y=280)

        self.heading4 = Label(self.Loginframe2, text="Total-Price", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading4.place(x=10, y=360)

        e1 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=item_ordered)
        e1.place(x=250, y=40)  # item

        n = tk.StringVar()
        quantity = ttk.Combobox(self.Loginframe2, width=17, textvariable=n, font=("arial 15 bold", 10))
        quantity['values'] = ["1", "2", "3", "4", "5", "6"]
        quantity.current()
        quantity.place(x=250, y=130)

        e2 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=location)
        e2.place(x=250, y=210)

        e3 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=Phone_num)
        e3.place(x=250, y=290)

        e4 = Entry(self.Loginframe2, width=10, font=("arial 15 bold", 20), fg="black", text=Total_price)
        e4.place(x=250, y=370)

        button1 = Button(self.Loginframe2, text="BACK", bg="black", fg="white", width=10, height=2,
                         command=self.back_but)
        button1.place(x=30, y=490)

        button2 = Button(self.Loginframe2, text="ORDER", bg="black", fg="white", width=10, height=2,
                         command=self.order_info)
        button2.place(x=240, y=490)

        button3 = Button(self.Loginframe2, text="EXIT", bg="black", fg="white", width=10, height=2,
                         command=self.exitt_but)
        button3.place(x=440, y=490)

    def exitt_but(shelf):
        exitt_but = tkinter.messagebox.askretrycancel("status", "Are you sure you want to exit")
        if exitt > 0:
            return self.root

    def back_but(self):
        back_but = tkinter.messagebox.askretrycancel("status", "go back to home home")
        if back > 0:
            return self.root

    def order_info(self):
        order_but = tkinter.messagebox.askokcancel("status", "your order is placed successfully")
        if order > 0:
            return self.root


#############################################################################################################

class window11:

        def __init__(self, master):
                self.master = master
                self.master.geometry("700x700")
                self.master.title("JUCIES")
                self.frame = Frame(self.master)
                self.frame.pack()

                img13 = Image.open('D:\pythonProject6\jjjjjjj1\jiffff\Screenshot (389).png')
                img13 = img13.resize((150, 120))
                self.photo_img13 = ImageTk.PhotoImage(img13)
                b13 = Button(self.frame, image=self.photo_img13, borderwidth=0)
                b13.grid(row=0, column=0, pady=10)

                self.frame1 = Label(self.frame, text="JUCIES".center(20), font=("arial 15 bold", 40), bg="gray15",
                                    fg="white", bd=2,
                                    relief="sunken", width=30, height=2)
                self.frame1.grid(row=0, column=2, padx=50, pady=10, columnspan=3)  # 2

                img14 = Image.open('D:\pythonProject6\jjjjjjj1\jiffff\ymmy\Screenshot (390).png')
                img14 = img14.resize((150, 120), Image.ANTIALIAS)
                self.photo_img14 = ImageTk.PhotoImage(img14)
                b14 = Button(self.frame, image=self.photo_img14, borderwidth=0)
                b14.grid(row=0, column=5)  # 5
                ###############################################################################################################
                self.Loginframe1 = Frame(self.frame, width=720, height=560, bd=10, relief="groove")
                self.Loginframe1.grid(row=1, column=0, columnspan=3)

                self.Loginframe2 = Frame(self.frame, width=693, height=560, bd=10, relief="groove")
                self.Loginframe2.grid(row=1, column=4, columnspan=3)

                self.Loginframe3 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black",
                                         pady=15,
                                         padx=10)
                self.Loginframe3.place(x=0, y=0)

                self.Loginframe4 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black",
                                         pady=5)
                self.Loginframe4.place(x=0, y=180)

                self.Loginframe5 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black",
                                         pady=15)
                self.Loginframe5.place(x=0, y=360)

                ######################################################################################################################
                img16 = Image.open('D:\pythonProject7\\nattii\pepper\Screenshot (509).png')
                img16 = img16.resize((140, 150))
                self.photo_img16 = ImageTk.PhotoImage(img16)
                b16 = Button(self.Loginframe1, image=self.photo_img16, borderwidth=3, padx=10, pady=5)
                b16.place(x=20, y=10)
                sud_name = Label(self.Loginframe1, text="Carrot-Juice\nRs-100", font=("arial 15 bold", 15),
                                 bg="gray60"
                                 , fg="black",
                                 relief="sunken", width=10, height=2, padx=10)
                sud_name.place(x=177, y=8)

                img18 = Image.open('D:\pythonProject7\\nattii\pepper\Screenshot (512).png')
                img18 = img18.resize((140, 150))
                self.photo_img18 = ImageTk.PhotoImage(img18)
                b18 = Button(self.Loginframe1, image=self.photo_img18, borderwidth=3, padx=10, pady=5)
                b18.place(x=530, y=10)
                cho_name = Label(self.Loginframe1, text="Watermelom-juice\nRs-100", font=("arial 15 bold", 15),
                                 bg="gray60"
                                 , fg="black",
                                 relief="sunken", width=13, height=2, padx=10)
                cho_name.place(x=350, y=120)

                img19 = Image.open('D:\pythonProject7\\nattii\pepper\Screenshot (511).png')
                img19 = img19.resize((130, 150))
                self.photo_img19 = ImageTk.PhotoImage(img19)
                b19 = Button(self.Loginframe4, image=self.photo_img19, borderwidth=3, padx=10, pady=5)
                b19.place(x=20, y=10)
                sud_name = Label(self.Loginframe4, text="Cherry-juice\nRs-100", font=("arial 15 bold", 15),
                                 bg="gray60"
                                 , fg="black",
                                 relief="sunken", width=10, height=2, padx=10)
                sud_name.place(x=177, y=8)

                img20 = Image.open('D:\pythonProject7\\nattii\pepper\Screenshot (510).png')
                img20 = img20.resize((130, 130))
                self.photo_img20 = ImageTk.PhotoImage(img20)
                b20 = Button(self.Loginframe4, image=self.photo_img20, borderwidth=3, padx=10, pady=5)
                b20.place(x=530, y=10)
                cho_name = Label(self.Loginframe4, text="Sugarcane-juice\nRs-150", font=("arial 15 bold", 15),
                                 bg="gray60"
                                 , fg="black",
                                 relief="sunken", width=13, height=2, padx=10)
                cho_name.place(x=350, y=110)

                img21 = Image.open('D:\pythonProject7\\nattii\pepper\Screenshot (509).png')
                img21 = img21.resize((130, 130))
                self.photo_img21 = ImageTk.PhotoImage(img21)
                b21 = Button(self.Loginframe5, image=self.photo_img21, borderwidth=3, padx=10, pady=5)
                b21.place(x=20, y=10)
                sud_name = Label(self.Loginframe5, text="Mango-juice\nRs-200", font=("arial 15 bold", 15),
                                 bg="gray60"
                                 , fg="black",
                                 relief="sunken", width=10, height=2, padx=10)
                sud_name.place(x=177, y=8)

                img22 = Image.open('D:\pythonProject7\\nattii\mango\Screenshot (517).png')
                img22 = img22.resize((130, 130))
                self.photo_img22 = ImageTk.PhotoImage(img22)
                b22 = Button(self.Loginframe5, image=self.photo_img22, borderwidth=3, padx=10, pady=5)
                b22.place(x=530, y=10)
                cho_name = Label(self.Loginframe5, text="Papaya-juice\nRs-180", font=("arial 15 bold", 15),
                                 bg="gray60"
                                 , fg="black",
                                 relief="sunken", width=13, height=2, padx=10)
                cho_name.place(x=350, y=100)

                item_ordered = StringVar()
                quatity = IntVar()
                location = StringVar()
                Phone_num = IntVar()
                Total_price = IntVar()

                self.heading = Label(self.Loginframe2, text="Item selected", font=("arial 15 bold", 15), bg="black",
                                     fg="white"
                                     , relief=RIDGE, padx=10, pady=10, width=10)
                self.heading.place(x=10, y=30)

                self.heading1 = Label(self.Loginframe2, text="Quantity", font=("arial 15 bold", 15), bg="black",
                                      fg="white"
                                      , relief=RIDGE, padx=10, pady=10, width=10)
                self.heading1.place(x=10, y=120)

                self.heading2 = Label(self.Loginframe2, text="Location", font=("arial 15 bold", 15), bg="black",
                                      fg="white"
                                      , relief=RIDGE, padx=10, pady=10, width=10)
                self.heading2.place(x=10, y=200)

                self.heading3 = Label(self.Loginframe2, text="Phone_No", font=("arial 15 bold", 15), bg="black",
                                      fg="white"
                                      , relief=RIDGE, padx=10, pady=10, width=10)
                self.heading3.place(x=10, y=280)

                self.heading4 = Label(self.Loginframe2, text="Total-Price", font=("arial 15 bold", 15), bg="black",
                                      fg="white"
                                      , relief=RIDGE, padx=10, pady=10, width=10)
                self.heading4.place(x=10, y=360)

                e1 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black",
                           textvariable=item_ordered)
                e1.place(x=250, y=40)  # item

                n = tk.StringVar()
                quantity = ttk.Combobox(self.Loginframe2, width=17, textvariable=n, font=("arial 15 bold", 10))
                quantity['values'] = ["1", "2", "3", "4", "5", "6"]
                quantity.current()
                quantity.place(x=250, y=130)

                e2 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=location)
                e2.place(x=250, y=210)

                e3 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=Phone_num)
                e3.place(x=250, y=290)

                e4 = Entry(self.Loginframe2, width=10, font=("arial 15 bold", 20), fg="black", text=Total_price)
                e4.place(x=250, y=370)

                button1 = Button(self.Loginframe2, text="BACK", bg="black", fg="white", width=10, height=2,
                                 command=self.back_but)
                button1.place(x=30, y=490)

                button2 = Button(self.Loginframe2, text="ORDER", bg="black", fg="white", width=10, height=2,
                                 command=self.order_info)
                button2.place(x=240, y=490)

                button3 = Button(self.Loginframe2, text="EXIT", bg="black", fg="white", width=10, height=2,
                                 command=self.exitt_but)
                button3.place(x=440, y=490)

        def exitt_but(shelf):
            exitt_but = tkinter.messagebox.askretrycancel("status", "Are you sure you want to exit")
            if exitt > 0:
                return self.root

        def back_but(self):
            back_but = tkinter.messagebox.askretrycancel("status", "go back to home home")
            if back > 0:
                return self.root

        def order_info(self):
            order_but = tkinter.messagebox.askokcancel("status", "your order is placed successfully")
            if order > 0:
                return self.root


#########################################################################################################3
class window12:

    def __init__(self, master):
        self.master = master
        self.master.geometry("700x700")
        self.master.title("SWEETS")
        self.frame = Frame(self.master)
        self.frame.pack()

        img13 = Image.open('D:\pythonProject6\jjjjjjj1\jiffff\Screenshot (389).png')
        img13 = img13.resize((150, 120))
        self.photo_img13 = ImageTk.PhotoImage(img13)
        b13 = Button(self.frame, image=self.photo_img13, borderwidth=0)
        b13.grid(row=0, column=0, pady=10)

        self.frame1 = Label(self.frame, text="SWEETS".center(20), font=("arial 15 bold", 40), bg="gray15",
                            fg="white", bd=2,
                            relief="sunken", width=30, height=2)
        self.frame1.grid(row=0, column=2, padx=50, pady=10, columnspan=3)  # 2

        img14 = Image.open('D:\pythonProject6\jjjjjjj1\jiffff\ymmy\Screenshot (390).png')
        img14 = img14.resize((150, 120), Image.ANTIALIAS)
        self.photo_img14 = ImageTk.PhotoImage(img14)
        b14 = Button(self.frame, image=self.photo_img14, borderwidth=0)
        b14.grid(row=0, column=5)  # 5
        ###############################################################################################################
        self.Loginframe1 = Frame(self.frame, width=720, height=560, bd=10, relief="groove")
        self.Loginframe1.grid(row=1, column=0, columnspan=3)

        self.Loginframe2 = Frame(self.frame, width=693, height=560, bd=10, relief="groove")
        self.Loginframe2.grid(row=1, column=4, columnspan=3)

        self.Loginframe3 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black",
                                 pady=15,
                                 padx=10)
        self.Loginframe3.place(x=0, y=0)

        self.Loginframe4 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black",
                                 pady=5)
        self.Loginframe4.place(x=0, y=180)

        self.Loginframe5 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black",
                                 pady=15)
        self.Loginframe5.place(x=0, y=360)

        ######################################################################################################################
        img16 = Image.open('D:\pythonProject7\\nattii\pepper\Screenshot (519).png')
        img16 = img16.resize((140, 150))
        self.photo_img16 = ImageTk.PhotoImage(img16)
        b16 = Button(self.Loginframe1, image=self.photo_img16, borderwidth=3, padx=10, pady=5)
        b16.place(x=20, y=10)
        sud_name = Label(self.Loginframe1, text="Cham-Cham Sweet\nRs-300", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        sud_name.place(x=177, y=8)

        img18 = Image.open('D:\pythonProject7\\nattii\pepper\Screenshot (518).png')
        img18 = img18.resize((140, 150))
        self.photo_img18 = ImageTk.PhotoImage(img18)
        b18 = Button(self.Loginframe1, image=self.photo_img18, borderwidth=3, padx=10, pady=5)
        b18.place(x=530, y=10)
        cho_name = Label(self.Loginframe1, text="Burfi\nRs-200", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=13, height=2, padx=10)
        cho_name.place(x=350, y=120)

        img19 = Image.open('D:\pythonProject7\\nattii\pepper\Screenshot (517).png')
        img19 = img19.resize((130, 150))
        self.photo_img19 = ImageTk.PhotoImage(img19)
        b19 = Button(self.Loginframe4, image=self.photo_img19, borderwidth=3, padx=10, pady=5)
        b19.place(x=20, y=10)
        sud_name = Label(self.Loginframe4, text="Rasagulla-sweer\nRs-300", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        sud_name.place(x=177, y=8)

        img20 = Image.open('D:\pythonProject7\\nattii\pepper\Screenshot (516).png')
        img20 = img20.resize((130, 130))
        self.photo_img20 = ImageTk.PhotoImage(img20)
        b20 = Button(self.Loginframe4, image=self.photo_img20, borderwidth=3, padx=10, pady=5)
        b20.place(x=530, y=10)
        cho_name = Label(self.Loginframe4, text="Rasamalai-Sweet\nRs-350", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=13, height=2, padx=10)
        cho_name.place(x=350, y=110)

        img21 = Image.open('D:\pythonProject7\\nattii\pepper\Screenshot (515).png')
        img21 = img21.resize((130, 130))
        self.photo_img21 = ImageTk.PhotoImage(img21)
        b21 = Button(self.Loginframe5, image=self.photo_img21, borderwidth=3, padx=10, pady=5)
        b21.place(x=20, y=10)
        sud_name = Label(self.Loginframe5, text="Halwa\nRs-200", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        sud_name.place(x=177, y=8)

        img22 = Image.open('D:\pythonProject7\\nattii\pepper\Screenshot (514).png')
        img22 = img22.resize((130, 130))
        self.photo_img22 = ImageTk.PhotoImage(img22)
        b22 = Button(self.Loginframe5, image=self.photo_img22, borderwidth=3, padx=10, pady=5)
        b22.place(x=530, y=10)
        cho_name = Label(self.Loginframe5, text="Glab-jamun\nRs-380", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=13, height=2, padx=10)
        cho_name.place(x=350, y=100)

        item_ordered = StringVar()
        quatity = IntVar()
        location = StringVar()
        Phone_num = IntVar()
        Total_price = IntVar()

        self.heading = Label(self.Loginframe2, text="Item selected", font=("arial 15 bold", 15), bg="black", fg="white"
                             , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading.place(x=10, y=30)

        self.heading1 = Label(self.Loginframe2, text="Quantity", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading1.place(x=10, y=120)

        self.heading2 = Label(self.Loginframe2, text="Location", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading2.place(x=10, y=200)

        self.heading3 = Label(self.Loginframe2, text="Phone_No", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading3.place(x=10, y=280)

        self.heading4 = Label(self.Loginframe2, text="Total-Price", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading4.place(x=10, y=360)

        e1 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=item_ordered)
        e1.place(x=250, y=40)  # item

        n = tk.StringVar()
        quantity = ttk.Combobox(self.Loginframe2, width=17, textvariable=n, font=("arial 15 bold", 10))
        quantity['values'] = ["1", "2", "3", "4", "5", "6"]
        quantity.current()
        quantity.place(x=250, y=130)

        e2 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=location)
        e2.place(x=250, y=210)

        e3 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black", textvariable=Phone_num)
        e3.place(x=250, y=290)

        e4 = Entry(self.Loginframe2, width=10, font=("arial 15 bold", 20), fg="black", text=Total_price)
        e4.place(x=250, y=370)

        button1 = Button(self.Loginframe2, text="BACK", bg="black", fg="white", width=10, height=2,
                         command=self.back_but)
        button1.place(x=30, y=490)

        button2 = Button(self.Loginframe2, text="ORDER", bg="black", fg="white", width=10, height=2,
                         command=self.order_info)
        button2.place(x=240, y=490)

        button3 = Button(self.Loginframe2, text="EXIT", bg="black", fg="white", width=10, height=2,
                         command=self.exitt_but)
        button3.place(x=440, y=490)

    def exitt_but(shelf):
        exitt_but = tkinter.messagebox.askretrycancel("status", "Are you sure you want to exit")
        if exitt > 0:
            return self.root

    def back_but(self):
        back_but = tkinter.messagebox.askretrycancel("status", "go back to home home")
        if back > 0:
            return self.root

    def order_info(self):
        order_but = tkinter.messagebox.askokcancel("status", "your order is placed successfully")
        if order > 0:
            return self.root




#####################################################################################################################

class window13:

    def __init__(self, master):
        self.master = master
        self.master.geometry("700x700")
        self.master.title("ROLLS")
        self.frame = Frame(self.master)
        self.frame.pack()

        img13 = Image.open('D:\pythonProject6\jjjjjjj1\jiffff\Screenshot (389).png')
        img13 = img13.resize((150, 120))
        self.photo_img13 = ImageTk.PhotoImage(img13)
        b13 = Button(self.frame, image=self.photo_img13, borderwidth=0)
        b13.grid(row=0, column=0, pady=10)

        self.frame1 = Label(self.frame, text="ROLLS".center(20), font=("arial 15 bold", 40), bg="gray15",
                            fg="white", bd=2,
                            relief="sunken", width=30, height=2)
        self.frame1.grid(row=0, column=2, padx=50, pady=10, columnspan=3)  # 2

        img14 = Image.open('D:\pythonProject6\jjjjjjj1\jiffff\ymmy\Screenshot (390).png')
        img14 = img14.resize((150, 120), Image.ANTIALIAS)
        self.photo_img14 = ImageTk.PhotoImage(img14)
        b14 = Button(self.frame, image=self.photo_img14, borderwidth=0)
        b14.grid(row=0, column=5)  # 5
        ###############################################################################################################
        self.Loginframe1 = Frame(self.frame, width=720, height=560, bd=10, relief="groove")
        self.Loginframe1.grid(row=1, column=0, columnspan=3)

        self.Loginframe2 = Frame(self.frame, width=693, height=560, bd=10, relief="groove")
        self.Loginframe2.grid(row=1, column=4, columnspan=3)

        self.Loginframe3 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black",
                                 pady=15,
                                 padx=10)
        self.Loginframe3.place(x=0, y=0)

        self.Loginframe4 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black",
                                 pady=5)
        self.Loginframe4.place(x=0, y=180)

        self.Loginframe5 = Frame(self.Loginframe1, width=693, height=180, bd=5, relief=RIDGE, bg="black",
                                 pady=15)
        self.Loginframe5.place(x=0, y=360)

        ######################################################################################################################
        img16 = Image.open('D:\pythonProject7\\venv\Scripts\\rolls\Screenshot (507).png')
        img16 = img16.resize((140, 150))
        self.photo_img16 = ImageTk.PhotoImage(img16)
        b16 = Button(self.Loginframe1, image=self.photo_img16, borderwidth=3, padx=10, pady=5)
        b16.place(x=20, y=10)
        sud_name = Label(self.Loginframe1, text="Springs\nRs-200", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        sud_name.place(x=177, y=8)

        img18 = Image.open('D:\pythonProject7\\venv\Scripts\\rolls\Screenshot (506).png')
        img18 = img18.resize((140, 150))
        self.photo_img18 = ImageTk.PhotoImage(img18)
        b18 = Button(self.Loginframe1, image=self.photo_img18, borderwidth=3, padx=10, pady=5)
        b18.place(x=530, y=10)
        cho_name = Label(self.Loginframe1, text="Chicken rolls\nRs-200", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=13, height=2, padx=10)
        cho_name.place(x=350, y=120)

        img19 = Image.open('D:\pythonProject7\\nattii\mango\Screenshot (515).png')
        img19 = img19.resize((130, 150))
        self.photo_img19 = ImageTk.PhotoImage(img19)
        b19 = Button(self.Loginframe4, image=self.photo_img19, borderwidth=3, padx=10, pady=5)
        b19.place(x=20, y=10)
        sud_name = Label(self.Loginframe4, text="Kebeb-rolls\nRs-300", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        sud_name.place(x=177, y=8)

        img20 = Image.open('D:\pythonProject7\\venv\Scripts\\rolls\Screenshot (510).png')
        img20 = img20.resize((130, 130))
        self.photo_img20 = ImageTk.PhotoImage(img20)
        b20 = Button(self.Loginframe4, image=self.photo_img20, borderwidth=3, padx=10, pady=5)
        b20.place(x=530, y=10)
        cho_name = Label(self.Loginframe4, text="Veg-rolls\nRs-350", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=13, height=2, padx=10)
        cho_name.place(x=350, y=110)

        img21 = Image.open('D:\pythonProject7\\venv\Scripts\\rolls\Screenshot (511).png')
        img21 = img21.resize((130, 130))
        self.photo_img21 = ImageTk.PhotoImage(img21)
        b21 = Button(self.Loginframe5, image=self.photo_img21, borderwidth=3, padx=10, pady=5)
        b21.place(x=20, y=10)
        sud_name = Label(self.Loginframe5, text="Paneer rolls\nRs-200", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=10, height=2, padx=10)
        sud_name.place(x=177, y=8)

        img22 = Image.open('D:\pythonProject7\\venv\Scripts\\rolls\Screenshot (509).png')
        img22 = img22.resize((130, 130))
        self.photo_img22 = ImageTk.PhotoImage(img22)
        b22 = Button(self.Loginframe5, image=self.photo_img22, borderwidth=3, padx=10, pady=5)
        b22.place(x=530, y=10)
        cho_name = Label(self.Loginframe5, text="Soya-rolls\nRs-380", font=("arial 15 bold", 15),
                         bg="gray60"
                         , fg="black",
                         relief="sunken", width=13, height=2, padx=10)
        cho_name.place(x=350, y=100)
        item_ordered=StringVar()
        quatity=IntVar()
        location=StringVar()
        Phone_num=IntVar()
        Total_price=IntVar()


        self.heading=Label(self.Loginframe2,text="Item selected",font=("arial 15 bold",15),bg="black",fg="white"
                           ,relief=RIDGE,padx=10,pady=10,width=10)
        self.heading.place(x=10,y=30)


        self.heading1 = Label(self.Loginframe2, text="Quantity", font=("arial 15 bold", 15), bg="black", fg="white"
                             , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading1.place(x=10, y=120)

        self.heading2 = Label(self.Loginframe2, text="Location", font=("arial 15 bold", 15), bg="black", fg="white"
                             , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading2.place(x=10, y=200)

        self.heading3 = Label(self.Loginframe2, text="Phone_No", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading3.place(x=10, y=280)

        self.heading4 = Label(self.Loginframe2, text="Total-Price", font=("arial 15 bold", 15), bg="black", fg="white"
                              , relief=RIDGE, padx=10, pady=10, width=10)
        self.heading4.place(x=10, y=360)

        e1=Entry(self.Loginframe2,width=20,font=("arial 15 bold",20),fg="black",textvariable=item_ordered)
        e1.place(x=250,y=40)#item

        n=tk.StringVar()
        quantity=ttk.Combobox(self.Loginframe2,width=17,textvariable=n,font=("arial 15 bold",10))
        quantity['values']=["1","2","3","4","5","6"]
        quantity.current()
        quantity.place(x=250,y=130)

        e2 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black",textvariable=location)
        e2.place(x=250, y=210)

        e3 = Entry(self.Loginframe2, width=20, font=("arial 15 bold", 20), fg="black",textvariable=Phone_num)
        e3.place(x=250, y=290)

        e4 = Entry(self.Loginframe2, width=10, font=("arial 15 bold", 20), fg="black",text=Total_price)
        e4.place(x=250, y=370)

        button1=Button(self.Loginframe2,text="BACK",bg="black",fg="white",width=10,height=2,
                       command=self.back_but)
        button1.place(x=30,y=490)

        button2 = Button(self.Loginframe2, text="ORDER", bg="black", fg="white", width=10, height=2,
                         command=self.order_info)
        button2.place(x=240, y=490)

        button3 = Button(self.Loginframe2, text="EXIT", bg="black", fg="white", width=10, height=2,
                         command=self.exitt_but)
        button3.place(x=440, y=490)

    def exitt_but(shelf):
        exitt_but = tkinter.messagebox.askretrycancel("status", "Are you sure you want to exit")
        if exitt > 0:
            return self.root

    def back_but(self):
        back_but = tkinter.messagebox.askretrycancel("status", "go back to home home")
        if back > 0:
            return self.root

    def order_info(self):
        order_but = tkinter.messagebox.askokcancel("status", "your order is placed successfully")
        if order > 0:
            return self.root





if __name__=="__main__":
    main()