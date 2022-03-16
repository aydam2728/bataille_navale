from math import *
from tkinter import *
from grille import *
from bateau import *
from model import grilles

root = Tk()
last=[-1,-2,-3]
orientation = "h"
list_bateaux=[]
def create_bateau(grille,n):
    list_bateaux.append(Bateau(1,1,1,n))
    for each in n:
        grilles[grille].setCase(each,4)

def change_orientation(event):
    global orientation 
    if orientation == "h":
        orientation = "v"
    else: 
        orientation = "h"
def pointeur(event,n,action=0):
    global grilles
    global last
    global orientation
    
    abscisse, ordonnée = event.x -25 , event.y-25
    if (action == 0):
        print(abscisse,ordonnée,floor(abscisse/50),floor(ordonnée/50))
        l=[floor(abscisse/50)*10 + floor(ordonnée/50)]
        create_bateau(n,l)
        return None
    elif(action == 1 and grilles[n].getCase(floor(abscisse/50),floor(ordonnée/50))!=4): 
        """
        if( last[0] != floor(abscisse/50)*10 + floor(ordonnée/50) and last[1] != floor(abscisse/50)*10 + floor(ordonnée/50)):
            grilles[n].changeColor(floor(abscisse/50)*10+floor(ordonnée/50),"green")
            grilles[n].changeColor(1+(floor(abscisse/50)*10+floor(ordonnée/50)),"green")
            grilles[n].changeColor(last[0],"")
            grilles[n].changeColor(last[1],"")
            last=[]
            last.append(floor(abscisse/50)*10+floor(ordonnée/50))
            last.append(1+(floor(abscisse/50)*10+floor(ordonnée/50)))
            
        elif(last[0]!=last[0] or last[1]!=last[1]):
            grilles[n].changeColor(last[0],"green")
            grilles[n].changeColor(last[1],"green")
            grilles[n].changeColor(last[0],"")
            grilles[n].changeColor(last[1],"")
            last=[]
            last.append(last[0])
            last.append(last[1])
        elif(last[1]==last[0]):
            print("yes")
            print(last)
        """
        num = floor(abscisse/50)*10 + floor(ordonnée/50)
        if (num!=last[0] and orientation == "h"):
            grilles[n].changeColor(last[0],"")
            #grilles[n].changeColor(last[1],"")
            #grilles[n].changeColor(last[2],"")
            grilles[n].changeColor(num,"green")
            #grilles[n].changeColor(num +1 ,"green")
            #grilles[n].changeColor(num +2 ,"green")
            last=[]
            last.append(num)
            #last.append(num+1)
            #last.append(num+2)
            print(floor(ordonnée/50))
            if floor(ordonnée/50) <0 or floor(ordonnée/50)>7: 
                grilles[n].changeColor(num,"red")
               # grilles[n].changeColor(num +1 ,"red")
               # grilles[n].changeColor(num +2 ,"red")
        

        elif (num!=last[0] and orientation == "v"):
            grilles[n].changeColor(last[0],"")
            grilles[n].changeColor(last[1],"")
            grilles[n].changeColor(last[2],"")
            grilles[n].changeColor(num,"green")
            grilles[n].changeColor(num +10 ,"green")
            grilles[n].changeColor(num +20 ,"green")
            last=[]
            last.append(num)
            last.append(num+10)
            last.append(num+20)
            print(floor(ordonnée/50))
            if floor(abscisse/50) <0 or floor(abscisse/50)>7: 
                grilles[n].changeColor(num,"red")
                grilles[n].changeColor(num +10 ,"red")
                grilles[n].changeColor(num +20 ,"red")

def show():
    global root
    global grilles

    # joueur 1 
    root.title("Bataille Navale, Joueur 1")
    root.geometry("1100x550")
    root.config(cursor='crosshair')


    grille = Grille(1,"bas",root,0,0)
    grille2 = Grille(2,"bas",root,550,0)
    grilles.append(grille)
    grilles.append(grille2)
    # joueur 2
    newWindow = Toplevel(root)
    newWindow.title("Bataille Navale, Joueur 2")
    newWindow.geometry("1100x550")
    newWindow.config(cursor='crosshair')

    grille3 = Grille(3,"bas",newWindow,0,0)
    grille4 = Grille(4,"bas",newWindow,550,0)
    grilles.append(grille3)
    grilles.append(grille4)


    grille.getCanvas().bind("<Button-1>",lambda event : pointeur(event,0))
    grille2.getCanvas().bind("<Button-1>",lambda event : pointeur(event,1))
    grille3.getCanvas().bind("<Button-1>",lambda event : pointeur(event,2))
    grille4.getCanvas().bind("<Button-1>",lambda event : pointeur(event,3))

    grille.getCanvas().bind("<Motion>",lambda event : pointeur(event,0,1))
    grille.getCanvas().bind("<Button-3>",change_orientation)

