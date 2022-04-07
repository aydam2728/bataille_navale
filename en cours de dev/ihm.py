from email.mime import image
from glob import escape
from math import *
from random import *
from textwrap import fill
import time
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
list_bateaux=[[],[]]
ref_bateau = None
tailleCarreau=50
v=False
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
                list_bateaux[n][ref_bateau].delete(grilles[n].getCanvas(),-1)
            except:
                print("")
            list_bateaux[n][ref_bateau].image(25+(abscisse-(abscisse%tailleCarreau)),25+(ordonnée-(ordonnée%tailleCarreau)),grilles[n].getCanvas(),0,v)
            lastx = abscisse-(abscisse%tailleCarreau)
            lasty = ordonnée-(ordonnée%tailleCarreau)

def isEmpty(abscisse,ordonnée,i):
    global grilles ,lastx,lasty , ref_bateau,list_bateaux,v
    for o in range(list_bateaux[i] [ref_bateau].taille):
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
            list_bateaux[i][ref_bateau].image(25+(abscisse-(abscisse%tailleCarreau)),25+(ordonnée-(ordonnée%tailleCarreau)),grilles[i].getCanvas(),1,None)
            #grilles[i].getCanvas().create_image(25+(abscisse-(abscisse%50)),25+(ordonnée-(ordonnée%50)),anchor=NW,image=list_bateaux_img_link_v[ref_bateau])
        else:
            list_bateaux[i][ref_bateau].image(25+(abscisse-(abscisse%tailleCarreau)),25+(ordonnée-(ordonnée%tailleCarreau)),grilles[i].getCanvas(),0,v)
            #grilles[i].getCanvas().create_image(25+(abscisse-(abscisse%50)),25+(ordonnée-(ordonnée%50)),anchor=NW,image=list_bateaux_img_link[ref_bateau])
        
        for o in range(list_bateaux[i][ref_bateau].taille):
            if v==False:
                grilles[i].setGrille2(floor(ordonnée/tailleCarreau),floor(abscisse/tailleCarreau)+o,list_bateaux[i] [ref_bateau])
                list_bateaux[i][ref_bateau].setPosition(floor(ordonnée/tailleCarreau),floor(abscisse/tailleCarreau)+o,1)
            else :
                grilles[i].setGrille2(floor(ordonnée/tailleCarreau)+o,floor(abscisse/tailleCarreau),list_bateaux[i] [ref_bateau])
                list_bateaux[i][ref_bateau].setPosition(floor(ordonnée/tailleCarreau)+o,floor(abscisse/tailleCarreau),1)
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
    for bateau in list_bateaux[n]:
        if bateau.status == 0 :
            return None
    num = floor(abscisse/tailleCarreau)*10 + floor(ordonnée/tailleCarreau)
    grilles[n].setGrille2(floor(ordonnée/tailleCarreau),floor(abscisse/tailleCarreau),10)
    grilles[n].changeColor(num,"red")
    grilles[0].setGrille2(floor(ordonnée/tailleCarreau),floor(abscisse/tailleCarreau),10)
    grilles[0].changeColor(num,"red")
    for bateau in list_bateaux[n]:
        for case in bateau.cases:
            if case[0] == floor(ordonnée/tailleCarreau) and case[1] == floor(abscisse/tailleCarreau):
                bateau.touche(floor(ordonnée/tailleCarreau),floor(abscisse/tailleCarreau))
    print("bateaux en lices",nbrVivant(n))
    
def nbrVivant(x):
    global list_bateaux
    c=0
    for bateau in list_bateaux[x]:
        if bateau.status == 1:
            c+=1
    return c

def auto(event):
    global grilles
    c=0
    while nbrVivant(0) !=0:
        c+=1  
        tir_difficile(grilles[0])
        print(nbrVivant(0))
        print(c,"compteur")
    #print(grilles[0].grille)
    for r in grilles[0].grille:
        for c in r:
            print(c,end = " ")
        print("")
    

def tir_super_simple(grille):
    y=randint(0,9)
    x=randint(0,9)
    case = grille.getCase(y,x)
    print(case,y,x)
    if case ==0:
        grille.changeColor(x*10+y,"green")
        print("manqué")
        return (y,x,False)
    else: 
        case.touche(y,x)
        grille.changeColor(x*10+y,"red")
        print("touché")
        return (y,x,True)
        

def tir_simple(grille,y=None,x=None):
    if x==None and y==None : 
        y=randint(0,9)
        x=randint(0,9)
    case = grille.getCase(y,x)
    if case !=0 and case !=2 and case !=1:
        case.touche(y,x)
        grille.setGrille2(y,x,1)
        grille.changeColor(x*10+y,"red")
        print("touché")
        return (y,x,case,True)
    elif(case !=2 and case !=1):
        grille.setGrille2(y,x,2)
        grille.changeColor(x*10+y,"green")
        print("manqué")
        return (y,x,False)
    return tir_simple(grille)
list_tirs=[]
def tir_moyen(grille):
    if len(list_tirs)>0 and list_tirs[-1][0][-1]==True or (len(list_tirs)>0 and list_tirs[-1][0][-1]==False and check_list()==False):
        print(generate_random())
        y,x = generate_random()
        print(y,x,"1",list_tirs[-1][0][0],"normalement y du tir precedent")
        exec=tir_simple(grille,list_tirs[-1][0][0]+y,list_tirs[-1][0][1]+x)
        list_tirs.append([exec,y,x])
    elif len(list_tirs)>0 and list_tirs[-1][0][-1]==False:
        y,x = generate_random(list_tirs[-1][-2],list_tirs[-1][-1])
        print(y,x,"2")
        exec=tir_simple(grille,list_tirs[-2][0][0]+y,list_tirs[-2][0][1]+x)
        list_tirs.append([exec,y,x])
    elif(len(list_tirs)==0):
        list_tirs.append([tir_simple(grille),0,0])
    print(list_tirs)
    print("rien",list_tirs[-1][0][-1])
    time.sleep(1)

