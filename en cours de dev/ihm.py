from email.mime import image
from glob import escape
from math import *
from random import *
import sys
from textwrap import fill
import time
from tkinter import *
from weakref import ref
from PIL import ImageTk,Image
import pygame
from grille import *
from bateau import *
from model import grilles
from PIL import Image, ImageTk
from tkinter import *
from tkinter import font

pygame.mixer.init()
sound1 = pygame.mixer.Sound('end.wav') 
sound2 = pygame.mixer.Sound('hit.wav') 
sound3 = pygame.mixer.Sound('water.wav') 
sound4 = pygame.mixer.Sound('ambiance.wav') 
sound5 = pygame.mixer.Sound('button.wav') 
root = Tk()
list_bateaux=[[],[]]
ref_bateau = None
tailleCarreau=50
v=False
speudo1 =None
speudo2 =None
multi=False
dif=None
compteurTirsPlayer1=0
compteurTirsPlayer2=0
def change_orientation(event,n,t):
    global v , lastx
    if v == True:
        v = False
    else:
        v = True
    lastx=None
    autre(event,n,t)
lastx=0
lasty=0
decallage=25
def autre(event,n,t):
    global grilles ,lastx,lasty , ref_bateau,list_bateaux,v,decallage
    abscisse, ordonnée = event.x -decallage , event.y-decallage
    canvasSize=int(grilles[n].getCanvas()['height'])-25
    if ref_bateau != None and 0<abscisse<canvasSize and 0<ordonnée<canvasSize and isEmpty(abscisse,ordonnée,n,t) == True :    
        if (abscisse-(abscisse%tailleCarreau) != lastx or ordonnée-(ordonnée%tailleCarreau) != lasty):
            try :
                list_bateaux[t][ref_bateau].delete(grilles[n].getCanvas(),-1)
            except:
                print("")
            list_bateaux[t][ref_bateau].createImage(25+(abscisse-(abscisse%tailleCarreau)),25+(ordonnée-(ordonnée%tailleCarreau)),grilles[n].getCanvas(),v)
            lastx = abscisse-(abscisse%tailleCarreau)
            lasty = ordonnée-(ordonnée%tailleCarreau)

def isEmpty(abscisse,ordonnée,i,t):
    global grilles ,lastx,lasty , ref_bateau,list_bateaux,v
    
    for o in range(list_bateaux[t][ref_bateau].taille):
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

def app(event,i,t):
    global grilles ,lastx,lasty , ref_bateau,list_bateaux,v,decallage
    abscisse, ordonnée = event.x -decallage , event.y-decallage
    if ref_bateau != None and isEmpty(abscisse,ordonnée,i,t) == True and ordonnée>=0 and abscisse>=0:
        if (v==True):
            list_bateaux[t][ref_bateau].createImage(25+(abscisse-(abscisse%tailleCarreau)),25+(ordonnée-(ordonnée%tailleCarreau)),grilles[i].getCanvas(),v)
        else:
            list_bateaux[t][ref_bateau].createImage(25+(abscisse-(abscisse%tailleCarreau)),25+(ordonnée-(ordonnée%tailleCarreau)),grilles[i].getCanvas(),v)
        
        for o in range(list_bateaux[t][ref_bateau].taille):
            if v==False:
                grilles[i].setGrille2(floor(ordonnée/tailleCarreau),floor(abscisse/tailleCarreau)+o,list_bateaux[t] [ref_bateau])
                list_bateaux[t][ref_bateau].setPosition(floor(ordonnée/tailleCarreau),floor(abscisse/tailleCarreau),v,1)
            else :
                grilles[i].setGrille2(floor(ordonnée/tailleCarreau)+o,floor(abscisse/tailleCarreau),list_bateaux[t] [ref_bateau])
                list_bateaux[t][ref_bateau].setPosition(floor(ordonnée/tailleCarreau),floor(abscisse/tailleCarreau),v,1)
        ref_bateau= None

   
def pointeur(event,n,action,t):
    global grilles
    global orientation , ref_bateau ; global list_bateaux
    abscisse, ordonnée = event.x -25 , event.y-25
    if ref_bateau == None:
        action = 1
    if (action == 0):
        app(event,n,t)
        return None
