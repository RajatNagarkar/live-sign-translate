import tkinter as t
from tkinter import *
from language_list import langauages

class Language:
    def __init__(self):
        self.selectedLang = "English"
        self.top = t.Tk()
        self.top.config(bg='#adb5bd')
        self.top.geometry("1500x800")
        self.top.title("SIGN LANGUAGE TRANSLATOR - SOLVING LANGUAGE BARRIER")
        self.Lb1 = t.Listbox(self.top, height=10, width=15, bg="#dbdfe6", bd=3, activestyle='dotbox', font="Helvetica", fg="#0b090a")
        self.label = t.Label(self.top, text=" SELECT YOUR preferred a Language", bg="#212529", bd=5, font="Helvetica", fg="#f8f9fa")
        self.Lb1.insert(1, "English")
        self.Lb1.insert(2, "Hindi")
        self.Lb1.insert(3, "Marathi")
        self.Lb1.insert(4, "Gujrati")
        self.Lb1.insert(5, "Telgu")
        self.Lb1.insert(6, "Tamil")
        self.Lb1.insert(7, "Bengali")
        self.Lb1.insert(8, "Malayalam")
        self.Lb1.insert(9, "Kannada")
        self.btn = t.Button(self.top, text="SUBMIT", bg="#00b4d8", bd=2, font="Calibri", command=self.storeSelected, fg="white", relief="raised")
        self.label.pack(anchor="n")
        self.Lb1.pack(anchor="center")
        self.btn.pack(anchor="center")
        self.top.mainloop()
        

    def storeSelected(self):
        self.selectedLang = self.Lb1.get(ANCHOR)
        self.top.destroy()
        

    def getSelected(self):
        try:
            return langauages[self.selectedLang]
        except:
            return 'en'
