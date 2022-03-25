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
    def image(self,x,y,canvas,num):
        self.images_created.append(canvas.create_image(x, y,anchor=NW,image=self.images[num]))
    def addImage(self,link):
        self.images.append(ImageTk.PhotoImage(PIL.Image.open(link)))
    def delete(self,canvas,i):
        canvas.delete(self.images_created[i])
        self.images_created=[]
    def updateImage(self,canvas,i):
        canvas.itemconfig(self.images_created[-1],image=self.images[i])
    
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