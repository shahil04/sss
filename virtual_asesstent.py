import speech_recognition as sr
import playsound
import random
from gtts import gTTS
import webbrowser
import ssl
import certifi
import time
import os
import subprocess
import pyautogui
import pyttsx3
import bs4 as bs
import urllib.request
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk   
import threading
from time import strftime

#def takeQuery():
class person:
    name=''
    def setName(self,name):
        self.name=name

class asis:
    name=''
    def setName(self,name):
        self.name=name

def there_exists(terms,voice_data):
    for term in terms:
        if term in voice_data:
            return True

def engine_helps():
    engine.say("hello there !, This is A I virtual assistant System made under python and tkinter. This project is submitted by jwal and rishabh . my sister easy will help you in your work you just need to ask her. For example., easy play music, easy play video from youtube, and many more.. , you can also change her name by saying easy your name should be, siri , To exit press esc button from keyboard,  Enjoy!")
    engine.runAndWait()

    

def record_audio():
    r=sr.Recognizer()
    r.pause_threshold=1
    print("your bot is listening..")
    with sr.Microphone() as source:
        try:
            audio=r.listen(source)
            voice_data=r.recognize_google(audio)
            print("you : "+ voice_data)
            textBox.delete(0, END)
            textBox.insert(0, voice_data)
            respond()
        except sr.UnknownValueError:
            print("Sorry sir, I did not get that")
        except sr.RequestError:
            print("Sorry the server is down")
        except Exception as e:
            print(e)
            print("not recognized..!")
        #print(">>", voice_data.lower())
        #return voice_data.lower()

def engine_speak(audio_string,voice_data):
        audio_string=str(audio_string)
        tts=gTTS(text=audio_string, lang='en')
        r=random.randint(1,20000000)
        audio_file='audio' +str(r)+'.mp3'
        tts.save(audio_file)
        msg.insert(END,person_obj.name+": "+voice_data)
        msg.insert(END,asis_obj.name+": "+audio_string)
        playsound.playsound(audio_file)
        print(asis_obj.name+":",audio_string)
        os.remove(audio_file)
        textBox.delete(0,END)
        msg.yview(END)

