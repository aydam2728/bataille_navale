import time
from tkinter import font
from ihm import root,menu,show
from email.mime import image
from math import *
from random import *
from textwrap import fill
from tkinter import *
from weakref import ref
from PIL import ImageTk,Image
from grille import *
from bateau import *
from model import grilles
import PIL.Image
from PIL import Image, ImageTk
import PIL.Image
import timeit
#menu()

root.title("SHIPS FIGHT")
root.iconbitmap('logo_black.ico')
root.geometry("1400x800")
root.config(cursor='crosshair')
canvas=Canvas(root,height=800,width=1422)
canvas.pack(expand=True,fill=BOTH)
width = int(canvas.cget('width'))
height = int(canvas.cget('height'))
image= PIL.Image.open("wallpaper.jpg")
image=image.resize((width,height), PIL.Image.ANTIALIAS)
logo= PIL.Image.open("logo.png")
logo = logo.resize((300,300), PIL.Image.ANTIALIAS)
#image.show()
image_tk=ImageTk.PhotoImage(image)
wallpaper_image=canvas.create_image(0,0,anchor=NW,image=image_tk)
image_tk2=ImageTk.PhotoImage(logo)
logo_image=canvas.create_image(1100,75,anchor=NW,image=image_tk2)
#backgroundLabel = Label(root,image=image_tk)
#backgroundLabel .place(x=0,y=0)
myfont = font.Font(family="Arial", size=14, weight="bold")
texte=canvas.create_text(50,750,text="A DAMIEN ORIGINAL",fill="white",anchor=NW,font=myfont)
points=canvas.create_text(250,750,text=".",fill="white",anchor=NW,font=myfont)
ButtonJouer = Button(root, text ="Jouer", command = show)
#ButtonJouer.pack()
ButtonDif = Button(root, text ="Diifficulte", command = '')
point=["."]
#ButtonDif.pack()
c=0
arret=randint(5,15)
def update():
    global canvas,points,point,c,arret
    c=c+1
    if c==arret:
        root.unbind("<Configure>")
        canvas.destroy()
        menu()
        return None
    if len(point)==3:
        point=[]
    else:
        point.append(".")
    
    canvas.itemconfigure(points, text=point)
    root.after(0, update) #mettre 500

last_h=800
last_c=1422
last_t=0
last_tc=0

def resize(event):
    global last_h,last_t,logo,root,logo_image,wallpaper_image,image,image_tk,image_tk2,points,texte,last_h,last_tc,last_c,start
    h= root.winfo_height()/last_h
    c=root.winfo_width()/last_c
    if timeit.default_timer()-start <0.1:
       return None
    width, height = logo.size
    logo=logo.resize((int(width*c),int(height*h)))
    width, height = image.size
    image=image.resize((int(width*c),int(height*h)),PIL.Image.LANCZOS )
    x,y = canvas.coords(logo_image)
    canvas.coords(logo_image,x*c,y*h)

    x,y = canvas.coords(points)
    canvas.coords(points,x*c,y*h)

    x,y = canvas.coords(texte)
    canvas.coords(texte,x*c,y*h)

    last_t=h
    last_tc=c
    last_h=root.winfo_height()
    last_c=root.winfo_width()
    image_tk=ImageTk.PhotoImage(image)
    image_tk2=ImageTk.PhotoImage(logo)

    width = int(canvas.cget('width'))
    height = int(canvas.cget('height'))
    canvas.config(width=int(width*c), height=int(height*h))

    canvas.itemconfig(wallpaper_image,image=image_tk)
    canvas.itemconfig(logo_image,image=image_tk2)
    
    
   
update()

start = timeit.default_timer()
root.bind("<Configure>", resize)
root.mainloop()
