from PIL import Image, ImageTk
from tkinter import *
import PIL.Image
root = Tk()
root.title("Bataille Navale, Joueur 1")
root.geometry("1300x550")
root.config(cursor='crosshair')
canvas=Canvas(root,height=450, width=250)
canvas.place(x=0,y=0)
class Image_class():
 
    def __init__(self):
        # Dessine tout
        self.images=[]
    def image(self,x,y,canvas,num):
        canvas.create_image(x, y,anchor=NW,image=self.images[num])

    def addImage(self,link):
        self.images.append(ImageTk.PhotoImage(PIL.Image.open(link)))
        print(self.images)

 
wind = Image_class()
wind.addImage('porte_avion_lexington_resized.png')
wind.image(0,0,canvas,0)
wind2 = Image_class()
wind2.addImage('porte_avion_lexington_resized_v.png')
wind2.image(100,100,canvas,0)
root.mainloop()