def respond():
    voice_data=textBox.get()
    if there_exists(["hi","hello","hellow","hey","hey boss","hola","namaste","watsup"],voice_data):
        greetings=['hey, how can i help you '+person_obj.name,'hi, how can i help you '+person_obj.name]
        greet=greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet,voice_data)

    elif there_exists(["tell me your name","what is your name"],voice_data):
        if asis_obj.name=='easy':
            if person_obj.name=="you":
                engine_speak("my name is easy, you can change my name by saying command your name should be,,,, by the way, what is your name",voice_data)
            else:
                engine_speak("my name is easy, you can change my name by saying command your name should be,,,,",voice_data)
        else:
            engine_speak("my name is "+ asis_obj.name,voice_data+","+person_obj.name)

    elif there_exists(["my name is "],voice_data):
        person_name=voice_data.split("is")[-1].strip()
        engine_speak("okay, i will remember that your name is "+person_name,voice_data)
        person_obj.setName(person_name)

    elif there_exists(["your name should be"],voice_data):
        asis_name=voice_data.split("be")[-1].strip()
        print("name")
        engine_speak("okay "+person_obj.name+ " i will remember that my name is "+asis_name,voice_data)
        asis_obj.setName(asis_name)

    elif there_exists([asis_obj.name+" how are you","how are you",asis_obj.name+" how are you doing","how are you doing"],voice_data):
        engine_speak("i am very well thanks for asking "+person_obj.name,voice_data)

    elif there_exists([asis_obj.name+" what are you doing","what are you","what are you doing","what you up to","watsup"],voice_data):
        engine_speak("i am assesting you " +person_obj.name+" in your work ",voice_data)

    elif there_exists([asis_obj.name+" Do you like your name ?"],voice_data):
        engine_speak("yes "+person_obj.name+" i like my name "+voice_data)

    elif there_exists([asis_obj.name+" dance"],voice_data):
        engine_speak("no "+person_obj.name+" i cannot dance "+voice_data)

    elif there_exists([asis_obj.name+" tum kya kya ker skti ho ?","tum kya kya","kya ker skti ho"],voice_data):
        engine_speak(person_obj.name+" i can help you in your daily work like calculation, music, browser, questions, and many more !",voice_data)  

    elif there_exists(["who are you ","who you","Who are you","tum kon ho"],voice_data):
        engine_speak("i am artificial virtual assistant robot  "+" and my name is "+asis_obj.name,voice_data)

    elif there_exists(["created","creates","who creates you","who created you"],voice_data):
        engine_speak("I am created by Ujjwal and rishab",voice_data)

    elif there_exists(["can you dance","can robat dance","will you able to dance ?"],voice_data):
        engine_speak("i don't know sir, will i dance i don't think so !",voice_data)

    elif there_exists(["human?"],voice_data):
        engine_speak("human is made up of cells and tissues !",voice_data)

    elif there_exists(["calculation"],voice_data):
        engine_speak("yes "+person_obj.name+" sir offcourse",voice_data)
        
    elif there_exists(["in which language you made with","you made with","made with which language"],voice_data):
        engine_speak(" i am made with python ",voice_data)

    elif there_exists(["eat","you eat","your food"],voice_data):
        engine_speak(" electricity is my favorite food ",voice_data)

    elif there_exists(["yourself","tell me about yourself"],voice_data):
        engine_speak(" electricity is my favorite food ",voice_data)

    elif there_exists(["live","language"],voice_data):
        engine_speak(" i live in computer and i mostly talk english language ",voice_data)

    elif there_exists(["thanks","thank you","nice","good","wonderful","good work","excellent","outstanding","beautiful","gorgoues","voice","cute","like","love"],voice_data):
        engine_speak(person_obj.name+" its my pleasure sir  ",voice_data)

    elif there_exists(["bad","idiot","worst","stupid","crazy","get lost","get out","dumb"],voice_data):
        engine_speak(" thank you "+person_obj.name+" , its my pleasure ",voice_data)

    elif there_exists(["whats the time","tell me the time","time now","current time","time"],voice_data):
        times=time.asctime(time.localtime(time.time()))
        engine_speak(times,voice_data)

    elif there_exists(["search for","Google","search in google","google search","search google"],voice_data) and 'youtube' not in voice_data:
        search_term=voice_data.split("for")[-1]
        url="https://google.com/search?q="+search_term
        webbrowser.get().open(url)
        engine_speak("here is what i found for"""+search_term+"on google",voice_data)

    elif there_exists(["what","who","when","how","where","which"],voice_data) and 'youtube' not in voice_data:
        search_term=voice_data.split(" ")[-1]
        url="https://google.com/search?q="+search_term
        webbrowser.get().open(url)
        engine_speak("here is what i found for"""+search_term+"on google",voice_data)

    elif there_exists(["search for","youtube","search in youtube","youtube search","search youtube"],voice_data):
        search_term=voice_data.split("'for")[-1]
        url="https://www.youtube.com/results?search_query="+search_term
        webbrowser.get().open(url)
        engine_speak("here is what i found for"+search_term+"on youtube",voice_data)

    elif there_exists(["price of","price"],voice_data):
        search_term=voice_data.split("of")[-1]
        url="https://google.com/search?q="+search_term
        webbrowser.get().open(url)
        engine_speak("here is what i found for"+search_term+"on google",voice_data)

    elif there_exists(["play video","video","video play"],voice_data):
       search_term=voice_data.split("of")[-1]
       url="https://google.com/search?q="+search_term
       webbrowser.get().open(url)
       engine_speak("here is what i found for"+search_term+"on google",voice_data)

    elif there_exists(["play song","song","song play","good song"],voice_data):
        search_term=voice_data.split("song")[-1]
        url="https://open.spotify.com/search/"+search_term
        webbrowser.get().open(url)
        engine_speak("here you are listening to"+search_term+"enjoy sir",voice_data)

    elif there_exists(["play music","music play"],voice_data):
        search_term=voice_data.split(" ")[-1]
        engine_speak("here you are listening to "+search_term+" enjoy sir",voice_data)
        def play():
            playsound.playsound('song.mp3',True)
        t2=threading.Thread(target=play)
        t2.start()

    elif there_exists(["amazon.com","amozon","amozon price","amazon","amazon price"],voice_data):
        search_term=voice_data.split("of")[-1]
        url="https://www.amazon.in"+search_term
        webbrowser.get().open(url)
        engine_speak("here is what i found for"+search_term+"on amazon.com",voice_data)

    elif there_exists(["make a note","routine","calender","schedule","time table"],voice_data):
        search_term=voice_data.split("on")[-1]
        url="https://keep.google.com/#home"+search_term
        webbrowser.get().open(url)
        engine_speak("here you can make notes",voice_data)

    elif there_exists(["open instagram","want to have some fun time","fun","fun time"],voice_data):
        search_term=voice_data.split("for")[-1]
        url="https://www.instagram.com/"
        webbrowser.get().open(url)
        engine_speak("opening instagram",voice_data)

    elif there_exists(["open twitter"],voice_data):
        search_term=voice_data.split("for")[-1]
        url="https://twitter.com/"
        webbrowser.get().open(url)
        engine_speak("opening twitter",voice_data)

    elif there_exists(["weather","tell me the weather report","whats the weather condition outside"],voice_data):
        search_term=voice_data.split("condition")[-1]
        url="https://google.com/search?q="+search_term
        webbrowser.get().open(url)
        engine_speak("here is what i found for on google ",voice_data)

    elif there_exists(["open my mail","gmail","check my email","email"],voice_data):
        search_term=voice_data.split("my")[-1]
        url="https://mail.google.com/mail/u/0/#inbox"
        webbrowser.get().open(url)
        engine_speak("here you can check your gmail",voice_data)


    elif there_exists(["toss","flip","coin"],voice_data):
        moves=["head","tails"]
        cmove=random.choice(moves)
        engine_speak("the computer choose"+cmove,voice_data)

    elif there_exists(["plus","add","subtract","minus","multiply","into","divide","power","+","-","*","/"],voice_data):
        opr=voice_data.split()[1]

        if opr=='+' or opr=='plus' or opr=='add':
            engine_speak(int(voice_data.split()[0])+int(voice_data.split()[2]),voice_data)
        elif opr=='-' or opr == 'subtract' or opr=='minus':
            engine_speak(int(voice_data.split()[0])-int(voice_data.split()[2]),voice_data)
        elif opr=='*' or opr=='multiply' or opr=='into':
            engine_speak(int(voice_data.split()[0])*int(voice_data.split()[2]),voice_data)
        elif opr=='/'or opr=='divide':
            engine_speak(int(voice_data.split()[0])/int(voice_data.split()[2]),voice_data)                          
        elif opr=='power':
            engine_speak(int(voice_data.split()[0])**int(voice_data.split()[2]),voice_data)           
        else:
            engine_speak("wrong operation",voice_data)

    elif there_exists(["capture","screenshot","my screen"],voice_data):
        msg.insert(END,person_obj.name+" : "+voice_data)
        msg.insert(END,asis_obj.name+" : "+"Screen captured successfully !")
        textBox.delete(0, END)
        myScreenshot=pyautogui.screenshot()
        myScreenshot.save('screenshot'+".jpg")


    elif there_exists(["exit","quit","goodbye","bye","see you"],voice_data):
        engine_speak("we could continue more sir, but for now byee ",voice_data)
        exit()

    else:
        #search_term=voice_data.split("for")[-1]
        url="https://google.com/search?q="+voice_data
        webbrowser.get().open(url)
        engine_speak("here is what i found for " +voice_data+" on google ",voice_data)
        

                    


