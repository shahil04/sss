import tkinter as tk
from tkinter import*
from tkinter import ttk                    # For comboBox (in security question)
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import numpy as np
from PIL import Image
import os
import cv2


window=tk.Toplevel()
window.title("User Registration")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

def login():
    window.destroy()
    window.quit()

def train_classifier():
    messagebox.showinfo('Information','it will take few second to complete, wait few seconds !')
    data_dir="data"
    path=[os.path.join(data_dir,f) for f in os.listdir(data_dir)]
    faces=[]
    ids=[]

    for image in path:
        img=Image.open(image).convert('L')
        imageNp=np.array(img,'uint8')
        id=int(os.path.split(image)[1].split(".")[1])
        #[C:\Users\Hp\Favorites\Desktop\Python\face_recoginition\data\]index(0)[[user]index(0).[1]index(1).1]index(1)
        faces.append(imageNp)
        ids.append(id)

    ids=np.array(ids)

    #train the classifier
    clf=cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces,ids)
    clf.write("classifier.xml")
    messagebox.showinfo('Result','Face Training Completed..!')



# Background image
bbg=ImageTk.PhotoImage(file='C:/Users/Hp/Favorites/Desktop/Python/Project/img3.jpg')
bg=Label(window,bg="#000000").place(x=0, y=0,relwidth=1,relheight=1)

# Background image
lleft=ImageTk.PhotoImage(file='C:/Users/Hp/Favorites/Desktop/Python/Project/img5.png')
left=Label(window,image=lleft).place(x=80, y=100,width=400,height=500)

# Register Frame
frame1= Frame(window, bg="#000000")
frame1.place(x=480, y=100, width=700, height=500)

title= Label(frame1, text="REGISTER HERE!!!",bd=5, font=("Goudy Old Style",25,"bold"),bg="red",fg="white").place(x=50,y=30)

# 1st line------------------------------
fname= tk.Label(frame1, text="First Name", font=("Copperplate Gothic Light",15,"bold"),bg="black",fg="white").place(x=50,y=100)
t_fname=tk.Entry(frame1, font=("times new roman",15),bg="lightgrey")
t_fname.place(x=50,y=130, width=250)

lname= tk.Label(frame1, text="Last Name", font=("Copperplate Gothic Light",15,"bold"),bg="black",fg="white").place(x=370,y=100)
t_lname= tk.Entry(frame1, font=("times new roman",15),bg="lightgrey")
t_lname.place(x=370,y=130, width=250)

# 2nd line------------------------------
contact= tk.Label(frame1, text="Phone No.", font=("Copperplate Gothic Light",15,"bold"),bg="black",fg="white").place(x=50,y=170)
t_contact= tk.Entry(frame1, font=("times new roman",15),bg="lightgrey")
t_contact.place(x=50,y=200, width=250)

email= tk.Label(frame1, text="Email", font=("Copperplate Gothic Light",15,"bold"),bg="black",fg="white").place(x=370,y=170)
t_email= tk.Entry(frame1, font=("times new roman",15),bg="lightgrey")
t_email.place(x=370,y=200, width=250)

# 3rd line------------------------------
question= Label(frame1, text="Security Question", font=("Copperplate Gothic Light",15,"bold"),bg="black",fg="white").place(x=50,y=240)
c_question= ttk.Combobox(frame1, font=("Copperplate Gothic Light",13),state='readonly', justify=CENTER)
c_question['values']= ("Select", "Your Birth Place", "Your Pet Name", "Your First School Name", "Your Favourite Tourist Spot", "Your Favourite Player")
c_question.place(x=50,y=270, width=250)
c_question.current(0)

answer= Label(frame1, text="Your answer", font=("Copperplate Gothic Light",15,"bold"),bg="black",fg="white").place(x=370,y=240)
t_answer= Entry(frame1, font=("Copperplate Gothic Light",15),bg="lightgrey").place(x=370,y=270, width=250)

# 4th line------------------------------
password= tk.Label(frame1, text="Create Password", font=("Copperplate Gothic Light",15,"bold"),bg="black",fg="white").place(x=50,y=310)
t_password= tk.Entry(frame1, font=("Copperplate Gothic Light",15),bg="lightgrey")
t_password.place(x=50,y=340, width=250)

cpassword= tk.Label(frame1, text="Confirm Password", font=("Copperplate Gothic Light",15,"bold"),bg="black",fg="white").place(x=370,y=310)
t_cpassword= tk.Entry(frame1, font=("Copperplate Gothic Light",15),bg="lightgrey")
t_cpassword.place(x=370,y=340, width=250)

# Check Box------------------------------
chk= Checkbutton(frame1, text="I Agree to the Terms & Conditions",onvalue=1, offvalue=0, bg="black",fg="white", font=("Copperplate Gothic Light",12)).place(x=50, y=380)

# Button---------------------------------
#btn_image= ImageTk.PhotoImage(file= "C:/Users/Hp/Favorites/Desktop/Python/Project/img1.jpg")

def signup():
    if t_fname.get()=="" or t_lname.get()=="" or t_contact.get()=="" or t_email.get()=="" or t_password.get()=="" or t_cpassword.get()=="":
        messagebox.showinfo('Message','Fields cannot be embty..!')
    else:
        if t_password.get()!=t_cpassword.get():
            messagebox.showinfo('Message','Password not matched..!')
        else:
            mydb=mysql.connector.connect(host="localhost",user="root",password="",database="FiProject")
            mycursor=mydb.cursor()
            mycursor.execute("SELECT * from PTable")
            my_rows=mycursor.fetchall()
            id=1
            for x in my_rows:
                id+=1
            sql="INSERT INTO PTable (id,t_fname,t_lname,t_contact,t_email,t_password) values(%s,%s,%s,%s,%s,%s)"
            val=(id,t_fname.get(),t_lname.get(),t_contact.get(),t_email.get(),t_password.get())
            mycursor.execute(sql,val)
            mydb.commit()
            
            cascade_face=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            def face_cropped(img):
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces=cascade_face.detectMultiScale(gray,1.3,5)

                if faces is ():
                    return None

                for x,y,w,h in faces:
                    cropped_face=img[y:y+h,x:x+w]
                return cropped_face #coordinates of cropped face

            cap = cv2.VideoCapture(0)
            img_id=0

            while True:
                ret,frame=cap.read()
                if face_cropped(frame) is not None:
                    img_id+=1
                    face = cv2.resize(face_cropped(frame),(400,400))
                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path,face)
                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    cv2.imshow("Cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo('Result','Face captured and Registeration successful! DO TRAIN YOUR FACE IS COMPULSORY')


btn= tk.Button(frame1,text="CAPTURE FACE & SIGNUP", bd=0,bg="deepskyblue2",font=("Copperplate Gothic Light",15,"bold"),fg="white", cursor="hand2", command=signup).place(x=50, y=420)
btn2= tk.Button(frame1,text="TRAIN FACE", bd=0,bg="deepskyblue2",font=("Copperplate Gothic Light",15,"bold"),fg="white", cursor="hand2", command=train_classifier).place(x=50, y=470)

lf3=tk.Label(frame1,text="Already registered?",font=("Arial bold",10),bg="black", fg="red")
lf3.place(x=370,y=420)
btn_login= Button(frame1, text="Sign in",font=("Copperplate Gothic Light",15,"bold"), fg="white",bg="deepskyblue2", bd=0, cursor="hand2",command=login).place(x=520, y=420)

window.geometry(str(screen_width)+"x"+str(screen_height))       
window.mainloop()
