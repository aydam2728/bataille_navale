from queue import Empty
from tkinter import *
from math import * 
import PIL.Image
from PIL import ImageTk,Image
class Grille():
    def __init__(self,id, usage,root,x,y):
        self.id= id
        self.usage = usage
        self.root = root
        self.x = x
        self.y = y
        self.canvas = Canvas(self.root,height=525, width=525)
        self.canvas.place(x=self.x,y=self.y)
        self.grille = [[0 for j in range(10)] for i in range (10)]
        self.rectangles=[]
        img= ImageTk.PhotoImage(PIL.Image.open("fond.gif"))
        self.canvas.create_image(0, 0, image = img,anchor=NW)
    ## generation de la grille en fond
        for i in range (0,500,50):
    #fenetre.attributes('-transparentcolor', 'white')

            #nombre de 1 à 10
            self.canvas.create_text(i+50,12,text=i//50+1)
            # lettre de A  à J
            a=["A","B","C","D","E","F","G","H","I","J"]
            self.canvas.create_text(12,i+50,text=a[i // 50])

            for j in range(0,500,50):
                self.rectangles.append(self.canvas.create_rectangle(25+i,25+j,75+i,75+j,outline="black",fill="#0066c4"))
    
    def getID(self):
        return self.id

    def getGrille(self):
        return self.grille

    def getCase(self,i,j):
        return self.grille[i][j]

    def getCanvas(self):
        return self.canvas

    def setGrille(self,i,j,x):
        self.grille[i][j]=x
        self.changeColor(i*10+j,"green")

    def setGrille2(self,i,j,x):
        self.grille[i][j]=x

    def setCase(self,n,x):
        i= n//10
        j= floor(n%10)
        self.grille[i][j]=x
        self.changeColor(i*10+j,"green")

    def changeColor(self,n,color):
        self.canvas.itemconfig(self.rectangles[n], fill=color)

    def check(self,i,j):
        if self.grille[i][j] == 0 : return True
