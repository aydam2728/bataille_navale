from tkinter import *
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
        self.canvas.create_image(0, 0, image = PhotoImage(file='fond.gif'))
    ## generation de la grille en fond
        for i in range (0,500,50):
    #fenetre.attributes('-transparentcolor', 'white')

            #nombre de 1 à 10
            self.canvas.create_text(i+50,12,text=i//50+1)
            # lettre de A  à J
            a=["A","B","C","D","E","F","G","H","I","J"]
            self.canvas.create_text(12,i+50,text=a[i // 50])

            for j in range(0,500,50):
                self.rectangles.append(self.canvas.create_rectangle(25+i,25+j,75+i,75+j,outline="black"))
    
    def getID(self):
        return self.id

    def getGrille(self):
        return self.grille

    def getCanvas(self):
        return self.canvas

    def setGrille(self,i,j,x):
        self.grille[i][j]=x
        print("ok")
        print(self.getGrille())
        self.changeColor(i*10+j)
    
    def changeColor(self,n):
        self.canvas.itemconfig(self.rectangles[n], fill='green')