time.sleep(1)
asis_obj=asis()
person_obj=person()
asis_obj.name='easy'
person_obj.name='you'
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


window=tk.Toplevel()
window.attributes('-fullscreen', True)
window.bind("<Escape>",lambda event: window.attributes("-fullscreen", False))
window.title("virtual assistant")
window.configure(bg='#000000')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

def timed():
	string = strftime('%H:%M:%S %p')
	lbl.config(text = string)
	lbl.after(1000, time)

load=Image.open("ai9.jpg")
photo=ImageTk.PhotoImage(load)

canvas=Canvas(window,width=screen_width, height=screen_height,bg="#000000")
canvas.create_image(screen_width/2,screen_height/2,image=photo) 
canvas.pack(fill=BOTH)

lbl = Label(canvas, font = ('Eras Light ITC', 30),
			background = 'black',
			foreground = '#00ff00')


lbl.place(x=1080,y=30)
timed()
##engine_help=pp.init()
##voices=engine_help.getProperty('voices')
##voices=engine_help.getProperty('voices')
##def helps():
##    engine_help.say("help")
##    engine_help.runAndWait()

def start_help():
    t3=threading.Thread(target=engine_helps)
    t3.start()
    
l1=tk.Button(canvas,text="?",font=("Courier",50),bg="black",fg="#00ff00",command=start_help)
l1.place(x=1180,y=100)

frame =Frame(canvas,bg="white",width=344,height=676) #708
#sc=Scrollbar(window)
msg=Listbox(frame,width=34,height=32,bg="black",fg="#00ff00",font=("Courier",13))
#sc.pack(side=RIGHT,fill=Y)
#msg.place(x=10,y=10)
msg.place(x=0,y=0)
frame.place(x=10,y=10)

textBox=Entry(canvas,font=("Courier",13))
textBox.place(x=10,y=695,width=1350)

b2=tk.Button(canvas,text="Ask >",font=("Courier",13),bg="black",fg="#00ff00",command=respond)
b2.place(x=10,y=725,width=1350)

def enter_fn(event):
    b2.invoke()

window.bind('<Return>', enter_fn)
#window.geometry("500x650")



def repeatL():
    times=time.asctime(time.localtime(time.time()))


    audio_string=str("Hi,how can i help you ?")
    tts=gTTS(text=audio_string, lang='en')
    r=random.randint(1,20000000)
    audio_file='audio' +str(r)+'.mp3'
    tts.save(audio_file)
    msg.insert(END,"easy : "+audio_string)
    playsound.playsound(audio_file)
    print(audio_string+"\n")
    os.remove(audio_file)
    msg.yview(END)


    
    while True:
        record_audio()
       # voice_data=record_audio("Recording")
       # print("Done")
       # print("you: ", voice_data)
       # respond(voice_data)
        

t=threading.Thread(target=repeatL)
t.start()



window.mainloop()
            
