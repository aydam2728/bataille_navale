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
tailleCarreau=50
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
decallage=25
def autre(event,n,t):
    global grilles ,lastx,lasty , ref_bateau,list_bateaux,v,decallage
    abscisse, ordonnée = event.x -decallage , event.y-decallage
    canvasSize=int(grilles[n].getCanvas()['height'])-25
    #print(decallage)
    if ref_bateau != None and 0<abscisse<canvasSize and 0<ordonnée<canvasSize and isEmpty(abscisse,ordonnée,n) == True :    
        #print(floor(ordonnée/tailleCarreau),floor(abscisse/tailleCarreau))
        if (abscisse-(abscisse%tailleCarreau) != lastx or ordonnée-(ordonnée%tailleCarreau) != lasty):
            try :
                #grilles[n].getCanvas().delete(bat[-1])
                list_bateaux[ref_bateau].delete(grilles[n].getCanvas(),-1)
            except:
                print("")
            list_bateaux[ref_bateau].image(25+(abscisse-(abscisse%tailleCarreau)),25+(ordonnée-(ordonnée%tailleCarreau)),grilles[n].getCanvas(),0,v)
            lastx = abscisse-(abscisse%tailleCarreau)
            lasty = ordonnée-(ordonnée%tailleCarreau)

def isEmpty(abscisse,ordonnée,i):
    global grilles ,lastx,lasty , ref_bateau,list_bateaux,v
    for o in range(list_bateaux [ref_bateau].taille):
        try :
            if (v==False):
                if (grilles[i].check(floor(ordonnée/tailleCarreau),floor(abscisse/tailleCarreau)+o) != True):
                    return False
            else:
                if (grilles[i].check(floor(ordonnée/tailleCarreau)+o,floor(abscisse/tailleCarreau)) != True ):
                    return False
        except:
            return None
    return True

def app(event,i):
    global grilles ,lastx,lasty , ref_bateau,list_bateaux,v,decallage
    abscisse, ordonnée = event.x -decallage , event.y-decallage
    #print(abscisse-(abscisse%50),ordonnée-(ordonnée%50))
    
    if ref_bateau != None and isEmpty(abscisse,ordonnée,i) == True and ordonnée>=0 and abscisse>=0:
        print(v)
        if (v==True):
            list_bateaux[ref_bateau].image(25+(abscisse-(abscisse%tailleCarreau)),25+(ordonnée-(ordonnée%tailleCarreau)),grilles[i].getCanvas(),1,None)
            #grilles[i].getCanvas().create_image(25+(abscisse-(abscisse%50)),25+(ordonnée-(ordonnée%50)),anchor=NW,image=list_bateaux_img_link_v[ref_bateau])
        else:
            list_bateaux[ref_bateau].image(25+(abscisse-(abscisse%tailleCarreau)),25+(ordonnée-(ordonnée%tailleCarreau)),grilles[i].getCanvas(),0,v)
            #grilles[i].getCanvas().create_image(25+(abscisse-(abscisse%50)),25+(ordonnée-(ordonnée%50)),anchor=NW,image=list_bateaux_img_link[ref_bateau])
        
        for o in range(list_bateaux[ref_bateau].taille):
            if v==False:
                grilles[i].setGrille2(floor(ordonnée/tailleCarreau),floor(abscisse/tailleCarreau)+o,list_bateaux [ref_bateau].taille)
                list_bateaux[ref_bateau].setPosition(floor(ordonnée/tailleCarreau),floor(abscisse/tailleCarreau)+o,1)
            else :
                grilles[i].setGrille2(floor(ordonnée/tailleCarreau)+o,floor(abscisse/tailleCarreau),list_bateaux [ref_bateau].taille)
                list_bateaux[ref_bateau].setPosition(floor(ordonnée/tailleCarreau)+o,floor(abscisse/tailleCarreau),1)
        print(grilles[0].getGrille())
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
    num = floor(abscisse/tailleCarreau)*10 + floor(ordonnée/tailleCarreau)
    grilles[n].setGrille2(floor(ordonnée/tailleCarreau),floor(abscisse/tailleCarreau),10)
    grilles[n].changeColor(num,"red")
    grilles[0].setGrille2(floor(ordonnée/tailleCarreau),floor(abscisse/tailleCarreau),10)
    grilles[0].changeColor(num,"red")
    for bateau in list_bateaux:
        for case in bateau.cases:
            if case[0] == floor(ordonnée/tailleCarreau) and case[1] == floor(abscisse/tailleCarreau):
                bateau.touche(floor(ordonnée/tailleCarreau),floor(abscisse/tailleCarreau))
    print("bateaux en lices",nbrVivant())
def nbrVivant():
    global list_bateaux
    c=0
    for bateau in list_bateaux:
        if bateau.status == 1:
            c+=1
    return c

root.title("Bataille Navale, Joueur 1")
root.geometry("1300x550")
root.config(cursor='crosshair')
def show():
    global root
    global grilles

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
    Bateau1.image(0,0+50*k,canvas_bateaux,0,None)
    list_bateaux.append(Bateau1)


def callback(event,x):
    global canvas_bateaux , ref_bateau,list_bateaux
    if (ref_bateau ==None):
        ref_bateau = event.y//50
        list_bateaux[ref_bateau].delete(canvas_bateaux,0)


canvas_bateaux.bind("<Button-1>",lambda event : callback(event,0))

def resize(event):
    w=500
    h=500
    root.geometry(f"{w}x{h}")

last_c=550
last_t=0
def resize(event):
    global last_c,carre,last_t,tailleCarreau,decallage,list_bateaux
    w=event.width
    h=event.height
    c= root.winfo_height()/last_c
    if c == last_t:
        return None
    #print("ccccccccccccccccccccccccccccc",c)
    #print("widget", event.widget)
    #print("height", event.height, "width", event.width)
    x1,y1,x2,y2 = canvas_bateaux.coords(carre)
    #print(x1,y1,x2*c,y2*c)
    canvas_bateaux.coords(carre, x1,y1,x2*c,y2*c)
    for i in range(10):
        for j in range(10):
            x1,y1,x2,y2 = grilles[0].getCanvas().coords(grilles[0].rectangles[i*10+j])
            grilles[0].getCanvas().coords(grilles[0].rectangles[i*10+j],x1*c,y1*c,x2*c,y2*c)
            #print(x2-x1)
    
    w,h = grilles[0].getCanvas().winfo_width(),grilles[0].getCanvas().winfo_height()

    grilles[0].getCanvas().configure(width=w*c, height=h*c)
    last_c=root.winfo_height()
    tailleCarreau=tailleCarreau*c
    decallage= decallage*c
    #print(tailleCarreau)
    last_t=c
    #print("liste",list_bateaux)
    #for bateau in list_bateaux:
    #    if orientation == "h":
     #       bateau.images[0]=bateau.images[0].resize((int(tailleCarreau*bateau.taille),int(tailleCarreau)))
        
        #bateau.updateAfterResize(grilles[0].getCanvas(),0)
    #root.geometry(f"{w}x{h}")

root.bind("<Configure>", resize)
carre=canvas_bateaux.create_rectangle(0,0,100,100,fill='red')


def menu():
    global root
    canvas=Canvas(root,height=400,width=400)
    canvas.pack()
    ButtonJouer = Button(root, text ="Jouer", command = show)
    ButtonJouer.pack()
    ButtonDif = Button(root, text ="Diifficulte", command = '')
    ButtonDif.pack()