def test(event,n,t):
    global grilles , ref_bateau ; global list_bateaux,dif,multi,sound2,sound3,compteurTirsPlayer1,compteurTirsPlayer2
    abscisse, ordonnée = event.x -25 , event.y-25
    if multi and n==3:
        compteurTirsPlayer2+=1
        x=0
    else:
        x=2
        compteurTirsPlayer1+=1
    for bateau in list_bateaux[t]:
        if bateau.status == 0 :
            return None
    num = floor(abscisse/tailleCarreau)*10 + floor(ordonnée/tailleCarreau)
    case=grilles[x].getCase(floor(ordonnée/tailleCarreau),floor(abscisse/tailleCarreau))
    if (case!=0):
        case.touche(floor(ordonnée/tailleCarreau),floor(abscisse/tailleCarreau))  
        sound2.play()
        grilles[n].setGrille2(floor(ordonnée/tailleCarreau),floor(abscisse/tailleCarreau),10)
        grilles[n].changeColor(num,"red")
        grilles[x].setGrille2(floor(ordonnée/tailleCarreau),floor(abscisse/tailleCarreau),10)
        grilles[x].changeColor(num,"red")
    else:
        sound3.play()
        grilles[n].setGrille2(floor(ordonnée/tailleCarreau),floor(abscisse/tailleCarreau),10)
        grilles[n].changeColor(num,"green")
        grilles[x].setGrille2(floor(ordonnée/tailleCarreau),floor(abscisse/tailleCarreau),10)
        grilles[x].changeColor(num,"green")
    if multi ==False:
        nbrVivant(1,0)
        if dif ==0:
            tir_super_simple(grilles[0])
        elif dif==1:
            tir_simple( grilles[0])
        elif dif==2:
            tir_moyen( grilles[0])
        else:
            tir_difficile(grilles[0])
        nbrVivant(0,1)
    else:
        if x==0:
            print("bateaux en lices",nbrVivant(0,n))
        else:
            print("bateaux en lices",nbrVivant(1,n))


def nbrVivant(t,x):
    global list_bateaux
    c=0
    for bateau in list_bateaux[t]:
        if bateau.status == 1:
            c+=1
    if c==0:
        menu_end(x)
    return c,x

def auto(event):
    global grilles
    c=0
    while nbrVivant(0) !=0:
        c+=1  
        tir_difficile(grilles[0])
        print(nbrVivant(0))
    

def tir_super_simple(grille):
    global sound3,sound2,compteurTirsPlayer2
    compteurTirsPlayer2+=1
    y=randint(0,9)
    x=randint(0,9)
    case = grille.getCase(y,x)
    if case ==0:
        grille.changeColor(x*10+y,"green")
        sound3.play()
        return (y,x,False)
    else: 
        case.touche(y,x)
        grille.changeColor(x*10+y,"red")
        sound2.play()
        return (y,x,True)
        

def tir_simple(grille,y=None,x=None):
    global sound3,sound2,compteurTirsPlayer2
    compteurTirsPlayer2+=1
    if x==None and y==None : 
        y=randint(0,9)
        x=randint(0,9)
    case = grille.getCase(y,x)
    if case !=0 and case !=2 and case !=1:
        case.touche(y,x)
        grille.setGrille2(y,x,1)
        grille.changeColor(x*10+y,"red")
        sound2.play()
        return (y,x,case,True)
    elif(case !=2 and case !=1):
        grille.setGrille2(y,x,2)
        grille.changeColor(x*10+y,"green")
        sound3.play()
        return (y,x,False)
    return tir_simple(grille)
list_tirs=[]
def tir_moyen(grille):
    if len(list_tirs)>0 and list_tirs[-1][0][-1]==True or (len(list_tirs)>0 and list_tirs[-1][0][-1]==False and check_list()==False):
        y,x = generate_random()
        exec=tir_simple(grille,list_tirs[-1][0][0]+y,list_tirs[-1][0][1]+x)
        list_tirs.append([exec,y,x])
    elif len(list_tirs)>0 and list_tirs[-1][0][-1]==False:
        y,x = generate_random(list_tirs[-1][-2],list_tirs[-1][-1])
        exec=tir_simple(grille,list_tirs[-2][0][0]+y,list_tirs[-2][0][1]+x)
        list_tirs.append([exec,y,x])
    elif(len(list_tirs)==0):
        list_tirs.append([tir_simple(grille),0,0])

