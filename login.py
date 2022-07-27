import tkinter as tk
from tkinter import*                  
from PIL import Image,ImageTk,ImageDraw
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


window=tk.Toplevel()
window.title("Login Window")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

def login():
    if txt_email.get()!="" and txt_pass.get()!="":
        mydb=mysql.connector.connect(host="localhost",user="root",password="",database="FiProject")
        mycursor=mydb.cursor(buffered=True)
        sql="select * from PTable WHERE t_email='" + txt_email.get() + "' AND t_password='" + txt_pass.get() + "'"
        mycursor.execute(sql)
        count=mycursor.rowcount
        if count==1:
            import virtual_asesstent
        else:
            messagebox.showinfo("Error","Invalid credintial!")
        mydb.disconnect()
    else:
        messagebox.showinfo("Error","Field can't be empty!")

# Background colors----------------------------
left_lbl= Label(window, bg="#031F3c", bd=0)
left_lbl.place(x=0,y=0,relheight=1,width=680)

right_lbl= Label(window, bg="#031F3c", bd=0)
right_lbl.place(x=650,y=0,relheight=1,relwidth=1)

# Frames---------------------------------------
l_frame=Frame(window, bg="white")
l_frame.place(x=250,y=100,width=800, height=500)

lleft=ImageTk.PhotoImage(file='C:/Users/Hp/Favorites/Desktop/Python/Project/left.jpg')
left=Label(window,image=lleft).place(x=80, y=130,width=320,height=390)

title= Label(l_frame, text="LOGIN HERE !!!",font=("Goudy Old Style", 30,"bold"), bg="white", fg="#08A3D2").place(x=250, y=50)

# 1st line-------------------------------------
email= Label(l_frame, text="Email Address",font=("Copperplate Gothic Light", 20,"bold"), bg="white", fg="grey").place(x=250, y=150)
txt_email= Entry(l_frame,font=("times new roman", 15), bg="lightgrey")
txt_email.place(x=250, y=190, width=350, height=35)

# 2nd line-------------------------------------
password= Label(l_frame, text="Password",font=("Copperplate Gothic Light", 20,"bold"), bg="white", fg="grey").place(x=250, y=250)
txt_pass= Entry(l_frame,font=("times new roman", 15), bg="lightgrey")
txt_pass.place(x=250, y=290, width=350, height=35)

def register():
    import register

# New Account, Forgot Password and Login--------
reg= Button(l_frame, text="new user?", font=("times new roman",12), bg="white", bd=0, fg="red").place(x=530, y=380)
b2=Button(l_frame,text="Signup",bg="#001a33",fg="white",bd=2,command=register)
b2.place(x=600,y=380)
login= Button(l_frame, text="LOGIN", font=("times new roman",18, "bold"), bg="green", fg="white", cursor="hand2", command=login).place(x=250, y=370, width=180, height=40)


window.geometry(str(screen_width)+"x"+str(screen_height))       
window.mainloop()
