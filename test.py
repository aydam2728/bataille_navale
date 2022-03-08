from math import *
from grille import *
from tkinter import *

root = Tk()

grilles=[]

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

#print(grille.getGrille())
def pointeur(event,n):
    abscisse, ordonnée = event.x -25 , event.y-25
    print(abscisse,ordonnée,floor(abscisse/50),floor(ordonnée/50))
    grilles[n].setGrille(floor(abscisse/50),floor(ordonnée/50),4)

grille.getCanvas().bind("<Button-1>",lambda event : pointeur(event,0))
grille2.getCanvas().bind("<Button-1>",lambda event : pointeur(event,1))
grille3.getCanvas().bind("<Button-1>",lambda event : pointeur(event,2))
grille4.getCanvas().bind("<Button-1>",lambda event : pointeur(event,3))
root.mainloop()

#grille.setGrille(0,0,"salut")