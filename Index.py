import cv2
from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import os
from time import strftime
from datetime import datetime
from tkinter import messagebox

class Face_Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("700x700+450+50")
        self.root.title("Number Plate Detection")

    
        img2 = Image.open(r"bg_img1.png")
        img2 = img2.resize((700,700) , Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        bg_img = Label(self.root,image =self.photoimg2)
        bg_img.place(x = 0,y = 0,width=700,height=700)

        def time():
            string=strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000, time)


        lbl= Label(self.root,font=("Comic Sans MS",9,"bold"),background="light green",foreground="navy blue")
        lbl.place(x=0,y=2,width=90,height=50)
        time()

        #button
        img3 = Image.open(r"detect.png")
        img3 = img3.resize((220,220) , Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(bg_img,image = self.photoimg3,cursor="hand2",command=self.car_number_plate)
        b1.place(x=100,y=80,width=220,height=220)
        
        b1_1 = Button(bg_img,text="Detect Number Plate",cursor="hand2",command=self.car_number_plate,font=("Comic Sans MS",15,"bold"),bg="white",fg="green")
        b1_1.place(x=100,y=300,width=220,height=30)

        #file button
        img4 = Image.open(r"photos_image.jpg")
        img4 = img4.resize((220,220) , Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img,image = self.photoimg4,cursor="hand2",command=self.file)
        b1.place(x=420,y=80,width=220,height=220)
        
        b1_1 = Button(bg_img,text="Saved Image",cursor="hand2",command=self.file,font=("Comic Sans MS",15,"bold"),bg="white",fg="darkblue")
        b1_1.place(x=420,y=300,width=220,height=30)


        #Exit button
        img5 = Image.open(r"Exit_image.jpg")
        img5 = img5.resize((220,220) , Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img,image = self.photoimg5,cursor="hand2",command=self.exit)
        b1.place(x=250,y=400,width=220,height=220)
        
        b1_1 = Button(bg_img,text="Exit",cursor="hand2",command=self.exit,font=("Comic Sans MS",15,"bold"),bg="white",fg="red")
        b1_1.place(x=250,y=620,width=220,height=30)



    def car_number_plate(self):

        #Car Number Plate Detection#######################
        framewidth = 640
        frameheight = 480
        nPlatecascade= cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
        minimumarea = 500
        color = (255,0,255)
        count = 0
        ######################
        cap = cv2.VideoCapture(0)
        cap.set(3,framewidth)
        cap.set(4,frameheight)

        while True:
            
            succsess , img = cap.read()
            imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            NumberPlates = nPlatecascade.detectMultiScale(imgGray,1.1,4)
            for (x,y,w,h) in NumberPlates:
                area = w*h
                if area> minimumarea:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
                    cv2.putText(img , "NumberPlate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX , 1  ,color,2)
                    #image region of interest a.k.a ROI
                    imgroi  =img[y:y+h , x:x+w]
                    cv2.imshow("Region of Interest",imgroi)
                    
            cv2.imshow("Result", img)
            if  cv2.waitKey(1) & 0xFF == ord('s'):
                cv2.imwrite("D:/Projects/Car_Number_Plate_Detection/Number_Plate_Image/NoPlate_"+str(count)+".jpg",imgroi)
                cv2.rectangle(img , (0,200),(640,300),(0,255,0),cv2.FILLED)
                cv2.putText(img , "Scan Saved",(150,265) , cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
                cv2.imshow("Result", img)
                cv2.waitKey(500)
                count+=1

            
            elif cv2.waitKey(1)==13:
                break
        cap.release()
        cv2.destroyAllWindows()


    #Exit
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Attendance","Exit this project??",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return

    #File
    def file(self):
        os.startfile("Number_Plate_Image")


if __name__=='__main__':
    root = Tk()
    obj = Face_Attendance(root)
    root.mainloop()
