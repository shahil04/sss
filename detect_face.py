import tkinter as tk
from tkinter import *

from PIL import Image,ImageTk
import pyttsx3 as pp
import speech_recognition as s
import threading
import numpy as np
import os
import cv2
from tkinter import messagebox
import mysql.connector


engine=pp.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

def register():
    #window.destroy()
    import register
    

def login():
    def recognize(img,classifier,scaleFactor,minNeighbhors,color,text,clf):
        gray_image=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbhors)
        #coords=[]

        for x,y,w,h in features:
            cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
            id,pred=clf.predict(gray_image[y:y+h,x:x+w]) #predicted by AI
            confidence=int(100*(1-pred/300))

            mydb=mysql.connector.connect(host="localhost",user="root",password="",database="FiProject")
            mycursor=mydb.cursor()
            mycursor.execute("SELECT t_fname from PTable WHERE id="+str(id))
            s_name=mycursor.fetchone()
            s_name= ''+''.join(s_name)

            if confidence>85:
                cv2.putText(img,s_name,(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,1,cv2.LINE_AA)
                video_capture.release()
                cv2.destroyAllWindows()
                import login
            elif confidence>60:
                cv2.putText(img,s_name,(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,color,1,cv2.LINE_AA)
            else:
                cv2.putText(img,"Unknown",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),1,cv2.LINE_AA)
                #messagebox.showinfo('Result','User not registered..!')

                


    faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    clf=cv2.face.LBPHFaceRecognizer_create()
    clf.read("classifier.xml")

    video_capture=cv2.VideoCapture(0)

    while True:
        ret,img=video_capture.read()
        recognize(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
        cv2.imshow("face detection",img)

        if cv2.waitKey(1)==13:
            break

    video_capture.release()
    cv2.destroyAllWindows()

window=tk.Tk()
window.attributes('-fullscreen', True)
window.bind("<Escape>",lambda event: window.attributes("-fullscreen", False))
window.title("Face detection")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
load=Image.open("img7.jpg")
photo=ImageTk.PhotoImage(load)

canvas=Canvas(window,width=screen_width, height=screen_height,bg="#000000")
canvas.create_image(screen_width/2,screen_height/2,image=photo) 
canvas.pack(fill=BOTH)

load2=Image.open("img8.jpg")
photo2=ImageTk.PhotoImage(load2)

b1=tk.Button(canvas,image=photo2,bg="#001a33",bd=6, command=login)
b1.place(x=528,y=480)
b2=tk.Button(canvas,text="Signup",bg="#001a33",fg="white",bd=2,command=register)
b2.place(x=48,y=120)

#window.geometry(str(screen_width)+"x"+ str(screen_height))
def repeatL():
    answer="Hello there!, Detect yourself by clicking the power button, and if your not registered then registered yourself first "
    speak(answer)

t=threading.Thread(target=repeatL)
t.start()
window.mainloop()