def tir_difficile(grille):
    global list_tirs,list_bateaux
    if len(list_tirs)==0:
        list_tirs.append(tir_simple(grille))
    elif (list_tirs[-1][-1] == True and list_tirs[-1][-2].getCaseAlive() != None):
        y,x = list_tirs[-1][-2].getCaseAlive()
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
def show(diff,entry,entry2):
    global root ,newWindow,canvas_bateaux,carre,grilles,speudo1,v,multi,dif,speudo2,sound5
    global grilles
    sound5.play()
    speudo1=entry.get()
    dif=diff
    newWindow = Toplevel(root)
    newWindow.title("SHIPS FIGHT PLAYER :"+str(speudo2))
    newWindow.geometry("1300x550")
    newWindow.config(cursor='crosshair') 
    newWindow.withdraw()
    grille = Grille(1,"bas",root,0,0)
    grille2 = Grille(2,"bas",root,550,0)
    grilles.append(grille)
    grilles.append(grille2)
    
    root.geometry("1300x550")
    root.title("SHIPS FIGHT PLAYER :" + speudo1)
    

    grille3 = Grille(3,"bas",newWindow,0,0)
    grille4 = Grille(4,"bas",newWindow,550,0)
    grilles.append(grille3)
    grilles.append(grille4)
    if entry2 !=None:
        speudo2=entry2.get()
        multi =True
        newWindow.deiconify()
    

    clearWidgets()


    grille.getCanvas().bind("<Button-1>",lambda event : pointeur(event,0,0,0))
    grille.getCanvas().bind("<Button-2>",auto)
    grille2.getCanvas().bind("<Button-1>",lambda event : test(event,1,0))
    grille4.getCanvas().bind("<Button-1>",lambda event : test(event,3,1))
    grille3.getCanvas().bind("<Button-1>",lambda event : pointeur(event,2,0,1))

    grille.getCanvas().bind("<Motion>",lambda event : autre(event,0,0))
    grille3.getCanvas().bind("<Motion>",lambda event : autre(event,2,1))
    grille.getCanvas().bind("<Button-3>",lambda event :change_orientation(event,0,0))
    grille3.getCanvas().bind("<Button-3>",lambda event :change_orientation(event,2,1))


    


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
        Bateau2 = Bateau(k,"","1",0,taille)
        Bateau2.addImage(list_imgs[k])
        Bateau1.createImage(0,0+50*k,canvas_bateaux[0],v)
        Bateau2.createImage(0,0+50*k,canvas_bateaux[1],v)
        list_bateaux[0].append(Bateau1)
        list_bateaux[1].append(Bateau2)

    canvas_bateaux[0].bind("<Button-1>",lambda event : callback(event,0))
    canvas_bateaux[1].bind("<Button-1>",lambda event : callback(event,1))   
    
    if multi == False:
        for k in range(len(list_bateaux[1])):
            place(list_bateaux[1][k])
        

 

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
    x1,y1,x2,y2 = canvas_bateaux[0].coords(carre)
    canvas_bateaux[0].coords(carre, x1,y1,x2*c,y2*c)
    for i in range(10):
        for j in range(10):
            x1,y1,x2,y2 = grilles[0].getCanvas().coords(grilles[0].rectangles[i*10+j])
            grilles[0].getCanvas().coords(grilles[0].rectangles[i*10+j],x1*c,y1*c,x2*c,y2*c)
    
    w,h = grilles[0].getCanvas().winfo_width(),grilles[0].getCanvas().winfo_height()

    grilles[0].getCanvas().configure(width=w*c, height=h*c)
    last_c=root.winfo_height()
    tailleCarreau=tailleCarreau*c
    decallage= decallage*c
    last_t=c
   


