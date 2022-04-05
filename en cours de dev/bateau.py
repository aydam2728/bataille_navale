from ast import Delete
from sre_parse import expand_template
from grille import * 
import tkinter as Tk
class Bateau():
    def __init__(self,id,nom,joueur,status = 0,taille=0):
        self.id = id
        self.nom = nom
        self.joueur = joueur
        self.cases = []
        self.status = status
        # 0 : pas placé
        # 1 : en jeu
        # 2 : détruit
        self.taille=taille
        self.images=[]
        self.images_created=[]
    def image(self,x,y,canvas,num,v):
        if (v==True):
            self.image_tk=ImageTk.PhotoImage(self.images[num].rotate(-90,expand=1))
        else:
            self.image_tk=ImageTk.PhotoImage(self.images[num])
        self.images_created.append(canvas.create_image(x, y,anchor=NW,image=self.image_tk))
    def addImage(self,link):
        self.images.append(Image.open(link))
    def delete(self,canvas,i):
        canvas.delete(self.images_created[i])
        self.images_created=[]
    def updateImage(self,canvas,i):
        image_tk=ImageTk.PhotoImage(self.images[0].rotate(90))
        canvas.itemconfig(self.images_created[-1],image=image_tk)
    
    def updateAfterResize(self,canvas,i):
        x=canvas.coords(self.images_created[-1])[0]
        y=canvas.coords(self.images_created[-1])[1]
        self.delete(canvas,i)
        self.image(x,y,canvas,i)
    
    def touche(self,x,y):
        c=0
        for case in self.cases:
            if case[0] == x and case[1]==y:
                self.cases[c][-1]=2
                if self.enVie()==False :
                   self.status = 2 
            c+=1

    def enVie(self):
        for case in self.cases:
            if case[-1] == 1:
                return True
        return False
            
    def setPosition(self,x,y,status):
        self.cases.append([x,y,status])
        if len(self.cases) == self.taille:
            self.status = 1