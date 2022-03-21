from email.mime import image
from math import *
from tkinter import *
from weakref import ref
from PIL import ImageTk,Image
from grille import *
from bateau import *
from model import grilles
import PIL.Image

root = Tk()
last=[-1,-2,-3]
orientation = "h"
list_bateaux=[]
ref_bateau = None
def create_bateau(grille,n):
    list_bateaux.append(Bateau(1,1,1,n))
    for each in n:
        grilles[grille].setCase(each,4)

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
bat=[]
def autre(event,n,t):
    abscisse, ordonnée = event.x -25 , event.y-25
    global grilles , list_bateaux_img,img,lastx, bat,lasty , ref_bateau,list_bateaux,list_bateaux_img_link,v
    if ref_bateau != None and 0<abscisse<500 and 0<ordonnée<500: 
        for o in range(list_bateaux [ref_bateau].id):
            try :
                if (v==False):
                    if (grilles[n].check(floor(ordonnée/50),floor(abscisse/50)+o) != True):
                        grilles[n].getCanvas().delete(bat[-1])
                else:
                    if (grilles[n].check(floor(ordonnée/50)+o,floor(abscisse/50)) != True ):
                        grilles[n].getCanvas().delete(bat[-1])
            except:
                
                return None
            
        if (abscisse-(abscisse%50) != lastx or ordonnée-(ordonnée%50) != lasty) :
            try :
                grilles[n].getCanvas().delete(bat[-1])
            except:
                print("")

            bat.append(grilles[n].getCanvas().create_image(25+(abscisse-(abscisse%50)),25+(ordonnée-(ordonnée%50)),anchor=NW,image=list_bateaux_img_link[ref_bateau]))
            if (v==True):
                grilles[0].getCanvas().itemconfig(bat[-1],image=list_bateaux_img_link_v[ref_bateau])
            lastx = abscisse-(abscisse%50)
            lasty = ordonnée-(ordonnée%50)

def app(event,i):
    abscisse, ordonnée = event.x -25 , event.y-25
    #print(abscisse-(abscisse%50),ordonnée-(ordonnée%50))
    global grilles , list_bateaux_img,img,lastx, bat,lasty , ref_bateau,list_bateaux,list_bateaux_img_link,list_bateaux_img_link_v,v
    
    if ref_bateau != None :
        if (v==True):
            grilles[i].getCanvas().create_image(25+(abscisse-(abscisse%50)),25+(ordonnée-(ordonnée%50)),anchor=NW,image=list_bateaux_img_link_v[ref_bateau])
        else:
            grilles[i].getCanvas().create_image(25+(abscisse-(abscisse%50)),25+(ordonnée-(ordonnée%50)),anchor=NW,image=list_bateaux_img_link[ref_bateau])
        
        Bateau("","","1",[floor(abscisse/50),floor(ordonnée/50)])
        for o in range(list_bateaux [ref_bateau].id):
            if v==False:
                grilles[i].setGrille2(floor(ordonnée/50),floor(abscisse/50)+o,list_bateaux [ref_bateau].id)
            else :
                grilles[i].setGrille2(floor(ordonnée/50)+o,floor(abscisse/50),list_bateaux [ref_bateau].id)
    ref_bateau= None

        


    
def pointeur(event,n,action=0):
    global grilles
    global last
    global orientation

    abscisse, ordonnée = event.x -25 , event.y-25
    if (action == 0):
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
            if floor(abscisse/50) <0 or floor(abscisse/50)>7:
                grilles[n].changeColor(num,"red")
                grilles[n].changeColor(num +10 ,"red")
                grilles[n].changeColor(num +20 ,"red")

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


    grille.getCanvas().bind("<Button-1>",lambda event : app(event,0))
    #grille2.getCanvas().bind("<Button-1>",lambda event : pointeur(event,1))
    #grille3.getCanvas().bind("<Button-1>",lambda event : pointeur(event,2))
    #grille4.getCanvas().bind("<Button-1>",lambda event : pointeur(event,3))

    grille.getCanvas().bind("<Motion>",lambda event : autre(event,0,0))
    grille.getCanvas().bind("<Button-3>",change_orientation)


    

    grilles[0].getCanvas().bind("<Button-3>",change_orientation)
v=False

canvas_bateaux=Canvas(root,height=450, width=250)
canvas_bateaux.place(x=1100,y=50)

    
list_bateaux_img=[]
list_bateaux_img_link=[]
list_bateaux_img_link_v=[]
img=ImageTk.PhotoImage(PIL.Image.open("porte_avion_lexington_resized.png"))
img_v=ImageTk.PhotoImage(PIL.Image.open("porte_avion_lexington_resized_v.png"))
list_bateaux_img.append(canvas_bateaux.create_image(0,0,anchor=NW, image=img))
list_bateaux_img_link.append(img)
list_bateaux_img_link_v.append(img_v)
list_bateaux.append(Bateau(5,"","1",None))
img2=ImageTk.PhotoImage(PIL.Image.open("croiseur_de_grasse_resized.png"))
img_2v=ImageTk.PhotoImage(PIL.Image.open("croiseur_de_grasse_resized_v.png"))
list_bateaux_img.append(canvas_bateaux.create_image(0,50,anchor=NW, image=img2))
list_bateaux_img_link.append(img2)
list_bateaux_img_link_v.append(img_2v)
list_bateaux.append(Bateau(4,"","1",None))
img3=ImageTk.PhotoImage(PIL.Image.open("destroyer_kleber_resized.png"))
img3_v=ImageTk.PhotoImage(PIL.Image.open("destroyer_kleber_resized_v.png"))
list_bateaux_img.append(canvas_bateaux.create_image(0,100,anchor=NW, image=img3))
list_bateaux_img_link.append(img3)
list_bateaux_img_link_v.append(img3_v)
list_bateaux.append(Bateau(3,"","1",None))
img4=ImageTk.PhotoImage(PIL.Image.open("sous_marin_resized.png"))
img4_v=ImageTk.PhotoImage(PIL.Image.open("sous_marin_resized_v.png"))
list_bateaux_img.append(canvas_bateaux.create_image(0,150,anchor=NW, image=img4))
list_bateaux_img_link.append(img4)
list_bateaux_img_link_v.append(img4_v)
list_bateaux.append(Bateau(3,"","1",None))
img5=ImageTk.PhotoImage(PIL.Image.open("cuirasse_normandie_resized.png"))
img5_v=ImageTk.PhotoImage(PIL.Image.open("cuirasse_normandie_resized_v.png"))
list_bateaux_img.append(canvas_bateaux.create_image(0,200,anchor=NW, image=img5))
list_bateaux_img_link.append(img5)
list_bateaux_img_link_v.append(img5_v)
list_bateaux.append(Bateau(2,"","1",None))



def callback(event,x):
    global canvas_bateaux , ref_bateau
    ref_bateau = list_bateaux_img[event.y//50] -1
    canvas_bateaux.delete(list_bateaux_img[event.y//50])




canvas_bateaux.bind("<Button-1>",lambda event : callback(event,0))

