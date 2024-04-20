from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")



        # title label
        title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # img top
        img_top = Image.open(r"images\help.jpg")
        img_top = img_top.resize((1530, 800), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=800)

        dev_label =Label(f_lbl,text='Email: college166@gmail.com' ,font=('times new roman',16,'bold'),fg = "red", bg = "white")
        dev_label.place(x= 630, y=60)







if __name__== "__main__":
    root =Tk()
    obj=Help(root)
    root.mainloop()