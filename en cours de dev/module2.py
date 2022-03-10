import pygame
import random
from tkinter import *

fenetre = Tk()
texte="hors"
bg=PhotoImage(file='fond.gif')
bg1=PhotoImage(file='trou.gif')
touché=bool
s0=0
s1=0
s2=0
s3=0
s4=0
tirs=[]

#*******************************************************************************

def interface_graph():
    global texte2,compteur

## Fenetre principale
    canvas.pack()

## Création + Affichage texte nombre de frappes
 #   texte1=Label(fenetre,text="Nombre de frappes : ",bg="#0267AA",fg="white")
 #   texte1.pack()
 #   texte1.place(x=10,y=60)

## Création + Affichage Touché ,Manqué
  #  texte2=Label(fenetre,text="résultat",bg="#0267AA",fg="white",font="12")
  #  texte2.pack()
  #  texte2.place(x=25,y=30)

## Création + Affichage texte Titre
  ##  titre=Label(fenetre,text="Bataille Navale",bg="#0267AA",fg="white",font= "Helvetica 30 bold italic")
  ##  titre.pack()
  ##  titre.place(x=200,y=30)

## Création + Affichage du compteur de frappes
    compteur=Label(fenetre,text="0",bg="#0267AA",fg="white")
    compteur.pack()
    compteur.place(x=120,y=60)


#*******************************************************************************

def musique():
    #pygame.mixer.init()
    #son= pygame.mixer.Sound("musique.wav")
    #son.play()
    return "none"

#*******************************************************************************
#On crée une fonction qui place les bateaux aléatoirement#
def coordonnées_ship(n):
    a=random.randint(0,9)
    b=random.randint(0,9)
    s=random.randint(0,9)
    global ship
    ship=[]
    if s==0:
        for k in range(n):
            if a>9-n:
                ship.append((a-k,b))


            else:
                ship.append((a+k,b))

    else:
        for k in range(n):
            if b>9-n:
                ship.append((a,b-k))

            else:
                ship.append((a,b+k))

    return ship



#*******************************************************************************

def pointeur(event):
    global abscisse, ordonnée,texte
    abscisse, ordonnée = event.x , event.y
    case=0

    for i in range (0,500,50):
        for j in range(0,500,50):
            if (abscisse>100+i and abscisse<150+i and ordonnée>100+j and ordonnée<150+j):
                colonne=i//50
                ligne=j//50
## case = variable qui stocke les coords de la case touchée
                case=(i,j)
                if case in tirs:
                    texte="Les coordonnées sont déjà attaquées"

                if (grille[ligne][colonne]==True):
                    texte="Touché"
                    canvas.create_rectangle(100+i,100+j,100+50+i,100+50+j,outline="black",fill="grey")
                    tirs.append(case)

                else:
                    texte="Manqué"
##                    canvas.create_image(125+i,125+j,image = bg1)
                    canvas.create_rectangle(100+i,100+j,100+50+i,100+50+j,outline="black",fill="#0484CA")
                    tirs.append(case)



## configure : change la valeur du text (tkinter)

    compteur.configure(text=len(tirs))
    texte2.configure(text=texte)

#*******************************************************************************
def generation_batteaux ():
    global ship0,ship1,ship2,ship3,ship4
        #on place le premier bâteau (le plus grand)#
    ship0=coordonnées_ship(5)
    print("Le porte-avion est placé et opérationnel.")

    #On place le second bâteau et on vérifie qu'il ne chevauche pas le premier#
    ship1=coordonnées_ship(4)
    for k in range(4):
        if ship1[k] in ship0:
            ship1=coordonnées_ship(4)
            while ship1[k] in ship0:
                ship1=coordonnées_ship(4)
    print("Le sous-marin est placé et opérationnel.")

    #On place les bâteaux suivants de la même façon, toujours en vérifiant qu'ils ne chevauchent pas les précédents#
    ship2=coordonnées_ship(3)
    for k in range(3):
        if ship2[k] in ship0 or ship2[k] in ship1:
            ship2=coordonnées_ship(3)
            while ship2[k] in ship0 or ship2[k] in ship1:
                ship2=coordonnées_ship(3)
    print("Le premier cuirassé est placé et opérationnel.")


    ship3=coordonnées_ship(3)
    for k in range(3):
        if ship3[k] in ship0 or ship3[k] in ship1 or ship3[k] in ship2:
            ship3=coordonnées_ship(3)
            while ship3[k] in ship0 or ship3[k] in ship1 or ship3[k] in ship2:
                ship3=coordonnées_ship(3)
    print("Le second cuirassé est placé et opérationnel.")


    ship4=coordonnées_ship(2)
    for k in range(2):
        if ship4[k] in ship0 or ship4[k] in ship1 or ship4[k] in ship2 or ship4[k] in ship3:
            ship4=coordonnées_ship(2)
            while ship4[k] in ship0 or ship4[k] in ship1 or ship4[k] in ship2 or ship4[k] in ship3:
                ship4=coordonnées_ship(2)
    print("La caravelle est placée et opérationnelle.")

#*******************************************************************************
## execution des fonctions

generation_batteaux()
musique()

#*******************************************************************************
## mise en place des bateaux sur la grille

ships=ship0+ship1+ship2+ship3+ship4
grille=[[False for j in range(10)] for i in range (10)]
for g in ships:
    x3=g[0]
    y3=g[1]
    grille[x3][y3]=True

#*******************************************************************************
## affichage tkinter + changement du pointeur de la souris

fenetre.title("Bataille Navale")
fenetre.geometry("700x610")
fenetre.config(cursor='crosshair')

canvas=Canvas(fenetre,height=800, width=800)
item = canvas.create_image(0, 0, image = bg)

interface_graph()

#*******************************************************************************
## generation de la grille en fond

for i in range (0,500,50):
    print(i)
    #fenetre.attributes('-transparentcolor', 'white')
    Label(fenetre,text=i//50+1).place(y=75,x=i+120) # fenêtre de nombre de A à J
    a=["A","B","C","D","E","F","G","H","I","J"]
    Label(fenetre, text=a[i // 50]).place(x=75, y=i + 120)   #fenêtre de nombre de 1 à 10

    for j in range(0,500,50):
        canvas.create_rectangle(100+i,100+j,100+50+i,100+50+j,outline="black")


#*******************************************************************************

## Lancement de la fonction pointeur grace au clic souris
fenetre.bind("<Button-1>",pointeur)

## fin des boucles
fenetre.mainloop()
pygame.quit()

