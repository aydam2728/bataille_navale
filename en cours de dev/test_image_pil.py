from tkinter import *
from tkinter import font
from PIL import *
import PIL.Image
from PIL import ImageTk 
root = Tk()
def menu():
    global root,image_tk
    
    root.title("SHIPS WARS")
    root.geometry("500x500")
    root.config(cursor='crosshair')
    canvas=Canvas(root,height=500,width=500,bg="red")
    canvas.pack(expand = YES, fill = BOTH)
    width = int(canvas.cget('width'))
    height = int(canvas.cget('height'))

    image_tk= ImageTk.PhotoImage(file ="porte_avion_lexington_resized.png")
    canvas.create_image(10,10,anchor=NW,image=image_tk)

    myfont = font.Font(family="Arial", size=14, weight="bold")
    ButtonJouer = Button(root, text ="PLAY",bg="gray" command = '',font=myfont,justify=CENTER,width=10,relief=FLAT,overrelief=FLAT)
    ButtonJouer.place(x=100,y=250,anchor=CENTER)
    ButtonOptions = Button(root, text ="SETTINGS", command = '',font=myfont,justify=CENTER,width=10,relief=FLAT,overrelief=FLAT)
    ButtonOptions.place(x=100,y=300,anchor=CENTER)
    ButtonCredits = Button(root, text ="CREDITS", command = '',font=myfont,justify=CENTER,width=10,relief=FLAT,overrelief=FLAT)
    ButtonCredits.place(x=100,y=350,anchor=CENTER)
    ButtonExit = Button(root, text ="EXIT", command = quit,font=myfont,justify=CENTER,width=10,relief=FLAT,overrelief=FLAT)
    ButtonExit.place(x=100,y=400,anchor=CENTER)
menu()
root.mainloop()