def tir_difficile(grille):
    global list_tirs,list_bateaux
    if len(list_tirs)==0:
        list_tirs.append(tir_simple(grille))
    elif (list_tirs[-1][-1] == True and list_tirs[-1][-2].getCaseAlive() != None):
        y,x = list_tirs[-1][-2].getCaseAlive()
        print("ici",y,x,list_tirs[-1][-2].taille)
        list_tirs.append(tir_simple(grille,y,x))
    else:
        list_tirs.append(tir_simple(grille))


def generate_random(e_y=-2,e_x=-2):
    y=randint(-1,1)
    x=randint(-1,1)
    if y+x == 0 or(x+y==e_y+e_x and (y==e_y or x==e_x)):
        generate_random(y,x)
    else:
        return (y,x)
def check_list():
    global list_tirs
    for tir in list_tirs:
        if tir[0] == True:
            return True
    return False
newWindow=None
def show():
    global root ,newWindow,canvas_bateaux,carre,grilles
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
    grille.getCanvas().bind("<Button-2>",auto)
    grille2.getCanvas().bind("<Button-1>",lambda event : test(event,1))
    grille3.getCanvas().bind("<Button-1>",lambda event : pointeur(event,3))
    #grille4.getCanvas().bind("<Button-1>",lambda event : pointeur(event,3))

    grille.getCanvas().bind("<Motion>",lambda event : autre(event,0,0))
    grille3.getCanvas().bind("<Motion>",lambda event : autre(event,2,0))
    grille.getCanvas().bind("<Button-3>",change_orientation)


    

    grilles[0].getCanvas().bind("<Button-3>",change_orientation)
    grilles[2].getCanvas().bind("<Button-3>",change_orientation)

    canvas_bateaux=[]
    canvas_bateaux.append(Canvas(root,height=450, width=250))
    canvas_bateaux[0].place(x=1100,y=50)
    canvas_bateaux.append(Canvas(newWindow,height=450, width=250))
    canvas_bateaux[1].place(x=1100,y=50)
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
        Bateau1.image(0,0+50*k,canvas_bateaux[0],0,None)
        Bateau1.image(0,0+50*k,canvas_bateaux[1],0,None)
        list_bateaux[0].append(Bateau1)
        list_bateaux[1].append(Bateau1)

    canvas_bateaux[0].bind("<Button-1>",lambda event : callback(event,0))
    canvas_bateaux[1].bind("<Button-1>",lambda event : callback(event,1))   
    #root.bind("<Configure>", resize)
    carre=canvas_bateaux[0].create_rectangle(0,0,100,100,fill='red')

    place(5)
    place(4)
    place(3)
    place(3)
    place(2)
    for r in grilles[2].grille:
        print("")
        for c in r:
            print(c,end = " ")

def callback(event,x):
    global canvas_bateaux , ref_bateau,list_bateaux
    if (ref_bateau ==None):
        ref_bateau = event.y//50
        list_bateaux[x][ref_bateau].delete(canvas_bateaux[x],0)




def resize(event):
    w=500
    h=500
    root.geometry(f"{w}x{h}")

last_c=550
last_t=0
def resize(event):
    global last_c,carre,last_t,tailleCarreau,decallage,list_bateaux,canvas_bateaux
    w=event.width
    h=event.height
    c= root.winfo_height()/last_c
    if c == last_t:
        return None
    #print("ccccccccccccccccccccccccccccc",c)
    #print("widget", event.widget)
    #print("height", event.height, "width", event.width)
    x1,y1,x2,y2 = canvas_bateaux[0].coords(carre)
    #print(x1,y1,x2*c,y2*c)
    canvas_bateaux[0].coords(carre, x1,y1,x2*c,y2*c)
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




def menu():
    global root
    root.title("SHIPS WARS")
    root.geometry("1300x550")
    root.config(cursor='crosshair')
    canvas=Canvas(root,height=400,width=400)
    canvas.pack(expand = YES, fill = BOTH)
    width = int(canvas.cget('width'))
    height = int(canvas.cget('height'))
    image= PIL.Image.open("porte_avion_lexington_resized.png")
    #image.resize((width,height))
    #image.show()
    image_tk=ImageTk.PhotoImage(image)
    canvas.create_image(10,10,anchor=NW,image=image_tk)
    backgroundLabel = Label(root,image=image_tk)
    backgroundLabel .place(x=0,y=0)
    ButtonJouer = Button(root, text ="Jouer", command = show)
    ButtonJouer.pack()
    ButtonDif = Button(root, text ="Diifficulte", command = '')
    ButtonDif.pack()

def place(t):
    global grilles
    x=randint(0,9)
    y=randint(0,9)
    o=randint(0,1)
    if 0<x+t<10 and 0<y+t<10 and check(y,x,t,o):
        if(o==0):
            for k in range(t):
                grilles[2].grille[y][x+k]=t
        else:
            for k in range(t):
                grilles[2].grille[y+k][x]=t
    else:
        return place(t)
def check(y,x,t,o):
    global grilles
    for k in range(t):
        if grilles[2].grille[y][x+k] != 0 and o==0:
            return False
        if grilles[2].grille[y+k][x] != 0 and o==1:
            return False
    return True

