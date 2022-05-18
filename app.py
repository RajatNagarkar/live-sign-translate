from tkinter import font
from PIL import Image, ImageTk
import tkinter as tk
import cv2
import os
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.models import model_from_json
import operator
import time
import sys, os
import matplotlib.pyplot as plt
import hunspell
import threading as thr
from hunspell import Hunspell 
from string import ascii_uppercase
from language_selector import Language
from TextToAudio import TextToAudio
from Translator import TextTranslate

class Application:
    def __init__(self):
        self.directory = 'model'

        #initialize models
        self.modelThread = thr.Thread(target=self.modelLoader, args=('model/translator-updated-bw-vgg16.h5', ))
        self.modelThread.start()

        while self.modelThread.is_alive() is True:
            print("model_loading")
            
        #initialize open cv

        self.hs = Hunspell("en_CA","en_CA.dic")
        self.vs = cv2.VideoCapture(0)
        self.current_image = None
        self.current_image2 = None

        languageObject = Language()
        self.pref_lang = languageObject.getSelected()
        self.speech = TextToAudio()
        self.speech.setLang(self.pref_lang)

        
        
        
        self.ct = {}
        self.ct['blank'] = 0
        self.blank_flag = 0
        for i in ascii_uppercase:
          self.ct[i] = 0
        print("Loaded model from disk")


        #initialize tkinter window
        self.root = tk.Tk()
        self.root.title("Live Sign Language Translator")
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)
        self.root.geometry("1500x900")
        self.panel = tk.Label(self.root)
        self.panel.place(x = 135, y = 10, width = 640, height = 640)
        self.panel2 = tk.Label(self.root) # initialize image panel
        self.panel2.place(x = 460, y = 95, width = 310, height = 310)
        
        self.T = tk.Label(self.root)
        self.T.place(x=31,y = 17)
        self.T.config(text = "Live Sign Translate",font=("courier",40,"bold"))
        self.panel3 = tk.Label(self.root) # Current SYmbol
        self.panel3.place(x = 1100,y=95)
        self.T1 = tk.Label(self.root)
        self.T1.place(x = 800,y = 100)
        self.T1.config(text="Letter :",font=("Courier",40,"bold"))
        self.panel4 = tk.Label(self.root) # Word
        self.panel4.place(x = 1150,y=165)
        self.T2 = tk.Label(self.root)
        self.T2.place(x = 920,y = 170)
        self.T2.config(text ="Word :",font=("Courier",40,"bold"))
        self.panel5 = tk.Label(self.root) # Sentence
        self.panel5.place(x = 30,y=750)
        self.T3 = tk.Label(self.root)
        self.T3.place(x = 10,y = 760)
        self.T3.config(text ="Sentence :",font=("Courier",40,"bold"))

        #Loading Msg Display
        self.loadingMsg = tk.Label(self.root)
        self.loadingMsg.place(x = 10, y = 650)
        self.loadingMsg.config(text='Please Wait While Model is Loading...', font=('Courier', 20))

        self.btcall = tk.Button(self.root,command = self.action_call,height = 0,width = 0)
        self.btcall.config(text = "About",font = ("Courier",14))
        self.btcall.place(x = 1400, y = 10)

        

        self.bt1=tk.Button(self.root, command=self.action1,height = 0,width = 0)
        self.bt1.place(x = 800,y=500)
        #self.bt1.grid(padx = 10, pady = 10)
        self.bt2=tk.Button(self.root, command=self.action2,height = 0,width = 0)
        self.bt2.place(x = 800,y=450)
        #self.panel3.place(x = 10,y=660)
        # self.bt2.grid(row = 4, column = 1, columnspan = 1, padx = 10, pady = 10, sticky = tk.NW)
        self.bt3=tk.Button(self.root, command=self.action3,height = 0,width = 0)
        self.bt3.place(x = 800,y=400)
        # self.bt3.grid(row = 4, column = 2, columnspan = 1, padx = 10, pady = 10, sticky = tk.NW)
        self.bt4=tk.Button(self.root, command=self.action4,height = 0,width = 0)
        self.bt4.place(x = 800,y=350)
        # self.bt4.grid(row = bt1, column = 0, columnspan = 1, padx = 10, pady = 10, sticky = tk.N)
        self.bt5=tk.Button(self.root, command=self.action5,height = 0,width = 0)
        self.bt5.place(x = 800,y=300)
        # self.bt5.grid(row = 5, column = 1, columnspan = 1, padx = 10, pady = 10, sticky = tk.N)

        #nextbutton
        self.btcall_next = tk.Button(self.root,command = self.nextWord,height = 0,width = 0)
        self.btcall_next.config(text = "Next",font = ("Courier",14))
        self.btcall_next.place(x = 950, y = 450)

        #clearButton
        self.btcall_clear = tk.Button(self.root,command = self.clearWord,height = 0,width = 0)
        self.btcall_clear.config(text = "Clear",font = ("Courier",14))
        self.btcall_clear.place(x = 1100, y = 450)

        #Translatebutton
        self.btcall_translate = tk.Button(self.root,command = self.showResult,height = 0,width = 0)
        self.btcall_translate.config(text = "Translate",font = ("Courier",14))
        self.btcall_translate.place(x = 1250, y = 450)

        self.str=""
        self.word=""
        self.current_symbol="Empty"
        self.photo="Empty"
        self.video_loop()

    def video_loop(self):
        ok, frame = self.vs.read()
        if ok:
            cv2image = cv2.flip(frame, 1)
            x1 = int(0.5*frame.shape[1])
            y1 = 10
            x2 = frame.shape[1]-10
            y2 = int(0.5*frame.shape[1])
            cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
            cv2image = cv2.cvtColor(cv2image, cv2.COLOR_BGR2RGBA)
            self.current_image = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=self.current_image)
            self.panel.imgtk = imgtk
            self.panel.config(image=imgtk)
            cv2image = cv2image[y1:y2, x1:x2]
            gray = cv2.cvtColor(cv2image, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray,(5,5),2)
            th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
            ret, res = cv2.threshold(th3, 70, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
            self.predict(res)
            self.current_image2 = Image.fromarray(res)
            imgtk = ImageTk.PhotoImage(image=self.current_image2)
            self.panel2.imgtk = imgtk
            self.panel2.config(image=imgtk)
            self.panel3.config(text=self.current_symbol,font=("Courier",40,'bold'))
            self.panel4.config(text=self.word,font=("Courier",30))
            self.panel5.config(text=self.str,font=("Calibri",20))
            predicts=self.hs.suggest(self.word)
            if(len(predicts) > 0):
                self.bt1.config(text=predicts[0],font = ("Courier",20))
            else:
                self.bt1.config(text="")

            if(len(predicts) > 1):
                self.bt2.config(text=predicts[1],font = ("Courier",20))
            else:
                self.bt2.config(text="")

            if(len(predicts) > 2):
                self.bt3.config(text=predicts[2],font = ("Courier",20))
            else:
                self.bt3.config(text="")

            if(len(predicts) > 3):
                self.bt4.config(text=predicts[3],font = ("Courier",20))
            else:
                self.bt4.config(text="")

            if(len(predicts) > 4):
                self.bt5.config(text=predicts[4],font = ("Courier",20))
            else:
                self.bt5.config(text="")                
        self.root.after(30, self.video_loop)
    def predict(self,test_image):
        test_image = cv2.resize(test_image, (224, 224))
        try:
            result = self.loaded_model.predict(test_image.reshape(1, 224, 224, 1))
            self.loadingMsg.config(text="")
        except:
            return

        prediction = {}
        result=[]
        prediction['blank'] = result[0][0]
        inde = 1
        for i in ascii_uppercase:
            prediction[i] = result[0][inde]
            inde += 1
        
        #LAYER 1
        prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
        self.current_symbol = prediction[0][0]

        #Further Processing of Symbol
        if(self.current_symbol == 'blank'):
            for i in ascii_uppercase:
                self.ct[i] = 0
        self.ct[self.current_symbol] += 1
        if(self.ct[self.current_symbol] > 10):
            for i in ascii_uppercase:
                if i == self.current_symbol:
                    continue
                tmp = self.ct[self.current_symbol] - self.ct[i]
                if tmp < 0:
                    tmp *= -1
                if tmp <= 20:
                    self.ct['blank'] = 0
                    for i in ascii_uppercase:
                        self.ct[i] = 0
                    return
            self.ct['blank'] = 0
            for i in ascii_uppercase:
                self.ct[i] = 0
            if self.current_symbol == 'blank':
                if self.blank_flag == 0:
                    self.blank_flag = 1
                    if len(self.str) > 0:
                        self.str += " "
                    self.str += self.word
                    self.word = ""
            else:
                if(len(self.str) > 16):
                    self.str = ""
                self.blank_flag = 0
                self.word += self.current_symbol
    
    def modelLoader(self, path):
        self.loaded_model = load_model(path)

    def action1(self):
    	predicts=self.hs.suggest(self.word)
    	if(len(predicts) > 0):
            self.word=""
            self.str+=" "
            self.str+=predicts[0] 

    def action2(self):
    	predicts=self.hs.suggest(self.word)
    	if(len(predicts) > 1):
            self.word=""
            self.str+=" "
            self.str+=predicts[1] 

    def action3(self):
    	predicts=self.hs.suggest(self.word)
    	if(len(predicts) > 2):
            self.word=""
            self.str+=" "
            self.str+=predicts[2] #Hello
            
    def action4(self):
    	predicts=self.hs.suggest(self.word)
    	if(len(predicts) > 3):
            self.word=""
            self.str+=" "
            self.str+=predicts[3]

    def action5(self):
    	predicts=self.hs.suggest(self.word)
    	if(len(predicts) > 4):
            self.word=""
            self.str+=" "
            self.str+=predicts[4]

    def destructor(self):
        print("Closing Application...")
        self.root.destroy()
        self.vs.release()
        del self.speech
        cv2.destroyAllWindows()
    
    def destructor1(self):
        print("Closing Application...")
        self.root1.destroy()

    def action_call(self) :
        print('About Section Opened')
        self.root1 = tk.Toplevel(self.root)
        self.root1.title("About")
        self.root1.protocol('WM_DELETE_WINDOW', self.destructor1)
        self.root1.geometry("900x900")
        
        
        self.tx = tk.Label(self.root1)
        self.tx.place(x = 330,y = 20)
        self.tx.config(text = "Efforts By", fg="red", font = ("Courier",30,"bold"))

        self.photo1 = tk.PhotoImage(file='assets/sagar.png')
        self.w1 = tk.Label(self.root1, image = self.photo1)
        self.w1.place(x = 20, y = 105)
        self.tx6 = tk.Label(self.root1)
        self.tx6.place(x = 20,y = 250)
        self.tx6.config(text = "Sagar\nIT18043", font = ("Courier",15,"bold"))

        self.photo2 = tk.PhotoImage(file='assets/vedank.png')
        self.w2 = tk.Label(self.root1, image = self.photo2)
        self.w2.place(x = 200, y = 105)
        self.tx2 = tk.Label(self.root1)
        self.tx2.place(x = 200,y = 250)
        self.tx2.config(text = "Vedank Singh\nIT18037", font = ("Courier",15,"bold"))

        
        self.photo3 = tk.PhotoImage(file='assets/amin.png')
        self.w3 = tk.Label(self.root1, image = self.photo3)
        self.w3.place(x = 380, y = 105)
        self.tx3 = tk.Label(self.root1)
        self.tx3.place(x = 380,y = 250)
        self.tx3.config(text = "Amin Khan\nIT18028", font = ("Courier",15,"bold"))

        self.photo4 = tk.PhotoImage(file='assets/rajat.png')
        self.w4 = tk.Label(self.root1, image = self.photo4)
        self.w4.place(x = 560, y = 105)
        self.tx4 = tk.Label(self.root1)
        self.tx4.place(x = 560,y = 250)
        self.tx4.config(text = "Rajat Nagarkar\nIT18037", font = ("Courier",15,"bold"))
        
        self.tx7 = tk.Label(self.root1)
        self.tx7.place(x = 170,y = 360)
        self.tx7.config(text = "Under the supervision of", fg="red", font = ("Courier",30,"bold"))

        self.photo6 = tk.PhotoImage(file='assets/project-guide.png')
        self.w6 = tk.Label(self.root1, image = self.photo6)
        self.w6.place(x = 350, y = 420)
        self.tx6 = tk.Label(self.root1)
        self.tx6.place(x = 230,y = 670)
        self.tx6.config(text = "Prof. Snehal Dongre", font = ("Courier",30,"bold"))
        self.root1.mainloop()
    
    def nextWord(self):
        self.str+=" "
        self.str+=self.word
        self.word=""

    def clearWord(self):
        self.word=""
        
    def showResult(self):
        #Translating Text
        self.translate = TextTranslate()
        self.translate.initialize(lang_ab=self.pref_lang, text=self.str)
        self.translatedText = self.translate.transalteText()
        
        #Converting to Audio
        self.speech.setText(self.translatedText)
        self.speech.toSpeech() #Audio file Generate
        self.speech.playAudio() #Play Audio
        del self.speech
        self.speech = TextToAudio()
        self.speech.setLang(self.pref_lang)


print("Starting Application...")
lvs = Application()
lvs.root.mainloop()
