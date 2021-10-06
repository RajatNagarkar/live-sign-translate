import tkinter as tk
import cv2
from PIL import Image, ImageTk

w = tk.Tk()
file="pictures/gif1.gif"

info = Image.open(file)

frames = info.n_frames
print(frames)
im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

var=None
count = 0
def animation(count):
    global var
    im2 = im[count]
    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    var = w.after(50,lambda :animation(count))


gif_label = tk.Label(w,image="")
gif_label.pack()

start=tk.Button(w,text="Start",command=lambda :animation(count))
start.pack()


# w.after(5000, lambda: w.destroy()) # Destroy the widget after 30 seconds
w.mainloop()
# root = tk.Tk()
# myimage=Image.open("C:\\Users\\vedank singh\\Desktop\\HTML+CSS\\model\\flag.jpg")
# myimage1=myimage.resize((900,1100),Image.ANTIALIAS)
# imagevar=ImageTk.PhotoImage(myimage1)
# # w=imagevar.width()
# # h=imagevar.height()
# root.title("Sign language to Text Converter")
# root.geometry("900x1100")
# # root.wm_attributes("-transparentcolor","grey") 
# # for opacity of window
# label=tk.Label(root,image=imagevar,bg="grey")
# label.place(x=0,y=0)
# panel = tk.Label(root)
# panel.place(x = 135, y = 100, width = 300, height = 300)
# panel2 = tk.Label(root) # initialize image panel
# panel2.place(x = 460, y = 100, width = 300, height = 300)

# T = tk.Label(root)
# T.place(x=250,y = 17)
# T.config(text = "Sign Language to Text",bg="#3984AB",font=("courier",25,"bold"))
# panel3 = tk.Label(root) # Current SYmbol
# panel3.place(x = 300,y=450,width=100,height=35)
# T1 = tk.Label(root)
# T1.place(x = 10,y = 450)
# T1.config(text="Character :",bg="#5292B5",font=("Courier",20,"italic"))
# panel4 = tk.Label(root) # Word
# # panel4.config(bg="")
# panel4.place(x = 130,y=500,width=100,height=35)
# T2 = tk.Label(root)
# T2.place(x = 10,y = 500)
# T2.config(text ="Word :",bg="#5292B5",font=("Courier",20,"italic"))
# panel5 = tk.Label(root) # Sentence
# panel5.place(x = 270,y=550,width=100,height=35)
# T3 = tk.Label(root)
# T3.place(x = 10,y = 550)
# T3.config(text ="Sentence :",bg="#5292B5",font=("Courier",20,"italic"))

# T4 = tk.Label(root)
# T4.place(x = 370, y= 630)
# T4.config(text = "Suggestions",font = ("Courier",20,"bold"))

# btcall = tk.Button(root,height = 0,width = 0)
# btcall.config(text = "About",fg="white",bg="blue",font = ("Courier",14))
# btcall.place(x = 825, y = 10)

# bt1=tk.Button(root,height = 1,width = 7)
# bt1.place(x = 250,y=680)

# bt2=tk.Button(root,height = 1,width = 7)
# bt2.place(x = 620,y=680)

# bt3=tk.Button(root,height = 1,width = 7)
# bt3.place(x = 100,y=735)

# bt4=tk.Button(root,height = 1,width = 7)
# bt4.place(x = 700,y=735)


# bt5=tk.Button(root,height = 1,width = 7)
# bt5.place(x = 400,y=735)
# root.mainloop()