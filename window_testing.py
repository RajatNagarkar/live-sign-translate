from PIL import Image, ImageTk
import tkinter as tk
from tkinter.ttk import *
import os
from language_selector import Language
from TextToAudio import TextToAudio
from Translator import TextTranslate

class window:
    def __init__(self):

        

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
        self.panel5.place(x = 350,y=735)
        self.T3 = tk.Label(self.root)
        self.T3.place(x = 10,y = 720)
        self.T3.config(text ="Sentence :",font=("Courier",40,"bold"))

        #Loading Msg Display
        self.loadingMsg = tk.Label(self.root)
        self.loadingMsg.place(x = 10, y = 650)
        self.loadingMsg.config(text='Please Wait While Model is Loading...', font=('Courier', 20))

        self.btcall = tk.Button(self.root,command = self.destructor,height = 0,width = 0)
        self.btcall.config(text = "About",font = ("Courier",14))
        self.btcall.place(x = 1400, y = 10)

        #language_Button
        self.lang_button = tk.Button(self.root,command = self.setPrefLang,height = 0,width = 0)
        self.lang_button.config(text = "Language",font = ("Courier",14))
        self.lang_button.place(x = 1367, y = 50)

        

        self.bt1=tk.Button(self.root, command=self.destructor,height = 0,width = 0)
        self.bt1.place(x = 800,y=500)
        #self.bt1.grid(padx = 10, pady = 10)
        self.bt2=tk.Button(self.root, command=self.destructor,height = 0,width = 0)
        self.bt2.place(x = 800,y=450)
        #self.panel3.place(x = 10,y=660)
        # self.bt2.grid(row = 4, column = 1, columnspan = 1, padx = 10, pady = 10, sticky = tk.NW)
        self.bt3=tk.Button(self.root, command=self.destructor,height = 0,width = 0)
        self.bt3.place(x = 800,y=400)
        # self.bt3.grid(row = 4, column = 2, columnspan = 1, padx = 10, pady = 10, sticky = tk.NW)
        self.bt4=tk.Button(self.root, command=self.destructor,height = 0,width = 0)
        self.bt4.place(x = 800,y=350)
        # self.bt4.grid(row = bt1, column = 0, columnspan = 1, padx = 10, pady = 10, sticky = tk.N)
        self.bt5=tk.Button(self.root, command=self.destructor,height = 0,width = 0)
        self.bt5.place(x = 800,y=300)
        # self.bt5.grid(row = 5, column = 1, columnspan = 1, padx = 10, pady = 10, sticky = tk.N)

        #nextbutton
        self.btcall_next = tk.Button(self.root,command = self.destructor,height = 0,width = 0)
        self.btcall_next.config(text = "Next",font = ("Courier",14))
        self.btcall_next.place(x = 950, y = 450)

        #backspace-button
        self.btcall_backspace = tk.Button(self.root,command = self.backspace,height = 0,width = 0)
        self.btcall_backspace.config(text = "Backspace",font = ("Courier",14))
        self.btcall_backspace.place(x = 1200, y = 250)

        #clearButton
        self.btcall_clear = tk.Button(self.root,command = self.destructor,height = 0,width = 0)
        self.btcall_clear.config(text = "Clear",font = ("Courier",14))
        self.btcall_clear.place(x = 1100, y = 730)

        #Translatebutton
        self.btcall_translate = tk.Button(self.root,command = self.destructor,height = 0,width = 0)
        self.btcall_translate.config(text = "Translate",font = ("Courier",14))
        self.btcall_translate.place(x = 1250, y = 450)

        self.str="Tomorrow is third day of the week."
        self.word="Happy"
        self.current_symbol="Empty"
        self.photo="Empty"

        self.panel5.config(text=self.str,font=("Calibri",20))
        self.panel4.config(text=self.word,font=("Calibri",40))
    def destructor(self):
        print("Closing Application...")
        self.root.destroy()

    def backspace(self):
        self.word = self.word[:-1]
        self.panel4.config(text=self.word, font=('Calibri', 40))
    def setPrefLang(self):
        languageObject = Language()
        self.pref_lang = languageObject.getSelected()
        try:
            del self.speech
        except:
            print("Audio Object Not Found")
        self.speech = TextToAudio()
        self.speech.setLang(self.pref_lang)
        print(self.pref_lang)
        del languageObject
         
abc = window()
abc.root.mainloop()        