liste_menu_widgets=[]
def menu():
    global root,image_tk_menu,canvas,liste_menu_widgets
    if len(liste_menu_widgets)>0:
        clearWidgets()
    root.title("SHIPS WARS")
    root.geometry("500x500")
    root.config(cursor='crosshair')
    canvas=Canvas(root,height=500,width=500,bg="red")
    canvas.pack(expand = YES, fill = BOTH)
    liste_menu_widgets.append(canvas)
    width = int(canvas.cget('width'))
    height = int(canvas.cget('height'))
    image_menu= PIL.Image.open("menu"+str(randint(1,3))+".jpg")
    image_menu=image_menu.resize((500,500))
    image_tk_menu= ImageTk.PhotoImage(image_menu)
    
    canvas.create_image(0,0,anchor=NW,image=image_tk_menu)
    
    myfont = font.Font(family="Arial", size=14, weight="bold")
    ButtonJouer = Button(root, text ="PLAY",bg="gray",borderwidth=0, command = menu_mode,font=myfont,justify=CENTER,width=10,relief=FLAT,overrelief=FLAT)
    ButtonJouer.place(x=100,y=250,anchor=CENTER)
    liste_menu_widgets.append(ButtonJouer)
    ButtonOptions = Button(root, text ="SETTINGS", bg="gray",borderwidth=0,command = restart,font=myfont,justify=CENTER,width=10,relief=FLAT,overrelief=FLAT)
    ButtonOptions.place(x=100,y=300,anchor=CENTER)
    liste_menu_widgets.append(ButtonOptions)
    ButtonCredits = Button(root, text ="CREDITS", bg="gray",borderwidth=0,command = '',font=myfont,justify=CENTER,width=10,relief=FLAT,overrelief=FLAT)
    ButtonCredits.place(x=100,y=350,anchor=CENTER)
    liste_menu_widgets.append(ButtonCredits)
    ButtonExit = Button(root, text ="EXIT", bg="gray",borderwidth=0,command = quit,font=myfont,justify=CENTER,width=10,relief=FLAT,overrelief=FLAT)
    ButtonExit.place(x=100,y=400,anchor=CENTER)
    liste_menu_widgets.append(ButtonExit)

