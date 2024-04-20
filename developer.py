from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")



        # title label
        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width=1530, height=55)

        #frame
        main_frame=Frame(self.root,bd=2)
        main_frame.place(x=0,y=45,width=1530,height=800)

        # # img top
        img_top = Image.open(r"images\dev7.jpg")
        img_top = img_top.resize((1530, 800), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(main_frame, image=self.photoimg_top)
        f_lbl.place(x=0, y=0, width=1530, height=800)

        


        # frame

        frame1=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,font=('times new roman',12,'bold'))
        frame1.place(x=10,y=250,width=500,height=300)

        # img top
        img_top1 = Image.open(r"images\dev_girlp.jpg")
        img_top1 = img_top1.resize((500, 300), Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl1 = Label(frame1, image=self.photoimg_top1)
        f_lbl1.place(x=0, y=0, width=500, height=300)


        #developer info
        dev_label1 =Label(frame1,text='Priyanka Sagar (IT Final Year)' ,font=('times new roman',16,'bold'),fg = "black", bg = "white")
        dev_label1.place(x= 90, y=200)

        dev_label1 =Label(frame1,text="Roll No. :2001660130042" ,font=('times new roman',16,'bold'),fg="black", bg = "white")
        dev_label1.place(x= 90, y=235)
        


        # frame 2

        frame2=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,font=('times new roman',12,'bold'))
        frame2.place(x=520,y=250,width=500,height=300)

        # img top
        img_top2 = Image.open(r"images\dev_girli3.jpg")
        img_top2 = img_top2.resize((500, 300), Image.LANCZOS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)

        f_lbl2 = Label(frame2, image=self.photoimg_top2)
        f_lbl2.place(x=0, y=0, width=500, height=300)


        #developer info
        dev_label1 =Label(frame2,text='Isha Rathi (IT Final Year)' ,font=('times new roman',16,'bold'),fg = "black", bg = "white")
        dev_label1.place(x= 90, y=200)

        dev_label1 =Label(frame2,text="Roll No. :2001660130027" ,font=('times new roman',16,'bold'),fg="black", bg = "white")
        dev_label1.place(x= 90, y=235)


        # frame 33
        frame3=LabelFrame(main_frame,bd=2,bg='white',relief=RIDGE,font=('times new roman',12,'bold'))
        frame3.place(x=1030,y=250,width=500,height=300)

        # img top
        img_top3 = Image.open(r"images\dev_girla2.jpg")
        img_top3 = img_top3.resize((500, 300), Image.LANCZOS)
        self.photoimg_top3 = ImageTk.PhotoImage(img_top3)

        f_lbl3 = Label(frame3, image=self.photoimg_top3)
        f_lbl3.place(x=0, y=0, width=500, height=300)


        #developer info
        dev_label1 =Label(frame3,text='Akanksha (IT Final Year)' ,font=('times new roman',16,'bold'),fg = "black", bg = "white")
        dev_label1.place(x= 90, y=200)

        dev_label1 =Label(frame3,text="Roll No. :2001660130006" ,font=('times new roman',16,'bold'),fg="black", bg = "white")
        dev_label1.place(x= 90, y=235)




if __name__== "__main__":
    root =Tk()
    obj=Developer(root)
    root.mainloop()