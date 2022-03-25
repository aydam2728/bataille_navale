from email.mime import image
from math import *
from tkinter import *
from weakref import ref
from PIL import ImageTk,Image
from grille import *
from bateau import *
from model import grilles
import PIL.Image
from PIL import Image, ImageTk
from tkinter import *
import PIL.Image

root = Tk()
orientation = "h"
list_bateaux=[]
ref_bateau = None
def change_orientation(event):
    global v , lastx
    if v == True:
        v = False
    else:
        v = True
    lastx=None
    autre(event,0,0)
lastx=0
lasty=0
def autre(event,n,t):
    abscisse, ordonnée = event.x -25 , event.y-25
    global grilles ,lastx,lasty , ref_bateau,list_bateaux,v
    if ref_bateau != None and 0<abscisse<500 and 0<ordonnée<500 and isEmpty(abscisse,ordonnée,n) == True :    
        if (abscisse-(abscisse%50) != lastx or ordonnée-(ordonnée%50) != lasty):
            try :
                #grilles[n].getCanvas().delete(bat[-1])
                list_bateaux[ref_bateau].delete(grilles[n].getCanvas(),-1)
            except:
                print("")
            list_bateaux[ref_bateau].image(25+(abscisse-(abscisse%50)),25+(ordonnée-(ordonnée%50)),grilles[n].getCanvas(),0)
            if (v==True):
                #grilles[n].getCanvas().itemconfig(bat[-1],image=list_bateaux[ref_bateau].images[1])
                list_bateaux[ref_bateau].updateImage(grilles[n].getCanvas(),-1)
            lastx = abscisse-(abscisse%50)
            lasty = ordonnée-(ordonnée%50)

def isEmpty(abscisse,ordonnée,i):
    global grilles ,lastx,lasty , ref_bateau,list_bateaux,v
    for o in range(list_bateaux [ref_bateau].taille):
        try :
            if (v==False):
                if (grilles[i].check(floor(ordonnée/50),floor(abscisse/50)+o) != True):
                    return False
            else:
                if (grilles[i].check(floor(ordonnée/50)+o,floor(abscisse/50)) != True ):
                    return False
        except:
            return None
    return True

def app(event,i):
    abscisse, ordonnée = event.x -25 , event.y-25
    #print(abscisse-(abscisse%50),ordonnée-(ordonnée%50))
    global grilles ,lastx,lasty , ref_bateau,list_bateaux,v
    
    if ref_bateau != None and isEmpty(abscisse,ordonnée,i) == True and ordonnée>=0 and abscisse>=0:
        if (v==True):
            list_bateaux[ref_bateau].image(25+(abscisse-(abscisse%50)),25+(ordonnée-(ordonnée%50)),grilles[i].getCanvas(),1)
            #grilles[i].getCanvas().create_image(25+(abscisse-(abscisse%50)),25+(ordonnée-(ordonnée%50)),anchor=NW,image=list_bateaux_img_link_v[ref_bateau])
        else:
            list_bateaux[ref_bateau].image(25+(abscisse-(abscisse%50)),25+(ordonnée-(ordonnée%50)),grilles[i].getCanvas(),0)
            #grilles[i].getCanvas().create_image(25+(abscisse-(abscisse%50)),25+(ordonnée-(ordonnée%50)),anchor=NW,image=list_bateaux_img_link[ref_bateau])
        
        for o in range(list_bateaux[ref_bateau].taille):
            if v==False:
                grilles[i].setGrille2(floor(ordonnée/50),floor(abscisse/50)+o,list_bateaux [ref_bateau].taille)
                list_bateaux[ref_bateau].setPosition(floor(ordonnée/50),floor(abscisse/50)+o,1)
            else :
                grilles[i].setGrille2(floor(ordonnée/50)+o,floor(abscisse/50),list_bateaux [ref_bateau].taille)
                list_bateaux[ref_bateau].setPosition(floor(ordonnée/50)+o,floor(abscisse/50),1)
        
        ref_bateau= None

   
def pointeur(event,n,action=0):
    global grilles
    global orientation , ref_bateau ; global list_bateaux
    n-=1
    abscisse, ordonnée = event.x -25 , event.y-25
    if ref_bateau == None:
        action = 1
    if (action == 0):
        app(event,n)
        return None
def test(event,n):
    global grilles
    global orientation , ref_bateau ; global list_bateaux
    abscisse, ordonnée = event.x -25 , event.y-25
    for bateau in list_bateaux:
        if bateau.status == 0 :
            return None
    num = floor(abscisse/50)*10 + floor(ordonnée/50)
    grilles[n].setGrille2(floor(ordonnée/50),floor(abscisse/50),10)
    grilles[n].changeColor(num,"red")
    grilles[0].setGrille2(floor(ordonnée/50),floor(abscisse/50),10)
    grilles[0].changeColor(num,"red")
    for bateau in list_bateaux:
        for case in bateau.cases:
            if case[0] == floor(ordonnée/50) and case[1] == floor(abscisse/50):
                bateau.touche(floor(ordonnée/50),floor(abscisse/50))
    print("bateaux en lices",nbrVivant())
def nbrVivant():
    global list_bateaux
    c=0
    for bateau in list_bateaux:
        if bateau.status == 1:
            c+=1
    return c
def show():
    global root
    global grilles

    # joueur 1
    root.title("Bataille Navale, Joueur 1")
    root.geometry("1300x550")
    root.config(cursor='crosshair')


    grille = Grille(1,"bas",root,0,0)
    grille2 = Grille(2,"bas",root,550,0)
    grilles.append(grille)
    grilles.append(grille2)
    # joueur 2
    newWindow = Toplevel(root)
    newWindow.title("Bataille Navale, Joueur 2")
    newWindow.geometry("1300x550")
    newWindow.config(cursor='crosshair')

    grille3 = Grille(3,"bas",newWindow,0,0)
    grille4 = Grille(4,"bas",newWindow,550,0)
    grilles.append(grille3)
    grilles.append(grille4)


    grille.getCanvas().bind("<Button-1>",lambda event : pointeur(event,1))
    grille2.getCanvas().bind("<Button-1>",lambda event : test(event,1))
    #grille3.getCanvas().bind("<Button-1>",lambda event : pointeur(event,2))
    #grille4.getCanvas().bind("<Button-1>",lambda event : pointeur(event,3))

    grille.getCanvas().bind("<Motion>",lambda event : autre(event,0,0))
    grille.getCanvas().bind("<Button-3>",change_orientation)


    

    grilles[0].getCanvas().bind("<Button-3>",change_orientation)
v=False

canvas_bateaux=Canvas(root,height=450, width=250)
canvas_bateaux.place(x=1100,y=50)

list_imgs=["porte_avion_lexington_resized.png","croiseur_de_grasse_resized.png","destroyer_kleber_resized.png","sous_marin_resized.png","cuirasse_normandie_resized.png"]

for k in range(len(list_imgs)):
    if k<= 2 :
        taille =5-1*k
    elif k==3 :
        taille = 3
    else:
        taille = 2
    Bateau1 = Bateau(k,"","1",0,taille)
    Bateau1.addImage(list_imgs[k])
    Bateau1.addImage(list_imgs[k].split(".")[-2]+"_v.png")
    Bateau1.image(0,0+50*k,canvas_bateaux,0)
    list_bateaux.append(Bateau1)


def callback(event,x):
    global canvas_bateaux , ref_bateau,list_bateaux
    if (ref_bateau ==None):
        ref_bateau = event.y//50
        list_bateaux[ref_bateau].delete(canvas_bateaux,0)


canvas_bateaux.bind("<Button-1>",lambda event : callback(event,0))