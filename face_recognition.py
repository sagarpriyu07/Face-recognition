from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import csv
import cv2
import os
# directory_location = os.listdir(r"C:\Users\ASUS\Documents\project\data")
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")


        title_lbl=Label(self.root, text = "FACE RECOGNITION", font = ("times new roman",35,"bold"), bg = "white", fg="green")
        title_lbl.place(x = 0, y=0, width = 1530, height = 45)



        #img1 top
        img_top= Image.open(r"images\face1.webp")
        img_top = img_top.resize((650,850), Image.LANCZOS)
        self.photoimg_top= ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image = self.photoimg_top)
        f_lbl.place(x = 0, y= 55, width = 650, height = 850)


        # img2
        img_bottom= Image.open(r"images\face4.jpg")
        img_bottom = img_bottom.resize((950,850), Image.LANCZOS)
        self.photoimg_bottom= ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image = self.photoimg_bottom)
        f_lbl.place(x = 650, y= 55, width = 950, height = 850)


        # button 
        b1_1 = Button(f_lbl,text='Face Recognition', cursor='hand2',command=self.face_recog,font = ("times new roman",25,"bold"), bg = "dark blue", fg="white")
        b1_1.place(x=200, y=520, width = 500, height =100)

    #=========================== Attendence ===============================
    def mark_attendence(self,i,r,n,d):
            with open ("attendance.csv","r+",newline="\n") as f:
                myDataList=f.readlines()
                name_list=[]
                for line in myDataList:
                    entry =line.split((","))
                    name_list.append(entry[0])
                if((i not in name_list) and (r not in name_list) and (n not in name_list )and (d not in name_list)):
                        now=datetime.now()
                        d1=now.strftime("%d/%m/%Y")
                        dtString=now.strftime("%H:%M:%S")
                        f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")




    # ==============================face recognition==========================


    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)


            coord = []

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w, y+h),(0,255,0),3)
                id, predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))


                conn = mysql.connector.connect(host = "localhost", user= "root", password="Priyanka@07",database="face_recognizer")
                my_cursor=conn.cursor() 

                # my_cursor.execute("select Name from student where Student_id="+str(id))
                my_cursor.execute("select Name from student where Student_id= %s",(id,))
                n=my_cursor.fetchone()
                # n="+".join(n )
               
                if n is not None:
                    n = "+".join(n)
                else:
                    n = "Unknown"

                my_cursor.execute("select Rollno from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                # print("Rollno:",r)
                # r="+".join(r)
                if r is not None:
                    r = "+".join(r)
                else:
                    r = "Unknown"

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                # print("Rollno:",r)
                # r="+".join(r)
                if i is not None:
                    i = "+".join(i)
                else:
                    i = "Unknown"

                my_cursor.execute("select Dep from student where Student_id= %s",(id,))
                d=my_cursor.fetchone()
                # n="+".join(n )
               
                if d is not None:
                    d = "+".join(d)
                else:
                    d = "Unknown"

                if confidence>77:
                    cv2.putText(img,f"Student ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Rollno:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w, y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,h]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img


        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognization",img)
            if cv2.waitKey(1) == 13:
                break
            
            if cv2.getWindowProperty("Welcome To Face Recognization", cv2.WND_PROP_VISIBLE) < 1:
                break
        video_cap.release()
        cv2.destroyAllWindows()




if __name__== "__main__":
    root =Tk()
    obj=Face_Recognition(root)
    root.mainloop()