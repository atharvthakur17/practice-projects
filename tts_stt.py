from tkinter import *
from tkinter.messagebox import showinfo
from gtts import gTTS
import speech_recognition as sr
import os
import cv2
cv2.destroyAllWindows()
mainwindow= Tk()
mainwindow.title(' Text-To-Speech and Speech-To-Text Converter')
mainwindow.geometry('500x500')
mainwindow.resizable(0, 0)
mainwindow.configure(bg='grey19')
def say(text1):
     language = 'en'
     speech = gTTS(text = text1, lang = language, slow = False)
     speech.save("text.mp3")
     os.system("start text.mp3")
 
def recordvoice():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            try:    
                text1 = r.recognize_google(audio,language="en-IN")
                with open("new.txt","a") as f:
                    f.write(f"{text1}\n")
                if "camera" in text1:  
                    vid = cv2.VideoCapture(0)
                    while(True):
                        ret, frame = vid.read()
                        cv2.imshow('frame', frame)
                        if cv2.waitKey(10) & 0xFF == ord('q'):
                            break
                        vid.release()
                        cv2.destroyAllWindows()

            except:
                print("cant recognize")
            return text1
def TextToSpeech():
    texttospeechwindow = Toplevel(mainwindow)
    texttospeechwindow.title('Text-to-Speech Converter')
    texttospeechwindow.geometry("500x500")
    texttospeechwindow.configure(bg='mistyrose2')
 
    Label(texttospeechwindow, text='Text-to-Speech Converter', font=("Times New Roman", 15), bg='Blue').place(x=50)
 
    text = Text(texttospeechwindow, height=5, width=30, font=12)
    text.place(x=7, y=60)
   
    speakbutton = Button(texttospeechwindow, text='listen', bg='coral', command=lambda: say(str(text.get(1.0, END))))
    speakbutton.place(x=140, y=200)
 
def SpeechToText():
    speechtotextwindow = Toplevel(mainwindow)
    speechtotextwindow.title('Speech-to-Text Converter')
    speechtotextwindow.geometry("500x500")
    speechtotextwindow.configure(bg='pink')
 
    Label(speechtotextwindow, text='Speech-to-Text Converter', font=("Comic Sans MS", 15), bg='IndianRed').place(x=50)
 
    text = Text(speechtotextwindow, font=12, height=3, width=30)
    text.place(x=7, y=100)
   
    recordbutton = Button(speechtotextwindow, text='Record', bg='Sienna', command=lambda: text.insert(END, recordvoice()))
    recordbutton.place(x=140, y=50)
 
Label(mainwindow, text='Text-To-Speech and Speech-To-Text Converter',
     font=('Times New Roman', 16), bg='mediumpurple', wrap=True, wraplength=450).place(x=25, y=0)
 
texttospeechbutton = Button(mainwindow, text='Text-To-Speech Conversion', font=('Times New Roman', 16), bg='mintcream', command=TextToSpeech)
texttospeechbutton.place(x=100, y=150)
 
speechtotextbutton = Button(mainwindow, text='Speech-To-Text Conversion', font=('Times New Roman', 16), bg='mintcream', command=SpeechToText)
speechtotextbutton.place(x=100, y=250)
 
mainwindow.update()
mainwindow.mainloop()