def menu_mode():
    global root , liste_menu_widgets,sound5
    sound5.play()
    clearWidgets()
    canvas=Canvas(root,height=500,width=500,bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    liste_menu_widgets.append(canvas)
    width = int(canvas.cget('width'))
    height = int(canvas.cget('height'))
    myfont = font.Font(family="Arial", size=14, weight="bold")
    ButtonJouer = Button(root, text ="SINGLEPLAYER",bg="gray",borderwidth=0, command = lambda : menu_dif(False),font=myfont,justify=CENTER,width=15,relief=FLAT,overrelief=FLAT)
    ButtonJouer.place(x=250,y=250,anchor=CENTER)
    liste_menu_widgets.append(ButtonJouer)
    ButtonOptions = Button(root, text ="MULTIPLAYER", bg="gray",borderwidth=0,command = lambda :menu_dif(True),font=myfont,justify=CENTER,width=15,relief=FLAT,overrelief=FLAT)
    ButtonOptions.place(x=250,y=350,anchor=CENTER)
    liste_menu_widgets.append(ButtonOptions)
    ButtonRetour= Button(root, text ="BACK", bg="gray",borderwidth=0,command = menu,font=myfont,justify=CENTER,width=5,relief=FLAT,overrelief=FLAT)
    ButtonRetour.place(x=450,y=450,anchor=CENTER)
    liste_menu_widgets.append(ButtonRetour)

def menu_dif(mult):
    global root , liste_menu_widgets,sound5
    sound5.play()
    clearWidgets()
    myfont = font.Font(family="Arial", size=14, weight="bold")
    canvas=Canvas(root,height=500,width=500,bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    liste_menu_widgets.append(canvas)
    entry = Entry(root,font=myfont)
    entry.place(x=300,y=100)
    liste_menu_widgets.append(entry)
    if mult == True:
        label = Label(root,text="YOUR SPEUDO, PLAYER 1 :",bg="gray",font=myfont)
        label.place(x=0,y=100)
        liste_menu_widgets.append(label)
        label2 = Label(root,text="YOUR SPEUDO, PLAYER 2  :",bg="gray",font=myfont)
        label2.place(x=0,y=150)
        liste_menu_widgets.append(label2)
        entry2 = Entry(root,font=myfont)
        entry2.place(x=300,y=150)
        liste_menu_widgets.append(entry2)
    else :
        label = Label(root,text="YOUR SPEUDO :",bg="gray",font=myfont)
        label.place(x=0,y=100)
        liste_menu_widgets.append(label)
        entry2=None

    
    width = int(canvas.cget('width'))
    height = int(canvas.cget('height'))
    
    
    myfont = font.Font(family="Arial", size=14, weight="bold")
    label3 = Label(root,text="SELECT THE DIFFICULTY",bg="gray",font=myfont)
    label3.place(x=100,y=200)
    liste_menu_widgets.append(label3)
    ButtonSFacile = Button(root, text ="VERRY SIMPLE",bg="gray",borderwidth=0, command = lambda : show(0,entry,entry2),font=myfont,justify=CENTER,width=15,relief=FLAT,overrelief=FLAT)
    ButtonSFacile.place(x=150,y=300,anchor=CENTER)
    liste_menu_widgets.append(ButtonSFacile)
    ButtonFacile = Button(root, text ="SIMPLE",bg="gray",borderwidth=0, command = lambda : show(1,entry,entry2),font=myfont,justify=CENTER,width=15,relief=FLAT,overrelief=FLAT)
    ButtonFacile.place(x=350,y=300,anchor=CENTER)
    liste_menu_widgets.append(ButtonFacile)
    ButtonMoyen = Button(root, text ="MEDIUM", bg="gray",borderwidth=0,command = lambda : show(2,entry,entry2),font=myfont,justify=CENTER,width=15,relief=FLAT,overrelief=FLAT)
    ButtonMoyen.place(x=150,y=350,anchor=CENTER)
    liste_menu_widgets.append(ButtonMoyen)
    ButtonDur= Button(root, text ="HARD", bg="gray",borderwidth=0,command = lambda : show(3,entry,entry2),font=myfont,justify=CENTER,width=15,relief=FLAT,overrelief=FLAT)
    ButtonDur.place(x=350,y=350,anchor=CENTER)
    ButtonRetour= Button(root, text ="BACK", bg="gray",borderwidth=0,command = menu_mode,font=myfont,justify=CENTER,width=5,relief=FLAT,overrelief=FLAT)
    ButtonRetour.place(x=450,y=450,anchor=CENTER)
    liste_menu_widgets.append(ButtonRetour)
def menu_end(x):
    global root ,liste_menu_widgets,multi,sound1,sound5,compteurTirsPlayer1,compteurTirsPlayer2
    sound5.play()
    for ele in root.winfo_children():
        ele.destroy()
    sound1.play()
    root.geometry("500x500")

    myfont = font.Font(family="Arial", size=14, weight="bold")
    canvas=Canvas(root,height=500,width=500,bg="black")
    canvas.pack(expand = YES, fill = BOTH)
    liste_menu_widgets.append(canvas)
    if x==0 and multi == True:
        winner= speudo1
        tirs=compteurTirsPlayer1
    elif( x==0 and multi == False):
        winner= speudo1
        tirs=compteurTirsPlayer1
    else:
        winner= "BOT"
        tirs=compteurTirsPlayer2
    label = Label(root,text=str(winner)+" WON THE BATLLE",bg="gray",font=myfont)
    label.place(x=250,y=200,anchor=CENTER)
    liste_menu_widgets.append(label)
    winrate=int((17/tirs)*100)
    label1 = Label(root,text="WITH "+str(tirs)+" SHOOTS, "+str(winrate)+ " % WINRATE",bg="gray",font=myfont)
    label1.place(x=250,y=250,anchor=CENTER)
    liste_menu_widgets.append(label1)
    ButtonRestart= Button(root, text ="RESTART", bg="gray",borderwidth=0,command = restart,font=myfont,justify=CENTER,width=8,relief=FLAT,overrelief=FLAT)
    ButtonRestart.place(x=450,y=450,anchor=CENTER)
    liste_menu_widgets.append(ButtonRestart)

def restart():
    global root,list_bateaux,ref_bateau,speudo1,speudo2,multi,dif,sound5
    sound5.play()
    for ele in root.winfo_children():
        ele.destroy()
    list_bateaux=[[],[]]
    ref_bateau = None
    speudo1 =None
    speudo2 =None
    multi=False
    dif=None
    menu()

def clearWidgets():
    global liste_menu_widgets
    for widget in liste_menu_widgets:
        widget.destroy()


def place(z):
    global grilles
    x=randint(0,9)
    y=randint(0,9)
    o=randint(0,1)
    if 0<x+z.taille<10 and 0<y+z.taille<10 and check(y,x,z.taille,o):
        for k in range(z.taille):
             if(o==0):
                grilles[2].grille[y][x+k]=z
             else:
                grilles[2].grille[y+k][x]=z
        z.setPosition(y,x,o,1)
    else:
        return place(z)

def check(y,x,t,o):
    global grilles
    for k in range(t):
        if grilles[2].grille[y][x+k] != 0 and o==0:
            return False
        if grilles[2].grille[y+k][x] != 0 and o==1:
            return False
    return True
